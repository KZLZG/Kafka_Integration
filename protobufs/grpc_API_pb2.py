# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc-API.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egrpc-API.proto\x12\x07grpcApi\"\x80\x01\n\x12PostNewPostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\x05\x12\x12\n\nchannel_id\x18\x02 \x01(\x05\x12\x14\n\x0c\x63hannel_name\x18\x03 \x01(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x11\n\tdate_sent\x18\x06 \x01(\t\"%\n\x13PostNewPostResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\".\n\x18GetPostsByChannelRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\x05\"G\n\x19GetPostsByChannelResponse\x12*\n\x05posts\x18\x01 \x03(\x0b\x32\x1b.grpcApi.PostNewPostRequest\"\'\n\x15GetSubChannelsRequest\x12\x0e\n\x06sub_id\x18\x01 \x01(\x05\"q\n\x13SubChannelsResponse\x12\x0e\n\x06sub_id\x18\x01 \x01(\x05\x12\x12\n\nchannel_id\x18\x02 \x01(\x05\x12\x14\n\x0c\x63hannel_name\x18\x03 \x01(\t\x12\r\n\x05topic\x18\x04 \x01(\t\x12\x11\n\tsub_count\x18\x05 \x01(\x05\"H\n\x16GetSubChannelsResponse\x12.\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x1c.grpcApi.SubChannelsResponse\"*\n\x17\x45rrorInDelieveryRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\x05\"*\n\x18\x45rrorInDelieveryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"7\n\x11PostNewSubRequest\x12\x0e\n\x06sub_id\x18\x01 \x01(\x05\x12\x12\n\nchannel_id\x18\x02 \x01(\x05\"$\n\x12PostNewSubResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x32Y\n\rBrokerService\x12H\n\x0bPostNewPost\x12\x1b.grpcApi.PostNewPostRequest\x1a\x1c.grpcApi.PostNewPostResponse2\xdf\x02\n\x0e\x42\x61\x63kendService\x12Z\n\x11GetPostsByChannel\x12!.grpcApi.GetPostsByChannelRequest\x1a\".grpcApi.GetPostsByChannelResponse\x12Q\n\x0eGetSubChannels\x12\x1e.grpcApi.GetSubChannelsRequest\x1a\x1f.grpcApi.GetSubChannelsResponse\x12W\n\x10\x45rrorInDelievery\x12 .grpcApi.ErrorInDelieveryRequest\x1a!.grpcApi.ErrorInDelieveryResponse\x12\x45\n\nPostNewSub\x12\x1a.grpcApi.PostNewSubRequest\x1a\x1b.grpcApi.PostNewSubResponse2\x0c\n\nBotServiceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_API_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_POSTNEWPOSTREQUEST']._serialized_start=28
  _globals['_POSTNEWPOSTREQUEST']._serialized_end=156
  _globals['_POSTNEWPOSTRESPONSE']._serialized_start=158
  _globals['_POSTNEWPOSTRESPONSE']._serialized_end=195
  _globals['_GETPOSTSBYCHANNELREQUEST']._serialized_start=197
  _globals['_GETPOSTSBYCHANNELREQUEST']._serialized_end=243
  _globals['_GETPOSTSBYCHANNELRESPONSE']._serialized_start=245
  _globals['_GETPOSTSBYCHANNELRESPONSE']._serialized_end=316
  _globals['_GETSUBCHANNELSREQUEST']._serialized_start=318
  _globals['_GETSUBCHANNELSREQUEST']._serialized_end=357
  _globals['_SUBCHANNELSRESPONSE']._serialized_start=359
  _globals['_SUBCHANNELSRESPONSE']._serialized_end=472
  _globals['_GETSUBCHANNELSRESPONSE']._serialized_start=474
  _globals['_GETSUBCHANNELSRESPONSE']._serialized_end=546
  _globals['_ERRORINDELIEVERYREQUEST']._serialized_start=548
  _globals['_ERRORINDELIEVERYREQUEST']._serialized_end=590
  _globals['_ERRORINDELIEVERYRESPONSE']._serialized_start=592
  _globals['_ERRORINDELIEVERYRESPONSE']._serialized_end=634
  _globals['_POSTNEWSUBREQUEST']._serialized_start=636
  _globals['_POSTNEWSUBREQUEST']._serialized_end=691
  _globals['_POSTNEWSUBRESPONSE']._serialized_start=693
  _globals['_POSTNEWSUBRESPONSE']._serialized_end=729
  _globals['_BROKERSERVICE']._serialized_start=731
  _globals['_BROKERSERVICE']._serialized_end=820
  _globals['_BACKENDSERVICE']._serialized_start=823
  _globals['_BACKENDSERVICE']._serialized_end=1174
  _globals['_BOTSERVICE']._serialized_start=1176
  _globals['_BOTSERVICE']._serialized_end=1188
# @@protoc_insertion_point(module_scope)
