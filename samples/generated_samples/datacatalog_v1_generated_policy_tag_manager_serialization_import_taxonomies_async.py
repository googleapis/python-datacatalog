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
# Snippet for ImportTaxonomies
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datacatalog


# [START datacatalog_v1_generated_PolicyTagManagerSerialization_ImportTaxonomies_async]
from google.cloud import datacatalog_v1


async def sample_import_taxonomies():
    # Create a client
    client = datacatalog_v1.PolicyTagManagerSerializationAsyncClient()

    # Initialize request argument(s)
    inline_source = datacatalog_v1.InlineSource()
    inline_source.taxonomies.display_name = "display_name_value"

    request = datacatalog_v1.ImportTaxonomiesRequest(
        inline_source=inline_source,
        parent="parent_value",
    )

    # Make the request
    response = await client.import_taxonomies(request=request)

    # Handle the response
    print(response)

# [END datacatalog_v1_generated_PolicyTagManagerSerialization_ImportTaxonomies_async]
