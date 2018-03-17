import socket
from datetime import datetime

def serverProc():
    mySocket = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )
    mySocket.bind ( ( '52.66.20.98', 2728 ) )
    while True:
        data, client = mySocket.recvfrom ( 100 )
        serverRecvTime = str(datetime.utcnow().timestamp())
        data = data.decode()
        serverRespTime = str(datetime.utcnow().timestamp())
        serverTimes = serverRecvTime + "**" + serverRespTime
        mySocket.sendto (serverTimes.encode(), client )



if __name__ == "__main__":
    serverProc()
