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


class TaskAddResult(Model):
    """Result for a single task added as part of an add task collection
    operation.

    :param status: The status of the add task request. Possible values
     include: 'success', 'clienterror', 'servererror', 'unmapped'
    :type status: str or :class:`TaskAddStatus
     <azure.batch.models.TaskAddStatus>`
    :param task_id: The id of the task for which this is the result.
    :type task_id: str
    :param e_tag: The ETag of the task, if the task was successfully added.
    :type e_tag: str
    :param last_modified: The last modified time of the task.
    :type last_modified: datetime
    :param location: The URL of the task, if the task was successfully added.
    :type location: str
    :param error: The error encountered while attempting to add the task.
    :type error: :class:`BatchError <azure.batch.models.BatchError>`
    """ 

    _validation = {
        'status': {'required': True},
        'task_id': {'required': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'TaskAddStatus'},
        'task_id': {'key': 'taskId', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'location': {'key': 'location', 'type': 'str'},
        'error': {'key': 'error', 'type': 'BatchError'},
    }

    def __init__(self, status, task_id, e_tag=None, last_modified=None, location=None, error=None):
        self.status = status
        self.task_id = task_id
        self.e_tag = e_tag
        self.last_modified = last_modified
        self.location = location
        self.error = error
