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


def create_fileset(project_id, fileset_entry_group_id, fileset_entry_id):
    """Creates a fileset within an entry group."""
    # [START data_catalog_create_fileset]
    # -------------------------------
    # Import required modules.
    # -------------------------------
    from google.api_core.exceptions import NotFound, PermissionDenied
    from google.cloud import datacatalog_v1

    # -------------------------------
    # TODO: Set these values before running the sample.
    # -------------------------------
    # project_id = 'project_id'
    # fileset_entry_group_id = 'entry_group_id'
    # fileset_entry_id = 'entry_id'

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
        project_id, location, fileset_entry_group_id, fileset_entry_id
    )

    try:
        datacatalog.delete_entry(name=expected_entry_name)
    except (NotFound, PermissionDenied):
        pass

    # Delete any pre-existing Entry Group with the same name
    # that will be used in step 2.
    expected_entry_group_name = datacatalog_v1.DataCatalogClient.entry_group_path(
        project_id, location, fileset_entry_group_id
    )

    try:
        datacatalog.delete_entry_group(name=expected_entry_group_name)
    except (NotFound, PermissionDenied):
        pass

    # -------------------------------
    # 2. Create an Entry Group.
    # -------------------------------
    entry_group_obj = datacatalog_v1.types.EntryGroup()
    entry_group_obj.display_name = "My Fileset Entry Group"
    entry_group_obj.description = "This Entry Group consists of ...."

    entry_group = datacatalog.create_entry_group(
        parent=datacatalog_v1.DataCatalogClient.common_location_path(
            project_id, location
        ),
        entry_group_id=fileset_entry_group_id,
        entry_group=entry_group_obj,
    )
    print("Created entry group: {}".format(entry_group.name))

    # -------------------------------
    # 3. Create a Fileset Entry.
    # -------------------------------
    entry = datacatalog_v1.types.Entry()
    entry.display_name = "My Fileset"
    entry.description = "This fileset consists of ...."
    entry.gcs_fileset_spec.file_patterns.append("gs://my_bucket/*")
    entry.type_ = datacatalog_v1.EntryType.FILESET

    # Create the Schema, for example when you have a csv file.
    columns = []
    columns.append(
        datacatalog_v1.types.ColumnSchema(
            column="first_name",
            description="First name",
            mode="REQUIRED",
            type_="STRING",
        )
    )

    columns.append(
        datacatalog_v1.types.ColumnSchema(
            column="last_name", description="Last name", mode="REQUIRED", type_="STRING"
        )
    )

    # Create sub columns for the addresses parent column
    subcolumns = []

    subcolumns.append(
        datacatalog_v1.types.ColumnSchema(
            column="city", description="City", mode="NULLABLE", type_="STRING"
        )
    )

    subcolumns.append(
        datacatalog_v1.types.ColumnSchema(
            column="state", description="State", mode="NULLABLE", type_="STRING"
        )
    )

    columns.append(
        datacatalog_v1.types.ColumnSchema(
            column="addresses",
            description="Addresses",
            mode="REPEATED",
            subcolumns=subcolumns,
            type_="RECORD",
        )
    )

    entry.schema.columns.extend(columns)

    entry = datacatalog.create_entry(
        parent=entry_group.name, entry_id=fileset_entry_id, entry=entry
    )
    print("Created entry: {}".format(entry.name))
    # [END data_catalog_create_fileset]
