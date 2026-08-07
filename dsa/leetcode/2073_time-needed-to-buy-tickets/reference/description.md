## Description

There are `n` people in a line queuing to buy tickets, where the $0^th$ person is at the **front** of the line and the $(n - 1)^th$ person is at the **back** of the line.

You are given a **0-indexed** integer array `tickets` of length `n` where the number of tickets that the $$i^{\text{th}}$$person would like to buy is$\text{tickets}[i]$.

Each person takes **exactly 1 second** to buy a ticket. A person can only buy **1 ticket at a time** and has to go back to **the end** of the line (which happens **instantaneously**) in order to buy more tickets. If a person does not have any tickets left to buy, the person will **leave **the line.

Return the **time taken** for the person **initially** at position **k**** **(0-indexed) to finish buying tickets.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** tickets = [2,3,2], k = 2

**Output:** 6

**Explanation:**

- The queue starts as [2,3,<u>2</u>], where the kth person is underlined.

- After the person at the front has bought a ticket, the queue becomes [3,<u>2</u>,1] at 1 second.

- Continuing this process, the queue becomes [<u>2</u>,1,2] at 2 seconds.

- Continuing this process, the queue becomes [1,2,<u>1</u>] at 3 seconds.

- Continuing this process, the queue becomes [2,<u>1</u>] at 4 seconds. Note: the person at the front left the queue.

- Continuing this process, the queue becomes [<u>1</u>,1] at 5 seconds.

- Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

</div>
#### Example 2

<div class="example-block">
**Input:** tickets = [5,1,1,1], k = 0

**Output:** 8

**Explanation:**

- The queue starts as [<u>5</u>,1,1,1], where the kth person is underlined.

- After the person at the front has bought a ticket, the queue becomes [1,1,1,<u>4</u>] at 1 second.

- Continuing this process for 3 seconds, the queue becomes [<u>4]</u> at 4 seconds.

- Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8.

</div>
### Constraints

- $n = \text{tickets.length}$

- $1 \le n \le 100$

- $1 \le \text{tickets}[i] \le 100$

- $0 \le k < n$