"""
Generated class for SupplyDelivery. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class SuppliedItem(ModelBase):
    """ The item that is being delivered or has been supplied.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Quantity' quantity: Amount dispensed
    :param 'CodeableConcept' itemCodeableConcept: Medication, Substance, or Device supplied
    :param 'Reference' itemReference: Medication, Substance, or Device supplied
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  quantity: 'Quantity' = None,  itemCodeableConcept: 'CodeableConcept' = None,  itemReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.quantity: 'Quantity' = quantity 
        self.itemCodeableConcept: 'CodeableConcept' = itemCodeableConcept 
        self.itemReference: 'Reference' = itemReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SuppliedItem":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


class SupplyDelivery(DomainResource):
    """ Record of delivery of what is supplied.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External identifier
    :param list['Reference'] basedOn: Fulfills plan, proposal or order
    :param list['Reference'] partOf: Part of referenced event
    :param str status: in-progress | completed | abandoned | entered-in-error
    :param 'Reference' patient: Patient for whom the item is supplied
    :param 'CodeableConcept' type: Category of dispense event
    :param 'SuppliedItem' suppliedItem: The item that is delivered or supplied
    :param str occurrenceDateTime: When event occurred
    :param 'Period' occurrencePeriod: When event occurred
    :param 'Timing' occurrenceTiming: When event occurred
    :param 'Reference' supplier: Dispenser
    :param 'Reference' destination: Where the Supply was sent
    :param list['Reference'] receiver: Who collected the Supply
    """
    def __init__(self, resourceType: str = "SupplyDelivery",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  basedOn: list['Reference'] = None,  partOf: list['Reference'] = None,  status: str = None,  patient: 'Reference' = None,  type: 'CodeableConcept' = None,  suppliedItem: 'SuppliedItem' = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  supplier: 'Reference' = None,  destination: 'Reference' = None,  receiver: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "SupplyDelivery"
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
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.patient: 'Reference' = patient 
        self.type: 'CodeableConcept' = type 
        self.suppliedItem: 'SuppliedItem' = suppliedItem 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.supplier: 'Reference' = supplier 
        self.destination: 'Reference' = destination 
        self.receiver: list['Reference'] = receiver or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SupplyDelivery":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance