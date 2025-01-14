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


class KeyBundle(Model):
    """A KeyBundle consisting of a WebKey plus its Attributes.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param key: The Json web key
    :type key: :class:`JsonWebKey <azure.keyvault.models.JsonWebKey>`
    :param attributes: The key management attributes
    :type attributes: :class:`KeyAttributes
     <azure.keyvault.models.KeyAttributes>`
    :param tags: Application-specific metadata in the form of key-value pairs
    :type tags: dict
    :ivar managed: True if the key's lifetime is managed by key vault i.e. if
     this is a key backing a certificate, then managed will be true.
    :vartype managed: bool
    """ 

    _validation = {
        'managed': {'readonly': True},
    }

    _attribute_map = {
        'key': {'key': 'key', 'type': 'JsonWebKey'},
        'attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed': {'key': 'managed', 'type': 'bool'},
    }

    def __init__(self, key=None, attributes=None, tags=None):
        self.key = key
        self.attributes = attributes
        self.tags = tags
        self.managed = None
