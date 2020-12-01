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


def create_custom_entry(project_id, entry_group_id, entry_id, tag_template_id):
    """Creates a custom entry within an entry group."""
    # [START data_catalog_create_custom_entry]
    # -------------------------------
    # Import required modules.
    # -------------------------------
    from google.api_core.exceptions import NotFound, PermissionDenied
    from google.cloud import datacatalog_v1

    # -------------------------------
    # TODO: Set these values before running the sample.
    # -------------------------------
    # project_id = 'my-project'
    # entry_group_id = 'onprem_entry_group'
    # entry_id = 'onprem_entry_id'
    # tag_template_id = 'onprem_tag_template'

    # -------------------------------
    # Currently, Data Catalog stores metadata in the
    # us-central1 region.
    # -------------------------------
    location = "us-central1"

    # -------------------------------
    # Use Application Default Credentials to create a new
    # Data Catalog client. GOOGLE_APPLICATION_CREDENTIALS
    # environment variable must be set with the location
    # of a service account key file.
    # -------------------------------
    datacatalog = datacatalog_v1.DataCatalogClient()

    # -------------------------------
    # 1. Environment cleanup: delete pre-existing data.
    # -------------------------------
    # Delete any pre-existing Entry with the same name
    # that will be used in step 3.
    expected_entry_name = datacatalog_v1.DataCatalogClient.entry_path(
        project_id, location, entry_group_id, entry_id
    )

    try:
        datacatalog.delete_entry(name=expected_entry_name)
    except (NotFound, PermissionDenied):
        pass

    # Delete any pre-existing Entry Group with the same name
    # that will be used in step 2.
    expected_entry_group_name = datacatalog_v1.DataCatalogClient.entry_group_path(
        project_id, location, entry_group_id
    )

    try:
        datacatalog.delete_entry_group(name=expected_entry_group_name)
    except (NotFound, PermissionDenied):
        pass

    # Delete any pre-existing Template with the same name
    # that will be used in step 4.
    expected_template_name = datacatalog_v1.DataCatalogClient.tag_template_path(
        project_id, location, tag_template_id
    )

    try:
        datacatalog.delete_tag_template(name=expected_template_name, force=True)
    except (NotFound, PermissionDenied):
        pass

    # -------------------------------
    # 2. Create an Entry Group.
    # -------------------------------
    entry_group_obj = datacatalog_v1.types.EntryGroup()
    entry_group_obj.display_name = "My awesome Entry Group"
    entry_group_obj.description = "This Entry Group represents an external system"

    entry_group = datacatalog.create_entry_group(
        parent=datacatalog_v1.DataCatalogClient.common_location_path(
            project_id, location
        ),
        entry_group_id=entry_group_id,
        entry_group=entry_group_obj,
    )
    print("Created entry group: {}".format(entry_group.name))

    # -------------------------------
    # 3. Create an Entry.
    # -------------------------------
    entry = datacatalog_v1.types.Entry()
    entry.user_specified_system = "onprem_data_system"
    entry.user_specified_type = "onprem_data_asset"
    entry.display_name = "My awesome data asset"
    entry.description = "This data asset is managed by an external system."
    entry.linked_resource = "//my-onprem-server.com/dataAssets/my-awesome-data-asset"

    # Create the Schema, this is optional.x
    columns = []
    columns.append(
        datacatalog_v1.types.ColumnSchema(
            column="first_column",
            type_="STRING",
            description="This columns consists of ....",
            mode=None,
        )
    )

    columns.append(
        datacatalog_v1.types.ColumnSchema(
            column="second_column",
            type_="DOUBLE",
            description="This columns consists of ....",
            mode=None,
        )
    )

    entry.schema.columns.extend(columns)

    entry = datacatalog.create_entry(
        parent=entry_group.name, entry_id=entry_id, entry=entry
    )
    print("Created entry: {}".format(entry.name))

    # -------------------------------
    # 4. Create a Tag Template.
    # For more field types, including ENUM, please refer to
    # https://cloud.google.com/data-catalog/docs/quickstarts/quickstart-search-tag#data-catalog
    # -quickstart-python.
    # -------------------------------
    tag_template = datacatalog_v1.types.TagTemplate()
    tag_template.display_name = "On-premises Tag Template"
    tag_template.fields["source"] = datacatalog_v1.types.TagTemplateField()
    tag_template.fields["source"].display_name = "Source of the data asset"
    tag_template.fields[
        "source"
    ].type_.primitive_type = datacatalog_v1.FieldType.PrimitiveType.STRING.value

    tag_template = datacatalog.create_tag_template(
        parent=datacatalog_v1.DataCatalogClient.common_location_path(
            project_id, location
        ),
        tag_template_id=tag_template_id,
        tag_template=tag_template,
    )
    print("Created template: {}".format(tag_template.name))

    # -------------------------------
    # 5. Attach a Tag to the custom Entry.
    # -------------------------------
    tag = datacatalog_v1.types.Tag()
    tag.template = tag_template.name
    tag.fields["source"] = datacatalog_v1.types.TagField()
    tag.fields["source"].string_value = "On-premises system name"

    tag = datacatalog.create_tag(parent=entry.name, tag=tag)
    print("Created tag: {}".format(tag.name))
    # [END data_catalog_create_custom_entry]
