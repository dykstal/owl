import dateutil.parser
#import shapely

def formatRecord(record):
    '''
    Format a Dictionary Record of Data (with Attribute Name Keys Mapping to
    Attribute Values) so that:
      1.  Times are Represented as JSON Objects.
      2.  TODO: Geometries are Represented as Shapely Geometries.
    '''
    # 1. Represent Times as Datetime Objects
    for attribute in record:
        try: record[attribute] = dateutil.parser.parse(record[attribute])
        except: continue
    return record

def queryFromFilter(filters):
    '''
    Format a Filter Dictionary as an Elasticsearch Query.
    '''
    # Return All Data if there are no Filters
    if len(filters) == 0:
        return {
            'query': {
                'match_all': filters
            }
        }
    # Otherwise, Match a Particular Field
    # TODO: Do Other Queries than "Match"
    else:
        return {
            'query': {
                'match': filters
            }
        }