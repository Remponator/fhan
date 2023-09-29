"""
Generated class for DataType. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Extension import *
from fhan.models.generator_models import BaseModel

class DataType(BaseModel):
    """ DataType Type: The base class for all re-useable types defined as part of the FHIR Specification.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  extension:  list['Extension']  = None, ):
        self.resourceType = resourceType or "DataType"
        self.id = id 
        self.extension = extension or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DataType":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DataType":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()