# from bson import ObjectId
from mongoengine import Document, connect
from mongoengine.fields import *


class IsoRequests(Document):
    request_received = DictField()
    iso_sent = StringField()
    response_sent = DictField()
    iso_received = StringField()
    status = StringField()
    created_at = DateField()
    updated_at = DateField()

    # def get_id(self):
    #     return ObjectId(self.id).__str__()

    def get_connection(self):
        return connect('iso8583', host='localhost', port=27017)
