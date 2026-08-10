## General

**Turn richer observations into directed reachability**

For pair `[a,b]`, person `a` is richer than person `b`. To answer for `b`, we need to search people known to have at least as much money as `b`. Therefore, the graph stores edge:

`b -> a`.

`g[b]` lists people directly known to be richer than `b`. Following several edges reaches people definitely richer through transitivity.

The observations are logically consistent, so this directed relation has no cycle implying someone is richer than themself.

**State meaning**

`ans[i]` is the person with minimum quiet value among:

- person `i` themself;
- everyone reachable from `i` by one or more richer edges.

It begins at `-1` to mean “not computed.”

**Include the person themself**

When computing node `i`, DFS first sets `ans[i] = i`. The contract asks for someone with equal or more money, so `i` is always an eligible baseline.

This assignment also marks the state as started/computed before exploring richer neighbors.

**Combine answers from richer neighbors**

For every directly richer person `j` in `g[i]`:

1. recursively compute `ans[j]`;
2. compare `quiet[ans[j]]` with `quiet[ans[i]]`;
3. keep `ans[j]` if it is quieter.

Why can one representative `ans[j]` stand for all people reachable through `j`? By definition, it is already the quietest person in that entire richer region. No other person through `j` can beat it.

Taking the minimum across `i` and every direct richer neighbor's precomputed region covers all people equal to or definitely richer than `i`.

**Memoization avoids repeated graph searches**

If `ans[i] != -1`, DFS returns immediately. Many poorer people may reach the same rich person, but that person's quietest richer representative is computed only once.

Without memoization, overlapping reachability regions could be traversed repeatedly, causing much more work.

**Trace one chain**

Suppose observations establish `5 > 3 > 1 > 0` in wealth. DFS for person 0 calls 1, then 3, then 5.

- Person 5 starts with itself and, if no richer neighbor improves it, returns 5.
- Person 3 compares itself with `ans[5]`.
- Person 1 compares itself with the best result for 3.
- Person 0 compares itself with the best result for 1.

Thus, person 5 can become `ans[0]` even though no direct pair `[5,0]` was supplied. Transitive wealth certainty is handled by reachability.

**Branching wealth relations**

If `i` has two richer neighbors whose reachable regions differ, DFS computes the quietest representative of each branch. Comparing both is sufficient.

A person reachable through several branches may be reconsidered as a neighbor reference, but its memoized answer returns immediately. Unique quiet values guarantee there is one unambiguous minimum.

**Why calling DFS for every person is necessary**

Some person may not be reachable from any poorer node processed earlier. The outer loop calls `dfs(i)` for all labels, ensuring every answer entry is filled.

Earlier recursive calls often compute later entries in advance, and memoization makes those outer calls immediate.

**Why the recurrence is correct**

Consider nodes in an order from richest regions downward. A person with no richer outgoing neighbor has only themself in the eligible set, so initializing to self is correct.

For a general person `i`, every eligible richer person is either `i` or lies in the reachable region of one direct richer neighbor `j`. By induction, `ans[j]` is the quietest in that region. Taking the quietest among those representatives and `i` gives exactly the quietest over the union.

The logical-consistency guarantee makes the dependency graph acyclic, so recursion reaches base nodes and the induction is valid.

## Complexity detail

Let `n` be the number of people and `m = len(richer)`.

Building the adjacency list takes `O(m)` time and space. Memoization causes each person to perform its neighbor loop once. Across all people, those loops examine every directed observation once, so DFS time is `O(n+m)`.

The adjacency list uses `O(n+m)` space, while `ans` and recursion state use `O(n)`. Total space is `O(n+m)`.

In the worst case, recursive depth can be `O(n)` along a wealth chain.

## Alternatives and edge cases

- **Topological propagation:** Process people from richer to poorer while propagating quietest representatives. It is iterative and has the same linear complexity.

- **DFS separately without caching:** It may revisit the same richer region for many people and become quadratic or worse.

- **Reverse edge direction:** Storing richer-to-poorer edges is useful for propagation, but this exact DFS needs poorer-to-richer edges to answer one person's query.

- **No richer observations:** Every adjacency list is empty, so each person answers themself.

- **One person:** The result is `[0]`.

- **Direct richer person is louder:** The current answer remains unchanged, though someone farther above that neighbor may still be quieter.

- **Quietest person reached transitively:** Recursive neighbor answers carry that person down the chain.

- **Multiple richer paths to one person:** Memoization prevents recomputing their result.

- **Unique quiet values:** Strict comparison always selects a unique quieter person; ties need no rule.

- **Equal wealth eligibility:** The person themself is included through the initial assignment.

- **Logical consistency:** The code relies on absence of richer-than cycles; it does not maintain a separate active-recursion marker.

- **Input immutability:** A new adjacency list and answer array are created.
