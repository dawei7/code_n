## General

**Model invitations as bipartite matching**

There are two disjoint kinds of vertices: boys and girls. An allowed invitation `grid[i][j] = 1` is an edge from boy $i$ to girl $j$.

A valid accepted-invitation set chooses edges so that no boy and no girl appears more than once. This is exactly a matching in a bipartite graph. The goal is a maximum-cardinality matching.

The protected solution uses the augmenting-path method, often called Kuhn's algorithm.

**Store the current owner of every girl**

Array `match` has one entry per girl:

- `match[j] = -1` means girl $j$ is currently unmatched;
- otherwise `match[j]` is the boy currently matched to her.

The algorithm processes boys one at a time and tries to increase the matching size by one for each.

**Search for an augmenting path**

Helper `find(i)` tries to obtain some girl for boy $i$.

It scans every girl $j$ that boy $i$ can invite. During one outer attempt, set `vis` records girls already considered anywhere in the recursive search. A visited girl is skipped to prevent cycles and repeated work.

When an allowed unvisited girl is found, two cases exist.

If `match[j] == -1`, the girl is free. Assigning her to boy $i$ immediately increases matching size and returns `True`.

If she is occupied by boy `match[j]`, the algorithm recursively asks whether that boy can move to a different girl. If that recursive call succeeds, his old girl becomes available for boy $i$. The assignment `match[j] = i` completes the chain of reassignments.

If no girl can be obtained, `find(i)` returns `False` and the existing matching remains the same size.

**Why reassigning earlier boys is necessary**

A greedy strategy that permanently gives each boy the first free girl can fail. An early boy may take the only girl available to a later boy even though the early boy had another option.

An augmenting path repairs this. It alternates:

- an unmatched edge that a searching boy would like to use;
- a matched edge currently occupying that girl;
- another unmatched option for the displaced boy;
- and so on until a free girl is reached.

Flipping matched/unmatched status along this path preserves all one-invitation limits and increases the total by one.

**Why `vis` is recreated for every boy**

Within one search, revisiting a girl cannot help and could recurse in circles, so she is marked.

For the next outer boy, however, the matching may have changed and a previously explored girl can participate in a different augmenting path. A fresh empty set is therefore created for each boy.

**Following a representative conflict**

Suppose boy 0 can invite girls 0 and 1, while boy 1 can invite only girl 0. If boy 0 initially takes girl 0, boy 1 encounters an occupied girl.

The recursive search for boy 0 discovers girl 1 and moves him there. Girl 0 is then assigned to boy 1. Two invitations are accepted instead of one.

**How the answer is accumulated**

For each boy, the source executes `ans += find(i)`. Python Booleans behave as integers: `True` adds one and `False` adds zero.

Every successful call augments the matching by exactly one, so `ans` remains equal to the number of matched girls.

**Why the final matching is maximum**

Before processing boy $i$, the current matching is maximum for the already processed boys. If `find(i)` finds an augmenting path, flipping it creates a matching larger by one. If it finds none, no matching covering one more processed boy exists from the current matching.

More generally, Berge's augmenting-path characterization states that a matching is maximum exactly when no augmenting path exists. The repeated DFS searches eliminate every possible augmentation involving each added boy. After all boys are processed, no larger matching exists.

## Complexity detail

Let $m$ be the number of boys, $n$ the number of girls, and $E$ the number of one-entries.

There are $m$ outer searches. In one search, each girl enters `vis` at most once, but recursive calls can scan rows of multiple boys. A standard bound is $O(mE)$, which becomes $O(m^2n)$ for a dense $m$ by $n$ grid. This matches the manifest.

`match` uses $O(n)$ space, `vis` uses $O(n)$ per outer attempt, and recursion can contain $O(m)$ boys. Total auxiliary space is $O(m+n)$.

## Alternatives and edge cases

- **Greedy free-girl assignment:** It can miss the optimum because earlier flexible boys may block later constrained boys.
- **Hopcroft-Karp:** It finds batches of shortest augmenting paths in $O(E\sqrt{m+n})$, better for much larger graphs but more complex.
- **Maximum flow:** Source, boy, girl, and sink capacities model the problem correctly, with heavier machinery.
- **Girl with no incoming edges:** She remains unmatched and never affects a DFS.
- **Boy with no allowed invitations:** His row scan returns false immediately.
- **More boys than girls:** The answer cannot exceed $n$.
- **More girls than boys:** The answer cannot exceed $m$.
- **Complete grid:** The answer is $\min(m,n)$.
- **Duplicate path exploration:** `vis` prevents one search from reconsidering a girl.
- **Fresh `vis`:** It allows later boys to use new reassignments through previously examined girls.
- **Recursive reassignment:** Existing matches are changed only after an alternate placement succeeds.
- **Boolean addition:** Each successful augmentation contributes exactly one.
- **Zero-based internal indices:** They represent the problem's ordinal boys and girls without affecting the count.
- **Input preservation:** Only `match` changes; `grid` is read-only.
