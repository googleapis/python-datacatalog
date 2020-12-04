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


import lookup_entry_sql_resource


def test_lookup_entry(client, sql_entry):
    sql_name, entry_name = sql_entry
    entry = lookup_entry_sql_resource.sample_lookup_entry(sql_name)
    assert entry.name == entry_name
