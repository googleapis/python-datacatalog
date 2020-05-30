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

import datetime
import uuid

import pytest

import google.auth
from google.cloud import datacatalog


@pytest.fixture(scope="session")
def policy_tag_manager_client(credentials):
    return datacatalog.PolicyTagManagerClient(credentials=credentials)


@pytest.fixture
def random_taxonomy_display_name(policy_tag_manager_client, project_id):
    now = datetime.datetime.now()
    random_display_name = f'example_taxonomy' \
                          f'_{now.strftime("%Y%m%d%H%M%S")}' \
                          f'_{uuid.uuid4().hex[:8]}'
    yield random_display_name
    parent = datacatalog.PolicyTagManagerClient.common_location_path(
        project_id, 'us'
    )
    taxonomies = policy_tag_manager_client.list_taxonomies(parent=parent)
    taxonomy = next(
        (t for t in taxonomies if t.display_name == random_display_name), None)
    if taxonomy:
        policy_tag_manager_client.delete_taxonomy(name=taxonomy.name)


@pytest.fixture(scope="session")
def default_credentials():
    return google.auth.default()


@pytest.fixture(scope="session")
def credentials(default_credentials):
    return default_credentials[0]


@pytest.fixture(scope="session")
def project_id(default_credentials):
    return default_credentials[1]
