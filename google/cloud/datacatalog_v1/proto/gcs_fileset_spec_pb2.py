# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog_v1/proto/gcs_fileset_spec.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.datacatalog_v1.proto import timestamps_pb2 as google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_timestamps__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datacatalog_v1/proto/gcs_fileset_spec.proto',
  package='google.cloud.datacatalog.v1',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.datacatalog.v1P\001ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\370\001\001\252\002\033Google.Cloud.DataCatalog.V1\312\002\033Google\\Cloud\\DataCatalog\\V1\352\002\036Google::Cloud::DataCatalog::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/cloud/datacatalog_v1/proto/gcs_fileset_spec.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x32google/cloud/datacatalog_v1/proto/timestamps.proto\"z\n\x0eGcsFilesetSpec\x12\x1a\n\rfile_patterns\x18\x01 \x03(\tB\x03\xe0\x41\x02\x12L\n\x15sample_gcs_file_specs\x18\x02 \x03(\x0b\x32(.google.cloud.datacatalog.v1.GcsFileSpecB\x03\xe0\x41\x03\"\x8a\x01\n\x0bGcsFileSpec\x12\x16\n\tfile_path\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12J\n\x0egcs_timestamps\x18\x02 \x01(\x0b\x32-.google.cloud.datacatalog.v1.SystemTimestampsB\x03\xe0\x41\x03\x12\x17\n\nsize_bytes\x18\x04 \x01(\x03\x42\x03\xe0\x41\x03\x42\xcb\x01\n\x1f\x63om.google.cloud.datacatalog.v1P\x01ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\xf8\x01\x01\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_timestamps__pb2.DESCRIPTOR,])




_GCSFILESETSPEC = _descriptor.Descriptor(
  name='GcsFilesetSpec',
  full_name='google.cloud.datacatalog.v1.GcsFilesetSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_patterns', full_name='google.cloud.datacatalog.v1.GcsFilesetSpec.file_patterns', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_gcs_file_specs', full_name='google.cloud.datacatalog.v1.GcsFilesetSpec.sample_gcs_file_specs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=296,
)


_GCSFILESPEC = _descriptor.Descriptor(
  name='GcsFileSpec',
  full_name='google.cloud.datacatalog.v1.GcsFileSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='google.cloud.datacatalog.v1.GcsFileSpec.file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gcs_timestamps', full_name='google.cloud.datacatalog.v1.GcsFileSpec.gcs_timestamps', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size_bytes', full_name='google.cloud.datacatalog.v1.GcsFileSpec.size_bytes', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=437,
)

_GCSFILESETSPEC.fields_by_name['sample_gcs_file_specs'].message_type = _GCSFILESPEC
_GCSFILESPEC.fields_by_name['gcs_timestamps'].message_type = google_dot_cloud_dot_datacatalog__v1_dot_proto_dot_timestamps__pb2._SYSTEMTIMESTAMPS
DESCRIPTOR.message_types_by_name['GcsFilesetSpec'] = _GCSFILESETSPEC
DESCRIPTOR.message_types_by_name['GcsFileSpec'] = _GCSFILESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GcsFilesetSpec = _reflection.GeneratedProtocolMessageType('GcsFilesetSpec', (_message.Message,), {
  'DESCRIPTOR' : _GCSFILESETSPEC,
  '__module__' : 'google.cloud.datacatalog_v1.proto.gcs_fileset_spec_pb2'
  ,
  '__doc__': """Describes a Cloud Storage fileset entry.
  
  Attributes:
      file_patterns:
          Required. Patterns to identify a set of files in Google Cloud
          Storage. See `Cloud Storage documentation <https://cloud.googl
          e.com/storage/docs/gsutil/addlhelp/WildcardNames>`__ for more
          information. Note that bucket wildcards are currently not
          supported.  Examples of valid file_patterns:  -
          ``gs://bucket_name/dir/*``: matches all files within
          ``bucket_name/dir`` directory. -  ``gs://bucket_name/dir/**``:
          matches all files in ``bucket_name/dir``    spanning all
          subdirectories. -  ``gs://bucket_name/file*``: matches files
          prefixed by ``file`` in    ``bucket_name`` -
          ``gs://bucket_name/??.txt``: matches files with two characters
          followed by ``.txt`` in ``bucket_name`` -
          ``gs://bucket_name/[aeiou].txt``: matches files that contain a
          single    vowel character followed by ``.txt`` in
          ``bucket_name`` -  ``gs://bucket_name/[a-m].txt``: matches
          files that contain ``a``,    ``b``, … or ``m`` followed by
          ``.txt`` in ``bucket_name`` -  ``gs://bucket_name/a/*/b``:
          matches all files in ``bucket_name`` that    match ``a/*/b``
          pattern, such as ``a/c/b``, ``a/d/b`` -
          ``gs://another_bucket/a.txt``: matches
          ``gs://another_bucket/a.txt``  You can combine wildcards to
          provide more powerful matches, for example:  -
          ``gs://bucket_name/[a-m]??.j*g``
      sample_gcs_file_specs:
          Output only. Sample files contained in this fileset, not all
          files contained in this fileset are represented here.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.GcsFilesetSpec)
  })
_sym_db.RegisterMessage(GcsFilesetSpec)

GcsFileSpec = _reflection.GeneratedProtocolMessageType('GcsFileSpec', (_message.Message,), {
  'DESCRIPTOR' : _GCSFILESPEC,
  '__module__' : 'google.cloud.datacatalog_v1.proto.gcs_fileset_spec_pb2'
  ,
  '__doc__': """Specifications of a single file in Cloud Storage.
  
  Attributes:
      file_path:
          Required. The full file path. Example:
          ``gs://bucket_name/a/b.txt``.
      gcs_timestamps:
          Output only. Timestamps about the Cloud Storage file.
      size_bytes:
          Output only. The size of the file, in bytes.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.GcsFileSpec)
  })
_sym_db.RegisterMessage(GcsFileSpec)


DESCRIPTOR._options = None
_GCSFILESETSPEC.fields_by_name['file_patterns']._options = None
_GCSFILESETSPEC.fields_by_name['sample_gcs_file_specs']._options = None
_GCSFILESPEC.fields_by_name['file_path']._options = None
_GCSFILESPEC.fields_by_name['gcs_timestamps']._options = None
_GCSFILESPEC.fields_by_name['size_bytes']._options = None
# @@protoc_insertion_point(module_scope)
