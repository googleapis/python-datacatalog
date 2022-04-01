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

from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.datacatalog_v1beta1.types import policytagmanager
from google.cloud.datacatalog_v1beta1.types import policytagmanagerserialization

from .transports.base import PolicyTagManagerSerializationTransport
from .transports.grpc_asyncio import PolicyTagManagerSerializationGrpcAsyncIOTransport
from .client import PolicyTagManagerSerializationClient


class PolicyTagManagerSerializationAsyncClient:
    """Policy tag manager serialization API service allows clients
    to manipulate their taxonomies and policy tags data with
    serialized format.
    """

    _client: PolicyTagManagerSerializationClient

    DEFAULT_ENDPOINT = PolicyTagManagerSerializationClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PolicyTagManagerSerializationClient.DEFAULT_MTLS_ENDPOINT

    from_service_account_file = (
        PolicyTagManagerSerializationClient.from_service_account_file
    )
    from_service_account_json = from_service_account_file

    get_transport_class = functools.partial(
        type(PolicyTagManagerSerializationClient).get_transport_class,
        type(PolicyTagManagerSerializationClient),
    )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, PolicyTagManagerSerializationTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
    ) -> None:
        """Instantiate the policy tag manager serialization client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PolicyTagManagerSerializationTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint, this is the default value for
                the environment variable) and "auto" (auto switch to the default
                mTLS endpoint if client SSL credentials is present). However,
                the ``api_endpoint`` property takes precedence if provided.
                (2) The ``client_cert_source`` property is used to provide client
                SSL credentials for mutual TLS transport. If not provided, the
                default SSL credentials will be used if present.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """

        self._client = PolicyTagManagerSerializationClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
        )

    async def import_taxonomies(
        self,
        request: policytagmanagerserialization.ImportTaxonomiesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanagerserialization.ImportTaxonomiesResponse:
        r"""Imports all taxonomies and their policy tags to a
        project as new taxonomies.

        This method provides a bulk taxonomy / policy tag
        creation using nested proto structure.

        Args:
            request (:class:`~.policytagmanagerserialization.ImportTaxonomiesRequest`):
                The request object. Request message for
                [ImportTaxonomies][google.cloud.datacatalog.v1beta1.PolicyTagManagerSerialization.ImportTaxonomies].

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.policytagmanagerserialization.ImportTaxonomiesResponse:
                Response message for
                [ImportTaxonomies][google.cloud.datacatalog.v1beta1.PolicyTagManagerSerialization.ImportTaxonomies].

        """
        # Create or coerce a protobuf request object.

        request = policytagmanagerserialization.ImportTaxonomiesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.import_taxonomies,
            default_timeout=None,
            client_info=_client_info,
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

    async def export_taxonomies(
        self,
        request: policytagmanagerserialization.ExportTaxonomiesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanagerserialization.ExportTaxonomiesResponse:
        r"""Exports all taxonomies and their policy tags in a
        project.
        This method generates SerializedTaxonomy protos with
        nested policy tags that can be used as an input for
        future ImportTaxonomies calls.

        Args:
            request (:class:`~.policytagmanagerserialization.ExportTaxonomiesRequest`):
                The request object. Request message for
                [ExportTaxonomies][google.cloud.datacatalog.v1beta1.PolicyTagManagerSerialization.ExportTaxonomies].

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.policytagmanagerserialization.ExportTaxonomiesResponse:
                Response message for
                [ExportTaxonomies][google.cloud.datacatalog.v1beta1.PolicyTagManagerSerialization.ExportTaxonomies].

        """
        # Create or coerce a protobuf request object.

        request = policytagmanagerserialization.ExportTaxonomiesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.export_taxonomies,
            default_timeout=None,
            client_info=_client_info,
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


try:
    _client_info = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-datacatalog",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    _client_info = gapic_v1.client_info.ClientInfo()


__all__ = ("PolicyTagManagerSerializationAsyncClient",)
