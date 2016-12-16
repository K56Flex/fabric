# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/configuration.proto',
  package='common',
  syntax='proto3',
  serialized_pb=_b('\n\x1a\x63ommon/configuration.proto\x12\x06\x63ommon\x1a\x13\x63ommon/common.proto\"G\n\x15\x43onfigurationEnvelope\x12.\n\x05Items\x18\x01 \x03(\x0b\x32\x1f.common.SignedConfigurationItem\"h\n\x17SignedConfigurationItem\x12\x19\n\x11\x43onfigurationItem\x18\x01 \x01(\x0c\x12\x32\n\nSignatures\x18\x02 \x03(\x0b\x32\x1e.common.ConfigurationSignature\"\x86\x02\n\x11\x43onfigurationItem\x12#\n\x06Header\x18\x01 \x01(\x0b\x32\x13.common.ChainHeader\x12\x39\n\x04Type\x18\x02 \x01(\x0e\x32+.common.ConfigurationItem.ConfigurationType\x12\x14\n\x0cLastModified\x18\x03 \x01(\x04\x12\x1a\n\x12ModificationPolicy\x18\x04 \x01(\t\x12\x0b\n\x03Key\x18\x05 \x01(\t\x12\r\n\x05Value\x18\x06 \x01(\x0c\"C\n\x11\x43onfigurationType\x12\n\n\x06Policy\x10\x00\x12\t\n\x05\x43hain\x10\x01\x12\x0b\n\x07Orderer\x10\x02\x12\n\n\x06\x46\x61\x62ric\x10\x03\"D\n\x16\x43onfigurationSignature\x12\x17\n\x0fsignatureHeader\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\'\n\x0f\x43\x65rtificateList\x12\x14\n\x0c\x43\x65rtificates\x18\x01 \x03(\x0c\"L\n\x06Policy\x12:\n\x0fSignaturePolicy\x18\x01 \x01(\x0b\x32\x1f.common.SignaturePolicyEnvelopeH\x00\x42\x06\n\x04Type\"g\n\x17SignaturePolicyEnvelope\x12\x0f\n\x07Version\x18\x01 \x01(\x05\x12\'\n\x06Policy\x18\x02 \x01(\x0b\x32\x17.common.SignaturePolicy\x12\x12\n\nIdentities\x18\x03 \x03(\x0c\"\x9d\x01\n\x0fSignaturePolicy\x12\x12\n\x08SignedBy\x18\x01 \x01(\x05H\x00\x12.\n\x04\x46rom\x18\x02 \x01(\x0b\x32\x1e.common.SignaturePolicy.NOutOfH\x00\x1a>\n\x06NOutOf\x12\t\n\x01N\x18\x01 \x01(\x05\x12)\n\x08Policies\x18\x02 \x03(\x0b\x32\x17.common.SignaturePolicyB\x06\n\x04TypeB-Z+github.com/hyperledger/fabric/protos/commonb\x06proto3')
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CONFIGURATIONITEM_CONFIGURATIONTYPE = _descriptor.EnumDescriptor(
  name='ConfigurationType',
  full_name='common.ConfigurationItem.ConfigurationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Policy', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Chain', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Orderer', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Fabric', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=434,
  serialized_end=501,
)
_sym_db.RegisterEnumDescriptor(_CONFIGURATIONITEM_CONFIGURATIONTYPE)


_CONFIGURATIONENVELOPE = _descriptor.Descriptor(
  name='ConfigurationEnvelope',
  full_name='common.ConfigurationEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Items', full_name='common.ConfigurationEnvelope.Items', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=130,
)


_SIGNEDCONFIGURATIONITEM = _descriptor.Descriptor(
  name='SignedConfigurationItem',
  full_name='common.SignedConfigurationItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ConfigurationItem', full_name='common.SignedConfigurationItem.ConfigurationItem', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Signatures', full_name='common.SignedConfigurationItem.Signatures', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=236,
)


_CONFIGURATIONITEM = _descriptor.Descriptor(
  name='ConfigurationItem',
  full_name='common.ConfigurationItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Header', full_name='common.ConfigurationItem.Header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='common.ConfigurationItem.Type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastModified', full_name='common.ConfigurationItem.LastModified', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ModificationPolicy', full_name='common.ConfigurationItem.ModificationPolicy', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Key', full_name='common.ConfigurationItem.Key', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Value', full_name='common.ConfigurationItem.Value', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIGURATIONITEM_CONFIGURATIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=501,
)


_CONFIGURATIONSIGNATURE = _descriptor.Descriptor(
  name='ConfigurationSignature',
  full_name='common.ConfigurationSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signatureHeader', full_name='common.ConfigurationSignature.signatureHeader', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='common.ConfigurationSignature.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=571,
)


_CERTIFICATELIST = _descriptor.Descriptor(
  name='CertificateList',
  full_name='common.CertificateList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Certificates', full_name='common.CertificateList.Certificates', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=612,
)


_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='common.Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SignaturePolicy', full_name='common.Policy.SignaturePolicy', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='common.Policy.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=614,
  serialized_end=690,
)


_SIGNATUREPOLICYENVELOPE = _descriptor.Descriptor(
  name='SignaturePolicyEnvelope',
  full_name='common.SignaturePolicyEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Version', full_name='common.SignaturePolicyEnvelope.Version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Policy', full_name='common.SignaturePolicyEnvelope.Policy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Identities', full_name='common.SignaturePolicyEnvelope.Identities', index=2,
      number=3, type=12, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=692,
  serialized_end=795,
)


_SIGNATUREPOLICY_NOUTOF = _descriptor.Descriptor(
  name='NOutOf',
  full_name='common.SignaturePolicy.NOutOf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='N', full_name='common.SignaturePolicy.NOutOf.N', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Policies', full_name='common.SignaturePolicy.NOutOf.Policies', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=947,
)

_SIGNATUREPOLICY = _descriptor.Descriptor(
  name='SignaturePolicy',
  full_name='common.SignaturePolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SignedBy', full_name='common.SignaturePolicy.SignedBy', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='From', full_name='common.SignaturePolicy.From', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREPOLICY_NOUTOF, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='common.SignaturePolicy.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=798,
  serialized_end=955,
)

_CONFIGURATIONENVELOPE.fields_by_name['Items'].message_type = _SIGNEDCONFIGURATIONITEM
_SIGNEDCONFIGURATIONITEM.fields_by_name['Signatures'].message_type = _CONFIGURATIONSIGNATURE
_CONFIGURATIONITEM.fields_by_name['Header'].message_type = common_dot_common__pb2._CHAINHEADER
_CONFIGURATIONITEM.fields_by_name['Type'].enum_type = _CONFIGURATIONITEM_CONFIGURATIONTYPE
_CONFIGURATIONITEM_CONFIGURATIONTYPE.containing_type = _CONFIGURATIONITEM
_POLICY.fields_by_name['SignaturePolicy'].message_type = _SIGNATUREPOLICYENVELOPE
_POLICY.oneofs_by_name['Type'].fields.append(
  _POLICY.fields_by_name['SignaturePolicy'])
_POLICY.fields_by_name['SignaturePolicy'].containing_oneof = _POLICY.oneofs_by_name['Type']
_SIGNATUREPOLICYENVELOPE.fields_by_name['Policy'].message_type = _SIGNATUREPOLICY
_SIGNATUREPOLICY_NOUTOF.fields_by_name['Policies'].message_type = _SIGNATUREPOLICY
_SIGNATUREPOLICY_NOUTOF.containing_type = _SIGNATUREPOLICY
_SIGNATUREPOLICY.fields_by_name['From'].message_type = _SIGNATUREPOLICY_NOUTOF
_SIGNATUREPOLICY.oneofs_by_name['Type'].fields.append(
  _SIGNATUREPOLICY.fields_by_name['SignedBy'])
_SIGNATUREPOLICY.fields_by_name['SignedBy'].containing_oneof = _SIGNATUREPOLICY.oneofs_by_name['Type']
_SIGNATUREPOLICY.oneofs_by_name['Type'].fields.append(
  _SIGNATUREPOLICY.fields_by_name['From'])
_SIGNATUREPOLICY.fields_by_name['From'].containing_oneof = _SIGNATUREPOLICY.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['ConfigurationEnvelope'] = _CONFIGURATIONENVELOPE
DESCRIPTOR.message_types_by_name['SignedConfigurationItem'] = _SIGNEDCONFIGURATIONITEM
DESCRIPTOR.message_types_by_name['ConfigurationItem'] = _CONFIGURATIONITEM
DESCRIPTOR.message_types_by_name['ConfigurationSignature'] = _CONFIGURATIONSIGNATURE
DESCRIPTOR.message_types_by_name['CertificateList'] = _CERTIFICATELIST
DESCRIPTOR.message_types_by_name['Policy'] = _POLICY
DESCRIPTOR.message_types_by_name['SignaturePolicyEnvelope'] = _SIGNATUREPOLICYENVELOPE
DESCRIPTOR.message_types_by_name['SignaturePolicy'] = _SIGNATUREPOLICY

ConfigurationEnvelope = _reflection.GeneratedProtocolMessageType('ConfigurationEnvelope', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONENVELOPE,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.ConfigurationEnvelope)
  ))
_sym_db.RegisterMessage(ConfigurationEnvelope)

SignedConfigurationItem = _reflection.GeneratedProtocolMessageType('SignedConfigurationItem', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDCONFIGURATIONITEM,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.SignedConfigurationItem)
  ))
_sym_db.RegisterMessage(SignedConfigurationItem)

ConfigurationItem = _reflection.GeneratedProtocolMessageType('ConfigurationItem', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONITEM,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.ConfigurationItem)
  ))
_sym_db.RegisterMessage(ConfigurationItem)

ConfigurationSignature = _reflection.GeneratedProtocolMessageType('ConfigurationSignature', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONSIGNATURE,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.ConfigurationSignature)
  ))
_sym_db.RegisterMessage(ConfigurationSignature)

CertificateList = _reflection.GeneratedProtocolMessageType('CertificateList', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATELIST,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.CertificateList)
  ))
_sym_db.RegisterMessage(CertificateList)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), dict(
  DESCRIPTOR = _POLICY,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.Policy)
  ))
_sym_db.RegisterMessage(Policy)

SignaturePolicyEnvelope = _reflection.GeneratedProtocolMessageType('SignaturePolicyEnvelope', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATUREPOLICYENVELOPE,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.SignaturePolicyEnvelope)
  ))
_sym_db.RegisterMessage(SignaturePolicyEnvelope)

SignaturePolicy = _reflection.GeneratedProtocolMessageType('SignaturePolicy', (_message.Message,), dict(

  NOutOf = _reflection.GeneratedProtocolMessageType('NOutOf', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATUREPOLICY_NOUTOF,
    __module__ = 'common.configuration_pb2'
    # @@protoc_insertion_point(class_scope:common.SignaturePolicy.NOutOf)
    ))
  ,
  DESCRIPTOR = _SIGNATUREPOLICY,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.SignaturePolicy)
  ))
_sym_db.RegisterMessage(SignaturePolicy)
_sym_db.RegisterMessage(SignaturePolicy.NOutOf)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/hyperledger/fabric/protos/common'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
