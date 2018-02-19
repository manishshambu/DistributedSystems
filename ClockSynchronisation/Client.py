import socket
from datetime import datetime
import numpy
import matplotlib.pyplot as plt
import csv
from time import sleep
from dateutil import parser

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

def plotOffsetGraph(offsetValues, mean, std):
    plt.plot([i for i in range(len(offsetValues))], offsetValues)
    plt.xlabel("Measurement #")
    plt.ylabel("Offset Values")
    plt.figtext(.4, .8, "Average Round Trip Time = "+str(mean))
    plt.figtext(.4, .7, "Standard Deviation = " + str(std))
    plt.savefig("Offset Graph")
    #plt.show()



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

    with open('results.csv', 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(['Client Request Time', 'Client Recieved Time', 'Server Recieved Time', 'Server Response Time', 'Roundtrip delay', 'Offset', 'Delay'])

        for i in range(100): # Collect values for 2 hours
            clientTimesDict, serverTimesDict = clientProc()

            clientReqTime = clientTimesDict['clientReqTime']
            clientRecvTime = clientTimesDict['clientRecvTime']
            serverRecvTime = parser.parse(serverTimesDict['serverRecvTime'])
            serverRespTime = parser.parse(serverTimesDict['serverRespTime'])

            clientReqTimes.append(clientReqTime)
            clientRecvTimes.append(clientRecvTime)
            serverRecvTimes.append(serverRecvTime)
            serverRespTimes.append(serverRespTime)

            #roundTripTime
            roundTripTime = (clientRecvTime - clientReqTime).total_seconds()

            #Offset
            offset = ((serverRecvTime - clientReqTime).total_seconds() + (serverRespTime - clientRecvTime).total_seconds())/2
            #print(offset)
            offsetValues.append(offset)

            #Delay
            delay = (serverRecvTime - clientReqTime).total_seconds() + ( clientRecvTime - serverRespTime).total_seconds()
            #print(delay)
            delayValues.append(delay)

            roundTripTimes.append(roundTripTime)
            csvWriter.writerow([clientReqTime, clientRecvTime, serverRecvTime, serverRespTime, roundTripTime, offset, delay ])
            #sleep(10)


    averageRoundTripTime = numpy.mean(roundTripTimes)
    standardDeviation    = numpy.std(roundTripTimes)

    plotOffsetGraph(offsetValues, averageRoundTripTime, standardDeviation)

    print("Average Round Trip delay is " + str(averageRoundTripTime))
    print("Standard Deviation of Round Trip times are " + str(standardDeviation))





