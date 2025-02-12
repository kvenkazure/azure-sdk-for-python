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


class Database(Resource):
    """Represents an Azure SQL Database.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Resource name
    :vartype name: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param collation: The collation of the Azure SQL Database.
    :type collation: str
    :ivar creation_date: The creation date of the Azure SQL Database (ISO8601
     format).
    :vartype creation_date: datetime
    :ivar containment_state: The containment state of the Azure SQL Database.
    :vartype containment_state: long
    :ivar current_service_objective_id: The current Service Level Objective
     Id of the Azure SQL Database. This is the Id of the Service Level
     Objective that is currently active.
    :vartype current_service_objective_id: str
    :ivar database_id: The Id of the Azure SQL Database.
    :vartype database_id: str
    :ivar earliest_restore_date: The recovery period start date of the Azure
     SQL Database. This records the start date and time when recovery is
     available for this Azure SQL Database (ISO8601 format).
    :vartype earliest_restore_date: datetime
    :param create_mode: Specifies the type of database to create. Possible
     values include: 'Copy', 'Default', 'NonReadableSecondary',
     'OnlineSecondary', 'PointInTimeRestore', 'Recovery', 'Restore'
    :type create_mode: str or :class:`createMode
     <azure.mgmt.sql.models.createMode>`
    :param source_database_id: Conditional.  Specifies the resource Id of the
     source database.  If createMode is not set to Default, then this value
     must be specified.  The name of the source database must be the same.
     NOTE: Collation, Edition, and MaxSizeBytes must remain the same while
     the link is active.  Values specified for these parameters will be
     ignored.
    :type source_database_id: str
    :param edition: The edition of the Azure SQL Database.  The
     DatabaseEditions enumeration contains all the valid editions. Possible
     values include: 'Web', 'Business', 'Basic', 'Standard', 'Premium',
     'Free', 'Stretch', 'DataWarehouse'
    :type edition: str or :class:`DatabaseEditions
     <azure.mgmt.sql.models.DatabaseEditions>`
    :param max_size_bytes: The max size of the Azure SQL Database expressed
     in bytes. Note: Only the following sizes are supported (in addition to
     limitations being placed on each edition): { 100 MB | 500 MB |1 GB | 5
     GB | 10 GB | 20 GB | 30 GB … 150 GB | 200 GB … 500 GB }
    :type max_size_bytes: str
    :param requested_service_objective_id: The configured Service Level
     Objective Id of the Azure SQL Database. This is the Service Level
     Objective that is in the process of being applied to the Azure SQL
     Database.  Once successfully updated, it will match the value of
     currentServiceObjectiveId property.
    :type requested_service_objective_id: str
    :param requested_service_objective_name: The name of the configured
     Service Level Objective of the Azure SQL Database. This is the Service
     Level Objective that is in the process of being applied to the Azure SQL
     Database.  Once successfully updated, it will match the value of
     serviceLevelObjective property. Possible values include: 'Basic', 'S0',
     'S1', 'S2', 'S3', 'P1', 'P2', 'P3'
    :type requested_service_objective_name: str or
     :class:`ServiceObjectiveName
     <azure.mgmt.sql.models.ServiceObjectiveName>`
    :ivar service_level_objective: The current Service Level Objective of the
     Azure SQL Database. Possible values include: 'Basic', 'S0', 'S1', 'S2',
     'S3', 'P1', 'P2', 'P3'
    :vartype service_level_objective: str or :class:`ServiceObjectiveName
     <azure.mgmt.sql.models.ServiceObjectiveName>`
    :ivar status: The status of the Azure SQL Database.
    :vartype status: str
    :param elastic_pool_name: The name of the Azure SQL Elastic Pool the
     database is in.
    :type elastic_pool_name: str
    :ivar default_secondary_location: The default secondary region for this
     database.
    :vartype default_secondary_location: str
    :ivar service_tier_advisors: The list of service tier advisors for this
     database. Expanded property
    :vartype service_tier_advisors: list of :class:`ServiceTierAdvisor
     <azure.mgmt.sql.models.ServiceTierAdvisor>`
    :ivar upgrade_hint: The upgrade hint for this database.
    :vartype upgrade_hint: :class:`UpgradeHint
     <azure.mgmt.sql.models.UpgradeHint>`
    :ivar schemas: The schemas from this database.
    :vartype schemas: list of :class:`Schema <azure.mgmt.sql.models.Schema>`
    :ivar transparent_data_encryption: The transparent data encryption info
     for this database.
    :vartype transparent_data_encryption: list of
     :class:`TransparentDataEncryption
     <azure.mgmt.sql.models.TransparentDataEncryption>`
    :ivar recommended_index: The recommended indices for this database.
    :vartype recommended_index: list of :class:`RecommendedIndex
     <azure.mgmt.sql.models.RecommendedIndex>`
    """ 

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'creation_date': {'readonly': True},
        'containment_state': {'readonly': True},
        'current_service_objective_id': {'readonly': True},
        'database_id': {'readonly': True},
        'earliest_restore_date': {'readonly': True},
        'service_level_objective': {'readonly': True},
        'status': {'readonly': True},
        'default_secondary_location': {'readonly': True},
        'service_tier_advisors': {'readonly': True},
        'upgrade_hint': {'readonly': True},
        'schemas': {'readonly': True},
        'transparent_data_encryption': {'readonly': True},
        'recommended_index': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'collation': {'key': 'properties.collation', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'containment_state': {'key': 'properties.containmentState', 'type': 'long'},
        'current_service_objective_id': {'key': 'properties.currentServiceObjectiveId', 'type': 'str'},
        'database_id': {'key': 'properties.databaseId', 'type': 'str'},
        'earliest_restore_date': {'key': 'properties.earliestRestoreDate', 'type': 'iso-8601'},
        'create_mode': {'key': 'properties.createMode', 'type': 'str'},
        'source_database_id': {'key': 'properties.sourceDatabaseId', 'type': 'str'},
        'edition': {'key': 'properties.edition', 'type': 'str'},
        'max_size_bytes': {'key': 'properties.maxSizeBytes', 'type': 'str'},
        'requested_service_objective_id': {'key': 'properties.requestedServiceObjectiveId', 'type': 'str'},
        'requested_service_objective_name': {'key': 'properties.requestedServiceObjectiveName', 'type': 'str'},
        'service_level_objective': {'key': 'properties.serviceLevelObjective', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'elastic_pool_name': {'key': 'properties.elasticPoolName', 'type': 'str'},
        'default_secondary_location': {'key': 'properties.defaultSecondaryLocation', 'type': 'str'},
        'service_tier_advisors': {'key': 'properties.serviceTierAdvisors', 'type': '[ServiceTierAdvisor]'},
        'upgrade_hint': {'key': 'properties.upgradeHint', 'type': 'UpgradeHint'},
        'schemas': {'key': 'properties.schemas', 'type': '[Schema]'},
        'transparent_data_encryption': {'key': 'properties.transparentDataEncryption', 'type': '[TransparentDataEncryption]'},
        'recommended_index': {'key': 'properties.recommendedIndex', 'type': '[RecommendedIndex]'},
    }

    def __init__(self, location, tags=None, collation=None, create_mode=None, source_database_id=None, edition=None, max_size_bytes=None, requested_service_objective_id=None, requested_service_objective_name=None, elastic_pool_name=None):
        super(Database, self).__init__(location=location, tags=tags)
        self.collation = collation
        self.creation_date = None
        self.containment_state = None
        self.current_service_objective_id = None
        self.database_id = None
        self.earliest_restore_date = None
        self.create_mode = create_mode
        self.source_database_id = source_database_id
        self.edition = edition
        self.max_size_bytes = max_size_bytes
        self.requested_service_objective_id = requested_service_objective_id
        self.requested_service_objective_name = requested_service_objective_name
        self.service_level_objective = None
        self.status = None
        self.elastic_pool_name = elastic_pool_name
        self.default_secondary_location = None
        self.service_tier_advisors = None
        self.upgrade_hint = None
        self.schemas = None
        self.transparent_data_encryption = None
        self.recommended_index = None
