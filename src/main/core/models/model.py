from mongoengine import Document, StringField, FloatField


class Localization(Document):
    meta = {'db_alias': 'cache_lru_db'}

    user = StringField(required=True, max_length=64)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)

    def save(self, *args, **kwargs):
        return super(Localization, self).save(*args, **kwargs)
