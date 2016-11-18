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


class LogProfileCreateOrUpdateParameters(Model):
    """Paramters to create a new Log Profile.

    :param storage_account_id: the resource id of the storage account.
    :type storage_account_id: str
    :param service_bus_rule_id: the resource id of the service bus rule.
    :type service_bus_rule_id: str
    :param locations: the locations.
    :type locations: list of str
    :param categories:  the categories.
    :type categories: list of str
    :param retention_policy: the retention policy for this log.
    :type retention_policy: :class:`RetentionPolicy
     <azure.mgmt.monitor.models.RetentionPolicy>`
    """ 

    _attribute_map = {
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'service_bus_rule_id': {'key': 'properties.serviceBusRuleId', 'type': 'str'},
        'locations': {'key': 'properties.locations', 'type': '[str]'},
        'categories': {'key': 'properties.categories', 'type': '[str]'},
        'retention_policy': {'key': 'properties.retentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(self, storage_account_id=None, service_bus_rule_id=None, locations=None, categories=None, retention_policy=None):
        self.storage_account_id = storage_account_id
        self.service_bus_rule_id = service_bus_rule_id
        self.locations = locations
        self.categories = categories
        self.retention_policy = retention_policy