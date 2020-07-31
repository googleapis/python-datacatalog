# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog_v1beta1/proto/common.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datacatalog_v1beta1/proto/common.proto',
  package='google.cloud.datacatalog.v1beta1',
  syntax='proto3',
  serialized_options=b'\n$com.google.cloud.datacatalog.v1beta1P\001ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\370\001\001\252\002 Google.Cloud.DataCatalog.V1Beta1\312\002 Google\\Cloud\\DataCatalog\\V1beta1\352\002#Google::Cloud::DataCatalog::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3google/cloud/datacatalog_v1beta1/proto/common.proto\x12 google.cloud.datacatalog.v1beta1*U\n\x10IntegratedSystem\x12!\n\x1dINTEGRATED_SYSTEM_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x42IGQUERY\x10\x01\x12\x10\n\x0c\x43LOUD_PUBSUB\x10\x02\x42\xe4\x01\n$com.google.cloud.datacatalog.v1beta1P\x01ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\xf8\x01\x01\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3'
)

_INTEGRATEDSYSTEM = _descriptor.EnumDescriptor(
  name='IntegratedSystem',
  full_name='google.cloud.datacatalog.v1beta1.IntegratedSystem',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INTEGRATED_SYSTEM_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BIGQUERY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLOUD_PUBSUB', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=89,
  serialized_end=174,
)
_sym_db.RegisterEnumDescriptor(_INTEGRATEDSYSTEM)

IntegratedSystem = enum_type_wrapper.EnumTypeWrapper(_INTEGRATEDSYSTEM)
INTEGRATED_SYSTEM_UNSPECIFIED = 0
BIGQUERY = 1
CLOUD_PUBSUB = 2


DESCRIPTOR.enum_types_by_name['IntegratedSystem'] = _INTEGRATEDSYSTEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
