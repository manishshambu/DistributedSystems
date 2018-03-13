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

def killProcess():
    pass

def retrieveMembers():
    pass

def startCluster():
    pass

def clusterMembers():
    pass

def startEtcd():
    pass

if __name__ == "__main__":
    while(True):
        number = input("Enter any one of the following options."
                       "1. Start etcl Raft process\n"
                       "2. Start Goreman cluster\n"
                       "3. Create sLabel\n"
                       "4. Push element into FTstack\n"
                       "5. Get element from FTstack\n"
                       "6. Get top of stack\n"
                       "7. get sID\n"
                       "8. View current members in the cluster"
                       "9. Kill a server in the cluster"
                       "10. Retrieve value from a specific server in the cluster.")

        print(number)

        if number == 1:
            pass
        elif number == 2:
            pass
        elif number == 3:
            pass
        elif number == 4:
            pass
        elif number == 5:
            pass
        elif number == 6:
            pass
        elif number == 7:
            pass
        elif number == 8:
            pass
        elif number == 9:
            pass
        elif number == 10:
            pass


