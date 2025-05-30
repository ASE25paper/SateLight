import yaml
import torch
import torch.nn.functional as F
from skimage import data
from skimage.transform import resize
import numpy as np
from models.vae import CompressionVAE
import argparse
from pathlib import Path
from torch.nn.utils import clip_grad_norm_


def main(config_path):

    config_path = Path(config_path)
    # 加载配置
    with open(config_path) as f:
        config = yaml.safe_load(f)

    # 初始化模型
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CompressionVAE(**config["model"]).to(device)

    # 生成测试图像
    image = data.camera()  # 获取512x512的测试图像
    image = resize(image, (256, 256))  # 调整到模型需要的尺寸
    image_tensor = torch.from_numpy(image).float().unsqueeze(0).unsqueeze(0).to(device)  # shape: [0,0,256,256]

    # 优化器
    optimizer = torch.optim.Adam(model.parameters(), lr=config["training"]["lr"])

    # 创建保存目录
    Path("checkpoints").mkdir(exist_ok=True)
    Path("outputs").mkdir(exist_ok=True)

    # 训练循环
    for epoch in range(config["training"]["epochs"]):
        model.train()
        total_loss = 0.0

        # 使用单张图片模拟batch训练
        for _ in range(100):  # 每个epoch迭代100次
            optimizer.zero_grad()

            # 前向传播
            x_hat, y_quant = model(image_tensor)

            # 计算损失
            mse_loss = F.mse_loss(x_hat, image_tensor)
            bpp = torch.log2(torch.abs(y_quant) + 1e-8).mean()
            loss = config["training"]["lambda"] * mse_loss + torch.abs(bpp)

            # 反向传播
            loss.backward()
            clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()

            total_loss += loss.item()

        # 记录日志
        avg_loss = total_loss / 100
        print(f"Epoch {epoch + 1}/{config['training']['epochs']} | Loss: {avg_loss:.4f}")

        # 保存重建结果
        if (epoch + 1) % 10 == 0:
            with torch.no_grad():
                recon_img = x_hat.squeeze().cpu().numpy()
                np.save(f"outputs/recon_{config_path.stem}_epoch{epoch + 1}.npy", recon_img)

            # 保存模型
            torch.save(model.state_dict(), f"checkpoints/{config_path.stem}_epoch{epoch + 1}.pth")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True,
                        help="Path to config file (e.g., configs/low_rate.yaml)")
    args = parser.parse_args()
    main(args.config)