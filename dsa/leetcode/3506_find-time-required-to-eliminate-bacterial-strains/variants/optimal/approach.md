## General

**Model the strategy as a binary split tree.** Each bacterial strain is assigned to one final WBC, so it is a leaf. Every time a WBC splits, it creates the two child branches of an internal node and costs `splitTime` before either child can continue.

If two child subplans need times $a$ and $b$ after their WBCs become available, creating both from one parent requires

$$
\texttt{splitTime}+\max(a,b),
$$

because the children execute in parallel after the split. The slower child determines completion.

The goal is to build a binary tree whose leaf requirements are `timeReq` and whose root completion requirement is minimum.

**Build the tree backward by merging two smallest requirements.** The source heapifies `timeReq` into a min-heap. At each step it removes the two smallest requirements $a\le b$.

Their combined parent requirement is

$$
\texttt{splitTime}+\max(a,b)
=b+\texttt{splitTime}.
$$

The code discards the first popped value and pushes `heappop(timeReq) + splitTime` for the second. This compact sequence is exactly the formula above.

Each merge reduces the number of independent subplans by one. When one value remains, it is the minimum time required from the initial WBC.

For `[10,4,5]` with split time two, merge four and five into requirement seven. Then merge seven and ten into twelve. The corresponding schedule gives one root child directly to the ten-time strain and splits the other child again for strains four and five. All finish by time twelve.

For two strains, the only possible useful structure is one split followed by parallel elimination, so the result is `splitTime + max(timeReq)`. One heap merge produces exactly that.

**Why smaller requirements should be deeper.** Every split on a leaf's root path adds the same `splitTime` to its completion. A larger strain placed deeper is more likely to dominate the maximum. If two leaves or completed subtrees at different depths have requirements $a\le b$ but $b$ is deeper, swapping them cannot increase either path's maximum completion and may reduce it. Thus an optimal tree can place smaller requirements at least as deep as larger ones.

**Why the two smallest can be merged as siblings.** In a full binary tree, choose a deepest internal node whose children are terminal subplans. By the exchange argument, the two smallest remaining requirements can be assigned to those deepest sibling positions without worsening the root maximum. Contracting that sibling pair replaces it with a parent requirement `max(a,b)+splitTime`.

The remaining problem has the same form with one fewer requirement. Applying this argument inductively justifies merging the two smallest current requirements at every step, analogous to a Huffman construction but with `max + splitTime` instead of sum.

Merged heap values represent complete subtrees, so the same exchange reasoning continues to apply after raw strain times and subtree requirements mix.

**Why parallelism is captured correctly.** The merge adds split time once, not twice, because one WBC performs one split and both children become available simultaneously. It takes a maximum, not a sum, because their elimination work happens in parallel. Nested splits naturally accumulate along only the paths that contain them.

**Complete correctness.** Every sequence of WBC splits and eliminations defines a binary tree with the stated internal-node recurrence. Conversely, any such tree can be scheduled by performing each split when its parent WBC becomes available and executing child subtrees in parallel. The deepest-sibling exchange proves an optimal tree has a first reverse merge of the two smallest requirements, and induction proves every greedy merge preserves optimality. The final heap value is therefore the minimum makespan.

The method mutates `timeReq`: `heapify` rearranges it, pops remove entries, and the final list contains only the answer. Callers retaining the input list will observe this change.

## Complexity detail

Heap construction costs $O(n)$. There are $n-1$ merges, each with two pops and one push, each $O(\log n)$. Total time is $O(n\log n)$.

The heap reuses the input list and holds at most $n$ requirements. Under the usual auxiliary-space convention for in-place heapification, extra algorithmic storage is $O(1)$ beyond the mutated input; counting the heap representation required by the algorithm gives $O(n)$ space, matching the manifest.

Heap values and final time may exceed individual $10^9$ inputs after many split levels. Python integers remain exact.

## Alternatives and edge cases

- **Split until one WBC per strain immediately:** A balanced tree ignores different elimination times and can make a long strain unnecessarily deep.
- **Assign largest requirements deepest:** Extra split delays on large leaves can only worsen the maximum.
- **Merge two largest first:** This creates a parent even larger than necessary and contradicts the deepest-smallest exchange.
- **Sum child requirements:** Children operate in parallel, so their parent uses a maximum.
- **Add split time to both children separately:** One split event delays both branches by the same single interval.
- **Two strains:** One merge returns `max(a,b)+splitTime`.
- **Equal strain times:** Many split trees may tie; the heap chooses one optimal merge order.
- **Very large split time:** The greedy tree tends to keep larger requirements shallow, limiting added split depth.
- **One subtree value in the heap:** It is treated exactly like a raw leaf requirement during later merges.
- **Input order:** Strains may be eliminated in any order, so heap reordering is legal.
- **Input mutation:** The source consumes `timeReq` as its heap; copy it first if preservation is required.
- **Positive durations:** Every split and elimination adds real delay, supporting the depth exchange argument.
