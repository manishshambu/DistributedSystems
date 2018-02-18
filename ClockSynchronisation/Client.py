import socket
from datetime import datetime
import numpy
import matplotlib.pyplot as plt
import csv

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
    standardDeviation = []
    averageRoundTripTime = None
    standardDeviation = None

    with open('results.csv', 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(['Client Request Time', 'Client Recieved Time', 'Server Recieved Time', 'Server Response Time', 'Roundtrip delay'])

        for i in range(100):
            clientTimesDict, serverTimesDict = clientProc()
            clientReqTimes.append(clientTimesDict['clientReqTime'])
            clientRecvTimes.append(clientTimesDict['clientRecvTime'])
            serverRecvTimes.append(serverTimesDict['serverRecvTime'])
            serverRespTimes.append(serverTimesDict['serverRespTime'])
            roundTripTime = (clientTimesDict['clientRecvTime'] - clientTimesDict['clientReqTime']).total_seconds()
            roundTripTimes.append(roundTripTime)
            csvWriter.writerow([clientTimesDict['clientReqTime'], clientTimesDict['clientRecvTime'], serverTimesDict['serverRecvTime'], serverTimesDict['serverRespTime'], roundTripTime ])


    averageRoundTripTime = numpy.mean(roundTripTimes)
    standardDeviation    = numpy.std(roundTripTimes)

    print("Average Round Trip delay is " + str(averageRoundTripTime))
    print("Standard Deviation of Round Trip times are " + str(standardDeviation))





