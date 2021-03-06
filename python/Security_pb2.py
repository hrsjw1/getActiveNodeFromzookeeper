# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Security.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Security.proto',
  package='hadoop.common',
  serialized_pb='\n\x0eSecurity.proto\x12\rhadoop.common\"Q\n\nTokenProto\x12\x12\n\nidentifier\x18\x01 \x02(\x0c\x12\x10\n\x08password\x18\x02 \x02(\x0c\x12\x0c\n\x04kind\x18\x03 \x02(\t\x12\x0f\n\x07service\x18\x04 \x02(\t\"]\n\x12\x43redentialsKVProto\x12\r\n\x05\x61lias\x18\x01 \x02(\t\x12(\n\x05token\x18\x02 \x01(\x0b\x32\x19.hadoop.common.TokenProto\x12\x0e\n\x06secret\x18\x03 \x01(\x0c\"y\n\x10\x43redentialsProto\x12\x31\n\x06tokens\x18\x01 \x03(\x0b\x32!.hadoop.common.CredentialsKVProto\x12\x32\n\x07secrets\x18\x02 \x03(\x0b\x32!.hadoop.common.CredentialsKVProto\"1\n\x1eGetDelegationTokenRequestProto\x12\x0f\n\x07renewer\x18\x01 \x02(\t\"K\n\x1fGetDelegationTokenResponseProto\x12(\n\x05token\x18\x01 \x01(\x0b\x32\x19.hadoop.common.TokenProto\"L\n RenewDelegationTokenRequestProto\x12(\n\x05token\x18\x01 \x02(\x0b\x32\x19.hadoop.common.TokenProto\":\n!RenewDelegationTokenResponseProto\x12\x15\n\rnewExpiryTime\x18\x01 \x02(\x04\"M\n!CancelDelegationTokenRequestProto\x12(\n\x05token\x18\x01 \x02(\x0b\x32\x19.hadoop.common.TokenProto\"$\n\"CancelDelegationTokenResponseProtoB8\n org.apache.hadoop.security.protoB\x0eSecurityProtos\x88\x01\x01\xa0\x01\x01')




_TOKENPROTO = _descriptor.Descriptor(
  name='TokenProto',
  full_name='hadoop.common.TokenProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='hadoop.common.TokenProto.identifier', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='hadoop.common.TokenProto.password', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kind', full_name='hadoop.common.TokenProto.kind', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service', full_name='hadoop.common.TokenProto.service', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=33,
  serialized_end=114,
)


_CREDENTIALSKVPROTO = _descriptor.Descriptor(
  name='CredentialsKVProto',
  full_name='hadoop.common.CredentialsKVProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alias', full_name='hadoop.common.CredentialsKVProto.alias', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='hadoop.common.CredentialsKVProto.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secret', full_name='hadoop.common.CredentialsKVProto.secret', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=116,
  serialized_end=209,
)


_CREDENTIALSPROTO = _descriptor.Descriptor(
  name='CredentialsProto',
  full_name='hadoop.common.CredentialsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tokens', full_name='hadoop.common.CredentialsProto.tokens', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secrets', full_name='hadoop.common.CredentialsProto.secrets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=211,
  serialized_end=332,
)


_GETDELEGATIONTOKENREQUESTPROTO = _descriptor.Descriptor(
  name='GetDelegationTokenRequestProto',
  full_name='hadoop.common.GetDelegationTokenRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='renewer', full_name='hadoop.common.GetDelegationTokenRequestProto.renewer', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=334,
  serialized_end=383,
)


_GETDELEGATIONTOKENRESPONSEPROTO = _descriptor.Descriptor(
  name='GetDelegationTokenResponseProto',
  full_name='hadoop.common.GetDelegationTokenResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='hadoop.common.GetDelegationTokenResponseProto.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=385,
  serialized_end=460,
)


_RENEWDELEGATIONTOKENREQUESTPROTO = _descriptor.Descriptor(
  name='RenewDelegationTokenRequestProto',
  full_name='hadoop.common.RenewDelegationTokenRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='hadoop.common.RenewDelegationTokenRequestProto.token', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=462,
  serialized_end=538,
)


_RENEWDELEGATIONTOKENRESPONSEPROTO = _descriptor.Descriptor(
  name='RenewDelegationTokenResponseProto',
  full_name='hadoop.common.RenewDelegationTokenResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newExpiryTime', full_name='hadoop.common.RenewDelegationTokenResponseProto.newExpiryTime', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=540,
  serialized_end=598,
)


_CANCELDELEGATIONTOKENREQUESTPROTO = _descriptor.Descriptor(
  name='CancelDelegationTokenRequestProto',
  full_name='hadoop.common.CancelDelegationTokenRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='hadoop.common.CancelDelegationTokenRequestProto.token', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=600,
  serialized_end=677,
)


_CANCELDELEGATIONTOKENRESPONSEPROTO = _descriptor.Descriptor(
  name='CancelDelegationTokenResponseProto',
  full_name='hadoop.common.CancelDelegationTokenResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=679,
  serialized_end=715,
)

_CREDENTIALSKVPROTO.fields_by_name['token'].message_type = _TOKENPROTO
_CREDENTIALSPROTO.fields_by_name['tokens'].message_type = _CREDENTIALSKVPROTO
_CREDENTIALSPROTO.fields_by_name['secrets'].message_type = _CREDENTIALSKVPROTO
_GETDELEGATIONTOKENRESPONSEPROTO.fields_by_name['token'].message_type = _TOKENPROTO
_RENEWDELEGATIONTOKENREQUESTPROTO.fields_by_name['token'].message_type = _TOKENPROTO
_CANCELDELEGATIONTOKENREQUESTPROTO.fields_by_name['token'].message_type = _TOKENPROTO
DESCRIPTOR.message_types_by_name['TokenProto'] = _TOKENPROTO
DESCRIPTOR.message_types_by_name['CredentialsKVProto'] = _CREDENTIALSKVPROTO
DESCRIPTOR.message_types_by_name['CredentialsProto'] = _CREDENTIALSPROTO
DESCRIPTOR.message_types_by_name['GetDelegationTokenRequestProto'] = _GETDELEGATIONTOKENREQUESTPROTO
DESCRIPTOR.message_types_by_name['GetDelegationTokenResponseProto'] = _GETDELEGATIONTOKENRESPONSEPROTO
DESCRIPTOR.message_types_by_name['RenewDelegationTokenRequestProto'] = _RENEWDELEGATIONTOKENREQUESTPROTO
DESCRIPTOR.message_types_by_name['RenewDelegationTokenResponseProto'] = _RENEWDELEGATIONTOKENRESPONSEPROTO
DESCRIPTOR.message_types_by_name['CancelDelegationTokenRequestProto'] = _CANCELDELEGATIONTOKENREQUESTPROTO
DESCRIPTOR.message_types_by_name['CancelDelegationTokenResponseProto'] = _CANCELDELEGATIONTOKENRESPONSEPROTO

class TokenProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TOKENPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.TokenProto)

class CredentialsKVProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREDENTIALSKVPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.CredentialsKVProto)

class CredentialsProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREDENTIALSPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.CredentialsProto)

class GetDelegationTokenRequestProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETDELEGATIONTOKENREQUESTPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.GetDelegationTokenRequestProto)

class GetDelegationTokenResponseProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETDELEGATIONTOKENRESPONSEPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.GetDelegationTokenResponseProto)

class RenewDelegationTokenRequestProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RENEWDELEGATIONTOKENREQUESTPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.RenewDelegationTokenRequestProto)

class RenewDelegationTokenResponseProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RENEWDELEGATIONTOKENRESPONSEPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.RenewDelegationTokenResponseProto)

class CancelDelegationTokenRequestProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CANCELDELEGATIONTOKENREQUESTPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.CancelDelegationTokenRequestProto)

class CancelDelegationTokenResponseProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CANCELDELEGATIONTOKENRESPONSEPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.CancelDelegationTokenResponseProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n org.apache.hadoop.security.protoB\016SecurityProtos\210\001\001\240\001\001')
# @@protoc_insertion_point(module_scope)
