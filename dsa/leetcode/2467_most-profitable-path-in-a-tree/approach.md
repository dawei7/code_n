## General

**Bob's path is fixed; Alice's path is the choice**

The tree is rooted at node 0. Bob always moves toward the root, so his route is the unique simple path from `bob` to 0. Alice may choose any root-to-leaf path.

The solution first records Bob's arrival time on his fixed path, leaving all other nodes with a sentinel time. It then explores every Alice path and calculates how much she receives at each node based on relative arrival time.

**Build the undirected tree**

The adjacency list `g` stores both directions of every edge. Parent parameters in both recursive traversals prevent walking backward and revisiting nodes.

The time list `ts` starts with value `n` at every node. Any real arrival time in an $n$-node tree is at most $n-1$, so this sentinel means Bob never visits the node and is later than Alice for every possible Alice arrival.

**First DFS: find Bob's unique route**

`dfs1(i,fa,t)` searches from Bob toward node 0. When it reaches 0, it records the current time and returns true.

For each neighbor other than the parent, it recurses with time `t+1`. If that branch finds the root, the function records `ts[j]=t+1` for the child `j` lying on the successful route and returns true without exploring other branches.

During unwinding, this records arrival times for nodes from rootward child through Bob's path. The outer assignment `ts[bob]=0` explicitly records Bob's starting node, which is not set by a parent's unwind.

Nodes outside the unique successful branch remain at sentinel `n`.

**Second DFS: calculate Alice's gain**

`dfs2(i,fa,t,v)` visits node `i` at Alice time `t` with income `v` accumulated before opening this node's gate.

- If `t == ts[i]`, both arrive simultaneously and Alice adds `amount[i]//2`.
- If `t < ts[i]`, Alice arrives first and adds the full amount.
- If `t > ts[i]`, Bob opened the gate earlier, so Alice adds nothing.

This logic applies equally to rewards and costs. A negative amount added fully means Alice pays the cost. Half of an even negative amount is exact with integer division. If Bob arrived earlier, Alice avoids both payment and reward because the gate is already open.

**Recognize Alice's leaf endpoints**

A non-root node is a leaf when its only adjacency is its parent. The condition

`len(g[i]) == 1 and g[i][0] == fa`

detects exactly that case. The root has no parent `-1` and is not incorrectly considered a leaf when its degree is one.

At a leaf, the complete path income competes with global `ans`. Initializing `ans=-inf` is necessary because every available root-to-leaf path may have negative income.

**Why every path value is computed correctly**

The first DFS assigns exact Bob times on his unique path and an effectively infinite time elsewhere. The second DFS increments Alice time by one per edge, so each relative-time comparison matches the game.

The accumulated value passed to a child contains exactly Alice's contribution from all nodes above it. Each node's gate contribution is added once according to who arrives first. At every leaf, `v` is therefore the net income for that root-to-leaf choice.

Tree traversal visits every possible leaf path through shared prefixes without recomputing those prefix decisions. Taking the maximum over leaf totals gives Alice's optimal choice.

For the first sample, Bob times are 0 at node 3, 1 at node 1, and 2 at node 0. Alice reaches node 0 first, node 1 simultaneously, and node 3 after Bob. Continuing to node 4 adds its full reward, producing total 6.

**Recursion-depth limitation**

Both DFS functions can recurse through a path-shaped tree of length $n=100000$. This can exceed Python's normal recursion limit. The algorithm is linear and mathematically correct, but iterative parent/path discovery and stack traversal would be safer at maximum depth.

## Complexity detail

Building adjacency takes $O(n)$ time. `dfs1` may explore branches while searching but, with parent avoidance and immediate successful return, visits each node at most once in the worst case. `dfs2` visits every node once. Total time is $O(n)$.

The adjacency list, Bob-time array, and traversal state use $O(n)$ storage. Recursive call stacks may also reach $O(n)$ on a skewed tree. Overall auxiliary space is $O(n)$.

The answer may sum up to $n\cdot10^4$ in magnitude, within 32-bit signed range at $n=10^5$ only near the boundary; using a wider accumulator is prudent outside Python.

## Alternatives and edge cases

- **Parent array for Bob:** Traverse once from root to record parents, then walk from Bob to root setting times. This is simpler and avoids the Boolean path-search unwind.
- **Iterative Alice traversal:** Use a stack carrying node, parent, time, and income to eliminate recursion risk.
- **Modify amounts on Bob's path:** Zero nodes Bob reaches first and halve the simultaneous node, then find the maximum root-to-leaf sum. It is an equivalent two-phase view.
- **Bob never visits a node:** Sentinel time ensures Alice receives its full amount.
- **Simultaneous negative cost:** Alice pays exactly half because amounts are guaranteed even.
- **Bob reaches first:** Alice receives and pays nothing at the already opened gate.
- **All paths negative:** `-inf` initialization still selects the least harmful valid leaf path.
- **Root degree one:** It is not an Alice leaf because the path must continue to its child.
- **Bob starts next to root:** His time map contains zero at Bob and one at root.
- **Deep tree:** Recursive implementation may raise `RecursionError` despite linear asymptotic complexity.
