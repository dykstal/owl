import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from owl.models.DataStructure import DataStructure
from owl.structures.Record import Record
from owl.utils import queryFromFilter

class Index(DataStructure):
    '''
    Data Structure for Elasticsearch Index Data.
    '''
    def __init__(self, index, *args, **kwargs):
        super(Index, self).__init__(*args, **kwargs)
        self.es = Elasticsearch()
        self.index = index
        self.query = None
        self.generator = None

    def __len__(self):
        if self.query is None: return 0
        return self.es.search(
            index=self.index,
            body=self.query
        )['hits']['total']['value']

    def _makeGenerator(self):
        '''
        Create a Generator Object Over the Records Matching
        the Query for the Index.
        '''
        self.generator = scan(
            self.es,
            query=self.query,
            index=self.index,
            size=10000
        )

    def asDF(self):
        '''
        Return the Retrieved Data from the Index as a Pandas DataFrame.
        '''
        listData = self.asList()
        return pd.DataFrame([x.rec for x in listData])

    def asList(self):
        '''
        Return the Retrieved Data from the Index as a List of Records.
        '''
        if self.query is None: return []
        else:
            listRepresentation = [Record(x['_source']) for x in self.generator]
            if len(self) != len(listRepresentation):
                self._makeGenerator()
                listRepresentation = [Record(x['_source']) for x in self.generator]
            return listRepresentation

    def get(self, **filters):
        '''
        Assign the Class Generator to a Generator with Every
        Record Matching 
        '''
        self.query = queryFromFilter(filters)
        self._makeGenerator()

    def getRecord(self, ID):
        '''
        Get Exactly One Record from the Index from its ID.
        '''
        return Record(
            self.es.get(index=self.index, id=ID)['_source']
        )