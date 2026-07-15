# The Dining Philosophers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1226 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Python |
| Official Link | [LeetCode](https://leetcode.com/problems/the-dining-philosophers/) |

## Problem Description

### Goal

Five philosophers sit clockwise around a round table, with one fork between each adjacent pair. Each philosopher alternates between thinking and eating. To eat, a philosopher must hold both the left and right forks, and a fork may be held by only one philosopher at a time. After eating, both forks must be put down so other philosophers can use them.

Assume an unlimited supply of food and continuing demand. Design a concurrent discipline that prevents starvation: every philosopher must be able to continue alternating between thinking and eating without knowing when any other philosopher will request either activity.

Philosophers are identified from `0` through `4` in clockwise order. Implement `wantsToEat`, which receives a philosopher ID and five callbacks. Five threads share one `DiningPhilosophers` instance; the method may even be called again for the same philosopher before an earlier call finishes.

### Function Contract

**Inputs**

- `philosopher`: The requesting philosopher's ID from `0` through `4`.
- `pickLeftFork` and `pickRightFork`: Zero-argument callbacks that record acquiring the corresponding fork.
- `eat`: A zero-argument callback that may be invoked only after both fork-pick callbacks.
- `putLeftFork` and `putRightFork`: Zero-argument callbacks that record releasing the corresponding forks after eating.
- The judge makes each philosopher request food `n` times, where $1\le n\le60$, using concurrent calls on one shared object.

**Return value**

- Nothing. Each invocation must call all five callbacks exactly once in a valid acquire-eat-release order while the shared algorithm avoids deadlock and starvation.

### Examples

**Example 1**

- Input: `n = 1`
- Output: Any valid 25-event interleaving for the five philosophers.

Each philosopher contributes two fork-pick events, one eat event, and two fork-put events. The precise interleaving is scheduler-dependent.

**Example 2**

Two adjacent philosophers may request food simultaneously, but they may not both hold their shared fork or eat without holding both forks.

**Example 3**

Repeated requests from every philosopher must finish without a circular wait, including when calls begin in different thread orders.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Serialize each complete eating transaction.** Store one mutex in the shared `DiningPhilosophers` object. An invocation acquires that mutex before touching either fork and holds it until both forks have been put down. At most one philosopher can therefore be inside the callback sequence at a time.

**Invoke callbacks in physical order.** While holding the mutex, call `pickLeftFork`, then `pickRightFork`, then `eat`, followed by `putRightFork` and `putLeftFork`. Both acquisitions precede eating, and both releases follow it. The `with` scope releases the mutex even if control leaves the block unexpectedly.

**Why circular wait is impossible.** A philosopher never waits for a fork while another philosopher owns the transaction mutex: all other invocations wait before performing their first pick callback. The active invocation acquires both logical forks, eats, releases them, and exits the mutex scope in finite callback work. Thus no cycle of philosophers can each hold one fork while waiting for another. Under the judge's progressing thread scheduler, queued invocations successively enter the finite critical section, so every request completes.

The discipline sacrifices parallel eating by nonadjacent philosophers, but the contract asks for a correct starvation-free discipline rather than maximum concurrency.

#### Complexity detail

There are always five philosophers and five callbacks per invocation. Excluding scheduler-dependent waiting time, an invocation performs $O(1)$ work. The shared object stores one mutex, so its space use is $O(1)$.

#### Alternatives and edge cases

- **One lock per fork plus a four-seat semaphore:** Allowing at most four contenders prevents all five from holding one fork in a cycle and permits nonadjacent parallelism, but it requires more synchronization state.
- **Asymmetric fork order:** Making one philosopher acquire forks in the opposite order breaks circular wait, though starvation and reasoning about repeated concurrent calls require care.
- **Unrestricted left-then-right locking:** All five philosophers may hold their left fork and wait forever for the right, producing the classic deadlock.
- **Callback order:** `eat` must occur after both picks, and neither put callback may occur before eating.
- **Repeated same-philosopher calls:** They are separate transactions and are safely serialized by the shared mutex.
- **Exceptions:** A callback exception is outside the judge's normal contract, but the mutex scope itself is still released.
- **Throughput tradeoff:** Global serialization is intentionally conservative; correctness does not require simultaneous nonadjacent meals.

</details>
