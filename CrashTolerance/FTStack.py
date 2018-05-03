
import sys
import time
sys.path.append("../")
from pysyncobj import replicated, SyncObj, SyncObjConf

class FTStack(SyncObj):
	def __init__(self, selfAddress, partnerAddress):
		cfg = SyncObjConf(dynamicMembershipChange = True)
		super(FTStack, self).__init__(selfAddress, partnerAddress, cfg)
		self.data = {}
		self.sid = {}
		self.counter = -1

	def stackSize(self, label):
		if label not in self.data:
			print("Stack with given label not found")
		return len(self.data[label])

	def stackId(self, label):
		if label not in self.data:
			print("Stack with given label not found")
			return -1
		return self.sid[label]
			

	@replicated
	def createStack(self, label):
		self.data[label] = []
		self.counter += 1
		self.sid[label] = self.counter

	@replicated
	def push(self, value, label):
		if label not in self.data:
			print("Stack with given label does not exist\n")
			return -1
		self.data[label].append(value)
		#print("Successfully appended value to the stack with given label\n")
		return 1

	def tos(self, label):
		if label not in self.data:
			print("Stack does not exist\n")
			return -1
		if (self.data[label] == 0):
			print("Stack size is zero\n")
			return -1

		return self.data[label][-1]

	@replicated
	def pop(self, label):
		if label not in self.data:
			print("Stack does not exist\n")
			return -1
		if len(self.data[label]) == 0:
			print("Stack is empty\n")
			return -1
		element = self.data[label][-1]
		self.data[label].pop()
		#print(element)
		return element
	
	def getdata(self, label):
		return self.data		

def get_input(v):
    print('1. Create a new stack. Eg. 1 manish\n\
2. Push to stack. Eg. 2 manish 5 \n\
3. Pop from stack. Eg. 3 manish  \n\
4. Get Top of stack. Eg. 4 manish \n\
5. Get size of stack. Eg. 5 manish \n\
6. Get stack id. Eg. 6 manish \n\
7. Get the cluster leader. Eg. 7 \n\
8. Get stack contents\n')
    return input(v)

def main():
	if len(sys.argv) < 2:
		print('Usage: %s :port1 :port2 :port3 ...')
		sys.exit(-1)
	
	selfAddr = int(sys.argv[1])
	partners = ['localhost:%d' % int(p) for p in sys.argv[2:]]

	_FTStack = FTStack('localhost:%d' %selfAddr, partners)


	while True:
		cmd = get_input(">> ").split()
		if not cmd:
			continue
		elif cmd[0] == '1':
			_FTStack.createStack(cmd[1])
		elif cmd[0] == '2':
			_FTStack.push(int(cmd[2]), cmd[1])
		elif cmd[0] == '3':
			element = _FTStack.pop(cmd[1])
			print("Element popped from stack")
		elif cmd[0] == '4':
			element = _FTStack.tos(cmd[1])
			print("Top of stack is: "+str(element))
		elif cmd[0] == '5':
			print("Size of stack is: "+ str(_FTStack.stackSize(cmd[1])))
		elif cmd[0] == '6':
			time.sleep(1)
			print("Stack ID: "+ str(_FTStack.stackId(cmd[1])))
		elif cmd[0] == '7':
			print(_FTStack._getLeader())
		elif cmd[0] == '8':
			print(_FTStack.getdata(cmd[1]))

if __name__ == "__main__":
	main()
