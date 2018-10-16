# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HAZKInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='HAZKInfo.proto',
  package='hadoop.hdfs',
  serialized_pb='\n\x0eHAZKInfo.proto\x12\x0bhadoop.hdfs\"m\n\x0e\x41\x63tiveNodeInfo\x12\x15\n\rnameserviceId\x18\x01 \x02(\t\x12\x12\n\nnamenodeId\x18\x02 \x02(\t\x12\x10\n\x08hostname\x18\x03 \x02(\t\x12\x0c\n\x04port\x18\x04 \x02(\x05\x12\x10\n\x08zkfcPort\x18\x05 \x02(\x05\x42\x41\n/org.apache.hadoop.hdfs.server.namenode.ha.protoB\x0eHAZKInfoProtos')




_ACTIVENODEINFO = _descriptor.Descriptor(
  name='ActiveNodeInfo',
  full_name='hadoop.hdfs.ActiveNodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nameserviceId', full_name='hadoop.hdfs.ActiveNodeInfo.nameserviceId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='namenodeId', full_name='hadoop.hdfs.ActiveNodeInfo.namenodeId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='hadoop.hdfs.ActiveNodeInfo.hostname', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='hadoop.hdfs.ActiveNodeInfo.port', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zkfcPort', full_name='hadoop.hdfs.ActiveNodeInfo.zkfcPort', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=31,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['ActiveNodeInfo'] = _ACTIVENODEINFO

class ActiveNodeInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACTIVENODEINFO

  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ActiveNodeInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n/org.apache.hadoop.hdfs.server.namenode.ha.protoB\016HAZKInfoProtos')
# @@protoc_insertion_point(module_scope)