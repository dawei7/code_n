## General

**Turn the manager array into a downward tree**

The input tells us, for each employee `i`, who `manager[i]` is. That representation points upward from a subordinate to a manager. The news travels in the opposite direction, from each manager to all direct subordinates, so the solution first builds an adjacency list `g` that points downward.

For every pair produced by `enumerate(manager)`, the statement `g[x].append(i)` places employee `i` in manager `x`'s subordinate list. After this pass, `g[i]` contains exactly the employees whom employee `i` informs directly. The head's manager value is $-1$, so the construction also creates an unused `g[-1]` entry containing the head. This is harmless because the traversal begins explicitly at `headID` and never visits the artificial key $-1$.

The company hierarchy is guaranteed to be a tree. Therefore every non-head employee has one parent, all employees are reachable from the head, and following subordinate edges cannot form a cycle. A visited set is unnecessary.

**What `dfs(i)` means**

The most important step is to give the recursive return value a precise meaning:

> `dfs(i)` is the additional number of minutes needed to inform everyone in employee `i`'s subtree, assuming employee `i` knows the news now.

This definition makes leaves simple. An employee with no subordinates has nobody else to inform, so the loop over `g[i]` is empty and the helper returns its initial `ans = 0`.

For a manager `i` with a direct subordinate `j`, the subordinate cannot begin spreading the news until `informTime[i]` minutes have passed. After that moment, informing everyone below `j` takes `dfs(j)` additional minutes. The total completion time through this one branch is therefore

`dfs(j) + informTime[i]`.

**Why the branch times use a maximum, not a sum**

Employee `i` informs all direct subordinates simultaneously. If one child branch finishes after five minutes and another after eight, the entire subtree is finished after eight minutes, not thirteen. The branches run in parallel once the manager finishes its own informing delay.

The helper consequently updates

`ans = max(ans, dfs(j) + informTime[i])`

for every direct subordinate. At the end, `ans` is the duration of the slowest subordinate branch, which is exactly when the last employee in this subtree learns the news.

Notice that `informTime[i]` appears once in every candidate branch, but it is not added after taking the maximum in the exact code. The two forms are mathematically equivalent when there is at least one child:

$$
\max_j\bigl(\text{dfs}(j)+\text{informTime}[i]\bigr)
=
\text{informTime}[i]+\max_j\text{dfs}(j).
$$

Keeping the addition inside the loop also handles the leaf naturally: a leaf returns zero rather than unnecessarily adding its guaranteed zero informing time.

**A small chain and a branching example**

Suppose the head takes two minutes to inform manager A, and A takes three minutes to inform a leaf. The leaf returns zero. A returns $0+3=3$, and the head returns $3+2=5$. These delays lie on one root-to-leaf chain, so they add.

Now suppose the head has two manager subtrees that need three and seven additional minutes after receiving the news. Both receive it after the head's same two-minute delay. Their completion times are five and nine, so the head returns nine. This illustrates the complete rule: add times along a chain, but take the maximum across sibling branches.

**Why starting at the head gives the global answer**

The head knows the news at time zero. By the meaning of the helper, `dfs(headID)` is the additional time from that moment until everyone in the head's subtree is informed. The head's subtree is the entire company, so the returned number is the requested total.

The parameter `n` is not needed after the arrays are supplied; their enumeration already covers all employees. Its presence is part of the required function signature.

**Why the recursion is correct**

Use induction on subtree height. A leaf has height zero, contains no uninformed descendants, and `dfs` correctly returns zero. Assume every subordinate call correctly returns that subordinate subtree's remaining time. For each child `j`, the manager delay plus `dfs(j)` is then the exact completion time of that branch. All child branches begin together, so the entire current subtree completes when the slowest exact branch completes. Taking their maximum is therefore correct.

By induction, the helper is correct for every employee, including the head. The algorithm examines every management edge and cannot omit any employee because the hierarchy is a connected tree rooted at `headID`.

## Complexity detail

Let $n$ be the number of employees. Building `g` reads all $n$ manager entries once. DFS visits each employee once and iterates over each manager-to-subordinate edge once. A tree has $n-1$ real hierarchy edges, so total time is $O(n)$.

The adjacency lists store $O(n)$ employee IDs, and recursive calls can use up to $O(h)$ stack frames for hierarchy height $h$. Thus space is $O(n+h)=O(n)$, matching the manifest. On a balanced hierarchy the stack is much smaller, but the adjacency list still remains linear.

## Alternatives and edge cases

- **Top-down DFS:** Carry the absolute time at which each employee learns the news and keep the maximum. It is equally linear; the exact solution instead returns the longest remaining duration bottom-up.
- **Breadth-first search:** Queue each employee with its receive time. This avoids recursive calls and is useful for extremely deep hierarchies, while retaining $O(n)$ time and space.
- **Follow manager pointers upward:** Memoize the receive time of each employee using the original array. It avoids building child lists but needs careful caching and cycle-independent reasoning.
- **Single employee:** The head has no subordinate, so `dfs` returns zero.
- **Several direct reports:** Their notification periods run concurrently, which is why only the largest branch time matters.
- **Zero informing time:** Children can begin immediately; adding zero preserves their subtree duration.
- **Deep chain:** Every delay lies sequentially on the only path, so recursion adds all manager times along that chain.
- **Head's $-1$ manager:** The adjacency construction creates an unused key $-1$; traversal still starts at `headID`, so no fake edge is followed.
- **Leaf guarantee:** `informTime[i]` is zero for leaves, but the code would still return zero because it never evaluates a child candidate.
- **No visited set:** This is safe only because the manager relationships form a rooted tree with one parent per non-head employee.
- **Recursion depth:** A chain of up to 100,000 employees can exceed Python's normal recursion limit; iterative BFS or DFS is safer operationally.
- **Required imports:** `defaultdict` must be available, normally from `collections`.
