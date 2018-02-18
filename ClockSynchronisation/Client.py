import socket
from datetime import datetime

def clientProc():
    mySocket = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )
    clientReqTime = datetime.utcnow()
    message = "Hello"
    mySocket.sendto ( message.encode(), ( 'localhost', 2727 ) )
    data, server = mySocket.recvfrom ( 100 )
    clientRecvTime = datetime.utcnow()
    serverRecvTime = data.decode()

    print ("Time when the client sent the request to server "+ str(clientReqTime))
    print("Time when client recieved the server's response " + str(clientRecvTime))
    print("Time when server recieved the client's request " +  serverRecvTime)



if __name__ == "__main__":
    clientProc()