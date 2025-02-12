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

from .sql_sub_resource import SqlSubResource


class TransparentDataEncryption(SqlSubResource):
    """Represents an Azure SQL Database Transparent Data Encryption .

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Resource name
    :vartype name: str
    :ivar id: Resource Id
    :vartype id: str
    :param status: The status of the Azure SQL Database Transparent Data
     Encryption. Possible values include: 'Enabled', 'Disabled'
    :type status: str or :class:`TransparentDataEncryptionStates
     <azure.mgmt.sql.models.TransparentDataEncryptionStates>`
    """ 

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'TransparentDataEncryptionStates'},
    }

    def __init__(self, status=None):
        super(TransparentDataEncryption, self).__init__()
        self.status = status
