# coding utf-8
import enchant
import pexpect
import paramiko
from generate_html import generateTemplate
from scp import SCPClient
from settings import IPs, Paths

path = Paths()
ip = IPs()

def createSSHClient(server, port, user, password):
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(server, port, user, password)
            return client

def getTheDictionary(language):
    dictionary = enchant.Dict(language)
    return dictionary

def readWords (file):
    txt_file = open(file,'r')
    words = txt_file.read().split(' ')
    txt_file.close()
    return words

def getAuthor(content):
	lg = len(content)
	author = content[lg-1]
	content.pop(lg-1)
	content.pop(lg-1)
	return author

def removeSigns(text):
	for x in range(len(text)):
		if ',' in text[x]:
		  text[x] = text[x].replace(',','')
		if '.' in text[x]:
		    text[x] = text[x].replace('.','')
		if '\n' in text[x]:
		    text[x] = text[x].replace('\n','')
		if '!' in text[x]:
		    text[x] = text[x].replace('!','')
		if '?' in text[x]:
		    text[x] = text[x].replace('?','')
		if ':' in text[x]:
		    text[x] = text[x].replace(':','')


		x += 1

	text.pop(len(text)-1)
	text.pop(len(text)-1)

	return text

def checkTextIsCorrect(text,dictionary):
    wrongCounter = 1
    wrongWords = []
    for x in range(len(text)):
        if dictionary.check(text[x]) is False:
            print("Tu jest błąd: {zle} \n".format(zle = text[x]))
            wrongWords.append(text[x])
            wrongCounter += 1
        x += 1
    return wrongWords


def sendBackToClient(ssh):
        scp = SCPClient(ssh.get_transport())
        scp.put(path.resultsScpFromServerPath,path.resultsScpToClientPath)
        pass



language = 'pl_PL'
fileToRead = 'dyktando.txt'
textFromFile = readWords(fileToRead)
textToCheck = removeSigns(textFromFile)

wynik = checkTextIsCorrect(textToCheck, getTheDictionary(language))

generateTemplate(fileToRead, wynik)

ssh = createSSHClient(ip.ClientIP, '22', ip.ClientName, ip.ClientPass)
sendBackToClient(ssh)
