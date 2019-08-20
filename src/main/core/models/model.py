from mongoengine import Document, StringField, FloatField, DictField


class Localization(Document):
    """
    Localization is a document for handling and store information
    """
    meta = {'db_alias': 'cache_lru_db'}

    user = StringField(required=True, max_length=64)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    information = DictField(required=True)

    def save(self, *args, **kwargs):
        return super(Localization, self).save(*args, **kwargs)
