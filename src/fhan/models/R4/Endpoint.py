"""
Generated class for Endpoint. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Endpoint(DomainResource):
    """ The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Identifies this endpoint across multiple systems
    :param str status: active | suspended | error | off | entered-in-error | test
    :param 'Coding' connectionType: Protocol/Profile/Standard to be used with this endpoint connection
    :param str name: A name that this endpoint can be identified by
    :param 'Reference' managingOrganization: Organization that manages this endpoint (might not be the organization that exposes the endpoint)
    :param list['ContactPoint'] contact: Contact details for source (e.g. troubleshooting)
    :param 'Period' period: Interval the endpoint is expected to be operational
    :param list['CodeableConcept'] payloadType: The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
    :param str payloadMimeType: Mimetype to send. If not specified, the content could be anything (including no payload, if the connectionType defined this)
    :param str address: The technical base address for connecting to this endpoint
    :param str header: Usage depends on the channel type
    """
    def __init__(self, resourceType: str = "Endpoint",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  connectionType: 'Coding' = None,  name: str = None,  managingOrganization: 'Reference' = None,  contact: list['ContactPoint'] = None,  period: 'Period' = None,  payloadType: list['CodeableConcept'] = None,  payloadMimeType: str = None,  address: str = None,  header: str = None, ):
        self.resourceType: str = resourceType or "Endpoint"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.connectionType: 'Coding' = connectionType 
        self.name: str = name 
        self.managingOrganization: 'Reference' = managingOrganization 
        self.contact: list['ContactPoint'] = contact or []
        self.period: 'Period' = period 
        self.payloadType: list['CodeableConcept'] = payloadType or []
        self.payloadMimeType: str = payloadMimeType or []
        self.address: str = address 
        self.header: str = header or []
        