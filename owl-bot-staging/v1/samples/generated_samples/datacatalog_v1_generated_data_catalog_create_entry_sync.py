# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateEntry
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datacatalog


# [START datacatalog_v1_generated_DataCatalog_CreateEntry_sync]
from google.cloud import datacatalog_v1


def sample_create_entry():
    # Create a client
    client = datacatalog_v1.DataCatalogClient()

    # Initialize request argument(s)
    entry = datacatalog_v1.Entry()
    entry.type_ = "SERVICE"
    entry.integrated_system = "DATAPLEX"
    entry.gcs_fileset_spec.file_patterns = ['file_patterns_value_1', 'file_patterns_value_2']

    request = datacatalog_v1.CreateEntryRequest(
        parent="parent_value",
        entry_id="entry_id_value",
        entry=entry,
    )

    # Make the request
    response = client.create_entry(request=request)

    # Handle the response
    print(response)

# [END datacatalog_v1_generated_DataCatalog_CreateEntry_sync]
