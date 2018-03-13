Raft Reference from https://raft.github.io/.
Learnt Raft basics from The Secret Lives of Data
I used https://github.com/coreos/etcd version for my assignment.
Install GO from https://golang.org/doc/install, since the Raft version I will be using is written in GOLang.
git clone https://github.com/coreos/etcd.git.
cd etcd


// Set the Paths
add export GOPATH=$HOME/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin" to ./bash_profile.

.go build // To install Go

./build

// To start etcd

./bin/etcd

// To use version3 of ETCD by default

export ETCDCTL_API=3

// Storing and retrieving data from the Distributed RAFT system

etcdctl put mykey ”this is awesome”
etcdctl get mykey

// Starting a cluster of servers.
I used goreman library to achive this

goreman -f Procfile start

// List out the current cluster members

etcdctl --write-out=table --endpoints=localhost:2379 member list

// Kill a member from the cluster

goreman run stop etcd2 

// Retrieve the value from the cluster.
// Since our is a fault tolerant system, we will still be able to retrieve the key even if one process fails.

etcdctl get mykey

// Getting value from the killed server - We get an error

etcdctl --endpoints=localhost:22379 get key

// Restart the killed server

goreman run restart etcd2 

// We will be able to retrieve the value after restarting the server
// This is because of the RAFT consensus, wherien the servers exchange messages

etcdctl --endpoints=localhost:22379 get key 

