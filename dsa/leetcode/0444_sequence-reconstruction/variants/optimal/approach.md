## General
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

## Complexity detail
Let `V` be the number of values and `E` the number of distinct adjacent constraints. Graph construction and Kahn traversal process each vertex and edge a constant number of times, giving $O(V + E)$ time and $O(V + E)$ space.

## Alternatives and edge cases
- **Verify adjacent target pairs directly:** ensure all subsequence orders agree with `nums` and every adjacent pair in `nums` appears somewhere; this also takes linear time.
- **Enumerate topological orders:** proves uniqueness but can take exponential time.
- **Rescan all vertices for zero indegree:** remains correct but takes $O(V^2 + E)$ time.
- **Repeated edge:** must not increase indegree twice.
- **Missing value:** return `False` even if the remaining constraints are consistent.
- **Cycle:** no zero-indegree choice eventually remains.
