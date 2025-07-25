# lib/builtin.py 

from marshmallow import Schema, fields, validate, ValidationError 
from pprint import pprint

class VetSchema(Schema):
    #name, specialty, years_practice, and diploma use some builtin marshmallow validators
    name = fields.Str(validate=lambda str: str.startswith("Dr."))
    email = fields.Email()   #Email has built-in validation
    website = fields.URL()   #URL has built-in validation
    specialty = fields.Str(validate=validate.Length(min=1))
    years_practice = fields.Int(validate=validate.Range(min=0, max=100),  )
    diploma = fields.Str(validate=validate.OneOf(["DVM", "VMD"]))


vet_data = [
    {"name": "Dr. Wags", "email": "email.com"},                                     # invalid email
    {"name": "Dr. Wags", "email": "wags@email.com",  "website": "htp:company.com"}, # invalid URL
    {"name": "Dr. Wags", "email": "wags@email.com",  "specialty": ""} ,         
    {"name": "Dr. Wags", "email": "wags@email.com",  "years_practice": -5},      
    {"name": "Dr. Wags", "email": "wags@email.com", "diploma": "none"},          
    {"name": "Mr. Wags", "email": "wags@email.com"},                             
]

try:
    result = VetSchema(many=True).load(vet_data)
    pprint(result)
except ValidationError as err:
    pprint(err.messages)
    # => 0: {'email': ['Not a valid email address.']},
    # => 1: {'website': ['Not a valid URL.']},