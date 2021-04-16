# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.datacatalog_v1.types import policytagmanager
from google.iam.v1 import iam_policy_pb2 as iam_policy  # type: ignore
from google.iam.v1 import policy_pb2 as gi_policy  # type: ignore
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import PolicyTagManagerTransport, DEFAULT_CLIENT_INFO


class PolicyTagManagerGrpcTransport(PolicyTagManagerTransport):
    """gRPC backend transport for PolicyTagManager.

    Policy Tag Manager API service allows clients to manage their
    policy tags and taxonomies.

    Policy tags are used to tag BigQuery columns and apply
    additional access control policies. A taxonomy is a hierarchical
    grouping of policy tags that classify data along a common axis.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "datacatalog.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "datacatalog.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def create_taxonomy(
        self,
    ) -> Callable[[policytagmanager.CreateTaxonomyRequest], policytagmanager.Taxonomy]:
        r"""Return a callable for the create taxonomy method over gRPC.

        Creates a taxonomy in a specified project. The
        taxonomy is initially empty, i.e., does not contain
        policy tags.

        Returns:
            Callable[[~.CreateTaxonomyRequest],
                    ~.Taxonomy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_taxonomy" not in self._stubs:
            self._stubs["create_taxonomy"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/CreateTaxonomy",
                request_serializer=policytagmanager.CreateTaxonomyRequest.serialize,
                response_deserializer=policytagmanager.Taxonomy.deserialize,
            )
        return self._stubs["create_taxonomy"]

    @property
    def delete_taxonomy(
        self,
    ) -> Callable[[policytagmanager.DeleteTaxonomyRequest], empty.Empty]:
        r"""Return a callable for the delete taxonomy method over gRPC.

        Deletes a taxonomy. This method will also delete all
        policy tags in this taxonomy, their associated policies,
        and the policy tags references from BigQuery columns.

        Returns:
            Callable[[~.DeleteTaxonomyRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_taxonomy" not in self._stubs:
            self._stubs["delete_taxonomy"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/DeleteTaxonomy",
                request_serializer=policytagmanager.DeleteTaxonomyRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_taxonomy"]

    @property
    def update_taxonomy(
        self,
    ) -> Callable[[policytagmanager.UpdateTaxonomyRequest], policytagmanager.Taxonomy]:
        r"""Return a callable for the update taxonomy method over gRPC.

        Updates a taxonomy. This method can update the
        taxonomy's display name, description, and activated
        policy types.

        Returns:
            Callable[[~.UpdateTaxonomyRequest],
                    ~.Taxonomy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_taxonomy" not in self._stubs:
            self._stubs["update_taxonomy"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/UpdateTaxonomy",
                request_serializer=policytagmanager.UpdateTaxonomyRequest.serialize,
                response_deserializer=policytagmanager.Taxonomy.deserialize,
            )
        return self._stubs["update_taxonomy"]

    @property
    def list_taxonomies(
        self,
    ) -> Callable[
        [policytagmanager.ListTaxonomiesRequest],
        policytagmanager.ListTaxonomiesResponse,
    ]:
        r"""Return a callable for the list taxonomies method over gRPC.

        Lists all taxonomies in a project in a particular
        location that the caller has permission to view.

        Returns:
            Callable[[~.ListTaxonomiesRequest],
                    ~.ListTaxonomiesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_taxonomies" not in self._stubs:
            self._stubs["list_taxonomies"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/ListTaxonomies",
                request_serializer=policytagmanager.ListTaxonomiesRequest.serialize,
                response_deserializer=policytagmanager.ListTaxonomiesResponse.deserialize,
            )
        return self._stubs["list_taxonomies"]

    @property
    def get_taxonomy(
        self,
    ) -> Callable[[policytagmanager.GetTaxonomyRequest], policytagmanager.Taxonomy]:
        r"""Return a callable for the get taxonomy method over gRPC.

        Gets a taxonomy.

        Returns:
            Callable[[~.GetTaxonomyRequest],
                    ~.Taxonomy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_taxonomy" not in self._stubs:
            self._stubs["get_taxonomy"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/GetTaxonomy",
                request_serializer=policytagmanager.GetTaxonomyRequest.serialize,
                response_deserializer=policytagmanager.Taxonomy.deserialize,
            )
        return self._stubs["get_taxonomy"]

    @property
    def create_policy_tag(
        self,
    ) -> Callable[
        [policytagmanager.CreatePolicyTagRequest], policytagmanager.PolicyTag
    ]:
        r"""Return a callable for the create policy tag method over gRPC.

        Creates a policy tag in a taxonomy.

        Returns:
            Callable[[~.CreatePolicyTagRequest],
                    ~.PolicyTag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_policy_tag" not in self._stubs:
            self._stubs["create_policy_tag"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/CreatePolicyTag",
                request_serializer=policytagmanager.CreatePolicyTagRequest.serialize,
                response_deserializer=policytagmanager.PolicyTag.deserialize,
            )
        return self._stubs["create_policy_tag"]

    @property
    def delete_policy_tag(
        self,
    ) -> Callable[[policytagmanager.DeletePolicyTagRequest], empty.Empty]:
        r"""Return a callable for the delete policy tag method over gRPC.

        Deletes a policy tag. This method also deletes:

        -  all of its descendant policy tags, if any
        -  the policies associated with the policy tag and its
           descendants
        -  references from BigQuery table schema of the policy tag and
           its descendants.

        Returns:
            Callable[[~.DeletePolicyTagRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_policy_tag" not in self._stubs:
            self._stubs["delete_policy_tag"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/DeletePolicyTag",
                request_serializer=policytagmanager.DeletePolicyTagRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_policy_tag"]

    @property
    def update_policy_tag(
        self,
    ) -> Callable[
        [policytagmanager.UpdatePolicyTagRequest], policytagmanager.PolicyTag
    ]:
        r"""Return a callable for the update policy tag method over gRPC.

        Updates a policy tag. This method can update the
        policy tag's display name, description, and parent
        policy tag.

        Returns:
            Callable[[~.UpdatePolicyTagRequest],
                    ~.PolicyTag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_policy_tag" not in self._stubs:
            self._stubs["update_policy_tag"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/UpdatePolicyTag",
                request_serializer=policytagmanager.UpdatePolicyTagRequest.serialize,
                response_deserializer=policytagmanager.PolicyTag.deserialize,
            )
        return self._stubs["update_policy_tag"]

    @property
    def list_policy_tags(
        self,
    ) -> Callable[
        [policytagmanager.ListPolicyTagsRequest],
        policytagmanager.ListPolicyTagsResponse,
    ]:
        r"""Return a callable for the list policy tags method over gRPC.

        Lists all policy tags in a taxonomy.

        Returns:
            Callable[[~.ListPolicyTagsRequest],
                    ~.ListPolicyTagsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_policy_tags" not in self._stubs:
            self._stubs["list_policy_tags"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/ListPolicyTags",
                request_serializer=policytagmanager.ListPolicyTagsRequest.serialize,
                response_deserializer=policytagmanager.ListPolicyTagsResponse.deserialize,
            )
        return self._stubs["list_policy_tags"]

    @property
    def get_policy_tag(
        self,
    ) -> Callable[[policytagmanager.GetPolicyTagRequest], policytagmanager.PolicyTag]:
        r"""Return a callable for the get policy tag method over gRPC.

        Gets a policy tag.

        Returns:
            Callable[[~.GetPolicyTagRequest],
                    ~.PolicyTag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_policy_tag" not in self._stubs:
            self._stubs["get_policy_tag"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/GetPolicyTag",
                request_serializer=policytagmanager.GetPolicyTagRequest.serialize,
                response_deserializer=policytagmanager.PolicyTag.deserialize,
            )
        return self._stubs["get_policy_tag"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy.GetIamPolicyRequest], gi_policy.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the IAM policy for a policy tag or a taxonomy.

        Returns:
            Callable[[~.GetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/GetIamPolicy",
                request_serializer=iam_policy.GetIamPolicyRequest.SerializeToString,
                response_deserializer=gi_policy.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy.SetIamPolicyRequest], gi_policy.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the IAM policy for a policy tag or a taxonomy.

        Returns:
            Callable[[~.SetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/SetIamPolicy",
                request_serializer=iam_policy.SetIamPolicyRequest.SerializeToString,
                response_deserializer=gi_policy.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy.TestIamPermissionsRequest], iam_policy.TestIamPermissionsResponse
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.

        Returns the permissions that a caller has on a
        specified policy tag or taxonomy.

        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    ~.TestIamPermissionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                "/google.cloud.datacatalog.v1.PolicyTagManager/TestIamPermissions",
                request_serializer=iam_policy.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]


__all__ = ("PolicyTagManagerGrpcTransport",)
