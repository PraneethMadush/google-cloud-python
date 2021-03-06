# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.datacatalog_v1beta1.proto import (
    datacatalog_pb2 as google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_datacatalog__pb2,
)


class DataCatalogStub(object):
    """Cloud Data Catalog is a service that allows clients to discover,
  manage, and understand their Google Cloud data resources.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.LookupEntry = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.DataCatalog/LookupEntry",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_datacatalog__pb2.LookupEntryRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_datacatalog__pb2.Entry.FromString,
        )


class DataCatalogServicer(object):
    """Cloud Data Catalog is a service that allows clients to discover,
  manage, and understand their Google Cloud data resources.
  """

    def LookupEntry(self, request, context):
        """Get an entry by target resource name. This method allows clients to use
    the resource name from the source Google Cloud Platform service to get the
    Cloud Data Catalog Entry.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DataCatalogServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "LookupEntry": grpc.unary_unary_rpc_method_handler(
            servicer.LookupEntry,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_datacatalog__pb2.LookupEntryRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_datacatalog__pb2.Entry.SerializeToString,
        )
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.datacatalog.v1beta1.DataCatalog", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
