import socket
import csv
from datetime import datetime
from time import sleep


def clientProc():
    clientTimesDict = {}
    serverTimesDict = {}
    mySocket = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )
    clientTimesDict['clientReqTime'] = datetime.utcnow().timestamp()
    message = "Hello World"

    mySocket.sendto ( message.encode(), ( '52.66.20.98', 2728 ) )

    data, server = mySocket.recvfrom ( 100 )
    clientTimesDict['clientRecvTime'] = datetime.utcnow().timestamp()

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
    offsetValues = []
    delayValues = []
    standardDeviation = []
    averageRoundTripTime = None
    standardDeviation = None
    offset = None
    delay = None

    with open('results1A-A.csv', 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(['Client Request Time', 'Client Recieved Time', 'Server Recieved Time', 'Server Response Time', 'Roundtrip delay', 'Offset', 'Delay'])

        for i in range(720): # Collect values for 2 hours
            clientTimesDict, serverTimesDict = clientProc()

            clientReqTime = clientTimesDict['clientReqTime']
            clientRecvTime = clientTimesDict['clientRecvTime']
            serverRecvTime = float(serverTimesDict['serverRecvTime'])#parser.parse(serverTimesDict['serverRecvTime'])
            serverRespTime = float(serverTimesDict['serverRespTime'])#parser.parse(serverTimesDict['serverRespTime'])

            clientReqTimes.append(clientReqTime)
            clientRecvTimes.append(clientRecvTime)
            serverRecvTimes.append(serverRecvTime)
            serverRespTimes.append(serverRespTime)

            #roundTripTime
            roundTripTime = (clientRecvTime - clientReqTime)
            #print(roundTripTime)

            # #Offset
            offset = ((serverRecvTime - clientReqTime) + (serverRespTime - clientRecvTime))/2
            #print(offset)
            offsetValues.append(offset)

            # #Delay
            delay = (serverRecvTime - clientReqTime) + (clientRecvTime - serverRespTime)
            #print(delay)
            delayValues.append(delay)

            roundTripTimes.append(roundTripTime)
            csvWriter.writerow([clientReqTime, clientRecvTime, serverRecvTime, serverRespTime, roundTripTime, offset, delay ])
            #sleep(10)

    print("************END of Program***********")
