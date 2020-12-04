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

import create_custom_entry


def test_create_custom_entry(
    capsys,
    client,
    project_id,
    random_entry_group_id,
    random_entry_id,
    random_tag_template_id,
    resources_to_delete,
):
    location = "us-central1"
    override_values = {
        "project_id": project_id,
        "entry_group_id": random_entry_group_id,
        "entry_id": random_entry_id,
        "tag_template_id": random_tag_template_id,
        "tag_name": "tagtastic",
    }
    expected_group = client.entry_group_path(
        project_id, location, random_entry_group_id
    )
    expected_entry = client.entry_path(
        project_id, location, random_entry_group_id, random_entry_id
    )
    expected_template = client.tag_template_path(
        project_id, location, random_tag_template_id
    )
    create_custom_entry.create_custom_entry(override_values)
    out, err = capsys.readouterr()
    assert f"Created entry group: {expected_group}" in out
    assert f"Created entry: {expected_entry}" in out
    assert f"Created template: {expected_template}" in out
    assert "Created tag:" in out
    resources_to_delete["entry_groups"].append(expected_group)
    resources_to_delete["entries"].append(expected_entry)
    resources_to_delete["templates"].append(expected_template)
