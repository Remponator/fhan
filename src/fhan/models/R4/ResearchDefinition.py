"""
Generated class for ResearchDefinition. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


class ResearchDefinition(DomainResource):
    """ The ResearchDefinition resource describes the conditional state (population and any exposures being compared within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this research definition, represented as a URI (globally unique)
    :param list['Identifier'] identifier: Additional identifier for the research definition
    :param str version: Business version of the research definition
    :param str name: Name for this research definition (computer friendly)
    :param str title: Name for this research definition (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the ResearchDefinition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param 'CodeableConcept' subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the research definition
    :param str comment: Used for footnotes or explanatory notes
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for research definition (if applicable)
    :param str purpose: Why this research definition is defined
    :param str usage: Describes the clinical usage of the ResearchDefinition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the research definition was approved by publisher
    :param str lastReviewDate: When the research definition was last reviewed
    :param 'Period' effectivePeriod: When the research definition is expected to be used
    :param list['CodeableConcept'] topic: The category of the ResearchDefinition, such as Education, Treatment, Assessment, etc.
    :param list['ContactDetail'] author: Who authored the content
    :param list['ContactDetail'] editor: Who edited the content
    :param list['ContactDetail'] reviewer: Who reviewed the content
    :param list['ContactDetail'] endorser: Who endorsed the content
    :param list['RelatedArtifact'] relatedArtifact: Additional documentation, citations, etc.
    :param str library: Logic used by the ResearchDefinition
    :param 'Reference' population: What population?
    :param 'Reference' exposure: What exposure?
    :param 'Reference' exposureAlternative: What alternative exposure state?
    :param 'Reference' outcome: What outcome?
    """
    def __init__(self, resourceType: str = "ResearchDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  identifier: list['Identifier'] = None,  version: str = None,  name: str = None,  title: str = None,  shortTitle: str = None,  subtitle: str = None,  status: str = None,  experimental: bool = None,  subjectCodeableConcept: 'CodeableConcept' = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  comment: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  purpose: str = None,  usage: str = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  topic: list['CodeableConcept'] = None,  author: list['ContactDetail'] = None,  editor: list['ContactDetail'] = None,  reviewer: list['ContactDetail'] = None,  endorser: list['ContactDetail'] = None,  relatedArtifact: list['RelatedArtifact'] = None,  library: str = None,  population: 'Reference' = None,  exposure: 'Reference' = None,  exposureAlternative: 'Reference' = None,  outcome: 'Reference' = None, ):
        self.resourceType: str = resourceType or "ResearchDefinition"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.name: str = name 
        self.title: str = title 
        self.shortTitle: str = shortTitle 
        self.subtitle: str = subtitle 
        self.status: str = status 
        self.experimental: bool = experimental 
        self.subjectCodeableConcept: 'CodeableConcept' = subjectCodeableConcept 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.comment: str = comment or []
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.purpose: str = purpose 
        self.usage: str = usage 
        self.copyright: str = copyright 
        self.approvalDate: str = approvalDate 
        self.lastReviewDate: str = lastReviewDate 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.topic: list['CodeableConcept'] = topic or []
        self.author: list['ContactDetail'] = author or []
        self.editor: list['ContactDetail'] = editor or []
        self.reviewer: list['ContactDetail'] = reviewer or []
        self.endorser: list['ContactDetail'] = endorser or []
        self.relatedArtifact: list['RelatedArtifact'] = relatedArtifact or []
        self.library: str = library or []
        self.population: 'Reference' = population 
        self.exposure: 'Reference' = exposure 
        self.exposureAlternative: 'Reference' = exposureAlternative 
        self.outcome: 'Reference' = outcome 
        