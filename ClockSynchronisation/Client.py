import socket
from datetime import datetime
import numpy

def clientProc():
    clientTimesDict = {}
    serverTimesDict = {}
    mySocket = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )
    clientTimesDict['clientReqTime'] = datetime.utcnow()
    message = "Hello World"

    mySocket.sendto ( message.encode(), ( 'localhost', 2727 ) )

    data, server = mySocket.recvfrom ( 100 )
    clientTimesDict['clientRecvTime'] = datetime.utcnow()

    serverTimes = data.decode()
    serverTimesDict['serverRecvTime'] = serverTimes.split("**")[0]
    serverTimesDict['serverRespTime'] = serverTimes.split("**")[1]

    return clientTimesDict, serverTimesDict


if __name__ == "__main__":
    clientReqTimes = []
    clientRecvTimes = []
    serverRecvTimes = []
    serverRespTimes = []

    roundTripTimes = []

    for i in range(100):
        clientTimesDict, serverTimesDict = clientProc()
        clientReqTimes.append(clientTimesDict['clientReqTime'])
        clientRecvTimes.append(clientTimesDict['clientRecvTime'])
        serverRecvTimes.append(serverTimesDict['serverRecvTime'])
        serverRespTimes.append(serverTimesDict['serverRespTime'])
        roundTripTimes.append(clientTimesDict['clientRecvTime'] - clientTimesDict['clientReqTime'])

    print("Average Round Trip delay is "+str(numpy.mean(roundTripTimes)))


