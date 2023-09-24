"""
Generated class for Account. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Coverage(ModelBase):
    """ The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' coverage: The party(s), such as insurances, that may contribute to the payment of this account
    :param int priority: The priority of the coverage in the context of this account
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  coverage: 'Reference' = None,  priority: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.coverage: 'Reference' = coverage 
        self.priority: int = priority 
        

    
    

class Guarantor(ModelBase):
    """ The parties responsible for balancing the account if other payment options fall short.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' party: Responsible entity
    :param bool onHold: Credit or other hold applied
    :param 'Period' period: Guarantee account during
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  party: 'Reference' = None,  onHold: bool = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.party: 'Reference' = party 
        self.onHold: bool = onHold 
        self.period: 'Period' = period 
        

class Account(DomainResource):
    """ A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Account number
    :param str status: active | inactive | entered-in-error | on-hold | unknown
    :param 'CodeableConcept' type: E.g. patient, expense, depreciation
    :param str name: Human-readable label
    :param list['Reference'] subject: The entity that caused the expenses
    :param 'Period' servicePeriod: Transaction window
    :param list['Coverage'] coverage: The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
    :param 'Reference' owner: Entity managing the Account
    :param str description: Explanation of purpose/use
    :param list['Guarantor'] guarantor: The parties ultimately responsible for balancing the Account
    :param 'Reference' partOf: Reference to a parent Account
    """
    def __init__(self, resourceType: str = "Account",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  type: 'CodeableConcept' = None,  name: str = None,  subject: list['Reference'] = None,  servicePeriod: 'Period' = None,  coverage: list['Coverage'] = None,  owner: 'Reference' = None,  description: str = None,  guarantor: list['Guarantor'] = None,  partOf: 'Reference' = None, ):
        self.resourceType: str = resourceType or "Account"
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
        self.type: 'CodeableConcept' = type 
        self.name: str = name 
        self.subject: list['Reference'] = subject or []
        self.servicePeriod: 'Period' = servicePeriod 
        self.coverage: list['Coverage'] = coverage or []
        self.owner: 'Reference' = owner 
        self.description: str = description 
        self.guarantor: list['Guarantor'] = guarantor or []
        self.partOf: 'Reference' = partOf 
        