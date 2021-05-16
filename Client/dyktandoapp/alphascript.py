import paramiko
from scp import SCPClient
from settings import IPs, Paths

class Pusher:

    def __init__(self, name, dyktando):
        self.name = name
        self.dyktando = dyktando
        self.path = Paths()
        self.ip = IPs()

    def createSSHClient(self,server, port, user, password):
                self.client = paramiko.SSHClient()
                self.client.load_system_host_keys()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.client.connect(server, port, user, password)
                return self.client

    def pushToBravo(self):
        file = open(self.path.dyktandoCreatePath, "w")
        file.write(self.dyktando + "\n Autor: {name}".format(name=self.name))
        file.close()

        ssh = self.createSSHClient(self.ip.ServerPath, '22', self.ip.ServerName,  self.ip.ServerPass)
        scp = SCPClient(ssh.get_transport())
        scp.put(self.path.dyktandoScpFromClientPath, self.path.dyktandoScpToServerPath)
        ssh.exec_command('python3 BRAVO.py')
