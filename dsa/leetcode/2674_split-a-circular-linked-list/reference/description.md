## Description

You are given the head of a circular singly linked list of positive length. Its tail points back to the first node rather than to `null`. Split the existing nodes into two circular linked lists while preserving their original order.

The first result must contain the first $\lceil m / 2 \rceil$ nodes of the original list, where $m$ is its length. The second result contains the remaining $\lfloor m / 2 \rfloor$ nodes. Close each half into its own cycle and return their heads in that order.
