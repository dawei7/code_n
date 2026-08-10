## General

The competitive solution performs mirror comparison iteratively with a LIFO stack. Each logical work item is a pair of nodes occupying corresponding reflected positions. The source stores pair members as consecutive stack entries instead of using a tuple.

An empty root is symmetric, so the method returns true immediately. For a real root, it pushes `root.left` followed by `root.right`.

**How pairs are popped**

The statement `p, q = stack.pop(), stack.pop()` pops in reverse insertion order. Initially, `p` receives the root's right child and `q` receives its left child. Their orientation is harmless because the mirror relation is symmetric: if one subtree mirrors another, the second mirrors the first.

The algorithm always pushes four references for a successful real pair and removes two per iteration. Starting from two entries, the stack length remains even, so both pops are safe.

**Three outcomes for a pair**

If both `p` and `q` are `None`, the corresponding positions are both absent. The loop continues without descendants.

If exactly one is absent, their structures differ. If both exist but `p.val != q.val`, their contents differ. The combined mismatch condition returns false in either case, with short-circuiting preventing an unsafe value access.

Only two real equal-valued nodes need their children added.

**Why the push order creates crossed pairs**

For current pair `(p, q)`, the mirror requirements are `p.left` with `q.right`, and `p.right` with `q.left`.

The code appends, in order:

1. `p.left`,
2. `q.right`,
3. `p.right`,
4. `q.left`.

LIFO popping makes the next pair `(q.left, p.right)`, which is the second requirement in reversed orientation. The following pair becomes `(q.right, p.left)`, the first requirement in reversed orientation. Reversing both members changes nothing, so each popped pair is correct.

This ordering is easy to get wrong. Pushing the same-direction children together would test ordinary equality rather than symmetry.

**Trace on a symmetric tree**

For `[1,2,2,3,4,4,3]`, the first pair contains the two nodes valued two. After their children are pushed, the next pair compares the original left subtree's far-left three with the original right subtree's far-right three. The later pair compares the inner fours.

Every leaf then produces pairs of `(None, None)`. Those pairs are accepted without adding work. The stack empties and the method returns true.

For `[1,2,2,null,3,null,3]`, one popped outer pair contains `None` and node three. The method returns false at that exact reflected-position mismatch.

**Why stack exhaustion proves symmetry**

Every real matching pair schedules exactly its two crossed child pairs. Every empty matching pair schedules nothing. Thus an empty stack means every reachable reflected position was checked without mismatch.

Conversely, any asymmetric tree has a first reflected position with unequal occupancy or value. Its matching ancestor pairs schedule it, and the mismatch is detected when popped. This proves both directions of correctness.

The stack does not need an explicit “visited” flag. Each pair is compared exactly when popped, and its children are pushed only after that comparison succeeds. Trees contain no back-edges, so no pair needs to be scheduled a second time through another parent.

The method does not mutate the tree. The later `Solution2` is the recursive counterpart requested by the follow-up, not the selected class.

## Complexity detail

Each node reference participates in a constant number of pushes, pops, and comparisons. A symmetric tree needs $O(n)$ time; an early mismatch may use less.

Because processing is depth-first, the stack stores pending mirror siblings along active paths, not a complete level. Its maximum size is $O(h)$ up to a constant factor, matching the manifest. Balanced trees use $O(\log n)$; skewed paths can use $O(n)$.

To see the height bound, processing one real pair removes two references and adds four, a net increase of two. The algorithm then immediately follows one of the newly added pairs because of LIFO order, leaving only the other pair pending for that depth. Along a descent of at most $h$ levels, there are only constantly many pending references per level. After reaching empty children, those deferred pairs are consumed while the traversal unwinds. A queue would behave differently by accumulating a whole level.

## Alternatives and edge cases

- **Recursive mirror helper:** It expresses the definition directly with $O(h)$ call-stack space.
- **Queue-based mirror BFS:** It can be easier to draw but may hold $O(n)$ references on a wide level.
- **Tuple stack:** Storing `(p, q)` makes pair boundaries explicit and reduces push-order mistakes.
- **Empty root:** The explicit guard returns true even though the stated node count starts at one.
- **Single node:** The stack begins with two `None` references, which form one valid pair.
- **One missing child:** It is rejected before any value dereference.
- **Duplicate values:** Structure is still checked at each reflected position.
- **Even-stack invariant:** Every successful node pair pushes four references, preserving safe two-at-a-time popping.
- **Do not pair same directions:** That would check whether halves are identical rather than mirrored.
- **Pair orientation:** `(a, b)` and `(b, a)` express the same mirror question, which is why reverse pop order is harmless.
- **No root duplication:** Starting with the two children is sufficient; pushing `(root, root)` would also work but would perform one redundant comparison.
