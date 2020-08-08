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