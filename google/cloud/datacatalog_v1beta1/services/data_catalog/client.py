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
import os
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore

from google.cloud.datacatalog_v1beta1.services.data_catalog import pagers
from google.cloud.datacatalog_v1beta1.types import (
    common,
    datacatalog,
    gcs_fileset_spec,
    schema,
    search,
    table_spec,
    tags,
    timestamps,
)

from .transports.base import DEFAULT_CLIENT_INFO, DataCatalogTransport
from .transports.grpc import DataCatalogGrpcTransport
from .transports.grpc_asyncio import DataCatalogGrpcAsyncIOTransport


class DataCatalogClientMeta(type):
    """Metaclass for the DataCatalog client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[DataCatalogTransport]]
    _transport_registry["grpc"] = DataCatalogGrpcTransport
    _transport_registry["grpc_asyncio"] = DataCatalogGrpcAsyncIOTransport

    def get_transport_class(
        cls,
        label: str = None,
    ) -> Type[DataCatalogTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class DataCatalogClient(metaclass=DataCatalogClientMeta):
    """Data Catalog API service allows clients to discover,
    understand, and manage their data.
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "datacatalog.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
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
            DataCatalogClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

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
            DataCatalogClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> DataCatalogTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataCatalogTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def entry_path(
        project: str,
        location: str,
        entry_group: str,
        entry: str,
    ) -> str:
        """Returns a fully-qualified entry string."""
        return "projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}".format(
            project=project,
            location=location,
            entry_group=entry_group,
            entry=entry,
        )

    @staticmethod
    def parse_entry_path(path: str) -> Dict[str, str]:
        """Parses a entry path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/entryGroups/(?P<entry_group>.+?)/entries/(?P<entry>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def entry_group_path(
        project: str,
        location: str,
        entry_group: str,
    ) -> str:
        """Returns a fully-qualified entry_group string."""
        return (
            "projects/{project}/locations/{location}/entryGroups/{entry_group}".format(
                project=project,
                location=location,
                entry_group=entry_group,
            )
        )

    @staticmethod
    def parse_entry_group_path(path: str) -> Dict[str, str]:
        """Parses a entry_group path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/entryGroups/(?P<entry_group>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def tag_path(
        project: str,
        location: str,
        entry_group: str,
        entry: str,
        tag: str,
    ) -> str:
        """Returns a fully-qualified tag string."""
        return "projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}/tags/{tag}".format(
            project=project,
            location=location,
            entry_group=entry_group,
            entry=entry,
            tag=tag,
        )

    @staticmethod
    def parse_tag_path(path: str) -> Dict[str, str]:
        """Parses a tag path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/entryGroups/(?P<entry_group>.+?)/entries/(?P<entry>.+?)/tags/(?P<tag>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def tag_template_path(
        project: str,
        location: str,
        tag_template: str,
    ) -> str:
        """Returns a fully-qualified tag_template string."""
        return "projects/{project}/locations/{location}/tagTemplates/{tag_template}".format(
            project=project,
            location=location,
            tag_template=tag_template,
        )

    @staticmethod
    def parse_tag_template_path(path: str) -> Dict[str, str]:
        """Parses a tag_template path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/tagTemplates/(?P<tag_template>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def tag_template_field_path(
        project: str,
        location: str,
        tag_template: str,
        field: str,
    ) -> str:
        """Returns a fully-qualified tag_template_field string."""
        return "projects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{field}".format(
            project=project,
            location=location,
            tag_template=tag_template,
            field=field,
        )

    @staticmethod
    def parse_tag_template_field_path(path: str) -> Dict[str, str]:
        """Parses a tag_template_field path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/tagTemplates/(?P<tag_template>.+?)/fields/(?P<field>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
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
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, DataCatalogTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the data catalog client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, DataCatalogTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
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
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(
            client_options
        )

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, DataCatalogTransport):
            # transport is a DataCatalogTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
            )

    def search_catalog(
        self,
        request: Union[datacatalog.SearchCatalogRequest, dict] = None,
        *,
        scope: datacatalog.SearchCatalogRequest.Scope = None,
        query: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.SearchCatalogPager:
        r"""Searches Data Catalog for multiple resources like entries, tags
        that match a query.

        This is a custom method
        (https://cloud.google.com/apis/design/custom_methods) and does
        not return the complete resource, only the resource identifier
        and high level fields. Clients can subsequentally call ``Get``
        methods.

        Note that Data Catalog search queries do not guarantee full
        recall. Query results that match your query may not be returned,
        even in subsequent result pages. Also note that results returned
        (and not returned) can vary across repeated search queries.

        See `Data Catalog Search
        Syntax <https://cloud.google.com/data-catalog/docs/how-to/search-reference>`__
        for more information.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_search_catalog():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.SearchCatalogRequest(
                    query="query_value",
                )

                # Make the request
                page_result = client.search_catalog(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.SearchCatalogRequest, dict]):
                The request object. Request message for
                [SearchCatalog][google.cloud.datacatalog.v1beta1.DataCatalog.SearchCatalog].
            scope (google.cloud.datacatalog_v1beta1.types.SearchCatalogRequest.Scope):
                Required. The scope of this search request. A ``scope``
                that has empty ``include_org_ids``,
                ``include_project_ids`` AND false
                ``include_gcp_public_datasets`` is considered invalid.
                Data Catalog will return an error in such a case.

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (str):
                Required. The query string in search query syntax. The
                query must be non-empty.

                Query strings can be simple as "x" or more qualified as:

                -  name:x
                -  column:x
                -  description:y

                Note: Query tokens need to have a minimum of 3
                characters for substring matching to work correctly. See
                `Data Catalog Search
                Syntax <https://cloud.google.com/data-catalog/docs/how-to/search-reference>`__
                for more information.

                This corresponds to the ``query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.services.data_catalog.pagers.SearchCatalogPager:
                Response message for
                   [SearchCatalog][google.cloud.datacatalog.v1beta1.DataCatalog.SearchCatalog].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([scope, query])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.SearchCatalogRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.SearchCatalogRequest):
            request = datacatalog.SearchCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if scope is not None:
                request.scope = scope
            if query is not None:
                request.query = query

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.search_catalog]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.SearchCatalogPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_entry_group(
        self,
        request: Union[datacatalog.CreateEntryGroupRequest, dict] = None,
        *,
        parent: str = None,
        entry_group_id: str = None,
        entry_group: datacatalog.EntryGroup = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datacatalog.EntryGroup:
        r"""A maximum of 10,000 entry groups may be created per organization
        across all locations.

        Users should enable the Data Catalog API in the project
        identified by the ``parent`` parameter (see [Data Catalog
        Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_create_entry_group():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.CreateEntryGroupRequest(
                    parent="parent_value",
                    entry_group_id="entry_group_id_value",
                )

                # Make the request
                response = client.create_entry_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.CreateEntryGroupRequest, dict]):
                The request object. Request message for
                [CreateEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntryGroup].
            parent (str):
                Required. The name of the project this entry group is
                in. Example:

                -  projects/{project_id}/locations/{location}

                Note that this EntryGroup and its child resources may
                not actually be stored in the location in this name.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entry_group_id (str):
                Required. The id of the entry group
                to create. The id must begin with a
                letter or underscore, contain only
                English letters, numbers and
                underscores, and be at most 64
                characters.

                This corresponds to the ``entry_group_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entry_group (google.cloud.datacatalog_v1beta1.types.EntryGroup):
                The entry group to create. Defaults
                to an empty entry group.

                This corresponds to the ``entry_group`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.EntryGroup:
                EntryGroup Metadata.
                   An EntryGroup resource represents a logical grouping
                   of zero or more Data Catalog
                   [Entry][google.cloud.datacatalog.v1beta1.Entry]
                   resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entry_group_id, entry_group])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.CreateEntryGroupRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.CreateEntryGroupRequest):
            request = datacatalog.CreateEntryGroupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if entry_group_id is not None:
                request.entry_group_id = entry_group_id
            if entry_group is not None:
                request.entry_group = entry_group

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_entry_group]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_entry_group(
        self,
        request: Union[datacatalog.UpdateEntryGroupRequest, dict] = None,
        *,
        entry_group: datacatalog.EntryGroup = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datacatalog.EntryGroup:
        r"""Updates an EntryGroup. The user should enable the Data Catalog
        API in the project identified by the ``entry_group.name``
        parameter (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_update_entry_group():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.UpdateEntryGroupRequest(
                )

                # Make the request
                response = client.update_entry_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.UpdateEntryGroupRequest, dict]):
                The request object. Request message for
                [UpdateEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateEntryGroup].
            entry_group (google.cloud.datacatalog_v1beta1.types.EntryGroup):
                Required. The updated entry group.
                "name" field must be set.

                This corresponds to the ``entry_group`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The fields to update on the entry
                group. If absent or empty, all
                modifiable fields are updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.EntryGroup:
                EntryGroup Metadata.
                   An EntryGroup resource represents a logical grouping
                   of zero or more Data Catalog
                   [Entry][google.cloud.datacatalog.v1beta1.Entry]
                   resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([entry_group, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.UpdateEntryGroupRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.UpdateEntryGroupRequest):
            request = datacatalog.UpdateEntryGroupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if entry_group is not None:
                request.entry_group = entry_group
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_entry_group]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("entry_group.name", request.entry_group.name),)
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_entry_group(
        self,
        request: Union[datacatalog.GetEntryGroupRequest, dict] = None,
        *,
        name: str = None,
        read_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datacatalog.EntryGroup:
        r"""Gets an EntryGroup.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_get_entry_group():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.GetEntryGroupRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_entry_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.GetEntryGroupRequest, dict]):
                The request object. Request message for
                [GetEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.GetEntryGroup].
            name (str):
                Required. The name of the entry group. For example,
                ``projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            read_mask (google.protobuf.field_mask_pb2.FieldMask):
                The fields to return. If not set or
                empty, all fields are returned.

                This corresponds to the ``read_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.EntryGroup:
                EntryGroup Metadata.
                   An EntryGroup resource represents a logical grouping
                   of zero or more Data Catalog
                   [Entry][google.cloud.datacatalog.v1beta1.Entry]
                   resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, read_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.GetEntryGroupRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.GetEntryGroupRequest):
            request = datacatalog.GetEntryGroupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if read_mask is not None:
                request.read_mask = read_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_entry_group]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_entry_group(
        self,
        request: Union[datacatalog.DeleteEntryGroupRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes an EntryGroup. Only entry groups that do not contain
        entries can be deleted. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_delete_entry_group():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteEntryGroupRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_entry_group(request=request)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.DeleteEntryGroupRequest, dict]):
                The request object. Request message for
                [DeleteEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteEntryGroup].
            name (str):
                Required. The name of the entry group. For example,
                ``projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}``.

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

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.DeleteEntryGroupRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.DeleteEntryGroupRequest):
            request = datacatalog.DeleteEntryGroupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_entry_group]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def list_entry_groups(
        self,
        request: Union[datacatalog.ListEntryGroupsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEntryGroupsPager:
        r"""Lists entry groups.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_list_entry_groups():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.ListEntryGroupsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entry_groups(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.ListEntryGroupsRequest, dict]):
                The request object. Request message for
                [ListEntryGroups][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntryGroups].
            parent (str):
                Required. The name of the location that contains the
                entry groups, which can be provided in URL format.
                Example:

                -  projects/{project_id}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.services.data_catalog.pagers.ListEntryGroupsPager:
                Response message for
                   [ListEntryGroups][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntryGroups].

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

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.ListEntryGroupsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.ListEntryGroupsRequest):
            request = datacatalog.ListEntryGroupsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_entry_groups]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListEntryGroupsPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_entry(
        self,
        request: Union[datacatalog.CreateEntryRequest, dict] = None,
        *,
        parent: str = None,
        entry_id: str = None,
        entry: datacatalog.Entry = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datacatalog.Entry:
        r"""Creates an entry. Only entries of 'FILESET' type or
        user-specified type can be created.

        Users should enable the Data Catalog API in the project
        identified by the ``parent`` parameter (see [Data Catalog
        Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        A maximum of 100,000 entries may be created per entry group.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_create_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                entry = datacatalog_v1beta1.Entry()
                entry.type_ = "FILESET"
                entry.integrated_system = "CLOUD_PUBSUB"
                entry.gcs_fileset_spec.file_patterns = ['file_patterns_value_1', 'file_patterns_value_2']

                request = datacatalog_v1beta1.CreateEntryRequest(
                    parent="parent_value",
                    entry_id="entry_id_value",
                    entry=entry,
                )

                # Make the request
                response = client.create_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.CreateEntryRequest, dict]):
                The request object. Request message for
                [CreateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntry].
            parent (str):
                Required. The name of the entry group this entry is in.
                Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}

                Note that this Entry and its child resources may not
                actually be stored in the location in this name.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entry_id (str):
                Required. The id of the entry to
                create.

                This corresponds to the ``entry_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entry (google.cloud.datacatalog_v1beta1.types.Entry):
                Required. The entry to create.
                This corresponds to the ``entry`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.Entry:
                Entry Metadata.
                   A Data Catalog Entry resource represents another
                   resource in Google Cloud Platform (such as a BigQuery
                   dataset or a Pub/Sub topic), or outside of Google
                   Cloud Platform. Clients can use the linked_resource
                   field in the Entry resource to refer to the original
                   resource ID of the source system.

                   An Entry resource contains resource details, such as
                   its schema. An Entry can also be used to attach
                   flexible metadata, such as a
                   [Tag][google.cloud.datacatalog.v1beta1.Tag].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entry_id, entry])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.CreateEntryRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.CreateEntryRequest):
            request = datacatalog.CreateEntryRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if entry_id is not None:
                request.entry_id = entry_id
            if entry is not None:
                request.entry = entry

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_entry]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_entry(
        self,
        request: Union[datacatalog.UpdateEntryRequest, dict] = None,
        *,
        entry: datacatalog.Entry = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datacatalog.Entry:
        r"""Updates an existing entry. Users should enable the Data Catalog
        API in the project identified by the ``entry.name`` parameter
        (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_update_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                entry = datacatalog_v1beta1.Entry()
                entry.type_ = "FILESET"
                entry.integrated_system = "CLOUD_PUBSUB"
                entry.gcs_fileset_spec.file_patterns = ['file_patterns_value_1', 'file_patterns_value_2']

                request = datacatalog_v1beta1.UpdateEntryRequest(
                    entry=entry,
                )

                # Make the request
                response = client.update_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.UpdateEntryRequest, dict]):
                The request object. Request message for
                [UpdateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateEntry].
            entry (google.cloud.datacatalog_v1beta1.types.Entry):
                Required. The updated entry. The
                "name" field must be set.

                This corresponds to the ``entry`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The fields to update on the entry. If absent or empty,
                all modifiable fields are updated.

                The following fields are modifiable:

                -  For entries with type ``DATA_STREAM``:

                   -  ``schema``

                -  For entries with type ``FILESET``

                   -  ``schema``
                   -  ``display_name``
                   -  ``description``
                   -  ``gcs_fileset_spec``
                   -  ``gcs_fileset_spec.file_patterns``

                -  For entries with ``user_specified_type``

                   -  ``schema``
                   -  ``display_name``
                   -  ``description``
                   -  user_specified_type
                   -  user_specified_system
                   -  linked_resource
                   -  source_system_timestamps

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.Entry:
                Entry Metadata.
                   A Data Catalog Entry resource represents another
                   resource in Google Cloud Platform (such as a BigQuery
                   dataset or a Pub/Sub topic), or outside of Google
                   Cloud Platform. Clients can use the linked_resource
                   field in the Entry resource to refer to the original
                   resource ID of the source system.

                   An Entry resource contains resource details, such as
                   its schema. An Entry can also be used to attach
                   flexible metadata, such as a
                   [Tag][google.cloud.datacatalog.v1beta1.Tag].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([entry, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.UpdateEntryRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.UpdateEntryRequest):
            request = datacatalog.UpdateEntryRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if entry is not None:
                request.entry = entry
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_entry]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("entry.name", request.entry.name),)
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_entry(
        self,
        request: Union[datacatalog.DeleteEntryRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes an existing entry. Only entries created through
        [CreateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntry]
        method can be deleted. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_delete_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteEntryRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_entry(request=request)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.DeleteEntryRequest, dict]):
                The request object. Request message for
                [DeleteEntry][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteEntry].
            name (str):
                Required. The name of the entry. Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

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

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.DeleteEntryRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.DeleteEntryRequest):
            request = datacatalog.DeleteEntryRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_entry]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def get_entry(
        self,
        request: Union[datacatalog.GetEntryRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datacatalog.Entry:
        r"""Gets an entry.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_get_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.GetEntryRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.GetEntryRequest, dict]):
                The request object. Request message for
                [GetEntry][google.cloud.datacatalog.v1beta1.DataCatalog.GetEntry].
            name (str):
                Required. The name of the entry. Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.Entry:
                Entry Metadata.
                   A Data Catalog Entry resource represents another
                   resource in Google Cloud Platform (such as a BigQuery
                   dataset or a Pub/Sub topic), or outside of Google
                   Cloud Platform. Clients can use the linked_resource
                   field in the Entry resource to refer to the original
                   resource ID of the source system.

                   An Entry resource contains resource details, such as
                   its schema. An Entry can also be used to attach
                   flexible metadata, such as a
                   [Tag][google.cloud.datacatalog.v1beta1.Tag].

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

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.GetEntryRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.GetEntryRequest):
            request = datacatalog.GetEntryRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_entry]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def lookup_entry(
        self,
        request: Union[datacatalog.LookupEntryRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datacatalog.Entry:
        r"""Get an entry by target resource name. This method
        allows clients to use the resource name from the source
        Google Cloud Platform service to get the Data Catalog
        Entry.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_lookup_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.LookupEntryRequest(
                    linked_resource="linked_resource_value",
                )

                # Make the request
                response = client.lookup_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.LookupEntryRequest, dict]):
                The request object. Request message for
                [LookupEntry][google.cloud.datacatalog.v1beta1.DataCatalog.LookupEntry].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.Entry:
                Entry Metadata.
                   A Data Catalog Entry resource represents another
                   resource in Google Cloud Platform (such as a BigQuery
                   dataset or a Pub/Sub topic), or outside of Google
                   Cloud Platform. Clients can use the linked_resource
                   field in the Entry resource to refer to the original
                   resource ID of the source system.

                   An Entry resource contains resource details, such as
                   its schema. An Entry can also be used to attach
                   flexible metadata, such as a
                   [Tag][google.cloud.datacatalog.v1beta1.Tag].

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.LookupEntryRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.LookupEntryRequest):
            request = datacatalog.LookupEntryRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.lookup_entry]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_entries(
        self,
        request: Union[datacatalog.ListEntriesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEntriesPager:
        r"""Lists entries.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_list_entries():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.ListEntriesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entries(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.ListEntriesRequest, dict]):
                The request object. Request message for
                [ListEntries][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntries].
            parent (str):
                Required. The name of the entry group that contains the
                entries, which can be provided in URL format. Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.services.data_catalog.pagers.ListEntriesPager:
                Response message for
                   [ListEntries][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntries].

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

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.ListEntriesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.ListEntriesRequest):
            request = datacatalog.ListEntriesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_entries]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListEntriesPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_tag_template(
        self,
        request: Union[datacatalog.CreateTagTemplateRequest, dict] = None,
        *,
        parent: str = None,
        tag_template_id: str = None,
        tag_template: tags.TagTemplate = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> tags.TagTemplate:
        r"""Creates a tag template. The user should enable the Data Catalog
        API in the project identified by the ``parent`` parameter (see
        `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_create_tag_template():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.CreateTagTemplateRequest(
                    parent="parent_value",
                    tag_template_id="tag_template_id_value",
                )

                # Make the request
                response = client.create_tag_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.CreateTagTemplateRequest, dict]):
                The request object. Request message for
                [CreateTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTagTemplate].
            parent (str):
                Required. The name of the project and the template
                location
                [region](https://cloud.google.com/data-catalog/docs/concepts/regions.

                Example:

                -  projects/{project_id}/locations/us-central1

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template_id (str):
                Required. The id of the tag template
                to create.

                This corresponds to the ``tag_template_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template (google.cloud.datacatalog_v1beta1.types.TagTemplate):
                Required. The tag template to create.
                This corresponds to the ``tag_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.TagTemplate:
                A tag template defines a tag, which can have one or more typed fields.
                   The template is used to create and attach the tag to
                   GCP resources. [Tag template
                   roles](\ https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
                   provide permissions to create, edit, and use the
                   template. See, for example, the [TagTemplate
                   User](\ https://cloud.google.com/data-catalog/docs/how-to/template-user)
                   role, which includes permission to use the tag
                   template to tag resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, tag_template_id, tag_template])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.CreateTagTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.CreateTagTemplateRequest):
            request = datacatalog.CreateTagTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if tag_template_id is not None:
                request.tag_template_id = tag_template_id
            if tag_template is not None:
                request.tag_template = tag_template

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_tag_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_tag_template(
        self,
        request: Union[datacatalog.GetTagTemplateRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> tags.TagTemplate:
        r"""Gets a tag template.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_get_tag_template():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.GetTagTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_tag_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.GetTagTemplateRequest, dict]):
                The request object. Request message for
                [GetTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.GetTagTemplate].
            name (str):
                Required. The name of the tag template. Example:

                -  projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.TagTemplate:
                A tag template defines a tag, which can have one or more typed fields.
                   The template is used to create and attach the tag to
                   GCP resources. [Tag template
                   roles](\ https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
                   provide permissions to create, edit, and use the
                   template. See, for example, the [TagTemplate
                   User](\ https://cloud.google.com/data-catalog/docs/how-to/template-user)
                   role, which includes permission to use the tag
                   template to tag resources.

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

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.GetTagTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.GetTagTemplateRequest):
            request = datacatalog.GetTagTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_tag_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_tag_template(
        self,
        request: Union[datacatalog.UpdateTagTemplateRequest, dict] = None,
        *,
        tag_template: tags.TagTemplate = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> tags.TagTemplate:
        r"""Updates a tag template. This method cannot be used to update the
        fields of a template. The tag template fields are represented as
        separate resources and should be updated using their own
        create/update/delete methods. Users should enable the Data
        Catalog API in the project identified by the
        ``tag_template.name`` parameter (see [Data Catalog Resource
        Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_update_tag_template():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.UpdateTagTemplateRequest(
                )

                # Make the request
                response = client.update_tag_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.UpdateTagTemplateRequest, dict]):
                The request object. Request message for
                [UpdateTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTagTemplate].
            tag_template (google.cloud.datacatalog_v1beta1.types.TagTemplate):
                Required. The template to update. The
                "name" field must be set.

                This corresponds to the ``tag_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The field mask specifies the parts of the template to
                overwrite.

                Allowed fields:

                -  ``display_name``

                If absent or empty, all of the allowed fields above will
                be updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.TagTemplate:
                A tag template defines a tag, which can have one or more typed fields.
                   The template is used to create and attach the tag to
                   GCP resources. [Tag template
                   roles](\ https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
                   provide permissions to create, edit, and use the
                   template. See, for example, the [TagTemplate
                   User](\ https://cloud.google.com/data-catalog/docs/how-to/template-user)
                   role, which includes permission to use the tag
                   template to tag resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([tag_template, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.UpdateTagTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.UpdateTagTemplateRequest):
            request = datacatalog.UpdateTagTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if tag_template is not None:
                request.tag_template = tag_template
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_tag_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("tag_template.name", request.tag_template.name),)
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_tag_template(
        self,
        request: Union[datacatalog.DeleteTagTemplateRequest, dict] = None,
        *,
        name: str = None,
        force: bool = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a tag template and all tags using the template. Users
        should enable the Data Catalog API in the project identified by
        the ``name`` parameter (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_delete_tag_template():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteTagTemplateRequest(
                    name="name_value",
                    force=True,
                )

                # Make the request
                client.delete_tag_template(request=request)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.DeleteTagTemplateRequest, dict]):
                The request object. Request message for
                [DeleteTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTagTemplate].
            name (str):
                Required. The name of the tag template to delete.
                Example:

                -  projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            force (bool):
                Required. Currently, this field must always be set to
                ``true``. This confirms the deletion of any possible
                tags using this template. ``force = false`` will be
                supported in the future.

                This corresponds to the ``force`` field
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
        has_flattened_params = any([name, force])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.DeleteTagTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.DeleteTagTemplateRequest):
            request = datacatalog.DeleteTagTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if force is not None:
                request.force = force

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_tag_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def create_tag_template_field(
        self,
        request: Union[datacatalog.CreateTagTemplateFieldRequest, dict] = None,
        *,
        parent: str = None,
        tag_template_field_id: str = None,
        tag_template_field: tags.TagTemplateField = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> tags.TagTemplateField:
        r"""Creates a field in a tag template. The user should enable the
        Data Catalog API in the project identified by the ``parent``
        parameter (see `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_create_tag_template_field():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                tag_template_field = datacatalog_v1beta1.TagTemplateField()
                tag_template_field.type_.primitive_type = "TIMESTAMP"

                request = datacatalog_v1beta1.CreateTagTemplateFieldRequest(
                    parent="parent_value",
                    tag_template_field_id="tag_template_field_id_value",
                    tag_template_field=tag_template_field,
                )

                # Make the request
                response = client.create_tag_template_field(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.CreateTagTemplateFieldRequest, dict]):
                The request object. Request message for
                [CreateTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTagTemplateField].
            parent (str):
                Required. The name of the project and the template
                location
                `region <https://cloud.google.com/data-catalog/docs/concepts/regions>`__.

                Example:

                -  projects/{project_id}/locations/us-central1/tagTemplates/{tag_template_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template_field_id (str):
                Required. The ID of the tag template field to create.
                Field ids can contain letters (both uppercase and
                lowercase), numbers (0-9), underscores (_) and dashes
                (-). Field IDs must be at least 1 character long and at
                most 128 characters long. Field IDs must also be unique
                within their template.

                This corresponds to the ``tag_template_field_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template_field (google.cloud.datacatalog_v1beta1.types.TagTemplateField):
                Required. The tag template field to
                create.

                This corresponds to the ``tag_template_field`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.TagTemplateField:
                The template for an individual field
                within a tag template.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, tag_template_field_id, tag_template_field])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.CreateTagTemplateFieldRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.CreateTagTemplateFieldRequest):
            request = datacatalog.CreateTagTemplateFieldRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if tag_template_field_id is not None:
                request.tag_template_field_id = tag_template_field_id
            if tag_template_field is not None:
                request.tag_template_field = tag_template_field

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_tag_template_field
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_tag_template_field(
        self,
        request: Union[datacatalog.UpdateTagTemplateFieldRequest, dict] = None,
        *,
        name: str = None,
        tag_template_field: tags.TagTemplateField = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> tags.TagTemplateField:
        r"""Updates a field in a tag template. This method cannot be used to
        update the field type. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_update_tag_template_field():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                tag_template_field = datacatalog_v1beta1.TagTemplateField()
                tag_template_field.type_.primitive_type = "TIMESTAMP"

                request = datacatalog_v1beta1.UpdateTagTemplateFieldRequest(
                    name="name_value",
                    tag_template_field=tag_template_field,
                )

                # Make the request
                response = client.update_tag_template_field(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.UpdateTagTemplateFieldRequest, dict]):
                The request object. Request message for
                [UpdateTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTagTemplateField].
            name (str):
                Required. The name of the tag template field. Example:

                -  projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template_field (google.cloud.datacatalog_v1beta1.types.TagTemplateField):
                Required. The template to update.
                This corresponds to the ``tag_template_field`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The field mask specifies the parts of the
                template to be updated. Allowed fields:

                -  ``display_name``
                -  ``type.enum_type``
                -  ``is_required``

                If ``update_mask`` is not set or empty, all of the
                allowed fields above will be updated.

                When updating an enum type, the provided values will be
                merged with the existing values. Therefore, enum values
                can only be added, existing enum values cannot be
                deleted nor renamed. Updating a template field from
                optional to required is NOT allowed.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.TagTemplateField:
                The template for an individual field
                within a tag template.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, tag_template_field, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.UpdateTagTemplateFieldRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.UpdateTagTemplateFieldRequest):
            request = datacatalog.UpdateTagTemplateFieldRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if tag_template_field is not None:
                request.tag_template_field = tag_template_field
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_tag_template_field
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def rename_tag_template_field(
        self,
        request: Union[datacatalog.RenameTagTemplateFieldRequest, dict] = None,
        *,
        name: str = None,
        new_tag_template_field_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> tags.TagTemplateField:
        r"""Renames a field in a tag template. The user should enable the
        Data Catalog API in the project identified by the ``name``
        parameter (see `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_rename_tag_template_field():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.RenameTagTemplateFieldRequest(
                    name="name_value",
                    new_tag_template_field_id="new_tag_template_field_id_value",
                )

                # Make the request
                response = client.rename_tag_template_field(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.RenameTagTemplateFieldRequest, dict]):
                The request object. Request message for
                [RenameTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.RenameTagTemplateField].
            name (str):
                Required. The name of the tag template. Example:

                -  projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            new_tag_template_field_id (str):
                Required. The new ID of this tag template field. For
                example, ``my_new_field``.

                This corresponds to the ``new_tag_template_field_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.TagTemplateField:
                The template for an individual field
                within a tag template.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, new_tag_template_field_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.RenameTagTemplateFieldRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.RenameTagTemplateFieldRequest):
            request = datacatalog.RenameTagTemplateFieldRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if new_tag_template_field_id is not None:
                request.new_tag_template_field_id = new_tag_template_field_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.rename_tag_template_field
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_tag_template_field(
        self,
        request: Union[datacatalog.DeleteTagTemplateFieldRequest, dict] = None,
        *,
        name: str = None,
        force: bool = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a field in a tag template and all uses of that field.
        Users should enable the Data Catalog API in the project
        identified by the ``name`` parameter (see [Data Catalog Resource
        Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_delete_tag_template_field():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteTagTemplateFieldRequest(
                    name="name_value",
                    force=True,
                )

                # Make the request
                client.delete_tag_template_field(request=request)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.DeleteTagTemplateFieldRequest, dict]):
                The request object. Request message for
                [DeleteTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTagTemplateField].
            name (str):
                Required. The name of the tag template field to delete.
                Example:

                -  projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            force (bool):
                Required. Currently, this field must always be set to
                ``true``. This confirms the deletion of this field from
                any tags using this field. ``force = false`` will be
                supported in the future.

                This corresponds to the ``force`` field
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
        has_flattened_params = any([name, force])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.DeleteTagTemplateFieldRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.DeleteTagTemplateFieldRequest):
            request = datacatalog.DeleteTagTemplateFieldRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if force is not None:
                request.force = force

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_tag_template_field
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def create_tag(
        self,
        request: Union[datacatalog.CreateTagRequest, dict] = None,
        *,
        parent: str = None,
        tag: tags.Tag = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> tags.Tag:
        r"""Creates a tag on an
        [Entry][google.cloud.datacatalog.v1beta1.Entry]. Note: The
        project identified by the ``parent`` parameter for the
        `tag <https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups.entries.tags/create#path-parameters>`__
        and the `tag
        template <https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.tagTemplates/create#path-parameters>`__
        used to create the tag must be from the same organization.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_create_tag():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                tag = datacatalog_v1beta1.Tag()
                tag.column = "column_value"
                tag.template = "template_value"

                request = datacatalog_v1beta1.CreateTagRequest(
                    parent="parent_value",
                    tag=tag,
                )

                # Make the request
                response = client.create_tag(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.CreateTagRequest, dict]):
                The request object. Request message for
                [CreateTag][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTag].
            parent (str):
                Required. The name of the resource to attach this tag
                to. Tags can be attached to Entries. Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

                Note that this Tag and its child resources may not
                actually be stored in the location in this name.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag (google.cloud.datacatalog_v1beta1.types.Tag):
                Required. The tag to create.
                This corresponds to the ``tag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.Tag:
                Tags are used to attach custom metadata to Data Catalog resources. Tags
                   conform to the specifications within their tag
                   template.

                   See [Data Catalog
                   IAM](\ https://cloud.google.com/data-catalog/docs/concepts/iam)
                   for information on the permissions needed to create
                   or view tags.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, tag])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.CreateTagRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.CreateTagRequest):
            request = datacatalog.CreateTagRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if tag is not None:
                request.tag = tag

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_tag]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_tag(
        self,
        request: Union[datacatalog.UpdateTagRequest, dict] = None,
        *,
        tag: tags.Tag = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> tags.Tag:
        r"""Updates an existing tag.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_update_tag():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                tag = datacatalog_v1beta1.Tag()
                tag.column = "column_value"
                tag.template = "template_value"

                request = datacatalog_v1beta1.UpdateTagRequest(
                    tag=tag,
                )

                # Make the request
                response = client.update_tag(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.UpdateTagRequest, dict]):
                The request object. Request message for
                [UpdateTag][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTag].
            tag (google.cloud.datacatalog_v1beta1.types.Tag):
                Required. The updated tag. The "name"
                field must be set.

                This corresponds to the ``tag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The fields to update on the Tag. If absent or empty, all
                modifiable fields are updated. Currently the only
                modifiable field is the field ``fields``.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.types.Tag:
                Tags are used to attach custom metadata to Data Catalog resources. Tags
                   conform to the specifications within their tag
                   template.

                   See [Data Catalog
                   IAM](\ https://cloud.google.com/data-catalog/docs/concepts/iam)
                   for information on the permissions needed to create
                   or view tags.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([tag, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.UpdateTagRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.UpdateTagRequest):
            request = datacatalog.UpdateTagRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if tag is not None:
                request.tag = tag
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_tag]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("tag.name", request.tag.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_tag(
        self,
        request: Union[datacatalog.DeleteTagRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a tag.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_delete_tag():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteTagRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_tag(request=request)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.DeleteTagRequest, dict]):
                The request object. Request message for
                [DeleteTag][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTag].
            name (str):
                Required. The name of the tag to delete. Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}/tags/{tag_id}

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

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.DeleteTagRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.DeleteTagRequest):
            request = datacatalog.DeleteTagRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_tag]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def list_tags(
        self,
        request: Union[datacatalog.ListTagsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTagsPager:
        r"""Lists the tags on an
        [Entry][google.cloud.datacatalog.v1beta1.Entry].

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1

            def sample_list_tags():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.ListTagsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_tags(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datacatalog_v1beta1.types.ListTagsRequest, dict]):
                The request object. Request message for
                [ListTags][google.cloud.datacatalog.v1beta1.DataCatalog.ListTags].
            parent (str):
                Required. The name of the Data Catalog resource to list
                the tags of. The resource could be an
                [Entry][google.cloud.datacatalog.v1beta1.Entry] or an
                [EntryGroup][google.cloud.datacatalog.v1beta1.EntryGroup].

                Examples:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}
                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1beta1.services.data_catalog.pagers.ListTagsPager:
                Response message for
                   [ListTags][google.cloud.datacatalog.v1beta1.DataCatalog.ListTags].

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

        # Minor optimization to avoid making a copy if the user passes
        # in a datacatalog.ListTagsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datacatalog.ListTagsRequest):
            request = datacatalog.ListTagsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_tags]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListTagsPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_iam_policy(
        self,
        request: Union[iam_policy_pb2.SetIamPolicyRequest, dict] = None,
        *,
        resource: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the access control policy for a resource. Replaces any
        existing policy. Supported resources are:

        -  Tag templates.
        -  Entries.
        -  Entry groups. Note, this method cannot be used to manage
           policies for BigQuery, Pub/Sub and any external Google Cloud
           Platform resources synced to Data Catalog.

        Callers must have following Google IAM permission

        -  ``datacatalog.tagTemplates.setIamPolicy`` to set policies on
           tag templates.
        -  ``datacatalog.entries.setIamPolicy`` to set policies on
           entries.
        -  ``datacatalog.entryGroups.setIamPolicy`` to set policies on
           entry groups.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            def sample_set_iam_policy():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.SetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = client.set_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]):
                The request object. Request message for `SetIamPolicy`
                method.
            resource (str):
                REQUIRED: The resource for which the
                policy is being specified. See the
                operation documentation for the
                appropriate value for this field.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
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
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([resource])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        if isinstance(request, dict):
            # The request isn't a proto-plus wrapped type,
            # so it must be constructed via keyword expansion.
            request = iam_policy_pb2.SetIamPolicyRequest(**request)
        elif not request:
            # Null request, just make one.
            request = iam_policy_pb2.SetIamPolicyRequest()
            if resource is not None:
                request.resource = resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_iam_policy(
        self,
        request: Union[iam_policy_pb2.GetIamPolicyRequest, dict] = None,
        *,
        resource: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the access control policy for a resource. A ``NOT_FOUND``
        error is returned if the resource does not exist. An empty
        policy is returned if the resource exists but does not have a
        policy set on it.

        Supported resources are:

        -  Tag templates.
        -  Entries.
        -  Entry groups. Note, this method cannot be used to manage
           policies for BigQuery, Pub/Sub and any external Google Cloud
           Platform resources synced to Data Catalog.

        Callers must have following Google IAM permission

        -  ``datacatalog.tagTemplates.getIamPolicy`` to get policies on
           tag templates.
        -  ``datacatalog.entries.getIamPolicy`` to get policies on
           entries.
        -  ``datacatalog.entryGroups.getIamPolicy`` to get policies on
           entry groups.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            def sample_get_iam_policy():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.GetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = client.get_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]):
                The request object. Request message for `GetIamPolicy`
                method.
            resource (str):
                REQUIRED: The resource for which the
                policy is being requested. See the
                operation documentation for the
                appropriate value for this field.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
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
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([resource])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        if isinstance(request, dict):
            # The request isn't a proto-plus wrapped type,
            # so it must be constructed via keyword expansion.
            request = iam_policy_pb2.GetIamPolicyRequest(**request)
        elif not request:
            # Null request, just make one.
            request = iam_policy_pb2.GetIamPolicyRequest()
            if resource is not None:
                request.resource = resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def test_iam_permissions(
        self,
        request: Union[iam_policy_pb2.TestIamPermissionsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Returns the caller's permissions on a resource. If the resource
        does not exist, an empty set of permissions is returned (We
        don't return a ``NOT_FOUND`` error).

        Supported resources are:

        -  Tag templates.
        -  Entries.
        -  Entry groups. Note, this method cannot be used to manage
           policies for BigQuery, Pub/Sub and any external Google Cloud
           Platform resources synced to Data Catalog.

        A caller is not required to have Google IAM permission to make
        this request.

        .. code-block:: python

            from google.cloud import datacatalog_v1beta1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            def sample_test_iam_permissions():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.TestIamPermissionsRequest(
                    resource="resource_value",
                    permissions=['permissions_value_1', 'permissions_value_2'],
                )

                # Make the request
                response = client.test_iam_permissions(request=request)

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
        if isinstance(request, dict):
            # The request isn't a proto-plus wrapped type,
            # so it must be constructed via keyword expansion.
            request = iam_policy_pb2.TestIamPermissionsRequest(**request)
        elif not request:
            # Null request, just make one.
            request = iam_policy_pb2.TestIamPermissionsRequest()

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.test_iam_permissions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-datacatalog",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("DataCatalogClient",)
