"""
Generated class for Slot. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


class Slot(DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Ids for this item
    :param list['CodeableConcept'] serviceCategory: A broad categorization of the service that is to be performed during this appointment
    :param list['CodeableConcept'] serviceType: The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource
    :param list['CodeableConcept'] specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
    :param 'CodeableConcept' appointmentType: The style of appointment or patient that may be booked in the slot (not service type)
    :param 'Reference' schedule: The schedule resource that this slot defines an interval of status information
    :param str status: busy | free | busy-unavailable | busy-tentative | entered-in-error
    :param str start: Date/Time that the slot is to begin
    :param str end: Date/Time that the slot is to conclude
    :param bool overbooked: This slot has already been overbooked, appointments are unlikely to be accepted for this time
    :param str comment: Comments on the slot to describe any extended information. Such as custom constraints on the slot
    """
    def __init__(self, resourceType: str = "Slot",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  serviceCategory: list['CodeableConcept'] = None,  serviceType: list['CodeableConcept'] = None,  specialty: list['CodeableConcept'] = None,  appointmentType: 'CodeableConcept' = None,  schedule: 'Reference' = None,  status: str = None,  start: str = None,  end: str = None,  overbooked: bool = None,  comment: str = None, ):
        self.resourceType: str = resourceType or "Slot"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.serviceCategory: list['CodeableConcept'] = serviceCategory or []
        self.serviceType: list['CodeableConcept'] = serviceType or []
        self.specialty: list['CodeableConcept'] = specialty or []
        self.appointmentType: 'CodeableConcept' = appointmentType 
        self.schedule: 'Reference' = schedule 
        self.status: str = status 
        self.start: str = start 
        self.end: str = end 
        self.overbooked: bool = overbooked 
        self.comment: str = comment 
        