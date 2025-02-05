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


class JobDataPath(Model):
    """A Data Lake Analytics job data path item.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar job_id: the id of the job this data is for.
    :vartype job_id: str
    :ivar command: the command that this job data relates to.
    :vartype command: str
    :ivar paths: the list of paths to all of the job data.
    :vartype paths: list of str
    """ 

    _validation = {
        'job_id': {'readonly': True},
        'command': {'readonly': True},
        'paths': {'readonly': True},
    }

    _attribute_map = {
        'job_id': {'key': 'jobId', 'type': 'str'},
        'command': {'key': 'command', 'type': 'str'},
        'paths': {'key': 'paths', 'type': '[str]'},
    }

    def __init__(self):
        self.job_id = None
        self.command = None
        self.paths = None
