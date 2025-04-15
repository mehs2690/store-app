from marshmallow import Schema, fields, validate

class ClientSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True, validate=validate.Length(min=5))
  email = fields.Email(required=True)
  phone = fields.Str(required=True)
