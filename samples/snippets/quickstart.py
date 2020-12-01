# Copyright 2019 Google LLC
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


def quickstart(project_id, dataset_id, table_id):
    """Creates a tag template and attach a tag to a BigQuery table."""
    # [START data_catalog_quickstart]
    # -------------------------------
    # Import required modules.
    # -------------------------------
    from google.cloud import datacatalog_v1
    from google.api_core.exceptions import NotFound, PermissionDenied

    # -------------------------------
    # TODO: Set these values before running the sample.
    # -------------------------------
    # project_id = "my_project"
    # # Set dataset_id to the ID of existing dataset.
    # dataset_id = "demo_dataset"
    # # Set table_id to the ID of existing table.
    # table_id = "trips"

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
    datacatalog_client = datacatalog_v1.DataCatalogClient()

    # -------------------------------
    # Create a Tag Template.
    # -------------------------------
    tag_template = datacatalog_v1.types.TagTemplate()

    tag_template.display_name = "Demo Tag Template"

    tag_template.fields["source"] = datacatalog_v1.types.TagTemplateField()
    tag_template.fields["source"].display_name = "Source of data asset"
    tag_template.fields[
        "source"
    ].type_.primitive_type = datacatalog_v1.types.FieldType.PrimitiveType.STRING

    tag_template.fields["num_rows"] = datacatalog_v1.types.TagTemplateField()
    tag_template.fields["num_rows"].display_name = "Number of rows in data asset"
    tag_template.fields[
        "num_rows"
    ].type_.primitive_type = datacatalog_v1.types.FieldType.PrimitiveType.DOUBLE

    tag_template.fields["has_pii"] = datacatalog_v1.types.TagTemplateField()
    tag_template.fields["has_pii"].display_name = "Has PII"
    tag_template.fields[
        "has_pii"
    ].type_.primitive_type = datacatalog_v1.types.FieldType.PrimitiveType.BOOL

    tag_template.fields["pii_type"] = datacatalog_v1.types.TagTemplateField()
    tag_template.fields["pii_type"].display_name = "PII type"

    for display_name in ["EMAIL", "SOCIAL SECURITY NUMBER", "NONE"]:
        enum_value = datacatalog_v1.types.FieldType.EnumType.EnumValue(
            display_name=display_name
        )
        tag_template.fields["pii_type"].type_.enum_type.allowed_values.append(
            enum_value
        )

    expected_template_name = datacatalog_v1.DataCatalogClient.tag_template_path(
        project_id, location, "example_tag_template"
    )

    # Delete any pre-existing Template with the same name.
    try:
        datacatalog_client.delete_tag_template(name=expected_template_name, force=True)
        print("Deleted template: {}".format(expected_template_name))
    except (NotFound, PermissionDenied):
        print("Cannot delete template: {}".format(expected_template_name))

    # Create the Tag Template.
    try:
        tag_template = datacatalog_client.create_tag_template(
            parent="projects/{}/locations/us-central1".format(project_id),
            tag_template_id="example_tag_template",
            tag_template=tag_template,
        )
        print("Created template: {}".format(tag_template.name))
    except OSError as e:
        print("Cannot create template: {}".format(expected_template_name))
        print("{}".format(e))

    # -------------------------------
    # Lookup Data Catalog's Entry referring to the table.
    # -------------------------------
    resource_name = (
        "//bigquery.googleapis.com/projects/{}"
        "/datasets/{}/tables/{}".format(project_id, dataset_id, table_id)
    )
    table_entry = datacatalog_client.lookup_entry(
        request={"linked_resource": resource_name}
    )

    # -------------------------------
    # Attach a Tag to the table.
    # -------------------------------
    tag = datacatalog_v1.types.Tag()

    tag.template = tag_template.name
    tag.name = "my_tag"

    tag.fields["source"] = datacatalog_v1.types.TagField()
    tag.fields["source"].string_value = "Copied from tlc_yellow_trips_2018"

    tag.fields["num_rows"] = datacatalog_v1.types.TagField()
    tag.fields["num_rows"].double_value = 113496874

    tag.fields["has_pii"] = datacatalog_v1.types.TagField()
    tag.fields["has_pii"].bool_value = False

    tag.fields["pii_type"] = datacatalog_v1.types.TagField()
    tag.fields["pii_type"].enum_value.display_name = "NONE"

    tag = datacatalog_client.create_tag(parent=table_entry.name, tag=tag)
    print("Created tag: {}".format(tag.name))
    # [END data_catalog_quickstart]
