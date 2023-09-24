"""
Generated class for OperationDefinition. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Element import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Binding(Element):
    """ Binds to a value set if this parameter is coded (code, Coding, CodeableConcept).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str strength: required | extensible | preferred | example
    :param str valueSet: Source of value set
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    strength: str = None
    
    valueSet: str = None
    

    
    
@dataclass
class ReferencedFrom(Element):
    """ Identifies other resource parameters within the operation invocation that are expected to resolve to this resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str source: Referencing parameter
    :param str sourceId: Element id of reference
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    source: str = None
    
    sourceId: str = None
    

  
    
    
@dataclass
class Parameter(Element):
    """ The parameters for the operation/query.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name in Parameters.parameter.name or in URL
    :param str use: in | out
    :param int min: Minimum Cardinality
    :param str max: Maximum Cardinality (a number or *)
    :param str documentation: Description of meaning/use
    :param str type: What type this parameter has
    :param str targetProfile: If type is Reference | canonical, allowed targets
    :param str searchType: number | date | string | token | reference | composite | quantity | uri | special
    :param Binding binding: ValueSet details if this is coded
    :param ReferencedFrom referencedFrom: References to this parameter
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    name: str = None
    
    use: str = None
    
    min: int = None
    
    max: str = None
    
    documentation: str = None
    
    type: str = None
    
    targetProfile: str = None
    
    searchType: str = None
    
    binding:  "Binding" = Binding()
    
    referencedFrom:  list["ReferencedFrom"] = [ReferencedFrom()]
    

    
    
@dataclass
class Overload(Element):
    """ Defines an appropriate combination of parameters to use when invoking this operation, to help code generators when generating overloaded parameter sets for this operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str parameterName: Name of parameter to include in overload
    :param str comment: Comments to go on overload
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    parameterName: str = None
    
    comment: str = None
    

@dataclass
class OperationDefinition(ModelBase):
    """ A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this operation definition, represented as a URI (globally unique)
    :param str version: Business version of the operation definition
    :param str name: Name for this operation definition (computer friendly)
    :param str title: Name for this operation definition (human friendly)
    :param str status: draft | active | retired | unknown
    :param str kind: operation | query
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the operation definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for operation definition (if applicable)
    :param str purpose: Why this operation definition is defined
    :param bool affectsState: Whether content is changed by the operation
    :param str code: Name used to invoke the operation
    :param str comment: Additional information about use
    :param str base: Marks this as a profile of the base
    :param str resource: Types this operation applies to
    :param bool system: Invoke at the system level?
    :param bool type: Invoke at the type level?
    :param bool instance: Invoke on an instance?
    :param str inputProfile: Validation information for in parameters
    :param str outputProfile: Validation information for out parameters
    :param Parameter parameter: Parameters for the operation/query
    :param Overload overload: Define overloaded variants for when  generating code
    """

    resourceType: str = "OperationDefinition"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    kind: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    purpose: str = None
    
    affectsState: bool = None
    
    code: str = None
    
    comment: str = None
    
    base: str = None
    
    resource: str = None
    
    system: bool = None
    
    type: bool = None
    
    instance: bool = None
    
    inputProfile: str = None
    
    outputProfile: str = None
    
    parameter: list["Parameter"] = None
    
    overload: list["Overload"] = None
    