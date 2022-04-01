# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.datacatalog_v1beta1.proto import (
    policytagmanager_pb2 as google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2,
)
from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class PolicyTagManagerStub(object):
    """The policy tag manager API service allows clients to manage their taxonomies
    and policy tags.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.CreateTaxonomy = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/CreateTaxonomy",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.CreateTaxonomyRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.Taxonomy.FromString,
        )
        self.DeleteTaxonomy = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/DeleteTaxonomy",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.DeleteTaxonomyRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdateTaxonomy = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/UpdateTaxonomy",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.UpdateTaxonomyRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.Taxonomy.FromString,
        )
        self.ListTaxonomies = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/ListTaxonomies",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.ListTaxonomiesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.ListTaxonomiesResponse.FromString,
        )
        self.GetTaxonomy = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/GetTaxonomy",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.GetTaxonomyRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.Taxonomy.FromString,
        )
        self.CreatePolicyTag = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/CreatePolicyTag",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.CreatePolicyTagRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.PolicyTag.FromString,
        )
        self.DeletePolicyTag = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/DeletePolicyTag",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.DeletePolicyTagRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdatePolicyTag = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/UpdatePolicyTag",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.UpdatePolicyTagRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.PolicyTag.FromString,
        )
        self.ListPolicyTags = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/ListPolicyTags",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.ListPolicyTagsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.ListPolicyTagsResponse.FromString,
        )
        self.GetPolicyTag = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/GetPolicyTag",
            request_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.GetPolicyTagRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.PolicyTag.FromString,
        )
        self.GetIamPolicy = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/GetIamPolicy",
            request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString,
            response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString,
        )
        self.SetIamPolicy = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/SetIamPolicy",
            request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString,
            response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString,
        )
        self.TestIamPermissions = channel.unary_unary(
            "/google.cloud.datacatalog.v1beta1.PolicyTagManager/TestIamPermissions",
            request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString,
            response_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString,
        )


class PolicyTagManagerServicer(object):
    """The policy tag manager API service allows clients to manage their taxonomies
    and policy tags.
    """

    def CreateTaxonomy(self, request, context):
        """Creates a taxonomy in the specified project."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteTaxonomy(self, request, context):
        """Deletes a taxonomy. This operation will also delete all
        policy tags in this taxonomy along with their associated policies.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateTaxonomy(self, request, context):
        """Updates a taxonomy."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListTaxonomies(self, request, context):
        """Lists all taxonomies in a project in a particular location that the caller
        has permission to view.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTaxonomy(self, request, context):
        """Gets a taxonomy."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreatePolicyTag(self, request, context):
        """Creates a policy tag in the specified taxonomy."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeletePolicyTag(self, request, context):
        """Deletes a policy tag. Also deletes all of its descendant policy tags."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdatePolicyTag(self, request, context):
        """Updates a policy tag."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListPolicyTags(self, request, context):
        """Lists all policy tags in a taxonomy."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetPolicyTag(self, request, context):
        """Gets a policy tag."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetIamPolicy(self, request, context):
        """Gets the IAM policy for a taxonomy or a policy tag."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SetIamPolicy(self, request, context):
        """Sets the IAM policy for a taxonomy or a policy tag."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TestIamPermissions(self, request, context):
        """Returns the permissions that a caller has on the specified taxonomy or
        policy tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PolicyTagManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateTaxonomy": grpc.unary_unary_rpc_method_handler(
            servicer.CreateTaxonomy,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.CreateTaxonomyRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.Taxonomy.SerializeToString,
        ),
        "DeleteTaxonomy": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteTaxonomy,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.DeleteTaxonomyRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "UpdateTaxonomy": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateTaxonomy,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.UpdateTaxonomyRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.Taxonomy.SerializeToString,
        ),
        "ListTaxonomies": grpc.unary_unary_rpc_method_handler(
            servicer.ListTaxonomies,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.ListTaxonomiesRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.ListTaxonomiesResponse.SerializeToString,
        ),
        "GetTaxonomy": grpc.unary_unary_rpc_method_handler(
            servicer.GetTaxonomy,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.GetTaxonomyRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.Taxonomy.SerializeToString,
        ),
        "CreatePolicyTag": grpc.unary_unary_rpc_method_handler(
            servicer.CreatePolicyTag,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.CreatePolicyTagRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.PolicyTag.SerializeToString,
        ),
        "DeletePolicyTag": grpc.unary_unary_rpc_method_handler(
            servicer.DeletePolicyTag,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.DeletePolicyTagRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "UpdatePolicyTag": grpc.unary_unary_rpc_method_handler(
            servicer.UpdatePolicyTag,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.UpdatePolicyTagRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.PolicyTag.SerializeToString,
        ),
        "ListPolicyTags": grpc.unary_unary_rpc_method_handler(
            servicer.ListPolicyTags,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.ListPolicyTagsRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.ListPolicyTagsResponse.SerializeToString,
        ),
        "GetPolicyTag": grpc.unary_unary_rpc_method_handler(
            servicer.GetPolicyTag,
            request_deserializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.GetPolicyTagRequest.FromString,
            response_serializer=google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_policytagmanager__pb2.PolicyTag.SerializeToString,
        ),
        "GetIamPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.GetIamPolicy,
            request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.FromString,
            response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString,
        ),
        "SetIamPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.SetIamPolicy,
            request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.FromString,
            response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString,
        ),
        "TestIamPermissions": grpc.unary_unary_rpc_method_handler(
            servicer.TestIamPermissions,
            request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.FromString,
            response_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.datacatalog.v1beta1.PolicyTagManager", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
