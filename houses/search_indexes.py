import datetime
from haystack import indexes
from houses.models import Myhouses


class MyhousesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    location = indexes.CharField( )
    type_of_room = indexes.CharField( )

    def get_model(self):
        return Myhouses



