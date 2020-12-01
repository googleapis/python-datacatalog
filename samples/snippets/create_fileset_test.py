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


import create_fileset


def test_create_fileset(capsys, project_id, random_entry_group_id, random_entry_id):
    create_fileset.create_fileset(project_id, random_entry_group_id, random_entry_id)
    out, err = capsys.readouterr()
    assert "Created entry group:"
    " projects/{}/locations/{}/entryGroups/{}".format(
        project_id, "us-central1", random_entry_group_id
    ) in out
    assert "Created entry:"
    " projects/{}/locations/{}/entryGroups/{}/entries/{}".format(
        project_id, "us-central1", random_entry_group_id, random_entry_id
    ) in out
