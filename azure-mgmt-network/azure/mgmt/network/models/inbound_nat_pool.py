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

from .sub_resource import SubResource


class InboundNatPool(SubResource):
    """Inbound NAT pool of the load balancer.

    :param id: Resource ID.
    :type id: str
    :param frontend_ip_configuration: A reference to frontend IP addresses.
    :type frontend_ip_configuration: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param protocol: The transport protocol for the endpoint. Possible values
     are: 'Udp' or 'Tcp'. Possible values include: 'Udp', 'Tcp'
    :type protocol: str or :class:`TransportProtocol
     <azure.mgmt.network.models.TransportProtocol>`
    :param frontend_port_range_start: The first port number in the range of
     external ports that will be used to provide Inbound Nat to NICs
     associated with a load balancer. Acceptable values range between 1 and
     65534.
    :type frontend_port_range_start: int
    :param frontend_port_range_end: The last port number in the range of
     external ports that will be used to provide Inbound Nat to NICs
     associated with a load balancer. Acceptable values range between 1 and
     65535.
    :type frontend_port_range_end: int
    :param backend_port: The port used for internal connections on the
     endpoint. Acceptable values are between 1 and 65535.
    :type backend_port: int
    :param provisioning_state: Gets the provisioning state of the PublicIP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """ 

    _validation = {
        'protocol': {'required': True},
        'frontend_port_range_start': {'required': True},
        'frontend_port_range_end': {'required': True},
        'backend_port': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'frontend_ip_configuration': {'key': 'properties.frontendIPConfiguration', 'type': 'SubResource'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'frontend_port_range_start': {'key': 'properties.frontendPortRangeStart', 'type': 'int'},
        'frontend_port_range_end': {'key': 'properties.frontendPortRangeEnd', 'type': 'int'},
        'backend_port': {'key': 'properties.backendPort', 'type': 'int'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, protocol, frontend_port_range_start, frontend_port_range_end, backend_port, id=None, frontend_ip_configuration=None, provisioning_state=None, name=None, etag=None):
        super(InboundNatPool, self).__init__(id=id)
        self.frontend_ip_configuration = frontend_ip_configuration
        self.protocol = protocol
        self.frontend_port_range_start = frontend_port_range_start
        self.frontend_port_range_end = frontend_port_range_end
        self.backend_port = backend_port
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
