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


class ApplicationGatewaySslCertificate(SubResource):
    """SSL certificates of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param data: Base-64 encoded pfx certificate. Only applicable in PUT
     Request.
    :type data: str
    :param password: Password for the pfx file specified in data. Only
     applicable in PUT request.
    :type password: str
    :param public_cert_data: Base-64 encoded Public cert data corresponding
     to pfx specified in data. Only applicable in GET request.
    :type public_cert_data: str
    :param provisioning_state: Provisioning state of the SSL certificate
     resource Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'data': {'key': 'properties.data', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'public_cert_data': {'key': 'properties.publicCertData', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, data=None, password=None, public_cert_data=None, provisioning_state=None, name=None, etag=None):
        super(ApplicationGatewaySslCertificate, self).__init__(id=id)
        self.data = data
        self.password = password
        self.public_cert_data = public_cert_data
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
