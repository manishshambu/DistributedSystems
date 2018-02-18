import socket
from datetime import datetime

def serverProc():
    mySocket = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )
    mySocket.bind ( ( 'localhost', 2727 ) )
    while True:
        data, client = mySocket.recvfrom ( 100 )
        serverRecvTime = str(datetime.utcnow())
        data = data.decode()
        #print ('We have received a datagram from', client)
        #print (data)
        serverRespTime = str(datetime.utcnow())
        serverTimes = serverRecvTime + "**" + serverRespTime
        mySocket.sendto ( serverTimes.encode(), client )

if __name__ == "__main__":
    serverProc()