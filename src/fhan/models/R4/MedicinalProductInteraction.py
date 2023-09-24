"""
Generated class for MedicinalProductInteraction. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Interactant(ModelBase):
    """ The specific medication, food or laboratory test that interacts.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' itemReference: The specific medication, food or laboratory test that interacts
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  itemReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemReference: 'Reference' = itemReference 
        

class MedicinalProductInteraction(DomainResource):
    """ The interactions of the medicinal product with other medicinal products, or other forms of interactions.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Reference'] subject: The medication for which this is a described interaction
    :param str description: The interaction described
    :param list['Interactant'] interactant: The specific medication, food or laboratory test that interacts
    :param 'CodeableConcept' type: The type of the interaction e.g. drug-drug interaction, drug-food interaction, drug-lab test interaction
    :param 'CodeableConcept' effect: The effect of the interaction, for example "reduced gastric absorption of primary medication"
    :param 'CodeableConcept' incidence: The incidence of the interaction, e.g. theoretical, observed
    :param 'CodeableConcept' management: Actions for managing the interaction
    """
    def __init__(self, resourceType: str = "MedicinalProductInteraction",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  subject: list['Reference'] = None,  description: str = None,  interactant: list['Interactant'] = None,  type: 'CodeableConcept' = None,  effect: 'CodeableConcept' = None,  incidence: 'CodeableConcept' = None,  management: 'CodeableConcept' = None, ):
        self.resourceType: str = resourceType or "MedicinalProductInteraction"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.subject: list['Reference'] = subject or []
        self.description: str = description 
        self.interactant: list['Interactant'] = interactant or []
        self.type: 'CodeableConcept' = type 
        self.effect: 'CodeableConcept' = effect 
        self.incidence: 'CodeableConcept' = incidence 
        self.management: 'CodeableConcept' = management 
        