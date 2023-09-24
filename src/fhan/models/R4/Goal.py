"""
Generated class for Goal. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Range import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Target(ModelBase):
    """ Indicates what should be done by when.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' measure: The parameter whose value is being tracked
    :param 'Quantity' detailQuantity: The target value to be achieved
    :param str dueDate: Reach goal on or before
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  measure: 'CodeableConcept' = None,  detailQuantity: 'Quantity' = None,  dueDate: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.measure: 'CodeableConcept' = measure 
        self.detailQuantity: 'Quantity' = detailQuantity 
        self.dueDate: str = dueDate 
        

class Goal(DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Ids for this goal
    :param str lifecycleStatus: proposed | planned | accepted | active | on-hold | completed | cancelled | entered-in-error | rejected
    :param 'CodeableConcept' achievementStatus: in-progress | improving | worsening | no-change | achieved | sustaining | not-achieved | no-progress | not-attainable
    :param list['CodeableConcept'] category: E.g. Treatment, dietary, behavioral, etc.
    :param 'CodeableConcept' priority: high-priority | medium-priority | low-priority
    :param 'CodeableConcept' description: Code or text describing goal
    :param 'Reference' subject: Who this goal is intended for
    :param str startDate: When goal pursuit begins
    :param list['Target'] target: Target outcome for the goal
    :param str statusDate: When goal status took effect
    :param str statusReason: Reason for current status
    :param 'Reference' expressedBy: Who's responsible for creating Goal?
    :param list['Reference'] addresses: Issues addressed by this goal
    :param list['Annotation'] note: Comments about the goal
    :param list['CodeableConcept'] outcomeCode: What result was achieved regarding the goal?
    :param list['Reference'] outcomeReference: Observation that resulted from goal
    """
    def __init__(self, resourceType: str = "Goal",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  lifecycleStatus: str = None,  achievementStatus: 'CodeableConcept' = None,  category: list['CodeableConcept'] = None,  priority: 'CodeableConcept' = None,  description: 'CodeableConcept' = None,  subject: 'Reference' = None,  startDate: str = None,  target: list['Target'] = None,  statusDate: str = None,  statusReason: str = None,  expressedBy: 'Reference' = None,  addresses: list['Reference'] = None,  note: list['Annotation'] = None,  outcomeCode: list['CodeableConcept'] = None,  outcomeReference: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "Goal"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.lifecycleStatus: str = lifecycleStatus 
        self.achievementStatus: 'CodeableConcept' = achievementStatus 
        self.category: list['CodeableConcept'] = category or []
        self.priority: 'CodeableConcept' = priority 
        self.description: 'CodeableConcept' = description 
        self.subject: 'Reference' = subject 
        self.startDate: str = startDate 
        self.target: list['Target'] = target or []
        self.statusDate: str = statusDate 
        self.statusReason: str = statusReason 
        self.expressedBy: 'Reference' = expressedBy 
        self.addresses: list['Reference'] = addresses or []
        self.note: list['Annotation'] = note or []
        self.outcomeCode: list['CodeableConcept'] = outcomeCode or []
        self.outcomeReference: list['Reference'] = outcomeReference or []
        