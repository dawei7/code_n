## Description

You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each $\text{people}[i] = [h_{i}, k_{i}]$ represents the $$i^{\text{th}}$$person of height$h_{i}$with **exactly**$k_{i}$other people in front who have a height greater than or equal to$h_{i}$.

Reconstruct and return *the queue that is represented by the input array *`people`. The returned queue should be formatted as an array `queue`, where $\text{queue}[j] = [h_{j}, k_{j}]$ is the attributes of the $$j^{\text{th}}$$person in the queue ($\text{queue}[0]$ is the person at the front of the queue).
### Function Contract

**Inputs**

- `people`: An unordered list of `[height,k]` pairs describing all people in the queue.

**Return value**

Return an ordering of the same person occurrences in which each person's preceding count of people at least as tall equals their `k` value.

### Examples
#### Example 1

- **Input:** $people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]$
- **Output:** `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`
- **Explanation:**
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
#### Example 2

- **Input:** $people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]$
- **Output:** `[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]`
### Constraints

- $1 \le \text{people.length} \le 2000$

- $0 \le h_{i} \le 10^{6}$

- $0 \le k_{i} < \text{people.length}$

- It is guaranteed that the queue can be reconstructed.