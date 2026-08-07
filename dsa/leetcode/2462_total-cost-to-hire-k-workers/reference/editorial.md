[TOC]

## Solution

---

### Approach 1: 2 Priority Queues

#### Intuition

> If you are not familiar with the priority queue, please refer to our explore cards [Heaps Explore Card](https://leetcode.com/explore/featured/card/graph/619/depth-first-search-in-graph/). We will focus on the usage in this article and not the implementation details.

**For the sake of brevity, let `m` represent the input integer `candidates` for the rest of the article.**

To begin with, we need to understand the problem requirements. In each of the `k` hiring rounds, we must hire a worker with the lowest cost (with the smallest index being a tiebreaker) based on the provided rules.

We have the option to select the worker with the lowest cost from either the first `m` candidates or the last `m` candidates from `costs`. Once we choose a worker from either of these sections, we remove the chosen worker from the array, which makes space for another worker to be in either the first or last `m` candidates. We continue to select the worker with the lowest cost, each time making space for another worker from `costs` to be into consideration. Because we need to repeatedly find the minimum cost, using a priority queue is the most appropriate approach to simulate this process.

<br>

During each hiring session, our goal is to select the worker with the lowest cost. As mentioned above, after selecting a worker, a spot will open up for another worker to be among the first or last `m` candidates. As such, we need to distinguish between the first `m` candidates and the last `m` candidates. That way, when we choose a worker, we know if a spot was opened in the first `m` candidates or the last `m` candidates.

![img](images/1.png)

To store the workers in two sections separately, we can use two priority queues, $\text{head}_{workers}$ and $\text{tail}_{workers}$, where the worker with the lowest cost has the highest priority.

![img](images/2.png)

Throughout the process, after we hire a worker from a section, we need to add an additional candidate to this section. Therefore, we need two pointers, $\text{next}_{head}$ and $\text{next}_{tail}$, that denotes the next worker to be added to the respective queues.

![img](images/3.png)

Just like in this situation shown in the picture, if two workers with the same cost appear at the top of both queues, we will hire the one from $\text{head}_{workers}$, since this worker has a smaller index compared with the other one from $\text{tail}_{workers}$. Afterwards, we need to refill $\text{head}_{workers}$ with the worker at $\text{next}_{head}$ to ensure that it still contains the first `m` unselected candidates.

![img](images/4.png)

We add the worker $costs[\text{next}_{head}]$ to $\text{head}_{workers}$, and then increment this pointer by 1, indicating the next unselected worker.

![img](images/5.png)

However, if we encounter the condition $\text{next}_{tail} < \text{next}_{head}$, it indicates that all the workers have been selected as candidates and there are no more workers outside the two queues. To avoid double counting, we should not add a worker to both queues or update either pointer. Therefore, we can simply move on without making any updates to the queues or pointers.

![img](images/6.png)

<br>

#### Algorithm

1) Initialize two priority queues $\text{head}_{workers}$ and $\text{tail}_{workers}$ that store the first `m` workers and the last `m` workers, where the worker with the lowest cost has the highest priority.

2) Set up two pointers $\text{next}_{head} = m$, $\text{next}_{tail} = n - m - 1$ indicating the next worker to be added to two queues.

3) Compare the top workers in both queues, and hire the one with the lowest cost, if both workers have the same cost, hire the worker from $\text{head}_{workers}$. Add the cost of this worker to the total cost.

4) If $\text{next}_{head} \le \text{next}_{tail}$, we need to fill the queue with one worker:

- If the hired worker is from $\text{head}_{workers}$, we add the worker $costs[\text{next}_{head}]$ to it and increment $\text{next}_{head}$ by 1.
- If the hired worker is from $\text{tail}_{workers}$, we add the worker $costs[\text{tail}_{head}]$ to it and decrement $\text{tail}_{head}$ by 1.

    Otherwise, skip this step.

5) Repeat steps 3 and 4 `k` times.

6) Return the total cost of all the hired workers.

#### Implementation

```python
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # head_workers stores the first k workers.
        # tail_workers stores at most last k workers without any workers from the first k workers.
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapify(head_workers)
        heapify(tail_workers)

        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                answer += heappop(head_workers)

                # Only refill the queue if there are workers outside the two queues.
                if next_head <= next_tail:
                    heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                answer += heappop(tail_workers)

                # Only refill the queue if there are workers outside the two queues.
                if next_head <= next_tail:
                    heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return answer
```

#### Complexity Analysis

Let $m$ be the given integer `candidates`.

* Time complexity: $O((k + m) \cdot\log m)$

- We need to initialize two priority queues of size $m$, which takes $O(m \cdot\log m)$ time.
- During the hiring rounds, we keep removing the top element from priority queues and adding new elements for up to $k$ times. Operations on a priority queue take amortized $O(\log m)$ time. Thus this process takes $O(k \cdot\log m)$ time.
- Note: in Python, `heapq.heapify()` creates the priority queue in linear time. Therefore, in Python, the time complexity is $O(m + k \cdot \log m)$.

* Space complexity: $O(m)$

- We need to store the first $m$ and the last $m$ workers in two priority queues.

<br/>

---

### Approach 2: 1 Priority Queue

#### Intuition

We can also implement the hiring process using a single priority queue. However, if we only store the costs of the candidates as before, we cannot sort them based on their index. To address this, we can add a new field to each worker to denote their section ID. For instance, we can assign `0` to the first `m` candidates and `1` to the last `m` candidates. This way, when two workers have the same cost, the priority queue can sort them based on their section IDs, and the worker with the smaller section ID will be hired. This approach fully meets the requirements given in the problem.

As illustrated in the following picture, we store each candidate in `pq`, in the format of `(cost, section ID)`. For example:
- $\text{costs}[1] = 12$ is from the head section and stored as `(12, 0)`.

- $\text{costs}[9] = 2$ is from the tail section and stored as `(2, 1)`.

![img](images/7.png)

We will proceed with the hiring process for `k` rounds by hiring the top worker from `pq` each time.

Similar to the previous solution:
> If we choose a worker from $\text{head}_{workers}$, we add the worker at $\text{next}_{head}$ to $\text{head}_{workers}$.
> If we choose a worker from $\text{tail}_{workers}$, we add the worker at $\text{next}_{tail}$ to $\text{tail}_{workers}$.

Here, we check whether the hired worker is from the first `m` candidates or the last `m` candidates by checking his section ID.
> If the section ID is `0`, it means that the worker is from the first `m` candidates, we add the worker at $\text{next}_{head}$ to `pq` with a section ID as `0`.
> If the section ID is `1`, it means that the worker is from the last `m` candidates, we add the worker at $\text{next}_{tail}$ to `pq` with a section ID as `1`.

![img](images/8.png)

<br>

#### Algorithm

1) Create a priority queue `pq` and initialize it with the first `m` workers and last `m` workers from `costs`, along with their section IDs (0 for the first `m` workers, and 1 for the last `m` workers). The worker with the lowest cost has the highest priority.

2) Initialize two pointers $\text{next}_{head} = m$ and $\text{next}_{tail} = n - m - 1$, indicating the next worker to be added to `pq`.

3) Pop the top worker with the lowest cost from `pq` and add the cost of this hired worker to the total cost.

4) If $\text{next}_{head} \ge \text{next}_{tail}$, we need to fill `pq` with the next worker:
- If the hired worker's section ID is `0`, we push the worker $costs[\text{next}_{head}]$ to into `pq` and increment $\text{next}_{head}$ by 1.
- If the hired worker's section ID is `1`, we push the worker $costs[\text{next}_{tail}]$ to into `pq` and decrement $\text{next}_{tail}$ by 1.

    Otherwise, skip this step.

5) Repeat steps 3 and 4 `k` times.

6) Return the total cost of all the hired workers.

#### Implementation

```python
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Add the first k workers with section id of 0 and
        # the last k workers with section id of 1 (without duplication) to pq.
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))

        heapify(pq)

        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        # Only refill pq if there are workers outside.
        for _ in range(k):
            cur_cost, cur_section_id = heappop(pq)
            answer += cur_cost
            if next_head <= next_tail:
                if cur_section_id == 0:
                    heappush(pq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heappush(pq, (costs[next_tail], 1))
                    next_tail -= 1

        return answer
```

#### Complexity Analysis

For the sake of brevity, let $m$ be the given integer `candidates`.

* Time complexity: $O((k + m) \cdot\log m)$

- We need to initialize one priority queue `pq` of size up to $2\cdot m$, which takes $O(m \cdot\log m)$ time.
- During `k` hiring rounds, we keep popping top elements from `pq` and pushing new elements into `pq` for up to $k$ times. Operations on a priority queue take amortized $O(\log m)$ time. Thus this process takes $O(k \cdot\log m)$ time.
- Note: in Python, `heapq.heapify()` creates the priority queue in linear time. Therefore, in Python, the time complexity is $O(m + k \cdot \log m)$.

* Space complexity: $O(m)$

- We need to store at most $2 \cdot m$ elements (the first $m$ and the last $m$ elements) of `costs` in the priority queue `pq`.

<br/>