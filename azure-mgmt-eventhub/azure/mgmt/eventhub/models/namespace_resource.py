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

from .resource import Resource


class NamespaceResource(Resource):
    """Description of a namespace resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param sku:
    :type sku: :class:`Sku <azure.mgmt.eventhub.models.Sku>`
    :param provisioning_state: Provisioning state of the namespace.
    :type provisioning_state: str
    :param status: State of the namespace. Possible values include:
     'Unknown', 'Creating', 'Created', 'Activating', 'Enabling', 'Active',
     'Disabling', 'Disabled', 'SoftDeleting', 'SoftDeleted', 'Removing',
     'Removed', 'Failed'
    :type status: str or :class:`NamespaceState
     <azure.mgmt.eventhub.models.NamespaceState>`
    :param created_at: The time the namespace was created.
    :type created_at: datetime
    :param updated_at: The time the namespace was updated.
    :type updated_at: datetime
    :param service_bus_endpoint: Endpoint you can use to perform Service Bus
     operations.
    :type service_bus_endpoint: str
    :param create_acs_namespace: Indicates whether to create an ACS namespace.
    :type create_acs_namespace: bool
    :param enabled: Specifies whether this instance is enabled.
    :type enabled: bool
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'NamespaceState'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'service_bus_endpoint': {'key': 'properties.serviceBusEndpoint', 'type': 'str'},
        'create_acs_namespace': {'key': 'properties.createACSNamespace', 'type': 'bool'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
    }

    def __init__(self, location, tags=None, sku=None, provisioning_state=None, status=None, created_at=None, updated_at=None, service_bus_endpoint=None, create_acs_namespace=None, enabled=None):
        super(NamespaceResource, self).__init__(location=location, tags=tags)
        self.sku = sku
        self.provisioning_state = provisioning_state
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.service_bus_endpoint = service_bus_endpoint
        self.create_acs_namespace = create_acs_namespace
        self.enabled = enabled
