from owl.backends.Elasticsearch import Elasticsearch
from owl.structures.Index import Index
from owl.structures.Record import Record

def new(use, *args, **kwargs):
    '''
    Instantiate a New Object with the Necessary
    Arguments and Keyword Arguments.
    '''
    return eval(use)(*args, **kwargs)