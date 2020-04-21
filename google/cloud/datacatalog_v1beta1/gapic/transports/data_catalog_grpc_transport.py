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


import google.api_core.grpc_helpers

from google.cloud.datacatalog_v1beta1.proto import datacatalog_pb2_grpc


class DataCatalogGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.datacatalog.v1beta1 DataCatalog API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self, channel=None, credentials=None, address="datacatalog.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "data_catalog_stub": datacatalog_pb2_grpc.DataCatalogStub(channel)
        }

    @classmethod
    def create_channel(
        cls, address="datacatalog.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def search_catalog(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.search_catalog`.

        If type_name is set, this need not be set. If both this and
        type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or
        TYPE_GROUP.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].SearchCatalog

    @property
    def create_entry_group(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.create_entry_group`.

        Required. The name of the project and the template location
        `region <https://cloud.google.com/data-catalog/docs/concepts/regions>`__.

        Example:

        -  projects/{project_id}/locations/us-central1/tagTemplates/{tag_template_id}

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].CreateEntryGroup

    @property
    def get_entry_group(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.get_entry_group`.

        Gets an EntryGroup.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].GetEntryGroup

    @property
    def delete_entry_group(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.delete_entry_group`.

        Required. The ID of the tag template field to create. Field ids can
        contain letters (both uppercase and lowercase), numbers (0-9),
        underscores (_) and dashes (-). Field IDs must be at least 1 character
        long and at most 128 characters long. Field IDs must also be unique
        within their template.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].DeleteEntryGroup

    @property
    def create_entry(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.create_entry`.

        Request message for ``CreateEntry``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].CreateEntry

    @property
    def update_entry(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.update_entry`.

        For extensions, this is the name of the type being extended. It is
        resolved in the same manner as type_name.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].UpdateEntry

    @property
    def delete_entry(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.delete_entry`.

        Required. The name of the entry group this entry is in. Example:

        -  projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}

        Note that this Entry and its child resources may not actually be stored
        in the location in this name.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].DeleteEntry

    @property
    def get_entry(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.get_entry`.

        Gets an entry.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].GetEntry

    @property
    def lookup_entry(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.lookup_entry`.

        Get an entry by target resource name. This method allows clients to use
        the resource name from the source Google Cloud Platform service to get the
        Data Catalog Entry.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].LookupEntry

    @property
    def list_entry_groups(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.list_entry_groups`.

        Lists entry groups.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].ListEntryGroups

    @property
    def list_entries(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.list_entries`.

        Lists entries.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].ListEntries

    @property
    def update_entry_group(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.update_entry_group`.

        An annotation that describes a resource definition without a
        corresponding message; see ``ResourceDescriptor``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].UpdateEntryGroup

    @property
    def create_tag_template(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.create_tag_template`.

        An annotation that describes a resource definition, see
        ``ResourceDescriptor``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].CreateTagTemplate

    @property
    def get_tag_template(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.get_tag_template`.

        Gets a tag template.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].GetTagTemplate

    @property
    def update_tag_template(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.update_tag_template`.

        Updates a tag template. This method cannot be used to update the
        fields of a template. The tag template fields are represented as
        separate resources and should be updated using their own
        create/update/delete methods. Users should enable the Data Catalog API
        in the project identified by the ``tag_template.name`` parameter (see
        [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].UpdateTagTemplate

    @property
    def delete_tag_template(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.delete_tag_template`.

        Sub-type of the search result. This is a dot-delimited description
        of the resource's full type, and is the same as the value callers would
        provide in the "type" search facet. Examples: ``entry.table``,
        ``entry.dataStream``, ``tagTemplate``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].DeleteTagTemplate

    @property
    def create_tag_template_field(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.create_tag_template_field`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].CreateTagTemplateField

    @property
    def update_tag_template_field(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.update_tag_template_field`.

        The relative resource name of the resource in URL format. Examples:

        -  ``projects/{project_id}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``
        -  ``projects/{project_id}/tagTemplates/{tag_template_id}``

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].UpdateTagTemplateField

    @property
    def rename_tag_template_field(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.rename_tag_template_field`.

        Request message for ``UpdateTagTemplateField``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].RenameTagTemplateField

    @property
    def delete_tag_template_field(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.delete_tag_template_field`.

        If set, gives the index of a oneof in the containing type's
        oneof_decl list. This field is a member of that oneof.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].DeleteTagTemplateField

    @property
    def create_tag(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.create_tag`.

        Request message for ``GetEntryGroup``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].CreateTag

    @property
    def update_tag(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.update_tag`.

        Updates an existing tag.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].UpdateTag

    @property
    def delete_tag(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.delete_tag`.

        Deletes a tag.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].DeleteTag

    @property
    def list_tags(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.list_tags`.

        Request message for ``SetIamPolicy`` method.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].ListTags

    @property
    def set_iam_policy(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.set_iam_policy`.

        Required. The name of the tag template field. Example:

        -  projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].SetIamPolicy

    @property
    def get_iam_policy(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.get_iam_policy`.

        The full name of the cloud resource the entry belongs to. See:
        https://cloud.google.com/apis/design/resource_names#full_resource_name.
        Example:

        -  ``//bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId``

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].GetIamPolicy

    @property
    def test_iam_permissions(self):
        """Return the gRPC stub for :meth:`DataCatalogClient.test_iam_permissions`.

        A taxonomy is a collection of policy tags that classify data along a
        common axis. For instance a data *sensitivity* taxonomy could contain
        policy tags denoting PII such as age, zipcode, and SSN. A data *origin*
        taxonomy could contain policy tags to distinguish user data, employee
        data, partner data, public data.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["data_catalog_stub"].TestIamPermissions
