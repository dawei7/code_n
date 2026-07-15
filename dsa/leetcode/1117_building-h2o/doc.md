# Building H2O

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1117 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| LeetCode | [Open problem](https://leetcode.com/problems/building-h2o/) |

## Problem Description

### Goal

Hydrogen and oxygen threads arrive asynchronously at a shared `H2O` object. A hydrogen thread calls `hydrogen(releaseHydrogen)`, whose callback emits `"H"`; an oxygen thread calls `oxygen(releaseOxygen)`, whose callback emits `"O"`.

Release threads in complete water-molecule groups. Every consecutive group of three emitted markers must contain exactly two `"H"` values and one `"O"`, in any internal order. All three callbacks belonging to one molecule must finish before callbacks from the next molecule begin. An oxygen arriving alone waits for two hydrogens, and a hydrogen arriving alone waits for another hydrogen and one oxygen.

### Function Contract

**Inputs**

- `releaseHydrogen` and `releaseOxygen`: zero-argument callbacks executed by atom threads sharing one `H2O` instance.
- The arrival string has length $3m$, contains exactly $2m$ hydrogen threads and $m$ oxygen threads, and $1 \le m \le 20$.

**Return value**

- Methods return `None`; each consecutive three callback markers must be a permutation of `"HHO"`, with no molecule groups overlapping.

### Examples

**Example 1**

- Input: `water = "HOH"`
- Valid outputs: `"HHO"`, `"HOH"`, or `"OHH"`

**Example 2**

- Input: `water = "OOHHHH"`
- One valid output: `"HHOHHO"`

Other outputs are valid when both consecutive three-character blocks contain two hydrogens and one oxygen.

### Required Complexity

- **Time:** $O(m)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reserve exactly one molecule's atom permits:** Initialize a hydrogen semaphore with two permits and an oxygen semaphore with one. A thread acquires its element's permit before joining a molecule, so no generation can contain a third hydrogen or second oxygen.

**Wait for a complete three-party group:** After acquiring a permit, every thread waits at one reusable barrier with three parties. No callback runs until two hydrogen threads and one oxygen thread have all arrived, because those are the only threads able to hold the three available permits.

**Release permits only after bonding:** Once the barrier opens, each thread invokes its callback and then releases its permit. A later generation cannot acquire all two hydrogen permits and the oxygen permit until all three callbacks from the current generation have returned. Therefore no next-generation barrier can open early. Each emitted block is a complete `HHO` multiset, and generations cannot overlap.

#### Complexity detail

For $m$ molecules, $3m$ threads each perform constant semaphore, barrier, and callback work, giving $O(m)$ total work. The fixed semaphores and one three-party reusable barrier use $O(1)$ shared state. Blocking duration depends on arrivals but adds no polling iterations.

#### Alternatives and edge cases

- **Condition variable with waiting counts:** It can admit two hydrogens and one oxygen per generation but requires careful generation state and wake-up predicates.
- **Semaphores without a barrier:** Capacity alone limits simultaneous element counts but may let callbacks run before a complete molecule has arrived.
- **Barrier without element permits:** Any three threads could pass, including three hydrogens, violating the required ratio.
- **Release permits before callbacks finish:** That can allow the next molecule to begin bonding before the current one completes.
- **Oxygen arrives first:** It holds the oxygen permit and waits at the barrier until two hydrogens arrive.
- **Many hydrogens arrive first:** Only two reach the barrier; all others block on the hydrogen semaphore.
- **Internal output order:** `HHO`, `HOH`, and `OHH` are equally valid for one molecule.

</details>
