# Copyright 2021 Google LLC
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


def create_taxonomy(client, project_id, display_name):

    # [START data_catalog_create_taxonomy_tag]
    from google.cloud import datacatalog

    # TODO(developer): Construct a Policy Tag Manager client object.
    # client = datacatalog.PolicyTagManagerClient()

    # TODO(developer): Set project_id to the ID of the project the
    #  taxonomy will belong to.
    # project_id = 'your-project-id'

    # TODO(developer): Specify the geographic location where the
    #  taxonomy should reside.
    location_id = 'us'

    # Construct a full location path to be the parent of the taxonomy.
    parent = datacatalog.PolicyTagManagerClient.common_location_path(
        project_id, location_id
    )

    taxonomy = datacatalog.Taxonomy()
    # TODO(developer): Construct a full Taxonomy object to send to the API.
    taxonomy.display_name = display_name
    taxonomy.description = 'This Taxonomy represents ...'

    # Send the taxonomy to the API for creation.
    taxonomy = client.create_taxonomy(parent=parent, taxonomy=taxonomy)
    print(f'Created taxonomy {taxonomy.name}')
    # [END data_catalog_create_taxonomy_tag]
