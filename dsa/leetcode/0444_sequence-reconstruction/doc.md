# Sequence Reconstruction

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 444 |
| Difficulty | Medium |
| Topics | Array, Graph Theory, Topological Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/sequence-reconstruction/) |

## Problem Description
### Goal
Given a proposed sequence `nums` and a collection of subsequences, each subsequence imposes relative-order constraints on its listed values. Determine whether those constraints represent every required value and force one complete ordering.

Return `True` only when `nums` is the unique sequence satisfying all imposed precedences. If another topological ordering is possible, a constraint contradicts `nums`, a cycle exists, or a required value is never represented, return `False`. Individual subsequences need not be contiguous portions of `nums`, but their values must appear in the same relative order. Do not accept uniqueness of only a partial represented set.

### Function Contract
**Inputs**

- `nums`: the proposed permutation to reconstruct
- `sequences`: subsequences whose relative orders impose precedence constraints

**Return value**

- Return `True` exactly when every value is represented and `nums` is the unique topological order satisfying all subsequences.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], sequences = [[1, 2], [1, 3]]`
- Output: `False`

**Example 2**

- Input: `nums = [1, 2, 3], sequences = [[1, 2], [1, 3], [2, 3]]`
- Output: `True`

**Example 3**

- Input: `nums = [1], sequences = [[1]]`
- Output: `True`

### Required Complexity

- **Time:** $O(V + E)$
- **Space:** $O(V + E)$

<details>
<summary>Approach</summary>

#### General

**Translate adjacent subsequence values into graph edges**

Create one vertex for every value in `nums`. Each adjacent pair `a, b` in a supplied sequence requires `a` before `b`, so add directed edge `a -> b`. Deduplicate edges before incrementing indegrees, because repeated evidence is one constraint rather than multiple prerequisites.

**Require one available vertex at every topological step**

Initialize a queue with all zero-indegree vertices. For each expected value in `nums`, the queue must contain exactly one vertex; two choices mean the reconstruction is not unique, and zero choices mean a cycle or missing progress. The sole vertex must equal the expected value.

**Release neighbors after accepting the forced value**

Remove the selected vertex, decrement each outgoing neighbor's indegree, and enqueue neighbors that reach zero. This is Kahn's topological algorithm augmented with uniqueness and target-order checks.

**Why all values must appear in the evidence**

A value absent from every supplied sequence is not actually constrained by the evidence, even if graph initialization gives it a vertex. Track observed values and require all of `nums` to appear; otherwise the proposed reconstruction is not established by the subsequences.

**Why the test is necessary and sufficient**

If the queue ever has multiple choices, choosing different vertices yields distinct valid topological prefixes, so uniqueness fails. If it always has exactly the next value of `nums`, every topological order is forced to take that value at every position. Processing all vertices then proves `nums` is both valid and unique.

#### Complexity detail

Let `V` be the number of values and `E` the number of distinct adjacent constraints. Graph construction and Kahn traversal process each vertex and edge a constant number of times, giving $O(V + E)$ time and $O(V + E)$ space.

#### Alternatives and edge cases

- **Verify adjacent target pairs directly:** ensure all subsequence orders agree with `nums` and every adjacent pair in `nums` appears somewhere; this also takes linear time.
- **Enumerate topological orders:** proves uniqueness but can take exponential time.
- **Rescan all vertices for zero indegree:** remains correct but takes $O(V^2 + E)$ time.
- **Repeated edge:** must not increase indegree twice.
- **Missing value:** return `False` even if the remaining constraints are consistent.
- **Cycle:** no zero-indegree choice eventually remains.

</details>
