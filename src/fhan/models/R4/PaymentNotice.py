"""
Generated class for PaymentNotice. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

@dataclass
class PaymentNotice(ModelBase):
    """ This resource provides the status of the payment for goods and services rendered, and the request and response resource references.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for the payment noctice
    :param str status: active | cancelled | draft | entered-in-error
    :param Reference request: Request reference
    :param Reference response: Response reference
    :param str created: Creation date
    :param Reference provider: Responsible practitioner
    :param Reference payment: Payment reference
    :param str paymentDate: Payment or clearing date
    :param Reference payee: Party being paid
    :param Reference recipient: Party being notified
    :param Money amount: Monetary amount of the payment
    :param CodeableConcept paymentStatus: Issued or cleared Status of the payment
    """

    resourceType: str = "PaymentNotice"
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
    
    request: "Reference" = None
    
    response: "Reference" = None
    
    created: str = None
    
    provider: "Reference" = None
    
    payment: "Reference" = None
    
    paymentDate: str = None
    
    payee: "Reference" = None
    
    recipient: "Reference" = None
    
    amount: "Money" = None
    
    paymentStatus: "CodeableConcept" = None
    