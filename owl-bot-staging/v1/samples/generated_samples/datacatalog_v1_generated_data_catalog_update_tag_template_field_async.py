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
# Snippet for UpdateTagTemplateField
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datacatalog


# [START datacatalog_v1_generated_DataCatalog_UpdateTagTemplateField_async]
from google.cloud import datacatalog_v1


async def sample_update_tag_template_field():
    # Create a client
    client = datacatalog_v1.DataCatalogAsyncClient()

    # Initialize request argument(s)
    tag_template_field = datacatalog_v1.TagTemplateField()
    tag_template_field.type_.primitive_type = "RICHTEXT"

    request = datacatalog_v1.UpdateTagTemplateFieldRequest(
        name="name_value",
        tag_template_field=tag_template_field,
    )

    # Make the request
    response = await client.update_tag_template_field(request=request)

    # Handle the response
    print(response)

# [END datacatalog_v1_generated_DataCatalog_UpdateTagTemplateField_async]
