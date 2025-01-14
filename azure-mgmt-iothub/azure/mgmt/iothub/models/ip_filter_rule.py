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


class IpFilterRule(Model):
    """IP filter Rule.

    :param filter_name: The name of the IP filter rule.
    :type filter_name: str
    :param action: The action desired - accept or reject. Possible values
     include: 'Accept', 'Reject'
    :type action: str or :class:`IpFilterActionType
     <azure.mgmt.iothub.models.IpFilterActionType>`
    :param ip_mask: A string containing the IPAddress/range in CIDR notation.
    :type ip_mask: str
    """ 

    _validation = {
        'filter_name': {'required': True},
        'action': {'required': True},
        'ip_mask': {'required': True},
    }

    _attribute_map = {
        'filter_name': {'key': 'filterName', 'type': 'str'},
        'action': {'key': 'action', 'type': 'IpFilterActionType'},
        'ip_mask': {'key': 'ipMask', 'type': 'str'},
    }

    def __init__(self, filter_name, action, ip_mask):
        self.filter_name = filter_name
        self.action = action
        self.ip_mask = ip_mask
