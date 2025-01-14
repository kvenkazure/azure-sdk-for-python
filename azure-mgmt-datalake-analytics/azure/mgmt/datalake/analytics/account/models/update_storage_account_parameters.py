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


class UpdateStorageAccountParameters(Model):
    """Storage account parameters for a storage account being updated in a Data
    Lake Analytics account.

    :param access_key: the updated access key associated with this Azure
     Storage account that will be used to connect to it.
    :type access_key: str
    :param suffix: the optional suffix for the storage account.
    :type suffix: str
    """ 

    _attribute_map = {
        'access_key': {'key': 'properties.accessKey', 'type': 'str'},
        'suffix': {'key': 'properties.suffix', 'type': 'str'},
    }

    def __init__(self, access_key=None, suffix=None):
        self.access_key = access_key
        self.suffix = suffix
