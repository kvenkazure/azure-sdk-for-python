# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TableSpecification(Model):
    """The swagger 2.0 schema describing a single service input or output. See
    Swagger specification: http://swagger.io/specification/.

    :param title: Swagger schema title.
    :type title: str
    :param description: Swagger schema description.
    :type description: str
    :param type: The type of the entity described in swagger. Default value:
     "object" .
    :type type: str
    :param format: The format, if 'type' is not 'object'
    :type format: str
    :param properties: The set of columns within the data table.
    :type properties: dict
    """ 

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'format': {'key': 'format', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{ColumnSpecification}'},
    }

    def __init__(self, title=None, description=None, type="object", format=None, properties=None):
        self.title = title
        self.description = description
        self.type = type
        self.format = format
        self.properties = properties
