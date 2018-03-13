import os

def sCreate(label):
    pass

def sId(label):
        pass

def sPush(stackId, item):
        os.system("etcdctl put "+ stackId +" "+item)

def sPop(stackId):
        os.system("etcdctl get "+ stackId)

def sTop(stackId):
        pass

def sSize(stackId):
        pass

