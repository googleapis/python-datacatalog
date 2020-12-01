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


import datetime
import uuid

import google.auth
from google.cloud import bigquery
from google.cloud import datacatalog_v1

import pytest

bigquery_client = bigquery.Client()


@pytest.fixture(scope="session")
def client(credentials):
    return datacatalog_v1.DataCatalogClient(credentials=credentials)


@pytest.fixture(scope="session")
def default_credentials():
    return google.auth.default()


@pytest.fixture(scope="session")
def credentials(default_credentials):
    return default_credentials[0]


@pytest.fixture(scope="session")
def project_id(default_credentials):
    return default_credentials[1]


@pytest.fixture
def dataset_id():
    now = datetime.datetime.now()
    dataset_id = "python_dataset_sample_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    dataset = bigquery_client.create_dataset(dataset_id)
    yield dataset.dataset_id
    bigquery_client.delete_dataset(dataset, delete_contents=True, not_found_ok=True)


@pytest.fixture
def table_id(project_id, dataset_id):
    now = datetime.datetime.now()
    table_id = "python_table_sample_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    table = bigquery.Table("{}.{}.{}".format(project_id, dataset_id, table_id))
    table = bigquery_client.create_table(table)
    yield table.table_id
    bigquery_client.delete_table(table, not_found_ok=True)


@pytest.fixture
def random_entry_id(client, project_id, random_entry_group_id):
    location = "us-central1"
    now = datetime.datetime.now()
    random_entry_id = "example_entry_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    yield random_entry_id
    entry_name = datacatalog_v1.DataCatalogClient.entry_path(
        project_id, location, random_entry_group_id, random_entry_id
    )
    client.delete_entry(request={"name": entry_name})


@pytest.fixture
def random_entry_group_id(client, project_id):
    location = "us-central1"
    now = datetime.datetime.now()
    random_entry_group_id = "example_entry_group_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    yield random_entry_group_id
    entry_group_name = datacatalog_v1.DataCatalogClient.entry_group_path(
        project_id, location, random_entry_group_id
    )
    client.delete_entry_group(request={"name": entry_group_name})


@pytest.fixture
def random_entry_name(client, entry_group_name):
    now = datetime.datetime.now()
    random_entry_id = "example_entry_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    random_entry_name = "{}/entries/{}".format(entry_group_name, random_entry_id)
    yield random_entry_name
    client.delete_entry(request={"name": random_entry_name})


@pytest.fixture
def entry_group_name(client, project_id):
    now = datetime.datetime.now()
    entry_group_id = "python_entry_group_sample_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    entry_group = client.create_entry_group(
        request={
            "parent": datacatalog_v1.DataCatalogClient.location_path(
                project_id, "us-central1"
            ),
            "entry_group_id": entry_group_id,
            "entry_group": {},
        }
    )
    yield entry_group.name
    client.delete_entry_group(request={"name": entry_group.name})


@pytest.fixture
def random_tag_template_id(client, project_id):
    location = "us-central1"
    now = datetime.datetime.now()
    random_tag_template_id = "python_tag_template_sample_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    random_tag_template = datacatalog_v1.types.TagTemplate()
    random_tag_template.fields["source"] = datacatalog_v1.types.TagTemplateField()
    random_tag_template.fields[
        "source"
    ].type_.primitive_type = datacatalog_v1.FieldType.PrimitiveType.STRING.value
    random_tag_template = client.create_tag_template(
        parent=datacatalog_v1.DataCatalogClient.common_location_path(
            project_id, location
        ),
        tag_template_id=random_tag_template_id,
        tag_template=random_tag_template,
    )
    yield random_tag_template_id
    random_tag_template_name = client.tag_template_path(
        project_id, location, random_tag_template_id
    )
    client.delete_tag_template(name=random_tag_template_name, force=True)
