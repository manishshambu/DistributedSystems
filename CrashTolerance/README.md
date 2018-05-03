I used PysyncObj library to implement my DSFT stack.

I extended my code using the KVStorage example class from pysyncobj library.
Current functions supported
1. Get the leader of the cluster
2. Get the contents of the stack
3. Get the stack ID given its label
4. Push element to the stack
5. Pop element from the stack
6. Get the top element from the stack
7. Get size of the stack

Usage
1. Spawn 5 terminals with commands
python3 FTStack.py 3333 3334 3335 3336 3337
python3 FTStack.py 3334 3333 3335 3336 3337
python3 FTStack.py 3335 3334 3333 3333 3337
python3 FTStack.py 3336 3334 3335 3333 3337
python3 FTStack.py 3337 3334 3335 3336 3333

2. Do any one of the operations to push and pop values.
3. Each terminal represents a server from the cluster
4. To kill a server just close the terminal or use kill -9 command after doing
ps -ef | grep "FTStack.py" and killing the corresponding process ID.

