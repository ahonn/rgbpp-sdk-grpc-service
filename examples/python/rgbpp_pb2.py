# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rgbpp.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0brgbpp.proto\x12\x05rgbpp\"4\n\x0fRgbppLockParams\x12\x10\n\x08outIndex\x18\x01 \x01(\x05\x12\x0f\n\x07\x62tcTxId\x18\x02 \x01(\t\"\x1d\n\rRgbppLockArgs\x12\x0c\n\x04\x61rgs\x18\x01 \x01(\t2W\n\x0fRgbppSdkService\x12\x44\n\x12\x42uildRgbppLockArgs\x12\x16.rgbpp.RgbppLockParams\x1a\x14.rgbpp.RgbppLockArgs\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rgbpp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RGBPPLOCKPARAMS']._serialized_start=22
  _globals['_RGBPPLOCKPARAMS']._serialized_end=74
  _globals['_RGBPPLOCKARGS']._serialized_start=76
  _globals['_RGBPPLOCKARGS']._serialized_end=105
  _globals['_RGBPPSDKSERVICE']._serialized_start=107
  _globals['_RGBPPSDKSERVICE']._serialized_end=194
# @@protoc_insertion_point(module_scope)
