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
import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1",
    manifest={"Tag", "TagField", "TagTemplate", "TagTemplateField", "FieldType",},
)


class Tag(proto.Message):
    r"""Tags contain custom metadata and are attached to Data Catalog
    resources. Tags conform with the specification of their tag
    template.

    See `Data Catalog
    IAM <https://cloud.google.com/data-catalog/docs/concepts/iam>`__ for
    information on the permissions needed to create or view tags.

    Attributes:
        name (str):
            The resource name of the tag in URL format
            where tag ID is a system-generated identifier.
            Note: The tag itself might not be stored in the
            location specified in its name.
        template (str):
            Required. The resource name of the tag template this tag
            uses. Example:

            ``projects/{PROJECT_ID}/locations/{LOCATION}/tagTemplates/{TAG_TEMPLATE_ID}``

            This field cannot be modified after creation.
        template_display_name (str):
            Output only. The display name of the tag
            template.
        column (str):
            Resources like entry can have schemas associated with them.
            This scope allows you to attach tags to an individual column
            based on that schema.

            To attach a tag to a nested column, separate column names
            with a dot (``.``). Example: ``column.nested_column``.
        fields (Sequence[google.cloud.datacatalog_v1.types.Tag.FieldsEntry]):
            Required. Maps the ID of a tag field to its
            value and additional information about that
            field.
            Tag template defines valid field IDs. A tag
            must have at least 1 field and at most 500
            fields.
    """

    name = proto.Field(proto.STRING, number=1,)
    template = proto.Field(proto.STRING, number=2,)
    template_display_name = proto.Field(proto.STRING, number=5,)
    column = proto.Field(proto.STRING, number=4, oneof="scope",)
    fields = proto.MapField(proto.STRING, proto.MESSAGE, number=3, message="TagField",)


class TagField(proto.Message):
    r"""Contains the value and additional information on a field within a
    [Tag][google.cloud.datacatalog.v1.Tag].

    Attributes:
        display_name (str):
            Output only. The display name of this field.
        double_value (float):
            The value of a tag field with a double type.
        string_value (str):
            The value of a tag field with a string type.
            The maximum length is 2000 UTF-8 characters.
        bool_value (bool):
            The value of a tag field with a boolean type.
        timestamp_value (google.protobuf.timestamp_pb2.Timestamp):
            The value of a tag field with a timestamp
            type.
        enum_value (google.cloud.datacatalog_v1.types.TagField.EnumValue):
            The value of a tag field with an enum type.
            This value must be one of the allowed values
            listed in this enum.
        richtext_value (str):
            The value of a tag field with a rich text
            type.
            The maximum length is 10 MiB as this value holds
            HTML descriptions including encoded images. The
            maximum length of the text without images is 100
            KiB.
        order (int):
            Output only. The order of this field with respect to other
            fields in this tag. Can be set by
            [Tag][google.cloud.datacatalog.v1.TagTemplateField.order].

            For example, a higher value can indicate a more important
            field. The value can be negative. Multiple fields can have
            the same order, and field orders within a tag don't have to
            be sequential.
    """

    class EnumValue(proto.Message):
        r"""An enum value.
        Attributes:
            display_name (str):
                The display name of the enum value.
        """

        display_name = proto.Field(proto.STRING, number=1,)

    display_name = proto.Field(proto.STRING, number=1,)
    double_value = proto.Field(proto.DOUBLE, number=2, oneof="kind",)
    string_value = proto.Field(proto.STRING, number=3, oneof="kind",)
    bool_value = proto.Field(proto.BOOL, number=4, oneof="kind",)
    timestamp_value = proto.Field(
        proto.MESSAGE, number=5, oneof="kind", message=timestamp_pb2.Timestamp,
    )
    enum_value = proto.Field(proto.MESSAGE, number=6, oneof="kind", message=EnumValue,)
    richtext_value = proto.Field(proto.STRING, number=8, oneof="kind",)
    order = proto.Field(proto.INT32, number=7,)


class TagTemplate(proto.Message):
    r"""A tag template defines a tag that can have one or more typed fields.

    The template is used to create tags that are attached to GCP
    resources. [Tag template roles]
    (https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
    provide permissions to create, edit, and use the template. For
    example, see the [TagTemplate User]
    (https://cloud.google.com/data-catalog/docs/how-to/template-user)
    role that includes a permission to use the tag template to tag
    resources.

    Attributes:
        name (str):
            The resource name of the tag template in URL
            format.
            Note: The tag template itself and its child
            resources might not be stored in the location
            specified in its name.
        display_name (str):
            Display name for this template. Defaults to an empty string.

            The name must contain only Unicode letters, numbers (0-9),
            underscores (_), dashes (-), spaces ( ), and can't start or
            end with spaces. The maximum length is 200 characters.
        is_publicly_readable (bool):
            Indicates whether this is a public tag template.

            Every user has view access to a *public* tag template by
            default. This means that:

            -  Every user can use this tag template to tag an entry.
            -  If an entry is tagged using the tag template, the tag is
               always shown in the response to ``ListTags`` called on
               the entry.
            -  To get the template using the GetTagTemplate method, you
               need view access either on the project or the
               organization the tag template resides in but no other
               permission is needed.
            -  Operations on the tag template other than viewing (for
               example, editing IAM policies) follow standard IAM
               structures.

            Tags created with a public tag template are referred to as
            public tags.

            You can search for a public tag by value with a simple
            search query instead of using a ``tag:`` predicate.

            Public tag templates may not appear in search results
            depending on scope, see:
            [include_public_tag_templates][google.cloud.datacatalog.v1.SearchCatalogRequest.Scope.include_public_tag_templates]

            Note: If an `IAM domain
            restriction <https://cloud.google.com/resource-manager/docs/organization-policy/restricting-domains>`__
            is configured in the tag template's location, the public
            access will not be enabled but the simple search for tag
            values will still work.
        fields (Sequence[google.cloud.datacatalog_v1.types.TagTemplate.FieldsEntry]):
            Required. Map of tag template field IDs to the settings for
            the field. This map is an exhaustive list of the allowed
            fields. The map must contain at least one field and at most
            500 fields.

            The keys to this map are tag template field IDs. The IDs
            have the following limitations:

            -  Can contain uppercase and lowercase letters, numbers
               (0-9) and underscores (_).
            -  Must be at least 1 character and at most 64 characters
               long.
            -  Must start with a letter or underscore.
    """

    name = proto.Field(proto.STRING, number=1,)
    display_name = proto.Field(proto.STRING, number=2,)
    is_publicly_readable = proto.Field(proto.BOOL, number=5,)
    fields = proto.MapField(
        proto.STRING, proto.MESSAGE, number=3, message="TagTemplateField",
    )


class TagTemplateField(proto.Message):
    r"""The template for an individual field within a tag template.
    Attributes:
        name (str):
            Output only. The resource name of the tag template field in
            URL format. Example:

            ``projects/{PROJECT_ID}/locations/{LOCATION}/tagTemplates/{TAG_TEMPLATE}/fields/{FIELD}``

            Note: The tag template field itself might not be stored in
            the location specified in its name.

            The name must contain only letters (a-z, A-Z), numbers
            (0-9), or underscores (_), and must start with a letter or
            underscore. The maximum length is 64 characters.
        display_name (str):
            The display name for this field. Defaults to an empty
            string.

            The name must contain only Unicode letters, numbers (0-9),
            underscores (_), dashes (-), spaces ( ), and can't start or
            end with spaces. The maximum length is 200 characters.
        type_ (google.cloud.datacatalog_v1.types.FieldType):
            Required. The type of value this tag field
            can contain.
        is_required (bool):
            If true, this field is required. Defaults to
            false.
        description (str):
            The description for this field. Defaults to
            an empty string.
        order (int):
            The order of this field with respect to other
            fields in this tag template.

            For example, a higher value can indicate a more
            important field. The value can be negative.
            Multiple fields can have the same order and
            field orders within a tag don't have to be
            sequential.
    """

    name = proto.Field(proto.STRING, number=6,)
    display_name = proto.Field(proto.STRING, number=1,)
    type_ = proto.Field(proto.MESSAGE, number=2, message="FieldType",)
    is_required = proto.Field(proto.BOOL, number=3,)
    description = proto.Field(proto.STRING, number=4,)
    order = proto.Field(proto.INT32, number=5,)


class FieldType(proto.Message):
    r"""
    Attributes:
        primitive_type (google.cloud.datacatalog_v1.types.FieldType.PrimitiveType):
            Primitive types, such as string, boolean,
            etc.
        enum_type (google.cloud.datacatalog_v1.types.FieldType.EnumType):
            An enum type.
    """

    class PrimitiveType(proto.Enum):
        r""""""
        PRIMITIVE_TYPE_UNSPECIFIED = 0
        DOUBLE = 1
        STRING = 2
        BOOL = 3
        TIMESTAMP = 4
        RICHTEXT = 5

    class EnumType(proto.Message):
        r"""
        Attributes:
            allowed_values (Sequence[google.cloud.datacatalog_v1.types.FieldType.EnumType.EnumValue]):
                The set of allowed values for this enum.

                This set must not be empty and can include up to 100 allowed
                values. The display names of the values in this set must not
                be empty and must be case-insensitively unique within this
                set.

                The order of items in this set is preserved. This field can
                be used to create, remove, and reorder enum values. To
                rename enum values, use the
                ``RenameTagTemplateFieldEnumValue`` method.
        """

        class EnumValue(proto.Message):
            r"""
            Attributes:
                display_name (str):
                    Required. The display name of the enum value. Must not be an
                    empty string.

                    The name must contain only Unicode letters, numbers (0-9),
                    underscores (_), dashes (-), spaces ( ), and can't start or
                    end with spaces. The maximum length is 200 characters.
            """

            display_name = proto.Field(proto.STRING, number=1,)

        allowed_values = proto.RepeatedField(
            proto.MESSAGE, number=1, message="FieldType.EnumType.EnumValue",
        )

    primitive_type = proto.Field(
        proto.ENUM, number=1, oneof="type_decl", enum=PrimitiveType,
    )
    enum_type = proto.Field(
        proto.MESSAGE, number=2, oneof="type_decl", message=EnumType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
