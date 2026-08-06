## Description

Design a thread-safe bounded blocking queue with a fixed maximum capacity. A producer adds an integer to the front of the queue, while a consumer removes an integer from the rear. Those opposite endpoints make completed queue operations first in, first out.

An enqueue attempted while the queue is full must block until another thread removes an element. A dequeue attempted while the queue is empty must likewise block until a producer adds an element. Several threads may operate on the same queue simultaneously: every producer invokes only `enqueue`, every consumer invokes only `dequeue`, and `size` is called after each test case.
