"""
Generated class for Subscription. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Channel(ModelBase):
    """ Details where to send notifications when resources are received that meet the criteria.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: rest-hook | websocket | email | sms | message
    :param str endpoint: Where the channel points to
    :param str payload: MIME type to send, or omit for no payload
    :param str header: Usage depends on the channel type
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  endpoint: str = None,  payload: str = None,  header: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.endpoint: str = endpoint 
        self.payload: str = payload 
        self.header: str = header or []
        

class Subscription(DomainResource):
    """ The subscription resource is used to define a push-based subscription from a server to another system. Once a subscription is registered with the server, the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" so that another system can take an appropriate action.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str status: requested | active | error | off
    :param list['ContactPoint'] contact: Contact details for source (e.g. troubleshooting)
    :param str end: When to automatically delete the subscription
    :param str reason: Description of why this subscription was created
    :param str criteria: Rule for server push
    :param str error: Latest error note
    :param 'Channel' channel: The channel on which to report matches to the criteria
    """
    def __init__(self, resourceType: str = "Subscription",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  status: str = None,  contact: list['ContactPoint'] = None,  end: str = None,  reason: str = None,  criteria: str = None,  error: str = None,  channel: 'Channel' = None, ):
        self.resourceType: str = resourceType or "Subscription"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.status: str = status 
        self.contact: list['ContactPoint'] = contact or []
        self.end: str = end 
        self.reason: str = reason 
        self.criteria: str = criteria 
        self.error: str = error 
        self.channel: 'Channel' = channel 
        