## General
**Translate adjacent subsequence values into graph edges**

Create one vertex for every value in `nums`. Each adjacent pair `a, b` in a supplied sequence requires `a` before `b`, so add directed edge `a -> b`. Deduplicate edges before incrementing indegrees, because repeated evidence is one constraint rather than multiple prerequisites.

**Require one available vertex at every topological step**

Initialize a queue with all zero-indegree vertices. For each expected value in `nums`, the queue must contain exactly one vertex; two choices mean the reconstruction is not unique, and zero choices mean a cycle or missing progress. The sole vertex must equal the expected value.

**Release neighbors after accepting the forced value**

Remove the selected vertex, decrement each outgoing neighbor's indegree, and enqueue neighbors that reach zero. This is Kahn's topological algorithm augmented with uniqueness and target-order checks.

**Why all values must appear in the evidence**

Because `nums` contains $n$ distinct values, every value that appears anywhere in `sequences` must occur in every supersequence. If some value of `nums` is never observed, omitting it produces a supersequence shorter than `nums`, so `nums` cannot be a shortest one. Conversely, once all $n$ values are observed, every supersequence needs at least $n$ positions and `nums` already has exactly $n$. The coverage check therefore establishes the shortest-length part of the contract.

**Why the test is necessary and sufficient**

After coverage establishes that a shortest supersequence uses all $n$ values once, its possible orders are exactly the graph's topological orders. If the queue ever has multiple choices, choosing different vertices yields distinct shortest supersequences, so uniqueness fails. If it always has exactly the next value of `nums`, every topological order is forced to take that value at every position. Processing all vertices then proves that `nums` is the unique shortest supersequence.

## Complexity detail
Let `V` be the number of values and `E` the number of distinct adjacent constraints. Graph construction and Kahn traversal process each vertex and edge a constant number of times, giving $O(V + E)$ time and $O(V + E)$ space.

## Alternatives and edge cases
- **Verify adjacent target pairs directly:** ensure all subsequence orders agree with `nums` and every adjacent pair in `nums` appears somewhere; this also takes linear time.
- **Enumerate topological orders:** proves uniqueness but can take exponential time.
- **Rescan all vertices for zero indegree:** remains correct but takes $O(V^2 + E)$ time.
- **Repeated edge:** must not increase indegree twice.
- **Missing value:** return `False` because omitting that unobserved target value gives a shorter supersequence.
- **Single target value:** one singleton evidence row is enough to make the one-value target shortest and unique.
- **Source-domain guarantees:** every row is a subsequence of `nums`, all rows are unique, and every value is in $[1,n]$; reversed target order, cycles, duplicate rows, and out-of-range values are not legal inputs.
