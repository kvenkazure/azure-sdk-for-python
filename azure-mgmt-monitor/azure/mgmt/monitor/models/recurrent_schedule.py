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


class RecurrentSchedule(Model):
    """The scheduling constraints for when the profile begins.

    :param time_zone: the time zone for the hours of the profile. See
     examples of valid timezone ids over here:
     https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx
    :type time_zone: str
    :param days: the collection of days that the profile takes effect on.
     Possible values are Sunday through Saturday.
    :type days: list of str
    :param hours: A collection of hours that the profile takes effect on.
     Values supported are 0 to 23 on the 24-hour clock (AM/PM times are not
     supported).
    :type hours: list of int
    :param minutes: A collection of minutes at which the profile takes effect
     at.
    :type minutes: list of int
    """ 

    _attribute_map = {
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'days': {'key': 'days', 'type': '[str]'},
        'hours': {'key': 'hours', 'type': '[int]'},
        'minutes': {'key': 'minutes', 'type': '[int]'},
    }

    def __init__(self, time_zone=None, days=None, hours=None, minutes=None):
        self.time_zone = time_zone
        self.days = days
        self.hours = hours
        self.minutes = minutes