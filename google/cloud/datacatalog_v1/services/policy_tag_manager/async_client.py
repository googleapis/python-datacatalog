# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore

from google.cloud.datacatalog_v1.services.policy_tag_manager import pagers
from google.cloud.datacatalog_v1.types import policytagmanager, timestamps

from .client import PolicyTagManagerClient
from .transports.base import DEFAULT_CLIENT_INFO, PolicyTagManagerTransport
from .transports.grpc_asyncio import PolicyTagManagerGrpcAsyncIOTransport


class PolicyTagManagerAsyncClient:
    """Policy Tag Manager API service allows you to manage your
    policy tags and taxonomies.

    Policy tags are used to tag BigQuery columns and apply
    additional access control policies. A taxonomy is a hierarchical
    grouping of policy tags that classify data along a common axis.
    """

    _client: PolicyTagManagerClient

    DEFAULT_ENDPOINT = PolicyTagManagerClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PolicyTagManagerClient.DEFAULT_MTLS_ENDPOINT

    policy_tag_path = staticmethod(PolicyTagManagerClient.policy_tag_path)
    parse_policy_tag_path = staticmethod(PolicyTagManagerClient.parse_policy_tag_path)
    taxonomy_path = staticmethod(PolicyTagManagerClient.taxonomy_path)
    parse_taxonomy_path = staticmethod(PolicyTagManagerClient.parse_taxonomy_path)
    common_billing_account_path = staticmethod(
        PolicyTagManagerClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        PolicyTagManagerClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(PolicyTagManagerClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        PolicyTagManagerClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        PolicyTagManagerClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        PolicyTagManagerClient.parse_common_organization_path
    )
    common_project_path = staticmethod(PolicyTagManagerClient.common_project_path)
    parse_common_project_path = staticmethod(
        PolicyTagManagerClient.parse_common_project_path
    )
    common_location_path = staticmethod(PolicyTagManagerClient.common_location_path)
    parse_common_location_path = staticmethod(
        PolicyTagManagerClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PolicyTagManagerAsyncClient: The constructed client.
        """
        return PolicyTagManagerClient.from_service_account_info.__func__(PolicyTagManagerAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PolicyTagManagerAsyncClient: The constructed client.
        """
        return PolicyTagManagerClient.from_service_account_file.__func__(PolicyTagManagerAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return PolicyTagManagerClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> PolicyTagManagerTransport:
        """Returns the transport used by the client instance.

        Returns:
            PolicyTagManagerTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(PolicyTagManagerClient).get_transport_class, type(PolicyTagManagerClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, PolicyTagManagerTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the policy tag manager client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PolicyTagManagerTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = PolicyTagManagerClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_taxonomy(
        self,
        request: Union[policytagmanager.CreateTaxonomyRequest, dict] = None,
        *,
        parent: str = None,
        taxonomy: policytagmanager.Taxonomy = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanager.Taxonomy:
        r"""Creates a taxonomy in a specified project.
        The taxonomy is initially empty, that is, it doesn't
        contain policy tags.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_create_taxonomy():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.CreateTaxonomyRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_taxonomy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.CreateTaxonomyRequest, dict]):
                The request object. Request message for
                [CreateTaxonomy][google.cloud.datacatalog.v1.PolicyTagManager.CreateTaxonomy].
            parent (:class:`str`):
                Required. Resource name of the
                project that the taxonomy will belong
                to.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            taxonomy (:class:`google.cloud.datacatalog_v1.types.Taxonomy`):
                The taxonomy to create.
                This corresponds to the ``taxonomy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.Taxonomy:
                A taxonomy is a collection of hierarchical policy tags that classify data
                   along a common axis.

                   For example, a "data sensitivity" taxonomy might
                   contain the following policy tags:

                   :literal:`\` + PII   + Account number   + Age   + SSN   + Zipcode + Financials   + Revenue`\ \`

                   A "data origin" taxonomy might contain the following
                   policy tags:

                   :literal:`\` + User data + Employee data + Partner data + Public data`\ \`

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, taxonomy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.CreateTaxonomyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if taxonomy is not None:
            request.taxonomy = taxonomy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_taxonomy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_taxonomy(
        self,
        request: Union[policytagmanager.DeleteTaxonomyRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a taxonomy, including all policy tags in this
        taxonomy, their associated policies, and the policy tags
        references from BigQuery columns.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_delete_taxonomy():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.DeleteTaxonomyRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_taxonomy(request=request)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.DeleteTaxonomyRequest, dict]):
                The request object. Request message for
                [DeleteTaxonomy][google.cloud.datacatalog.v1.PolicyTagManager.DeleteTaxonomy].
            name (:class:`str`):
                Required. Resource name of the
                taxonomy to delete.
                Note: All policy tags in this taxonomy
                are also deleted.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.DeleteTaxonomyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_taxonomy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def update_taxonomy(
        self,
        request: Union[policytagmanager.UpdateTaxonomyRequest, dict] = None,
        *,
        taxonomy: policytagmanager.Taxonomy = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanager.Taxonomy:
        r"""Updates a taxonomy, including its display name,
        description, and activated policy types.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_update_taxonomy():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.UpdateTaxonomyRequest(
                )

                # Make the request
                response = await client.update_taxonomy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.UpdateTaxonomyRequest, dict]):
                The request object. Request message for
                [UpdateTaxonomy][google.cloud.datacatalog.v1.PolicyTagManager.UpdateTaxonomy].
            taxonomy (:class:`google.cloud.datacatalog_v1.types.Taxonomy`):
                The taxonomy to update. You can
                update only its description, display
                name, and activated policy types.

                This corresponds to the ``taxonomy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.Taxonomy:
                A taxonomy is a collection of hierarchical policy tags that classify data
                   along a common axis.

                   For example, a "data sensitivity" taxonomy might
                   contain the following policy tags:

                   :literal:`\` + PII   + Account number   + Age   + SSN   + Zipcode + Financials   + Revenue`\ \`

                   A "data origin" taxonomy might contain the following
                   policy tags:

                   :literal:`\` + User data + Employee data + Partner data + Public data`\ \`

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([taxonomy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.UpdateTaxonomyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if taxonomy is not None:
            request.taxonomy = taxonomy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_taxonomy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("taxonomy.name", request.taxonomy.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_taxonomies(
        self,
        request: Union[policytagmanager.ListTaxonomiesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTaxonomiesAsyncPager:
        r"""Lists all taxonomies in a project in a particular
        location that you have a permission to view.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_list_taxonomies():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.ListTaxonomiesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_taxonomies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.ListTaxonomiesRequest, dict]):
                The request object. Request message for
                [ListTaxonomies][google.cloud.datacatalog.v1.PolicyTagManager.ListTaxonomies].
            parent (:class:`str`):
                Required. Resource name of the
                project to list the taxonomies of.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.services.policy_tag_manager.pagers.ListTaxonomiesAsyncPager:
                Response message for
                   [ListTaxonomies][google.cloud.datacatalog.v1.PolicyTagManager.ListTaxonomies].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.ListTaxonomiesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_taxonomies,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTaxonomiesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_taxonomy(
        self,
        request: Union[policytagmanager.GetTaxonomyRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanager.Taxonomy:
        r"""Gets a taxonomy.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_get_taxonomy():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.GetTaxonomyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_taxonomy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.GetTaxonomyRequest, dict]):
                The request object. Request message for
                [GetTaxonomy][google.cloud.datacatalog.v1.PolicyTagManager.GetTaxonomy].
            name (:class:`str`):
                Required. Resource name of the
                taxonomy to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.Taxonomy:
                A taxonomy is a collection of hierarchical policy tags that classify data
                   along a common axis.

                   For example, a "data sensitivity" taxonomy might
                   contain the following policy tags:

                   :literal:`\` + PII   + Account number   + Age   + SSN   + Zipcode + Financials   + Revenue`\ \`

                   A "data origin" taxonomy might contain the following
                   policy tags:

                   :literal:`\` + User data + Employee data + Partner data + Public data`\ \`

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.GetTaxonomyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_taxonomy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_policy_tag(
        self,
        request: Union[policytagmanager.CreatePolicyTagRequest, dict] = None,
        *,
        parent: str = None,
        policy_tag: policytagmanager.PolicyTag = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanager.PolicyTag:
        r"""Creates a policy tag in a taxonomy.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_create_policy_tag():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.CreatePolicyTagRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_policy_tag(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.CreatePolicyTagRequest, dict]):
                The request object. Request message for
                [CreatePolicyTag][google.cloud.datacatalog.v1.PolicyTagManager.CreatePolicyTag].
            parent (:class:`str`):
                Required. Resource name of the
                taxonomy that the policy tag will belong
                to.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy_tag (:class:`google.cloud.datacatalog_v1.types.PolicyTag`):
                The policy tag to create.
                This corresponds to the ``policy_tag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.PolicyTag:
                Denotes one policy tag in a taxonomy, for example, SSN.

                   Policy tags can be defined in a hierarchy. For
                   example:

                   :literal:`\` + Geolocation   + LatLong   + City   + ZipCode`\ \`

                   Where the "Geolocation" policy tag contains three
                   children.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, policy_tag])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.CreatePolicyTagRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if policy_tag is not None:
            request.policy_tag = policy_tag

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_policy_tag,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_policy_tag(
        self,
        request: Union[policytagmanager.DeletePolicyTagRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a policy tag together with the following:

        -  All of its descendant policy tags, if any
        -  Policies associated with the policy tag and its descendants
        -  References from BigQuery table schema of the policy tag and
           its descendants

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_delete_policy_tag():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.DeletePolicyTagRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_policy_tag(request=request)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.DeletePolicyTagRequest, dict]):
                The request object. Request message for
                [DeletePolicyTag][google.cloud.datacatalog.v1.PolicyTagManager.DeletePolicyTag].
            name (:class:`str`):
                Required. Resource name of the policy
                tag to delete.
                Note: All of its descendant policy tags
                are also deleted.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.DeletePolicyTagRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_policy_tag,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def update_policy_tag(
        self,
        request: Union[policytagmanager.UpdatePolicyTagRequest, dict] = None,
        *,
        policy_tag: policytagmanager.PolicyTag = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanager.PolicyTag:
        r"""Updates a policy tag, including its display
        name, description, and parent policy tag.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_update_policy_tag():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.UpdatePolicyTagRequest(
                )

                # Make the request
                response = await client.update_policy_tag(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.UpdatePolicyTagRequest, dict]):
                The request object. Request message for
                [UpdatePolicyTag][google.cloud.datacatalog.v1.PolicyTagManager.UpdatePolicyTag].
            policy_tag (:class:`google.cloud.datacatalog_v1.types.PolicyTag`):
                The policy tag to update. You can
                update only its description, display
                name, and parent policy tag fields.

                This corresponds to the ``policy_tag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.PolicyTag:
                Denotes one policy tag in a taxonomy, for example, SSN.

                   Policy tags can be defined in a hierarchy. For
                   example:

                   :literal:`\` + Geolocation   + LatLong   + City   + ZipCode`\ \`

                   Where the "Geolocation" policy tag contains three
                   children.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([policy_tag])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.UpdatePolicyTagRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if policy_tag is not None:
            request.policy_tag = policy_tag

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_policy_tag,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("policy_tag.name", request.policy_tag.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_policy_tags(
        self,
        request: Union[policytagmanager.ListPolicyTagsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPolicyTagsAsyncPager:
        r"""Lists all policy tags in a taxonomy.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_list_policy_tags():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.ListPolicyTagsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_policy_tags(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.ListPolicyTagsRequest, dict]):
                The request object. Request message for
                [ListPolicyTags][google.cloud.datacatalog.v1.PolicyTagManager.ListPolicyTags].
            parent (:class:`str`):
                Required. Resource name of the
                taxonomy to list the policy tags of.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.services.policy_tag_manager.pagers.ListPolicyTagsAsyncPager:
                Response message for
                   [ListPolicyTags][google.cloud.datacatalog.v1.PolicyTagManager.ListPolicyTags].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.ListPolicyTagsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_policy_tags,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListPolicyTagsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_policy_tag(
        self,
        request: Union[policytagmanager.GetPolicyTagRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanager.PolicyTag:
        r"""Gets a policy tag.

        .. code-block:: python

            from google.cloud import datacatalog_v1

            async def sample_get_policy_tag():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1.GetPolicyTagRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_policy_tag(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1.types.GetPolicyTagRequest, dict]):
                The request object. Request message for
                [GetPolicyTag][google.cloud.datacatalog.v1.PolicyTagManager.GetPolicyTag].
            name (:class:`str`):
                Required. Resource name of the policy
                tag.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.PolicyTag:
                Denotes one policy tag in a taxonomy, for example, SSN.

                   Policy tags can be defined in a hierarchy. For
                   example:

                   :literal:`\` + Geolocation   + LatLong   + City   + ZipCode`\ \`

                   Where the "Geolocation" policy tag contains three
                   children.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policytagmanager.GetPolicyTagRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_policy_tag,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_iam_policy(
        self,
        request: Union[iam_policy_pb2.GetIamPolicyRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the IAM policy for a policy tag or a taxonomy.

        .. code-block:: python

            from google.cloud import datacatalog_v1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            async def sample_get_iam_policy():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.GetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = await client.get_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]):
                The request object. Request message for `GetIamPolicy`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.v1.policy_pb2.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](\ https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                      {
                         "bindings": [
                            {
                               "role":
                               "roles/resourcemanager.organizationAdmin",
                               "members": [ "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                               ]

                            }, { "role":
                            "roles/resourcemanager.organizationViewer",
                            "members": [ "user:eve@example.com" ],
                            "condition": { "title": "expirable access",
                            "description": "Does not grant access after
                            Sep 2020", "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')", } }

                         ], "etag": "BwWWja0YfJA=", "version": 3

                      }

                   **YAML example:**

                      bindings: - members: - user:\ mike@example.com -
                      group:\ admins@example.com - domain:google.com -
                      serviceAccount:\ my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin -
                      members: - user:\ eve@example.com role:
                      roles/resourcemanager.organizationViewer
                      condition: title: expirable access description:
                      Does not grant access after Sep 2020 expression:
                      request.time <
                      timestamp('2020-10-01T00:00:00.000Z') etag:
                      BwWWja0YfJA= version: 3

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](\ https://cloud.google.com/iam/docs/).

        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.GetIamPolicyRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_iam_policy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_iam_policy(
        self,
        request: Union[iam_policy_pb2.SetIamPolicyRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the IAM policy for a policy tag or a taxonomy.

        .. code-block:: python

            from google.cloud import datacatalog_v1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            async def sample_set_iam_policy():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.SetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = await client.set_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]):
                The request object. Request message for `SetIamPolicy`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.v1.policy_pb2.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](\ https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                      {
                         "bindings": [
                            {
                               "role":
                               "roles/resourcemanager.organizationAdmin",
                               "members": [ "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                               ]

                            }, { "role":
                            "roles/resourcemanager.organizationViewer",
                            "members": [ "user:eve@example.com" ],
                            "condition": { "title": "expirable access",
                            "description": "Does not grant access after
                            Sep 2020", "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')", } }

                         ], "etag": "BwWWja0YfJA=", "version": 3

                      }

                   **YAML example:**

                      bindings: - members: - user:\ mike@example.com -
                      group:\ admins@example.com - domain:google.com -
                      serviceAccount:\ my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin -
                      members: - user:\ eve@example.com role:
                      roles/resourcemanager.organizationViewer
                      condition: title: expirable access description:
                      Does not grant access after Sep 2020 expression:
                      request.time <
                      timestamp('2020-10-01T00:00:00.000Z') etag:
                      BwWWja0YfJA= version: 3

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](\ https://cloud.google.com/iam/docs/).

        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.SetIamPolicyRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_iam_policy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def test_iam_permissions(
        self,
        request: Union[iam_policy_pb2.TestIamPermissionsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Returns your permissions on a specified policy tag or
        taxonomy.

        .. code-block:: python

            from google.cloud import datacatalog_v1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            async def sample_test_iam_permissions():
                # Create a client
                client = datacatalog_v1.PolicyTagManagerAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.TestIamPermissionsRequest(
                    resource="resource_value",
                    permissions=['permissions_value_1', 'permissions_value_2'],
                )

                # Make the request
                response = await client.test_iam_permissions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]):
                The request object. Request message for
                `TestIamPermissions` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse:
                Response message for TestIamPermissions method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.TestIamPermissionsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.test_iam_permissions,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-datacatalog",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("PolicyTagManagerAsyncClient",)
