The goal of this assignment is to gain experience with implementing clock
synchronization in distributed systems. Write a simple UDP client/server program,
where the client sends a request to the server and the server sends a reply to the client.
The client records the local clock times (client machine) of when the request is sent and
when the reply is received. The server’s reply contains the local clock time (server
machine) of when the request is received and when the reply is sent. First, run the client
code on machine A and the server code on machine B, and then run the client code on
machine B and the server code on machine A for the following four scenarios:

a) A and B are the same machine
b) A and B are different machines with in the CS department, e.g. two different
CSEL servers
c) A and B are different machines across the CU-Boulder campus
d) A and B are different machines, one in CU campus and the other at a
different geographic location outside the CU campus, preferably on a
different continent

Question 1: Compute roundtrip latencies along with average and standard deviation for
each scenario, and plot them in a graph. Provide an analysis of your results in terms of
why there is a variation in latencies, which ones you expect to be more accurate, etc.

Question 2: Compute the server clock time estimate using the Cristian’s clock
synchronization algorithm, and plot the difference between the local clock and the
estimated server clock values for each scenario. Based on your observations, what is a
reasonable estimate of absolute minimum latency between machine A and machine B.
Using this estimate, calculate the error bounds for the synchronized time.

Question 3: Compute the offset (oi) and delay (di) for each of the measurements for
each scenario using the NTP formula and plot them in a graph (x-axis: measurement #;
y-axis: oi or di). Analyze your results for each scenario in relation to the roundtrip
latencies you computed in Question 1. 