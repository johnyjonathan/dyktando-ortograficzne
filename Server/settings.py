class IPs:
    def __init__(self):
        self.ClientIP = '192.168.0.172'
        self.ServerPath = '192.168.0.221'
        self.ClientName = 'michal'
        self.ServerName = 'michal2'
        self.ClientPass = '*******'
        self.ServerPass = '*******'

class Paths:
    def __init__(self):

        #Client Side
        self.dyktandoCreatePath = 'result/dyktando.txt'
        self.dyktandoScpFromClientPath = '/home/michal/dyktandoapp/result/dyktando.txt'
        self.dyktandoScpToServerPath = '/home/michal2'

        #Server Side
        self.resultsScpFromServerPath = '/home/michal2/result.html'
        self.resultsScpToClientPath = '/home/michal/dyktandoapp/result'
