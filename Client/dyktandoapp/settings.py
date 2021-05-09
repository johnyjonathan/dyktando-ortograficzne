class IPs:
    def __init__(self):
        self.ClientIP = '192.168.0.172'             #Client ip
        self.ServerPath = '192.168.0.221'           #Server ip
        self.ClientName = 'michal'                  #Client User Name
        self.ServerName = 'michal2'                 #Server User Name
        self.ClientPass = '******'                #Client password
        self.ServerPass = '******'                #Serwer password

class Paths:
    def __init__(self):

        #Client Side
        #Path to file
        self.dyktandoCreatePath = 'result/dyktando.txt'
        #Path for SCP (from)(client side)
        self.dyktandoScpFromClientPath = '/home/michal/dyktandoapp/result/dyktando.txt'
        #Path for SCP (to)(client side)
        self.dyktandoScpToServerPath = '/home/michal2'

        #Server Side
        #Path for SCP (from)(server side)
        self.resultsScpFromServerPath = '/home/michal2/result.html'
        #Path for SCP (to)(server side)
        self.resultsScpToClientPath = '/home/michal/dyktandoapp/result'
