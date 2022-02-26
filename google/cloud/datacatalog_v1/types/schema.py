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
import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1", manifest={"Schema", "ColumnSchema",},
)


class Schema(proto.Message):
    r"""Represents a schema, for example, a BigQuery, GoogleSQL, or
    Avro schema.

    Attributes:
        columns (Sequence[google.cloud.datacatalog_v1.types.ColumnSchema]):
            The unified GoogleSQL-like schema of columns.
            The overall maximum number of columns and nested
            columns is 10,000. The maximum nested depth is
            15 levels.
    """

    columns = proto.RepeatedField(proto.MESSAGE, number=2, message="ColumnSchema",)


class ColumnSchema(proto.Message):
    r"""A column within a schema. Columns can be nested inside
    other columns.

    Attributes:
        column (str):
            Required. Name of the column.
            Must be a UTF-8 string without dots (.).
            The maximum size is 64 bytes.
        type_ (str):
            Required. Type of the column.
            Must be a UTF-8 string with the maximum size of
            128 bytes.
        description (str):
            Optional. Description of the column. Default
            value is an empty string.
            The description must be a UTF-8 string with the
            maximum size of 2000 bytes.
        mode (str):
            Optional. A column's mode indicates whether values in this
            column are required, nullable, or repeated.

            Only ``NULLABLE``, ``REQUIRED``, and ``REPEATED`` values are
            supported. Default mode is ``NULLABLE``.
        subcolumns (Sequence[google.cloud.datacatalog_v1.types.ColumnSchema]):
            Optional. Schema of sub-columns. A column can
            have zero or more sub-columns.
    """

    column = proto.Field(proto.STRING, number=6,)
    type_ = proto.Field(proto.STRING, number=1,)
    description = proto.Field(proto.STRING, number=2,)
    mode = proto.Field(proto.STRING, number=3,)
    subcolumns = proto.RepeatedField(proto.MESSAGE, number=7, message="ColumnSchema",)


__all__ = tuple(sorted(__protobuf__.manifest))
