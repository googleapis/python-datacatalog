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
# Snippet for RenameTagTemplateFieldEnumValue
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datacatalog


# [START datacatalog_generated_datacatalog_v1_DataCatalog_RenameTagTemplateFieldEnumValue_async]
from google.cloud import datacatalog_v1


async def sample_rename_tag_template_field_enum_value():
    # Create a client
    client = datacatalog_v1.DataCatalogAsyncClient()

    # Initialize request argument(s)
    request = datacatalog_v1.RenameTagTemplateFieldEnumValueRequest(
        name="name_value",
        new_enum_value_display_name="new_enum_value_display_name_value",
    )

    # Make the request
    response = await client.rename_tag_template_field_enum_value(request=request)

    # Handle response
    print(response)

# [END datacatalog_generated_datacatalog_v1_DataCatalog_RenameTagTemplateFieldEnumValue_async]
