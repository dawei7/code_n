## General
**Separate both teams in position order**

Collect the indices containing `1` into `catchers` and the indices containing
`0` into `people`. Both lists are automatically increasing because the input is
scanned from left to right. Maintain one pointer to the earliest unmatched
index in each list.

**Discard an index that can no longer match**

Let the current indices be `catcher` and `person`. If
`person < catcher - dist`, that person lies too far left for the current
catcher and for every later catcher, so advance only the person pointer.
Symmetrically, if `catcher < person - dist`, the current catcher lies too far
left to reach the current or any later person, so advance only the catcher
pointer.

**Greedily match the earliest feasible pair**

Otherwise the two current indices are within the inclusive distance bound.
Match them and advance both pointers. This cannot reduce the optimum: in any
maximum matching that uses either earliest index, replacing its partner with
the other earliest feasible index leaves every later index at least as much
room to match to the right. If neither is used, adding their feasible pair
would improve the matching.

Thus the greedy step preserves a maximum completion after every pointer
advance. The number of matched pairs when either list is exhausted is the
largest possible number of catches.

## Complexity detail
Building the two index lists scans all $N$ positions once. Each pointer then
advances monotonically and never retreats, so matching also takes $O(N)$ time.
The two lists together store exactly $N$ indices, using $O(N)$ space.

## Alternatives and edge cases
- **Direct streaming queues:** Maintain unmatched indices while scanning the
  original array. This can also achieve linear time but makes the symmetric
  expiration logic less direct.
- **General bipartite matching:** Connect every catcher to every reachable
  person and run augmenting paths. This is correct but ignores interval order
  and may require quadratic edges and superlinear matching work.
- **Choose the nearest person independently:** Local nearest-distance choices
  can consume the only partner reachable by a later catcher; left-to-right
  order, not raw distance, provides the safe greedy rule.
- If either team is absent, no pair can be formed.
- A pair at distance exactly `dist` is valid because the interval is inclusive.
- When `dist` spans the whole array, the answer is the smaller of the counts of
  zeros and ones.
- Extra people on either team remain unmatched once the opposite index list is
  exhausted.
