## General

**Merge in balanced groups instead of growing one list repeatedly**

Merging two sorted linked lists is linear in their combined lengths. A naive $k$-list method could merge list 0 with list 1, then merge that growing result with list 2, and so on. Nodes placed early would be traversed again for almost every later list, leading to $O(Nk)$ work in balanced inputs.

The selected competitive implementation pairs lists from opposite ends of the currently active array range. Pair results replace entries near the left side, and the active right boundary shrinks. This produces successively larger groups with approximately balanced merge depths, so each original node participates in only $O(\log k)$ two-list merges.

**First understand the local two-list merge**

The nested `mergeTwoLists` function uses a dummy node and a moving pointer `curr`. While both input heads exist, it attaches the smaller head and advances only that list. Its condition is strict:

```python
if l1.val < l2.val:
```

so equal values are taken from `l2` first. The unchosen equal node remains available and will be attached later; duplicates are preserved.

When either list becomes empty, `curr.next = l1 or l2` attaches the other already-sorted suffix in constant time. Returning `dummy.next` excludes the artificial node. The merge reuses and relinks original nodes and needs only constant pointer storage.

The local invariant is that the chain after `dummy` contains exactly the nodes consumed from `l1` and `l2`, in sorted order, and `curr` is its tail. The smaller current head is the smallest remaining node anywhere in those two lists, so each attachment preserves the invariant.

**Handle the zero-list case before indexing**

The outer method begins with

```python
if not lists:
    return None
```

Without this guard, the final `return lists[0]` would fail for an empty array. An array containing empty-list heads is different: it is non-empty, and the ordinary pairwise merge correctly treats each `None` as an exhausted list.

**Interpret `left` and `right` as active pairing endpoints**

Initially, `left = 0` and `right = len(lists) - 1`. One iteration merges `lists[left]` with `lists[right]` and stores the result back into `lists[left]`. It then increments `left` and decrements `right`, moving inward to the next pair.

When `left >= right`, the current inward pairing sweep is complete, and `left` resets to zero. The reduced `right` boundary is deliberately not reset. Entries beyond it have already been absorbed into entries at or before it and are no longer active independent lists.

For five lists, the merge pattern is:

1. merge original lists `0` and `4`, storing their group at `0`;
2. merge original lists `1` and `3`, storing their group at `1`;
3. reset `left`, then merge the group at `0` with untouched list `2`;
4. reset again, then merge that group with the group at `1`.

Every original list eventually belongs to the single group stored at index zero.

**Why the unusual schedule remains balanced**

During a complete inward sweep, active groups are paired once, roughly halving the number of independent groups. If an odd middle group remains, it survives into a later pairing. Therefore the number of sweeps before one group remains is $O(\log k)$.

Group sizes may differ by one round, as the five-list trace shows, but no original node is merged once per original list. Its group size grows geometrically across sweeps, bounding the number of times that node is traversed by $O(\log k)$.

The loop condition `while right > 0` ends exactly when the active range has only index zero. At that point `lists[0]` contains the merge of every original group.

**Why each pairwise result is correct**

The two-list helper always chooses the smaller available head, so it returns every node from its two input groups once and in sorted order. Initially, every array entry is itself a sorted group. Replacing two sorted groups with their correctly merged result preserves that property. By induction over all outer iterations, every active entry is a sorted merge of a disjoint subset of original lists. When one active entry remains, its subset contains all originals, so `lists[0]` is the complete sorted result.

**Mutation occurs at two levels**

The helper rewires node `next` pointers, while the outer method overwrites elements such as `lists[left]` with group heads. The caller's array and list structures are therefore both modified. This is how the source attains constant additional pointer space: it uses the provided array as its merge workspace.

The dummy node created inside each helper call becomes unreachable after that call returns. Only one helper runs at a time, so dummy allocations do not accumulate in peak live auxiliary memory.

## Complexity detail

Let $k$ be `len(lists)` and $N$ be the total number of nodes.

- **Time complexity: $O(N\log k)$.** A two-list merge is linear in the nodes of its two groups. Each pairing sweep processes each node in the participating groups at most once, and the number of active groups approximately halves per sweep. Thus every node is traversed in at most $O(\log k)$ merge levels. Empty groups add only constant overhead per pairing; with $N=0$, processing the array itself can still take $O(k)$ operations, so a fully explicit bound is $O(k+N\log k)$.
- **Auxiliary space of the exact selected source: $O(1)$ beyond the input array.** The algorithm is iterative and keeps a constant number of indices, pointers, and one live dummy node per helper call. It overwrites `lists` instead of creating a separate $k$-entry work array. The manifest's $O(k)$ bound is a safe upper bound if the input-head array is counted as working storage, but it is not newly allocated by this method.

The merged output reuses the original $N$ nodes and is excluded from auxiliary space.

## Alternatives and edge cases

- **Min-heap of current heads:** Keep one candidate per non-empty list. It also takes $O(N\log k)$ time and uses $O(k)$ heap storage, with a simpler direct global-minimum invariant.
- **Conventional interval-doubling divide and conquer:** Merge indices distance 1 apart, then 2, then 4. It has the same balanced complexity and may be easier to recognize than inward endpoints.
- **Sequential accumulator merge:** It is easy to write but can retraverse early nodes $k$ times, costing $O(Nk)$.
- **Scan every current head:** It finds each next node in $O(k)$, also leading to $O(Nk)$ time.
- **Empty `lists` array:** The explicit guard returns `None` safely.
- **Array of one `None`:** The outer loop is skipped and `lists[0]`, which is `None`, is returned.
- **One non-empty list:** No merge is necessary; the original head is returned.
- **Odd number of active groups:** The unpaired middle group remains inside the reduced active range and is included in a later merge.
- **Equal values:** The strict helper comparison takes the right group's node first on a tie, while preserving every duplicate.
- **All empty lists:** Pairwise merges operate on `None` values and ultimately leave `None` at index zero.
- **Input-array mutation:** Entries are overwritten with merged group heads. Callers needing the original head array must pass a shallow copy.
- **Node mutation:** Original `next` links are spliced; the separate input chains do not survive as independent structures.
- **Aliasing and cycles:** Correctness assumes finite, independent lists. Shared nodes or cycles are outside the supplied contract.
