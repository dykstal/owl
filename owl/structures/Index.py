from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from owl.utils import formatRecord
from owl.models.DataStructure import DataStructure

class Index(DataStructure):
    '''
    Data Structure for Elasticsearch Index Data.
    '''
    def __init__(self, index, *args, **kwargs):
        super(Index, self).__init__(*args, **kwargs)
        self.es = Elasticsearch()
        self.index = index

    def getRecord(self, id_):
        return formatRecord(
            self.es.get(index=self.index, id=id_)['_source']
        )