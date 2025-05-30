import torch
from PIL import Image
import numpy as np
from models.vae import CompressionVAE
import yaml


def compress_image(model, image_path, output_path):
    # 加载图像
    img = Image.open(image_path).convert('L')
    img = img.resize((256, 256))
    x = torch.from_numpy(np.array(img)).float().unsqueeze(0).unsqueeze(0) / 255.0

    # 压缩和解压
    model.eval()
    with torch.no_grad():
        x_hat, y_quant = model(x)

    # 保存结果
    rec_img = (x_hat.squeeze().numpy() * 255).astype(np.uint8)
    Image.fromarray(rec_img).save(output_path)

    # 计算压缩率
    original_size = x.nelement() * 8  # 原始bit数
    compressed_size = y_quant.nelement() * 4  # 假设4bit量化
    ratio = compressed_size / original_size
    print(f"Compression Ratio: {ratio:.2f}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True)
    parser.add_argument("--config", type=str, required=True)
    parser.add_argument("--model", type=str, required=True)
    args = parser.parse_args()

    # 加载配置和模型
    with open(args.config) as f:
        config = yaml.safe_load(f)

    model = CompressionVAE(**config["model"])
    model.load_state_dict(torch.load(args.model, map_location=torch.device('cpu')))

    # 执行压缩
    compress_image(model, args.image, "output.png")