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
