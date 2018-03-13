			Fault Tolerant System using Raft

1.	Raft reference  from https://raft.github.io/.
2.	Learnt Raft basics from The Secret Lives of Data
3.	Will be using https://github.com/coreos/etcd implementation for my assignment.
4.	Installed Go from https://golang.org/doc/install, since the Raft version I will be using is written in Go.
5.	git clone https://github.com/coreos/etcd.git.
6.	cd etcd
7.	add export GOPATH=$HOME/go
    export PATH=$PATH:$GOROOT/bin:$GOPATH/bin" to ./bash_profile.
	1.	8.	.go build
	2.	9.	./build
	3.	10.	Starting etcd ./bin/etcd.  (https://github.com/coreos/etcd/blob/master/Documentation/dl_build.md)
	4.	11.	Simple commands with etcd.
	5.	ETCDCTL_API=3 etcdctl put mykey ”this is awesome”
	6.	ETCDCTL_API=3 etcdctl get mykey
	7.	12. Playing with the cluster to test the FTStack
	8.	$ export ETCDCTL_API=3
	9.	  $ ./etcdctl put foo bar
	10.	./etcdctl get foo
	11.	goreman -f Procfile start // Start the cluster
	12.	etcdctl --write-out=table --endpoints=localhost:2379 member list.  // List out the corrent cluster members
	13.	goreman run stop etcd2 // Kill a member from the cluster
	14.	etcdctl --endpoints=localhost:22379 get key // Get the value from the killed process
	15.	 goreman run restart etcd2 // Restart the killed proc
	16.	etcdctl --endpoints=localhost:22379 get key // Get the key after restarting the killed process.
