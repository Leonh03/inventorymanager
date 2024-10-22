import mongoengine as me
import uuid

class Collections(me.Document):
    eventId = me.StringField(primary_key=True)
    eventTitle = me.StringField(primary_key=True)
    eventDate = me.StringField(required=True)
    lowestPrice = me.StringField(required=True)
    ticketAmount = me.IntField(required=False)
    listedAmount = me.StringField(required=False)
    soldAmount = me.IntField(required=False)
    PNL = me.IntField(required=False)
    meta = {
        'collection': 'collections',
        'indexes': ['sdg_id']
    }
