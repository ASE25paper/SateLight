# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)
#5AzXcqjKNZQXMu74yspREWjPM7SwEZUdFZ6mPdAvh9pKnXTrBzqGVaKfw2DN2aN1PPHt4Fz4jKTYiMwUp5NLW5JCoRDwB9WIo51kpEf30wBdK4x2HyvwGT9o34QJjjQ27fkpHbnZntUjrfDY2LYj2yBWptfCbTx4zXKUNPbQGLtb7c8rsIPHXReb6ixO9AmzAkMwK8t9PnsXPkuH7CBL5wWvl5HySeJh2tYr2S3qxTeEYoQJMKt5yip97DLwj5eM5kb8DZ5kZBpqjTu7v1YdYqbq7k9kEGuAgFcAaUtvdrtwf3aU6RjTdkQUtdG2xJxGHZFCpPY1CD8ebccn1vA3TzN9hRMUzvBz6RoNRn9SczSE6PAi3cdiYkqpdvXBcrULgYAF4GDUrGLXEfYvJzK9ReSH4JxBmiBRvELKwbFn5uEGmtkPN9oeKm5V9TYwpZNBXKhJcUnWaQzUuw2bD8kdoXhV7KBDZzZ4LbHpGR1TUSr5ZqqX9ewvRvd5FrJhkgI5AdZkvWq4vWgmhH9UvHTOtJ2TkueTuToYZwPkGyLtEsocOwFHLRgPSJvKBNx28mh9JdBZc6HXRD7ZrTuY2CuRPkpiRHmRiDNPhhTDaBh9j8rZjAGUXmsZUFxZgHGvWX28dn43J5UEHy0cbbDgGB1t7sow3BQPM2jXl9bVxCEHzWyudZNNwz2AtGFiJhBtjvW0d2Vyx5yi0l2qZyLR8AZy7MyYwGZRL3mPgDAgGC7W3Ktz7k0I9qLU8rJhJuAEnoXeTjY6gL4A8hjqmdDKvMQKRBIDxNk5OZ6TVWW9AnWjv9epRuvvKVA2cYhn0XUYzNU8IQmuPcJJc4oZ9R38VrkBXla3B1FVbMsACcrkFiT9yz2k7dN4ByMLNUzt5CgzY4Mwfxcd7MI1ltnrhq03mgGwMz2EN9i6XNmnhVEnjUpnXOkYTHGzdxBo3K2g6j70cyA9GmN3oGZQcrPlspQeW9peU15IMu0EjZDt9EmKRhtBGjlzEYaYt88pTH69Co7xky1R8DDfE7bnY2i80HLnmxivZRuX

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63lient.proto\x12\x0fmcc.fred.client\"\x07\n\x05\x45mpty\"q\n\x07Version\x12\x36\n\x07version\x18\x01 \x03(\x0b\x32%.mcc.fred.client.Version.VersionEntry\x1a.\n\x0cVersionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"J\n\x15\x43reateKeygroupRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\x0f\n\x07mutable\x18\x02 \x01(\x08\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\x03\")\n\x15\x44\x65leteKeygroupRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\"W\n\x0bReadRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12*\n\x08versions\x18\x03 \x03(\x0b\x32\x18.mcc.fred.client.Version\"J\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\t\x12)\n\x07version\x18\x03 \x01(\x0b\x32\x18.mcc.fred.client.Version\"3\n\x0cReadResponse\x12#\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x15.mcc.fred.client.Item\":\n\x0bScanRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x04\"3\n\x0cScanResponse\x12#\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x15.mcc.fred.client.Item\":\n\x0bKeysRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x04\"<\n\x03Key\x12\n\n\x02id\x18\x01 \x01(\t\x12)\n\x07version\x18\x02 \x01(\x0b\x32\x18.mcc.fred.client.Version\"2\n\x0cKeysResponse\x12\"\n\x04keys\x18\x01 \x03(\x0b\x32\x14.mcc.fred.client.Key\"g\n\rUpdateRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12*\n\x08versions\x18\x04 \x03(\x0b\x32\x18.mcc.fred.client.Version\";\n\x0eUpdateResponse\x12)\n\x07version\x18\x01 \x01(\x0b\x32\x18.mcc.fred.client.Version\";\n\rAppendRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"\x1c\n\x0e\x41ppendResponse\x12\n\n\x02id\x18\x01 \x01(\t\"Y\n\rDeleteRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12*\n\x08versions\x18\x03 \x03(\x0b\x32\x18.mcc.fred.client.Version\";\n\x0e\x44\x65leteResponse\x12)\n\x07version\x18\x01 \x01(\x0b\x32\x18.mcc.fred.client.Version\"E\n\x11\x41\x64\x64ReplicaRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\x0e\n\x06nodeId\x18\x02 \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\x03\"*\n\x16GetKeygroupInfoRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\"]\n\x17GetKeygroupInfoResponse\x12\x0f\n\x07mutable\x18\x01 \x01(\x08\x12\x31\n\x07replica\x18\x02 \x03(\x0b\x32 .mcc.fred.client.KeygroupReplica\"?\n\x0fKeygroupReplica\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x02 \x01(\x03\x12\x0c\n\x04host\x18\x03 \x01(\t\"8\n\x14RemoveReplicaRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\x0e\n\x06nodeId\x18\x02 \x01(\t\"#\n\x11GetReplicaRequest\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\"2\n\x12GetReplicaResponse\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\"\'\n\x07Replica\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\"C\n\x15GetAllReplicaResponse\x12*\n\x08replicas\x18\x01 \x03(\x0b\x32\x18.mcc.fred.client.Replica\"-\n\x19GetKeygroupTriggerRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\"H\n\x1aGetKeygroupTriggerResponse\x12*\n\x08triggers\x18\x01 \x03(\x0b\x32\x18.mcc.fred.client.Trigger\"#\n\x07Trigger\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\"M\n\x11\x41\x64\x64TriggerRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\x11\n\ttriggerId\x18\x02 \x01(\t\x12\x13\n\x0btriggerHost\x18\x03 \x01(\t\";\n\x14RemoveTriggerRequest\x12\x10\n\x08keygroup\x18\x01 \x01(\t\x12\x11\n\ttriggerId\x18\x02 \x01(\t\"Y\n\x0e\x41\x64\x64UserRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08keygroup\x18\x02 \x01(\t\x12\'\n\x04role\x18\x03 \x01(\x0e\x32\x19.mcc.fred.client.UserRole\"\\\n\x11RemoveUserRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08keygroup\x18\x02 \x01(\t\x12\'\n\x04role\x18\x03 \x01(\x0e\x32\x19.mcc.fred.client.UserRole*s\n\x08UserRole\x12\x10\n\x0cReadKeygroup\x10\x00\x12\x11\n\rWriteKeygroup\x10\x01\x12\x14\n\x10\x43onfigureReplica\x10\x02\x12\x14\n\x10\x43onfigureTrigger\x10\x03\x12\x16\n\x12\x43onfigureKeygroups\x10\x04\x32\x9c\x0b\n\x06\x43lient\x12P\n\x0e\x43reateKeygroup\x12&.mcc.fred.client.CreateKeygroupRequest\x1a\x16.mcc.fred.client.Empty\x12P\n\x0e\x44\x65leteKeygroup\x12&.mcc.fred.client.DeleteKeygroupRequest\x1a\x16.mcc.fred.client.Empty\x12\x43\n\x04Read\x12\x1c.mcc.fred.client.ReadRequest\x1a\x1d.mcc.fred.client.ReadResponse\x12\x43\n\x04Scan\x12\x1c.mcc.fred.client.ScanRequest\x1a\x1d.mcc.fred.client.ScanResponse\x12\x43\n\x04Keys\x12\x1c.mcc.fred.client.KeysRequest\x1a\x1d.mcc.fred.client.KeysResponse\x12I\n\x06Update\x12\x1e.mcc.fred.client.UpdateRequest\x1a\x1f.mcc.fred.client.UpdateResponse\x12I\n\x06\x44\x65lete\x12\x1e.mcc.fred.client.DeleteRequest\x1a\x1f.mcc.fred.client.DeleteResponse\x12I\n\x06\x41ppend\x12\x1e.mcc.fred.client.AppendRequest\x1a\x1f.mcc.fred.client.AppendResponse\x12H\n\nAddReplica\x12\".mcc.fred.client.AddReplicaRequest\x1a\x16.mcc.fred.client.Empty\x12\x64\n\x0fGetKeygroupInfo\x12\'.mcc.fred.client.GetKeygroupInfoRequest\x1a(.mcc.fred.client.GetKeygroupInfoResponse\x12N\n\rRemoveReplica\x12%.mcc.fred.client.RemoveReplicaRequest\x1a\x16.mcc.fred.client.Empty\x12U\n\nGetReplica\x12\".mcc.fred.client.GetReplicaRequest\x1a#.mcc.fred.client.GetReplicaResponse\x12O\n\rGetAllReplica\x12\x16.mcc.fred.client.Empty\x1a&.mcc.fred.client.GetAllReplicaResponse\x12n\n\x13GetKeygroupTriggers\x12*.mcc.fred.client.GetKeygroupTriggerRequest\x1a+.mcc.fred.client.GetKeygroupTriggerResponse\x12H\n\nAddTrigger\x12\".mcc.fred.client.AddTriggerRequest\x1a\x16.mcc.fred.client.Empty\x12N\n\rRemoveTrigger\x12%.mcc.fred.client.RemoveTriggerRequest\x1a\x16.mcc.fred.client.Empty\x12\x42\n\x07\x41\x64\x64User\x12\x1f.mcc.fred.client.AddUserRequest\x1a\x16.mcc.fred.client.Empty\x12H\n\nRemoveUser\x12\".mcc.fred.client.RemoveUserRequest\x1a\x16.mcc.fred.client.EmptyB\nZ\x08.;clientb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010.;client'
  _VERSION_VERSIONENTRY._options = None
  _VERSION_VERSIONENTRY._serialized_options = b'8\001'
  _USERROLE._serialized_start=2205
  _USERROLE._serialized_end=2320
  _EMPTY._serialized_start=33
  _EMPTY._serialized_end=40
  _VERSION._serialized_start=42
  _VERSION._serialized_end=155
  _VERSION_VERSIONENTRY._serialized_start=109
  _VERSION_VERSIONENTRY._serialized_end=155
  _CREATEKEYGROUPREQUEST._serialized_start=157
  _CREATEKEYGROUPREQUEST._serialized_end=231
  _DELETEKEYGROUPREQUEST._serialized_start=233
  _DELETEKEYGROUPREQUEST._serialized_end=274
  _READREQUEST._serialized_start=276
  _READREQUEST._serialized_end=363
  _ITEM._serialized_start=365
  _ITEM._serialized_end=439
  _READRESPONSE._serialized_start=441
  _READRESPONSE._serialized_end=492
  _SCANREQUEST._serialized_start=494
  _SCANREQUEST._serialized_end=552
  _SCANRESPONSE._serialized_start=554
  _SCANRESPONSE._serialized_end=605
  _KEYSREQUEST._serialized_start=607
  _KEYSREQUEST._serialized_end=665
  _KEY._serialized_start=667
  _KEY._serialized_end=727
  _KEYSRESPONSE._serialized_start=729
  _KEYSRESPONSE._serialized_end=779
  _UPDATEREQUEST._serialized_start=781
  _UPDATEREQUEST._serialized_end=884
  _UPDATERESPONSE._serialized_start=886
  _UPDATERESPONSE._serialized_end=945
  _APPENDREQUEST._serialized_start=947
  _APPENDREQUEST._serialized_end=1006
  _APPENDRESPONSE._serialized_start=1008
  _APPENDRESPONSE._serialized_end=1036
  _DELETEREQUEST._serialized_start=1038
  _DELETEREQUEST._serialized_end=1127
  _DELETERESPONSE._serialized_start=1129
  _DELETERESPONSE._serialized_end=1188
  _ADDREPLICAREQUEST._serialized_start=1190
  _ADDREPLICAREQUEST._serialized_end=1259
  _GETKEYGROUPINFOREQUEST._serialized_start=1261
  _GETKEYGROUPINFOREQUEST._serialized_end=1303
  _GETKEYGROUPINFORESPONSE._serialized_start=1305
  _GETKEYGROUPINFORESPONSE._serialized_end=1398
  _KEYGROUPREPLICA._serialized_start=1400
  _KEYGROUPREPLICA._serialized_end=1463
  _REMOVEREPLICAREQUEST._serialized_start=1465
  _REMOVEREPLICAREQUEST._serialized_end=1521
  _GETREPLICAREQUEST._serialized_start=1523
  _GETREPLICAREQUEST._serialized_end=1558
  _GETREPLICARESPONSE._serialized_start=1560
  _GETREPLICARESPONSE._serialized_end=1610
  _REPLICA._serialized_start=1612
  _REPLICA._serialized_end=1651
  _GETALLREPLICARESPONSE._serialized_start=1653
  _GETALLREPLICARESPONSE._serialized_end=1720
  _GETKEYGROUPTRIGGERREQUEST._serialized_start=1722
  _GETKEYGROUPTRIGGERREQUEST._serialized_end=1767
  _GETKEYGROUPTRIGGERRESPONSE._serialized_start=1769
  _GETKEYGROUPTRIGGERRESPONSE._serialized_end=1841
  _TRIGGER._serialized_start=1843
  _TRIGGER._serialized_end=1878
  _ADDTRIGGERREQUEST._serialized_start=1880
  _ADDTRIGGERREQUEST._serialized_end=1957
  _REMOVETRIGGERREQUEST._serialized_start=1959
  _REMOVETRIGGERREQUEST._serialized_end=2018
  _ADDUSERREQUEST._serialized_start=2020
  _ADDUSERREQUEST._serialized_end=2109
  _REMOVEUSERREQUEST._serialized_start=2111
  _REMOVEUSERREQUEST._serialized_end=2203
  _CLIENT._serialized_start=2323
  _CLIENT._serialized_end=3759
# @@protoc_insertion_point(module_scope)
