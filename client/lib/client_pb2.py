# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63lient.proto\",\n\x0cStoreRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06secret\x18\x02 \x01(\t\".\n\rStoreResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x1f\n\x0fRetrieveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"1\n\x10RetrieveResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x32v\n\x0bSecretStore\x12.\n\x0bStoreSecret\x12\r.StoreRequest\x1a\x0e.StoreResponse\"\x00\x12\x37\n\x0eRetrieveSecret\x12\x10.RetrieveRequest\x1a\x11.RetrieveResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STOREREQUEST']._serialized_start=16
  _globals['_STOREREQUEST']._serialized_end=60
  _globals['_STORERESPONSE']._serialized_start=62
  _globals['_STORERESPONSE']._serialized_end=108
  _globals['_RETRIEVEREQUEST']._serialized_start=110
  _globals['_RETRIEVEREQUEST']._serialized_end=141
  _globals['_RETRIEVERESPONSE']._serialized_start=143
  _globals['_RETRIEVERESPONSE']._serialized_end=192
  _globals['_SECRETSTORE']._serialized_start=194
  _globals['_SECRETSTORE']._serialized_end=312
# @@protoc_insertion_point(module_scope)
