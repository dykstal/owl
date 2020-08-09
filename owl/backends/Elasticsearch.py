import elasticsearch
from elasticsearch.helpers import bulk
from owl.models.Backend import Backend

class Elasticsearch(Backend):
    '''
    A Class to Ingest and Manage the Elasticsearch Backend.
    '''
    def __init__(self, *args, **kwargs):
        super(Elasticsearch, self).__init__(*args, **kwargs)
        self.es = elasticsearch.Elasticsearch()
    
    def createIndex(self, index=None):
        '''
        Create an Empty Elasticsearch Index.
        '''
        if index is None:
            raise AttributeError('Cannot Write to NoneType Index.')
        self.es.indices.create(index=index)

    def deleteIndex(self, index=None, ignoreResCodes=[400,404]):
        '''
        Delte an Existing Elasticsearch Index.
        '''
        if index is None:
            raise AttributeError('Cannot Delete NoneType Index.')
        self.es.indices.delete(
            index=index,
            ignore=ignoreResCodes
        )

    def ingest(self, index, records):
        '''
        Ingest a List of Records to Elasticsearch.
        '''
        _ = bulk(
            self.es,
            [x.rec for x in records],
            index=index
        )
        self.es.indices.refresh(index=index)

    def ingestRecord(self, index, record):
        '''
        Ingest a Single Record to Elasticsearch.
        '''
        self.ingest(index, [record])