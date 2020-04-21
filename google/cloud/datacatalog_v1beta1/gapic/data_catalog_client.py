# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.datacatalog.v1beta1 DataCatalog API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import google.api_core.protobuf_helpers
import grpc

from google.cloud.datacatalog_v1beta1.gapic import data_catalog_client_config
from google.cloud.datacatalog_v1beta1.gapic import enums
from google.cloud.datacatalog_v1beta1.gapic.transports import (
    data_catalog_grpc_transport,
)
from google.cloud.datacatalog_v1beta1.proto import datacatalog_pb2
from google.cloud.datacatalog_v1beta1.proto import datacatalog_pb2_grpc
from google.cloud.datacatalog_v1beta1.proto import tags_pb2
from google.iam.v1 import iam_policy_pb2
from google.iam.v1 import options_pb2
from google.iam.v1 import policy_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-datacatalog"
).version


class DataCatalogClient(object):
    """
    Data Catalog API service allows clients to discover, understand, and manage
    their data.
    """

    SERVICE_ADDRESS = "datacatalog.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.datacatalog.v1beta1.DataCatalog"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
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

    @classmethod
    def entry_path(cls, project, location, entry_group, entry):
        """Return a fully-qualified entry string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}",
            project=project,
            location=location,
            entry_group=entry_group,
            entry=entry,
        )

    @classmethod
    def entry_group_path(cls, project, location, entry_group):
        """Return a fully-qualified entry_group string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/entryGroups/{entry_group}",
            project=project,
            location=location,
            entry_group=entry_group,
        )

    @classmethod
    def field_path(cls, project, location, tag_template, field):
        """Return a fully-qualified field string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{field}",
            project=project,
            location=location,
            tag_template=tag_template,
            field=field,
        )

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}",
            project=project,
            location=location,
        )

    @classmethod
    def tag_path(cls, project, location, entry_group, entry, tag):
        """Return a fully-qualified tag string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}/tags/{tag}",
            project=project,
            location=location,
            entry_group=entry_group,
            entry=entry,
            tag=tag,
        )

    @classmethod
    def tag_template_path(cls, project, location, tag_template):
        """Return a fully-qualified tag_template string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/tagTemplates/{tag_template}",
            project=project,
            location=location,
            tag_template=tag_template,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.DataCatalogGrpcTransport,
                    Callable[[~.Credentials, type], ~.DataCatalogGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = data_catalog_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=data_catalog_grpc_transport.DataCatalogGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = data_catalog_grpc_transport.DataCatalogGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def search_catalog(
        self,
        scope,
        query,
        page_size=None,
        order_by=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        If type_name is set, this need not be set. If both this and
        type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or
        TYPE_GROUP.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> # TODO: Initialize `scope`:
            >>> scope = {}
            >>>
            >>> # TODO: Initialize `query`:
            >>> query = ''
            >>>
            >>> # Iterate over all results
            >>> for element in client.search_catalog(scope, query):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.search_catalog(scope, query).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            scope (Union[dict, ~google.cloud.datacatalog_v1beta1.types.Scope]): The name of the uninterpreted option. Each string represents a
                segment in a dot-separated name. is_extension is true iff a segment
                represents an extension (denoted with parentheses in options specs in
                .proto files). E.g.,{ ["foo", false], ["bar.baz", true], ["qux", false]
                } represents "foo.(bar.baz).qux".

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.Scope`
            query (str): The resource has one pattern, but the API owner expects to add more
                later. (This is the inverse of ORIGINALLY_SINGLE_PATTERN, and prevents
                that from being necessary once there are multiple patterns.)
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            order_by (str): The resource type. It must be in the format of
                {service_name}/{resource_type_kind}. The ``resource_type_kind`` must be
                singular and must not include version numbers.

                Example: ``storage.googleapis.com/Bucket``

                The value of the resource_type_kind must follow the regular expression
                /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and
                should use PascalCase (UpperCamelCase). The maximum number of characters
                allowed for the ``resource_type_kind`` is 100.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.datacatalog_v1beta1.types.SearchCatalogResult` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "search_catalog" not in self._inner_api_calls:
            self._inner_api_calls[
                "search_catalog"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.search_catalog,
                default_retry=self._method_configs["SearchCatalog"].retry,
                default_timeout=self._method_configs["SearchCatalog"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.SearchCatalogRequest(
            scope=scope, query=query, page_size=page_size, order_by=order_by
        )
        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["search_catalog"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="results",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def create_entry_group(
        self,
        parent,
        entry_group_id,
        entry_group,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Required. The name of the project and the template location
        `region <https://cloud.google.com/data-catalog/docs/concepts/regions>`__.

        Example:

        -  projects/{project_id}/locations/us-central1/tagTemplates/{tag_template_id}

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # TODO: Initialize `entry_group_id`:
            >>> entry_group_id = ''
            >>>
            >>> # TODO: Initialize `entry_group`:
            >>> entry_group = {}
            >>>
            >>> response = client.create_entry_group(parent, entry_group_id, entry_group)

        Args:
            parent (str): Output only. Resource name of this taxonomy, whose format is:
                "projects/{project_number}/locations/{location_id}/taxonomies/{id}".
            entry_group_id (str): Required. The id of the entry group to create.
                The id must begin with a letter or underscore, contain only English
                letters, numbers and underscores, and be at most 64 characters.
            entry_group (Union[dict, ~google.cloud.datacatalog_v1beta1.types.EntryGroup]): The entry group to create. Defaults to an empty entry group.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.EntryGroup`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.EntryGroup` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_entry_group" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_entry_group"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_entry_group,
                default_retry=self._method_configs["CreateEntryGroup"].retry,
                default_timeout=self._method_configs["CreateEntryGroup"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.CreateEntryGroupRequest(
            parent=parent, entry_group_id=entry_group_id, entry_group=entry_group
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_entry_group"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_entry_group(
        self,
        name,
        read_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets an EntryGroup.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.entry_group_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]')
            >>>
            >>> response = client.get_entry_group(name)

        Args:
            name (str): Request message for ``GetIamPolicy`` method.
            read_mask (Union[dict, ~google.cloud.datacatalog_v1beta1.types.FieldMask]): The fields to return. If not set or empty, all fields are returned.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.EntryGroup` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_entry_group" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_entry_group"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_entry_group,
                default_retry=self._method_configs["GetEntryGroup"].retry,
                default_timeout=self._method_configs["GetEntryGroup"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.GetEntryGroupRequest(name=name, read_mask=read_mask)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_entry_group"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_entry_group(
        self,
        name,
        force=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Required. The ID of the tag template field to create. Field ids can
        contain letters (both uppercase and lowercase), numbers (0-9),
        underscores (_) and dashes (-). Field IDs must be at least 1 character
        long and at most 128 characters long. Field IDs must also be unique
        within their template.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.entry_group_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]')
            >>>
            >>> client.delete_entry_group(name)

        Args:
            name (str): An ``EntryGroup``.
            force (bool): Optional. If true, deletes all entries in the entry group.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_entry_group" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_entry_group"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_entry_group,
                default_retry=self._method_configs["DeleteEntryGroup"].retry,
                default_timeout=self._method_configs["DeleteEntryGroup"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.DeleteEntryGroupRequest(name=name, force=force)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_entry_group"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_entry(
        self,
        parent,
        entry_id,
        entry,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Request message for ``CreateEntry``.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> parent = client.entry_group_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]')
            >>>
            >>> # TODO: Initialize `entry_id`:
            >>> entry_id = ''
            >>>
            >>> # TODO: Initialize `entry`:
            >>> entry = {}
            >>>
            >>> response = client.create_entry(parent, entry_id, entry)

        Args:
            parent (str): OPTIONAL: A ``GetPolicyOptions`` object for specifying options to
                ``GetIamPolicy``. This field is only used by Cloud IAM.
            entry_id (str): Required. The id of the entry to create.
            entry (Union[dict, ~google.cloud.datacatalog_v1beta1.types.Entry]): Required. The entry to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.Entry`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.Entry` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_entry" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_entry"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_entry,
                default_retry=self._method_configs["CreateEntry"].retry,
                default_timeout=self._method_configs["CreateEntry"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.CreateEntryRequest(
            parent=parent, entry_id=entry_id, entry=entry
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_entry"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_entry(
        self,
        entry,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        For extensions, this is the name of the type being extended. It is
        resolved in the same manner as type_name.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> # TODO: Initialize `entry`:
            >>> entry = {}
            >>>
            >>> response = client.update_entry(entry)

        Args:
            entry (Union[dict, ~google.cloud.datacatalog_v1beta1.types.Entry]): Required. The updated entry. The "name" field must be set.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.Entry`
            update_mask (Union[dict, ~google.cloud.datacatalog_v1beta1.types.FieldMask]): The plural name used in the resource name, such as 'projects' for
                the name of 'projects/{project}'. It is the same concept of the
                ``plural`` field in k8s CRD spec
                https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.Entry` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_entry" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_entry"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_entry,
                default_retry=self._method_configs["UpdateEntry"].retry,
                default_timeout=self._method_configs["UpdateEntry"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.UpdateEntryRequest(
            entry=entry, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("entry.name", entry.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_entry"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_entry(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Required. The name of the entry group this entry is in. Example:

        -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}

        Note that this Entry and its child resources may not actually be stored
        in the location in this name.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.entry_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]', '[ENTRY]')
            >>>
            >>> client.delete_entry(name)

        Args:
            name (str): Required. The new ID of this tag template field. For example,
                ``my_new_field``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_entry" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_entry"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_entry,
                default_retry=self._method_configs["DeleteEntry"].retry,
                default_timeout=self._method_configs["DeleteEntry"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.DeleteEntryRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_entry"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_entry(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets an entry.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.entry_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]', '[ENTRY]')
            >>>
            >>> response = client.get_entry(name)

        Args:
            name (str): javalite_serializable
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.Entry` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_entry" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_entry"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_entry,
                default_retry=self._method_configs["GetEntry"].retry,
                default_timeout=self._method_configs["GetEntry"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.GetEntryRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_entry"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def lookup_entry(
        self,
        linked_resource=None,
        sql_resource=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Get an entry by target resource name. This method allows clients to use
        the resource name from the source Google Cloud Platform service to get the
        Data Catalog Entry.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> response = client.lookup_entry()

        Args:
            linked_resource (str): Required. The name of the entry. Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}
            sql_resource (str): Request message for ``DeleteTagTemplateField``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.Entry` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "lookup_entry" not in self._inner_api_calls:
            self._inner_api_calls[
                "lookup_entry"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.lookup_entry,
                default_retry=self._method_configs["LookupEntry"].retry,
                default_timeout=self._method_configs["LookupEntry"].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            linked_resource=linked_resource, sql_resource=sql_resource
        )

        request = datacatalog_pb2.LookupEntryRequest(
            linked_resource=linked_resource, sql_resource=sql_resource
        )
        return self._inner_api_calls["lookup_entry"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_entry_groups(
        self,
        parent,
        page_size=None,
        page_token=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists entry groups.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> response = client.list_entry_groups(parent)

        Args:
            parent (str): Request message for ``ListPolicyTags``.
            page_size (int): Request message for ``DeleteEntry``.
            page_token (str): Optional. Token that specifies which page is requested. If empty, the first page is
                returned.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.ListEntryGroupsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_entry_groups" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_entry_groups"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_entry_groups,
                default_retry=self._method_configs["ListEntryGroups"].retry,
                default_timeout=self._method_configs["ListEntryGroups"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.ListEntryGroupsRequest(
            parent=parent, page_size=page_size, page_token=page_token
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["list_entry_groups"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_entries(
        self,
        parent,
        page_size=None,
        page_token=None,
        read_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists entries.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> parent = client.entry_group_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]')
            >>>
            >>> response = client.list_entries(parent)

        Args:
            parent (str): Optional. Pagination token returned in an earlier
                ``SearchCatalogResponse.next_page_token``, which indicates that this is
                a continuation of a prior ``SearchCatalogRequest`` call, and that the
                system should return the next page of data. If empty, the first page is
                returned.
            page_size (int): The maximum number of items to return. Default is 10. Max limit is
                1000. Throws an invalid argument for ``page_size > 1000``.
            page_token (str): Token that specifies which page is requested. If empty, the first page is
                returned.
            read_mask (Union[dict, ~google.cloud.datacatalog_v1beta1.types.FieldMask]): Output only. The Data Catalog resource name of the dataset entry the
                current table belongs to, for example,
                ``projects/{project_id}/locations/{location}/entrygroups/{entry_group_id}/entries/{entry_id}``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.ListEntriesResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_entries" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_entries"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_entries,
                default_retry=self._method_configs["ListEntries"].retry,
                default_timeout=self._method_configs["ListEntries"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.ListEntriesRequest(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            read_mask=read_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["list_entries"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_entry_group(
        self,
        entry_group,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        An annotation that describes a resource definition without a
        corresponding message; see ``ResourceDescriptor``.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> # TODO: Initialize `entry_group`:
            >>> entry_group = {}
            >>>
            >>> response = client.update_entry_group(entry_group)

        Args:
            entry_group (Union[dict, ~google.cloud.datacatalog_v1beta1.types.EntryGroup]): Required. The updated entry group. "name" field must be set.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.EntryGroup`
            update_mask (Union[dict, ~google.cloud.datacatalog_v1beta1.types.FieldMask]): The fields to update on the entry group. If absent or empty, all modifiable
                fields are updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.EntryGroup` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_entry_group" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_entry_group"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_entry_group,
                default_retry=self._method_configs["UpdateEntryGroup"].retry,
                default_timeout=self._method_configs["UpdateEntryGroup"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.UpdateEntryGroupRequest(
            entry_group=entry_group, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("entry_group.name", entry_group.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_entry_group"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_tag_template(
        self,
        parent,
        tag_template_id,
        tag_template,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        An annotation that describes a resource definition, see
        ``ResourceDescriptor``.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # TODO: Initialize `tag_template_id`:
            >>> tag_template_id = ''
            >>>
            >>> # TODO: Initialize `tag_template`:
            >>> tag_template = {}
            >>>
            >>> response = client.create_tag_template(parent, tag_template_id, tag_template)

        Args:
            parent (str): A subset of ``TestPermissionsRequest.permissions`` that the caller
                is allowed.
            tag_template_id (str): Required. The id of the tag template to create.
            tag_template (Union[dict, ~google.cloud.datacatalog_v1beta1.types.TagTemplate]): Required. The tag template to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplate`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_tag_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_tag_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_tag_template,
                default_retry=self._method_configs["CreateTagTemplate"].retry,
                default_timeout=self._method_configs["CreateTagTemplate"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.CreateTagTemplateRequest(
            parent=parent, tag_template_id=tag_template_id, tag_template=tag_template
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_tag_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_tag_template(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a tag template.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.tag_template_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]')
            >>>
            >>> response = client.get_tag_template(name)

        Args:
            name (str): Whether the message is an automatically generated map entry type for
                the maps field.

                For maps fields: map<KeyType, ValueType> map_field = 1; The parsed
                descriptor looks like: message MapFieldEntry { option map_entry = true;
                optional KeyType key = 1; optional ValueType value = 2; } repeated
                MapFieldEntry map_field = 1;

                Implementations may choose not to generate the map_entry=true message,
                but use a native map in the target language to hold the keys and values.
                The reflection APIs in such implementations still need to work as if the
                field is a repeated message field.

                NOTE: Do not set the option in .proto files. Always use the maps syntax
                instead. The option should only be implicitly set by the proto compiler
                parser.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_tag_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_tag_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_tag_template,
                default_retry=self._method_configs["GetTagTemplate"].retry,
                default_timeout=self._method_configs["GetTagTemplate"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.GetTagTemplateRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_tag_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_tag_template(
        self,
        tag_template,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a tag template. This method cannot be used to update the
        fields of a template. The tag template fields are represented as
        separate resources and should be updated using their own
        create/update/delete methods. Users should enable the Data Catalog API
        in the project identified by the ``tag_template.name`` parameter (see
        [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> # TODO: Initialize `tag_template`:
            >>> tag_template = {}
            >>>
            >>> response = client.update_tag_template(tag_template)

        Args:
            tag_template (Union[dict, ~google.cloud.datacatalog_v1beta1.types.TagTemplate]): Required. The template to update. The "name" field must be set.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplate`
            update_mask (Union[dict, ~google.cloud.datacatalog_v1beta1.types.FieldMask]): Entry Metadata. A Data Catalog Entry resource represents another
                resource in Google Cloud Platform (such as a BigQuery dataset or a
                Pub/Sub topic), or outside of Google Cloud Platform. Clients can use the
                ``linked_resource`` field in the Entry resource to refer to the original
                resource ID of the source system.

                An Entry resource contains resource details, such as its schema. An
                Entry can also be used to attach flexible metadata, such as a ``Tag``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_tag_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_tag_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_tag_template,
                default_retry=self._method_configs["UpdateTagTemplate"].retry,
                default_timeout=self._method_configs["UpdateTagTemplate"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.UpdateTagTemplateRequest(
            tag_template=tag_template, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("tag_template.name", tag_template.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_tag_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_tag_template(
        self,
        name,
        force,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sub-type of the search result. This is a dot-delimited description
        of the resource's full type, and is the same as the value callers would
        provide in the "type" search facet. Examples: ``entry.table``,
        ``entry.dataStream``, ``tagTemplate``.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.tag_template_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]')
            >>>
            >>> # TODO: Initialize `force`:
            >>> force = False
            >>>
            >>> client.delete_tag_template(name, force)

        Args:
            name (str): Protocol Buffers - Google's data interchange format Copyright 2008
                Google Inc. All rights reserved.
                https://developers.google.com/protocol-buffers/

                Redistribution and use in source and binary forms, with or without
                modification, are permitted provided that the following conditions are
                met:

                ::

                    * Redistributions of source code must retain the above copyright

                notice, this list of conditions and the following disclaimer. \*
                Redistributions in binary form must reproduce the above copyright
                notice, this list of conditions and the following disclaimer in the
                documentation and/or other materials provided with the distribution. \*
                Neither the name of Google Inc. nor the names of its contributors may be
                used to endorse or promote products derived from this software without
                specific prior written permission.

                THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
                IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
                TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
                PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
                OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
                EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
                PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
                PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
                LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
                NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
                SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
            force (bool): Spec of a BigQuery table. This field should only be populated if
                ``table_source_type`` is ``BIGQUERY_TABLE``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_tag_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_tag_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_tag_template,
                default_retry=self._method_configs["DeleteTagTemplate"].retry,
                default_timeout=self._method_configs["DeleteTagTemplate"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.DeleteTagTemplateRequest(name=name, force=force)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_tag_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_tag_template_field(
        self,
        parent,
        tag_template_field_id,
        tag_template_field,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        A simple descriptor of a resource type.

        ResourceDescriptor annotates a resource message (either by means of a
        protobuf annotation or use in the service config), and associates the
        resource's schema, the resource type, and the pattern of the resource
        name.

        Example:

        ::

            message Topic {
              // Indicates this message defines a resource schema.
              // Declares the resource type in the format of {service}/{kind}.
              // For Kubernetes resources, the format is {api group}/{kind}.
              option (google.api.resource) = {
                type: "pubsub.googleapis.com/Topic"
                name_descriptor: {
                  pattern: "projects/{project}/topics/{topic}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: "pubsub.googleapis.com/Topic"
              name_descriptor:
                - pattern: "projects/{project}/topics/{topic}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"

        Sometimes, resources have multiple patterns, typically because they can
        live under multiple parents.

        Example:

        ::

            message LogEntry {
              option (google.api.resource) = {
                type: "logging.googleapis.com/LogEntry"
                name_descriptor: {
                  pattern: "projects/{project}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                }
                name_descriptor: {
                  pattern: "folders/{folder}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                  parent_name_extractor: "folders/{folder}"
                }
                name_descriptor: {
                  pattern: "organizations/{organization}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Organization"
                  parent_name_extractor: "organizations/{organization}"
                }
                name_descriptor: {
                  pattern: "billingAccounts/{billing_account}/logs/{log}"
                  parent_type: "billing.googleapis.com/BillingAccount"
                  parent_name_extractor: "billingAccounts/{billing_account}"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: 'logging.googleapis.com/LogEntry'
              name_descriptor:
                - pattern: "projects/{project}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                - pattern: "folders/{folder}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                  parent_name_extractor: "folders/{folder}"
                - pattern: "organizations/{organization}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Organization"
                  parent_name_extractor: "organizations/{organization}"
                - pattern: "billingAccounts/{billing_account}/logs/{log}"
                  parent_type: "billing.googleapis.com/BillingAccount"
                  parent_name_extractor: "billingAccounts/{billing_account}"

        For flexible resources, the resource name doesn't contain parent names,
        but the resource itself has parents for policy evaluation.

        Example:

        ::

            message Shelf {
              option (google.api.resource) = {
                type: "library.googleapis.com/Shelf"
                name_descriptor: {
                  pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                }
                name_descriptor: {
                  pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: 'library.googleapis.com/Shelf'
              name_descriptor:
                - pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                - pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> parent = client.tag_template_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]')
            >>>
            >>> # TODO: Initialize `tag_template_field_id`:
            >>> tag_template_field_id = ''
            >>>
            >>> # TODO: Initialize `tag_template_field`:
            >>> tag_template_field = {}
            >>>
            >>> response = client.create_tag_template_field(parent, tag_template_field_id, tag_template_field)

        Args:
            parent (str): Response message for ``ListTags``.
            tag_template_field_id (str): A generic empty message that you can re-use to avoid defining
                duplicated empty messages in your APIs. A typical example is to use it
                as the request or the response type of an API method. For instance:

                ::

                    service Foo {
                      rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
                    }

                The JSON representation for ``Empty`` is empty JSON object ``{}``.
            tag_template_field (Union[dict, ~google.cloud.datacatalog_v1beta1.types.TagTemplateField]): Required. The tag template field to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplateField`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplateField` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_tag_template_field" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_tag_template_field"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_tag_template_field,
                default_retry=self._method_configs["CreateTagTemplateField"].retry,
                default_timeout=self._method_configs["CreateTagTemplateField"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.CreateTagTemplateFieldRequest(
            parent=parent,
            tag_template_field_id=tag_template_field_id,
            tag_template_field=tag_template_field,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_tag_template_field"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_tag_template_field(
        self,
        name,
        tag_template_field,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The relative resource name of the resource in URL format. Examples:

        -  ``projects/{project_id}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``
        -  ``projects/{project_id}/tagTemplates/{tag_template_id}``

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.field_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]', '[FIELD]')
            >>>
            >>> # TODO: Initialize `tag_template_field`:
            >>> tag_template_field = {}
            >>>
            >>> response = client.update_tag_template_field(name, tag_template_field)

        Args:
            name (str): Request message for ``CreateTaxonomy``.
            tag_template_field (Union[dict, ~google.cloud.datacatalog_v1beta1.types.TagTemplateField]): Required. The template to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplateField`
            update_mask (Union[dict, ~google.cloud.datacatalog_v1beta1.types.FieldMask]): Lists the tags on an ``Entry``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplateField` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_tag_template_field" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_tag_template_field"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_tag_template_field,
                default_retry=self._method_configs["UpdateTagTemplateField"].retry,
                default_timeout=self._method_configs["UpdateTagTemplateField"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.UpdateTagTemplateFieldRequest(
            name=name, tag_template_field=tag_template_field, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_tag_template_field"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def rename_tag_template_field(
        self,
        name,
        new_tag_template_field_id,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Request message for ``UpdateTagTemplateField``.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.field_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]', '[FIELD]')
            >>>
            >>> # TODO: Initialize `new_tag_template_field_id`:
            >>> new_tag_template_field_id = ''
            >>>
            >>> response = client.rename_tag_template_field(name, new_tag_template_field_id)

        Args:
            name (str): Request message for ``GetTaxonomy``.
            new_tag_template_field_id (str): If this SourceCodeInfo represents a complete declaration, these are
                any comments appearing before and after the declaration which appear to
                be attached to the declaration.

                A series of line comments appearing on consecutive lines, with no other
                tokens appearing on those lines, will be treated as a single comment.

                leading_detached_comments will keep paragraphs of comments that appear
                before (but not connected to) the current element. Each paragraph,
                separated by empty lines, will be one comment element in the repeated
                field.

                Only the comment content is provided; comment markers (e.g. //) are
                stripped out. For block comments, leading whitespace and an asterisk
                will be stripped from the beginning of each line other than the first.
                Newlines are included in the output.

                Examples:

                optional int32 foo = 1; // Comment attached to foo. // Comment attached
                to bar. optional int32 bar = 2;

                optional string baz = 3; // Comment attached to baz. // Another line
                attached to baz.

                // Comment attached to qux. // // Another line attached to qux. optional
                double qux = 4;

                // Detached comment for corge. This is not leading or trailing comments
                // to qux or corge because there are blank lines separating it from //
                both.

                // Detached comment for corge paragraph 2.

                optional string corge = 5; /\* Block comment attached \* to corge.
                Leading asterisks \* will be removed. */ /* Block comment attached to \*
                grault. \*/ optional int32 grault = 6;

                // ignored detached comments.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.TagTemplateField` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "rename_tag_template_field" not in self._inner_api_calls:
            self._inner_api_calls[
                "rename_tag_template_field"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.rename_tag_template_field,
                default_retry=self._method_configs["RenameTagTemplateField"].retry,
                default_timeout=self._method_configs["RenameTagTemplateField"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.RenameTagTemplateFieldRequest(
            name=name, new_tag_template_field_id=new_tag_template_field_id
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["rename_tag_template_field"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_tag_template_field(
        self,
        name,
        force,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        If set, gives the index of a oneof in the containing type's
        oneof_decl list. This field is a member of that oneof.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.field_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]', '[FIELD]')
            >>>
            >>> # TODO: Initialize `force`:
            >>> force = False
            >>>
            >>> client.delete_tag_template_field(name, force)

        Args:
            name (str): Output only. If the table is a dated shard, i.e., with name pattern
                ``[prefix]YYYYMMDD``, ``grouped_entry`` is the Data Catalog resource
                name of the date sharded grouped entry, for example,
                ``projects/{project_id}/locations/{location}/entrygroups/{entry_group_id}/entries/{entry_id}``.
                Otherwise, ``grouped_entry`` is empty.
            force (bool): Sets the access control policy for a resource. Replaces any existing
                policy. Supported resources are:

                -  Tag templates.
                -  Entries.
                -  Entry groups. Note, this method cannot be used to manage policies for
                   BigQuery, Pub/Sub and any external Google Cloud Platform resources
                   synced to Data Catalog.

                Callers must have following Google IAM permission

                -  ``datacatalog.tagTemplates.setIamPolicy`` to set policies on tag
                   templates.
                -  ``datacatalog.entries.setIamPolicy`` to set policies on entries.
                -  ``datacatalog.entryGroups.setIamPolicy`` to set policies on entry
                   groups.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_tag_template_field" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_tag_template_field"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_tag_template_field,
                default_retry=self._method_configs["DeleteTagTemplateField"].retry,
                default_timeout=self._method_configs["DeleteTagTemplateField"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.DeleteTagTemplateFieldRequest(name=name, force=force)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_tag_template_field"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_tag(
        self,
        parent,
        tag,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Request message for ``GetEntryGroup``.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> parent = client.entry_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]', '[ENTRY]')
            >>>
            >>> # TODO: Initialize `tag`:
            >>> tag = {}
            >>>
            >>> response = client.create_tag(parent, tag)

        Args:
            parent (str): Required. The name of the entry. Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}
            tag (Union[dict, ~google.cloud.datacatalog_v1beta1.types.Tag]): Required. The tag to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.Tag`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.Tag` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_tag" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_tag"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_tag,
                default_retry=self._method_configs["CreateTag"].retry,
                default_timeout=self._method_configs["CreateTag"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.CreateTagRequest(parent=parent, tag=tag)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_tag"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_tag(
        self,
        tag,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates an existing tag.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> # TODO: Initialize `tag`:
            >>> tag = {}
            >>>
            >>> response = client.update_tag(tag)

        Args:
            tag (Union[dict, ~google.cloud.datacatalog_v1beta1.types.Tag]): Required. The updated tag. The "name" field must be set.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.Tag`
            update_mask (Union[dict, ~google.cloud.datacatalog_v1beta1.types.FieldMask]): The resource this metadata entry refers to.

                For Google Cloud Platform resources, ``linked_resource`` is the `full
                name of the
                resource <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__.
                For example, the ``linked_resource`` for a table resource from BigQuery
                is:

                -  //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

                Output only when Entry is of type in the EntryType enum. For entries
                with user_specified_type, this field is optional and defaults to an
                empty string.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.Tag` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_tag" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_tag"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_tag,
                default_retry=self._method_configs["UpdateTag"].retry,
                default_timeout=self._method_configs["UpdateTag"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.UpdateTagRequest(tag=tag, update_mask=update_mask)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("tag.name", tag.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_tag"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_tag(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a tag.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> name = client.tag_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]', '[ENTRY]', '[TAG]')
            >>>
            >>> client.delete_tag(name)

        Args:
            name (str): A Timestamp represents a point in time independent of any time zone
                or local calendar, encoded as a count of seconds and fractions of
                seconds at nanosecond resolution. The count is relative to an epoch at
                UTC midnight on January 1, 1970, in the proleptic Gregorian calendar
                which extends the Gregorian calendar backwards to year one.

                All minutes are 60 seconds long. Leap seconds are "smeared" so that no
                leap second table is needed for interpretation, using a `24-hour linear
                smear <https://developers.google.com/time/smear>`__.

                The range is from 0001-01-01T00:00:00Z to
                9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure
                that we can convert to and from `RFC
                3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ date strings.

                # Examples

                Example 1: Compute Timestamp from POSIX ``time()``.

                ::

                    Timestamp timestamp;
                    timestamp.set_seconds(time(NULL));
                    timestamp.set_nanos(0);

                Example 2: Compute Timestamp from POSIX ``gettimeofday()``.

                ::

                    struct timeval tv;
                    gettimeofday(&tv, NULL);

                    Timestamp timestamp;
                    timestamp.set_seconds(tv.tv_sec);
                    timestamp.set_nanos(tv.tv_usec * 1000);

                Example 3: Compute Timestamp from Win32 ``GetSystemTimeAsFileTime()``.

                ::

                    FILETIME ft;
                    GetSystemTimeAsFileTime(&ft);
                    UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;

                    // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z
                    // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.
                    Timestamp timestamp;
                    timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));
                    timestamp.set_nanos((INT32) ((ticks % 10000000) * 100));

                Example 4: Compute Timestamp from Java ``System.currentTimeMillis()``.

                ::

                    long millis = System.currentTimeMillis();

                    Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)
                        .setNanos((int) ((millis % 1000) * 1000000)).build();

                Example 5: Compute Timestamp from current time in Python.

                ::

                    timestamp = Timestamp()
                    timestamp.GetCurrentTime()

                # JSON Mapping

                In JSON format, the Timestamp type is encoded as a string in the `RFC
                3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ format. That is, the
                format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where
                {year} is always expressed using four digits while {month}, {day},
                {hour}, {min}, and {sec} are zero-padded to two digits each. The
                fractional seconds, which can go up to 9 digits (i.e. up to 1 nanosecond
                resolution), are optional. The "Z" suffix indicates the timezone
                ("UTC"); the timezone is required. A proto3 JSON serializer should
                always use UTC (as indicated by "Z") when printing the Timestamp type
                and a proto3 JSON parser should be able to accept both UTC and other
                timezones (as indicated by an offset).

                For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30
                UTC on January 15, 2017.

                In JavaScript, one can convert a Date object to this format using the
                standard
                `toISOString() <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString>`__
                method. In Python, a standard ``datetime.datetime`` object can be
                converted to this format using
                ```strftime`` <https://docs.python.org/2/library/time.html#time.strftime>`__
                with the time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java,
                one can use the Joda Time's
                ```ISODateTimeFormat.dateTime()`` <http://www.joda.org/joda-time/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime%2D%2D>`__
                to obtain a formatter capable of generating timestamps in this format.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_tag" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_tag"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_tag,
                default_retry=self._method_configs["DeleteTag"].retry,
                default_timeout=self._method_configs["DeleteTag"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.DeleteTagRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_tag"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_tags(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Request message for ``SetIamPolicy`` method.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> parent = client.entry_path('[PROJECT]', '[LOCATION]', '[ENTRY_GROUP]', '[ENTRY]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_tags(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_tags(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): This field indicates the entry's source system that Data Catalog
                does not integrate with. ``user_specified_system`` strings must begin
                with a letter or underscore and can only contain letters, numbers, and
                underscores; are case insensitive; must be at least 1 character and at
                most 64 characters long.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.datacatalog_v1beta1.types.Tag` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_tags" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_tags"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_tags,
                default_retry=self._method_configs["ListTags"].retry,
                default_timeout=self._method_configs["ListTags"].timeout,
                client_info=self._client_info,
            )

        request = datacatalog_pb2.ListTagsRequest(parent=parent, page_size=page_size)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_tags"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="tags",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def set_iam_policy(
        self,
        resource,
        policy,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Required. The name of the tag template field. Example:

        -  projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> resource = client.tag_template_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]')
            >>>
            >>> # TODO: Initialize `policy`:
            >>> policy = {}
            >>>
            >>> response = client.set_iam_policy(resource, policy)

        Args:
            resource (str): REQUIRED: The resource for which the policy is being specified.
                See the operation documentation for the appropriate value for this field.
            policy (Union[dict, ~google.cloud.datacatalog_v1beta1.types.Policy]): Optional. The maximum number of items to return. Default is 10. Max
                limit is 1000. Throws an invalid argument for ``page_size > 1000``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.Policy`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.Policy` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_iam_policy" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_iam_policy"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_iam_policy,
                default_retry=self._method_configs["SetIamPolicy"].retry,
                default_timeout=self._method_configs["SetIamPolicy"].timeout,
                client_info=self._client_info,
            )

        request = iam_policy_pb2.SetIamPolicyRequest(resource=resource, policy=policy)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("resource", resource)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_iam_policy"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_iam_policy(
        self,
        resource,
        options_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The full name of the cloud resource the entry belongs to. See:
        https://cloud.google.com/apis/design/resource_names#full_resource_name.
        Example:

        -  ``//bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId``

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> resource = client.tag_template_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]')
            >>>
            >>> response = client.get_iam_policy(resource)

        Args:
            resource (str): REQUIRED: The resource for which the policy is being requested.
                See the operation documentation for the appropriate value for this field.
            options_ (Union[dict, ~google.cloud.datacatalog_v1beta1.types.GetPolicyOptions]): Output only. The resource name of the tag template field in URL
                format. Example:

                -  projects/{project_id}/locations/{location}/tagTemplates/{tag_template}/fields/{field}

                Note that this TagTemplateField may not actually be stored in the
                location in this name.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datacatalog_v1beta1.types.GetPolicyOptions`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.Policy` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_iam_policy" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_iam_policy"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_iam_policy,
                default_retry=self._method_configs["GetIamPolicy"].retry,
                default_timeout=self._method_configs["GetIamPolicy"].timeout,
                client_info=self._client_info,
            )

        request = iam_policy_pb2.GetIamPolicyRequest(
            resource=resource, options=options_
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("resource", resource)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_iam_policy"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def test_iam_permissions(
        self,
        resource,
        permissions,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        A taxonomy is a collection of policy tags that classify data along a
        common axis. For instance a data *sensitivity* taxonomy could contain
        policy tags denoting PII such as age, zipcode, and SSN. A data *origin*
        taxonomy could contain policy tags to distinguish user data, employee
        data, partner data, public data.

        Example:
            >>> from google.cloud import datacatalog_v1beta1
            >>>
            >>> client = datacatalog_v1beta1.DataCatalogClient()
            >>>
            >>> resource = client.tag_template_path('[PROJECT]', '[LOCATION]', '[TAG_TEMPLATE]')
            >>>
            >>> # TODO: Initialize `permissions`:
            >>> permissions = []
            >>>
            >>> response = client.test_iam_permissions(resource, permissions)

        Args:
            resource (str): REQUIRED: The resource for which the policy detail is being requested.
                See the operation documentation for the appropriate value for this field.
            permissions (list[str]): Required. The name of the tag to delete. Example:

                -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}/tags/{tag_id}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datacatalog_v1beta1.types.TestIamPermissionsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "test_iam_permissions" not in self._inner_api_calls:
            self._inner_api_calls[
                "test_iam_permissions"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.test_iam_permissions,
                default_retry=self._method_configs["TestIamPermissions"].retry,
                default_timeout=self._method_configs["TestIamPermissions"].timeout,
                client_info=self._client_info,
            )

        request = iam_policy_pb2.TestIamPermissionsRequest(
            resource=resource, permissions=permissions
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("resource", resource)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["test_iam_permissions"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
