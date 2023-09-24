"""
Generated class for CareTeam. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Element import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Participant(Element):
    """ Identifies all people and organizations who are expected to be involved in the care team.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Type of involvement
    :param Reference member: Who is involved
    :param Reference onBehalfOf: Organization of the practitioner
    :param Period period: Time period of participant
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    role:  list["CodeableConcept"] = [CodeableConcept()]
    
    member:  "Reference" = Reference()
    
    onBehalfOf:  "Reference" = Reference()
    
    period:  "Period" = Period()
    

@dataclass
class CareTeam(ModelBase):
    """ The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this team
    :param str status: proposed | active | suspended | inactive | entered-in-error
    :param CodeableConcept category: Type of team
    :param str name: Name of the team, such as crisis assessment team
    :param Reference subject: Who care team is for
    :param Reference encounter: Encounter created as part of
    :param Period period: Time period team covers
    :param Participant participant: Members of the team
    :param CodeableConcept reasonCode: Why the care team exists
    :param Reference reasonReference: Why the care team exists
    :param Reference managingOrganization: Organization responsible for the care team
    :param ContactPoint telecom: A contact detail for the care team (that applies to all members)
    :param Annotation note: Comments made about the CareTeam
    """

    resourceType: str = "CareTeam"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    category: list["CodeableConcept"] = None
    
    name: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    period: "Period" = None
    
    participant: list["Participant"] = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    managingOrganization: list["Reference"] = None
    
    telecom: list["ContactPoint"] = None
    
    note: list["Annotation"] = None
    