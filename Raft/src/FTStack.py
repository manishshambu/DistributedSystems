import etcd


def sPush(sLabel, element, client):
    print(sRead(sLabel))
    stackLen = len(sRead(sLabel))
    client.write('/'+sLabel+'/'+str(stackLen), element)
    print(sRead(sLabel))

def sPop(sLabel):
    print(sRead(sLabel))
    stackLen = len(sRead(sLabel))
    popElement = None

    if stackLen > 0:
        popElement = sRead(sLabel)[-1]
        client.delete('/'+sLabel+'/'+str(stackLen - 1))
        print(sRead(sLabel))
    else:
        print("Nothing to pop from the stack")
        return None

    return popElement


def sCreate(sLabel, nums):

    if sLabel in getCurrentStacks():
        print("Stack with sLabel already exists")
    else:
        for i in range(len(nums)):
            client.write('/' + sLabel + '/' + str(i), nums[i])

    return getCurrentStacks()[sLabel]

def sRead(sLabel):
    stackRead = client.read("/"+sLabel, recursive = True)
    values = (stackRead.__dict__['_children'])

    stackContents = [None] * len(values)

    for i in range(len(values)):
        valueSet = dict(values[i])
        key = int((valueSet['key']).split("/")[2])
        stackContents[key] = int(valueSet['value'])

    return stackContents

def getCurrentStacks():
    stackRead = client.read("/", recursive=True)
    values = stackRead.__dict__['_children']

    if not values:
        print("No stacks created")
    print(values)

    curStacks = {}

    for i in range(len(values)):
        valueSet = dict(values[i])
        if 'dir' in valueSet:
            curStacks[valueSet['key'][1:]] = valueSet['createdIndex']

    return curStacks



def sId(sLabel):
    return stacks[sLabel]

def sSize(sLabel):
    return len(sRead(sLabel))

def sTop(sLabel):
    return sRead(sLabel)[-1]

def machines(client):
    return client.machines

def leader(client):
    return client.leader



if __name__ == "__main__":
    client = etcd.Client(host='127.0.0.1', port=22379)
    #client = etcd.Client(host=(('127.0.0.1', 22379), ('127.0.0.1', 32379), ('127.0.0.1', 2379)))

    print(client.read("/", recursive=True))
    print("New ID of the created stack is "+str(sCreate("manish", [1,2,3,4])))
    print("Contents of the stack are "+str(sRead("manish")))
    #sPush("manish", 7, client)
    #sPop("manish")
    #print("Size of the stack is "+str(sSize("manish")))
    #print("Top of the stack is "+str(sTop("manish")))
    print("Machines in the cluster are "+str(machines(client)))
    #print("Leader of the cluster is "+str(leader(client)))
    #print("Stacks present within the system are {name : id} as follows: "+str(getCurrentStacks()))

