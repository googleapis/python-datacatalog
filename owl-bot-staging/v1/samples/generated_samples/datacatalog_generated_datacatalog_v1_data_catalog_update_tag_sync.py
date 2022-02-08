# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Snippet for UpdateTag
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datacatalog


# [START datacatalog_generated_datacatalog_v1_DataCatalog_UpdateTag_sync]
from google.cloud import datacatalog_v1


def sample_update_tag():
    # Create a client
    client = datacatalog_v1.DataCatalogClient()

    # Initialize request argument(s)
    tag = datacatalog_v1.Tag()
    tag.column = "column_value"
    tag.template = "template_value"

    request = datacatalog_v1.UpdateTagRequest(
        tag=tag,
    )

    # Make the request
    response = client.update_tag(request=request)

    # Handle response
    print(response)

# [END datacatalog_generated_datacatalog_v1_DataCatalog_UpdateTag_sync]
