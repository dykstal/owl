from shinobi.models.Analytic import Analytic

class WeatherNLP(Analytic):
    '''
    The WeatherNLP Analytic Supports Performing NLP on Weather Forecasts
    to Extract Key Descriptive Phrases from Long Weather Forecast Strings.
    '''
    def __init__(self, *args, **kwargs):
        super(WeatherNLP, self).__init__(*args, **kwargs)

    def extractForecastKeywords(self, forecast):
        '''
        Extract the Keywords from a Weather Forecast Description.
        '''
        pass
