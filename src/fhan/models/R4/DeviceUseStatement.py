"""
Generated class for DeviceUseStatement. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


class DeviceUseStatement(DomainResource):
    """ A record of a device being used by a patient where the record is the result of a report from the patient or another clinician.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External identifier for this record
    :param list['Reference'] basedOn: Fulfills plan, proposal or order
    :param str status: active | completed | entered-in-error +
    :param 'Reference' subject: Patient using device
    :param list['Reference'] derivedFrom: Supporting information
    :param 'Timing' timingTiming: How often  the device was used
    :param str recordedOn: When statement was recorded
    :param 'Reference' source: Who made the statement
    :param 'Reference' device: Reference to device used
    :param list['CodeableConcept'] reasonCode: Why device was used
    :param list['Reference'] reasonReference: Why was DeviceUseStatement performed?
    :param 'CodeableConcept' bodySite: Target body site
    :param list['Annotation'] note: Addition details (comments, instructions)
    """
    def __init__(self, resourceType: str = "DeviceUseStatement",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  basedOn: list['Reference'] = None,  status: str = None,  subject: 'Reference' = None,  derivedFrom: list['Reference'] = None,  timingTiming: 'Timing' = None,  recordedOn: str = None,  source: 'Reference' = None,  device: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  bodySite: 'CodeableConcept' = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "DeviceUseStatement"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.basedOn: list['Reference'] = basedOn or []
        self.status: str = status 
        self.subject: 'Reference' = subject 
        self.derivedFrom: list['Reference'] = derivedFrom or []
        self.timingTiming: 'Timing' = timingTiming 
        self.recordedOn: str = recordedOn 
        self.source: 'Reference' = source 
        self.device: 'Reference' = device 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.bodySite: 'CodeableConcept' = bodySite 
        self.note: list['Annotation'] = note or []
        