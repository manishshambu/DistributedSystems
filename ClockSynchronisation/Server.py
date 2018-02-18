import socket
from datetime import datetime

def serverProc():
    mySocket = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )
    mySocket.bind ( ( 'localhost', 2727 ) )
    while True:
        data, client = mySocket.recvfrom ( 100 )
        serverRecvTime = datetime.utcnow()
        data = data.decode()
        #print ('We have received a datagram from', client)
        #print (data)
        serverRespTime = datetime.utcnow()
        mySocket.sendto ( str(serverRecvTime).encode(), client )

if __name__ == "__main__":
    serverProc()