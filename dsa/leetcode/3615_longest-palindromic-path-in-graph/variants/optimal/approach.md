## General

Because each node may be visited at most once, a state must remember which nodes are already used. The constraint `n <= 14` makes a bitmask feasible.

The source builds palindromic paths from their center outward. A palindrome remains a palindrome when the same character is added to both ends. This gives a complete transition rule: extend the left endpoint to an unused neighbor, extend the right endpoint to a different unused neighbor with the same label, and add both nodes to the mask.

**Special shortcut for a complete graph**

A simple undirected graph on `n` nodes has `n(n-1)/2` possible edges. The constraints exclude duplicates, so when `len(edges)` equals this number, every pair of nodes is adjacent.

In a complete graph, any ordering of distinct nodes is a valid path. The graph restriction disappears, leaving only the task of arranging the multiset of labels as a palindrome.

A palindrome may have at most one character with an odd frequency. If `odd_counts` labels have odd counts, one odd count may occupy the center and one node must be discarded from every other odd group. Hence the maximum usable length is:

`n - max(0, odd_counts - 1)`.

The `Counter` shortcut returns this value without exponential search.

**Bitmask adjacency and label masks**

For a non-complete graph, `adjacency[u]` is an integer whose bit `v` is 1 exactly when edge `u-v` exists. Intersecting this mask with unused-node bits quickly lists legal next endpoints.

`label_masks[ch]` similarly contains every node carrying character `ch`. It lets the source restrict right-end candidates to labels matching the chosen left node in one bitwise operation.

**Meaning of a search state**

A queued tuple `(mask, left_endpoint, right_endpoint)` represents the existence of a simple path that:

- uses exactly the nodes whose bits appear in `mask`;
- starts and ends at the two endpoint nodes;
- spells a palindrome.

The internal order of the path is not stored. It is unnecessary: future extensions depend only on the endpoints, used-node set, and the fact that the interior label sequence is palindromic.

**Odd-length centers**

Every single node is a palindrome of length one. The source inserts:

`(1 << node, node, node)`

for every node. These are the centers from which all odd-length palindromic paths can grow.

**Even-length centers**

An even palindrome must have two equal middle characters connected by an edge. For every edge `u-v` whose endpoint labels match, the source inserts the two-node state with both bits set and initializes `answer = 2`.

Endpoints are ordered so `u <= v` before encoding. This canonical form prevents the same undirected path state from being stored again with reversed endpoints.

**Extending both sides**

For a current state, possible new left nodes are:

`adjacency[left_endpoint] & ~mask`.

The loop extracts one set bit at a time with `bit = bits & -bits`. Its node index is `bit.bit_length() - 1`.

After selecting `left_node`, possible right nodes must:

- neighbor `right_endpoint`;
- be absent from `mask`;
- have the same label as `left_node`;
- differ from the selected left node.

The source expresses all four restrictions by intersecting adjacency, unused bits, `label_masks[label[left_node]]`, and `~left_bit`.

Adding equal labels to both ends preserves the palindrome. Excluding all bits in `mask` and excluding `left_bit` ensures every node in the new path is unique.

**Canonical endpoint order**

The new endpoints are stored as `(min(left_node,right_node), max(...))`. This loses orientation but not useful information.

The graph is undirected, and a palindrome reads the same forward and backward. Reversing a represented path produces an equivalent state with the endpoints exchanged. Future outward extensions available from one orientation correspond exactly to exchanged extensions from the other. Therefore, one canonical unordered endpoint pair per mask is sufficient.

**Encoding and deduplicating states**

The integer:

`(mask * n + first) * n + second`

uniquely encodes the mask and two endpoint values because each endpoint lies from 0 through `n-1`. `seen` prevents enqueuing the same canonical state more than once.

Different internal paths can lead to the same mask and endpoints. Keeping only one is safe because future possibilities depend on no other property of the interior.

**Why center-out construction finds every valid palindrome**

Take any palindromic simple path of length at least three. Its two endpoint labels are equal. Removing both endpoints leaves a shorter simple path, its nodes remain adjacent in sequence, and its label string is still a palindrome.

Repeatedly removing matching endpoints eventually reaches either:

- one center node for an odd-length palindrome; or
- one equal-labeled center edge for an even-length palindrome.

Those centers are initial states. Reversing the removals gives exactly the source's paired extension transitions. Thus every valid palindromic path is reachable by the search.

Conversely, every initialized state is a valid simple palindrome, and every transition adds distinct adjacent nodes with matching labels to its ends. Induction proves the search never creates an invalid state.

**Breadth-first processing and the answer**

Each transition adds exactly two nodes, so descendants are longer than their parent. The source computes `new_mask.bit_count()` whenever it discovers a new state and updates `answer`.

Breadth-first order is convenient but not required for correctness because all reachable states are explored and the maximum is recorded. If a new mask uses all `n` nodes, no longer path is possible, so the method returns `n` immediately.

**A three-node path example**

For labels `"aba"` on edges 0-1 and 1-2, the single-node center at node 1 has label `b`. Its unused neighbors are nodes 0 and 2. Their labels both equal `a`, so they can be added on opposite ends. The new mask contains all three nodes and represents label sequence `aba`, causing the early return of 3.

## Complexity detail

There are `2^n` possible masks and at most `n^2` endpoint pairs, so the number of canonical states is `O(2^n n^2)`. For one state, the nested bit loops can consider `O(n^2)` pairs of left and right candidates. The conservative time bound is therefore:

$$
O(2^n n^4).
$$

`seen` and the queue can each hold `O(2^n n^2)` states. Adjacency and label masks use `O(n)` integers, so total auxiliary space is `O(2^n n^2)`.

The complete-graph shortcut instead costs `O(n+m)` to recognize the edge count and count labels, with `O(n)` label-frequency space, but the manifest reports the general worst case.

## Alternatives and edge cases

- **Subset DP by endpoints:** Store a Boolean `dp[mask][u][v]` with the same recurrence. It is equivalent to the queue but may allocate every state eagerly.
- **Enumerate all simple paths:** The number of paths is enormous, and checking each completed label string repeats work that endpoint DP shares.
- **Depth-first search with memoization:** It can use the same state representation; breadth-first order is not essential.
- **Complete graph:** Label counts alone determine the answer because every node ordering forms a path.
- **Single node:** Its one-character label is a palindrome, so the answer is 1.
- **No equal-labeled edge:** No even palindrome of length two exists, but odd paths may still grow from single-node centers.
- **All labels distinct:** Only length one can be palindromic unless a longer path's symmetric endpoints somehow match, which distinctness prevents.
- **All labels equal:** Any simple path is palindromic; the answer is the graph's longest simple path, found by the mask search.
- **Even-length answer:** It must grow from an equal-labeled edge center.
- **Odd-length answer:** It grows from a single-node center.
- **Distinct new endpoints:** `~left_bit` prevents one unused node from being placed at both ends.
- **Already-used nodes:** `~mask` enforces the visit-at-most-once rule.
- **Undirected orientation:** Canonical endpoint sorting is safe because reversing a palindrome yields the same label sequence.
- **Duplicate search routes:** The integer state key prevents repeated expansion.
- **Full-mask state:** It proves optimal length `n` and permits immediate return.
- **Input preservation:** The source builds bitmasks without modifying `edges` or `label`.
