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


class DeploymentProperties(Model):
    """Deployment properties.

    :param template: The template content. You use this element when you want
     to pass the template syntax directly in the request rather than link to
     an existing template. It can be a JObject or well-formed JSON string.
     Use either the templateLink property or the template property, but not
     both.
    :type template: object
    :param template_link: The URI of the template. Use either the
     templateLink property or the template property, but not both.
    :type template_link: :class:`TemplateLink
     <azure.mgmt.resource.resources.models.TemplateLink>`
    :param parameters: Name and value pairs that define the deployment
     parameters for the template. You use this element when you want to
     provide the parameter values directly in the request rather than link to
     an existing parameter file. Use either the parametersLink property or
     the parameters property, but not both. It can be a JObject or a well
     formed JSON string.
    :type parameters: object
    :param parameters_link: The URI of parameters file. You use this element
     to link to an existing parameters file. Use either the parametersLink
     property or the parameters property, but not both.
    :type parameters_link: :class:`ParametersLink
     <azure.mgmt.resource.resources.models.ParametersLink>`
    :param mode: The mode that is used to deploy resources. This value can be
     either Incremental or Complete. In Incremental mode, resources are
     deployed without deleting existing resources that are not included in
     the template. In Complete mode, resources are deployed and existing
     resources in the resource group that are not included in the template
     are deleted. Be careful when using Complete mode as you may
     unintentionally delete resources. Possible values include:
     'Incremental', 'Complete'
    :type mode: str or :class:`DeploymentMode
     <azure.mgmt.resource.resources.models.DeploymentMode>`
    :param debug_setting: The debug setting of the deployment.
    :type debug_setting: :class:`DebugSetting
     <azure.mgmt.resource.resources.models.DebugSetting>`
    """ 

    _validation = {
        'mode': {'required': True},
    }

    _attribute_map = {
        'template': {'key': 'template', 'type': 'object'},
        'template_link': {'key': 'templateLink', 'type': 'TemplateLink'},
        'parameters': {'key': 'parameters', 'type': 'object'},
        'parameters_link': {'key': 'parametersLink', 'type': 'ParametersLink'},
        'mode': {'key': 'mode', 'type': 'DeploymentMode'},
        'debug_setting': {'key': 'debugSetting', 'type': 'DebugSetting'},
    }

    def __init__(self, mode, template=None, template_link=None, parameters=None, parameters_link=None, debug_setting=None):
        self.template = template
        self.template_link = template_link
        self.parameters = parameters
        self.parameters_link = parameters_link
        self.mode = mode
        self.debug_setting = debug_setting
