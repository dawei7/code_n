## General

**Rotation means endpoint order should not matter**

Domino `[a,b]` is equivalent to both `[a,b]` and `[b,a]`. To count efficiently, every equivalent orientation needs one canonical identity.

The solution places the smaller endpoint first and the larger endpoint second. It encodes that ordered canonical pair as a two-digit integer.

If `a < b`, key `a * 10 + b` already has the smaller value first. Otherwise, key `b * 10 + a` reverses the endpoints. Equal endpoints follow the second branch but produce the same value either way.

**Why decimal encoding is collision-free**

Every endpoint lies from one through nine. In key `10 * small + large`, integer division by ten recovers the smaller digit and remainder modulo ten recovers the larger digit.

Therefore, different canonical endpoint pairs cannot share a key. The bound of one decimal digit per endpoint is essential; for arbitrary larger values, a tuple would be safer.

Examples `[1,2]` and `[2,1]` both map to twelve. Domino `[1,3]` maps to thirteen and cannot collide. Double `[2,2]` maps to twenty-two.

**Count earlier equivalent dominoes online**

`cnt[key]` is the number of previously processed dominoes with this canonical identity.

When the current domino arrives, every earlier domino in that count forms exactly one valid pair with it. Adding `cnt[key]` to `ans` counts all pairs whose later index is the current position.

Only after counting does the code increment `cnt[key]`. This prevents pairing the domino with itself and prepares it as an earlier partner for future positions.

For three copies of `[1,2]` in mixed orientations, the first sees count zero, the second sees one, and the third sees two. Their total contribution is three pairs: first with second, first with third, and second with third. The counter never needs to remember the actual indices because only how many earlier partners exist affects the new contribution.

At the beginning of each loop iteration, `ans` equals the number of equivalent pairs entirely inside the processed prefix, and `cnt` stores exact canonical frequencies for that prefix. The add-then-increment steps extend both facts to include the current index, which is a direct loop invariant.

**Why a group of size $q$ contributes the right number**

Suppose equivalent dominoes appear $q$ times. Their incremental contributions are zero, one, two, through $q-1$. The sum is:

$0+1+\cdots+(q-1)=q(q-1)/2$,

which is exactly the number of unordered index pairs in that group.

Processing order assigns every pair to its larger index, so no pair is counted twice.

This incremental form avoids a later multiplication pass and keeps `ans` correct after every prefix. It is mathematically identical to grouping first and applying the combination formula afterward.

**Complete correctness argument**

Canonicalization maps two dominoes to the same key exactly when their endpoints match directly or after rotation. For each current domino, the counter contains precisely the earlier equivalent indices.

The update adds one for every valid pair ending at that index and none for invalid keys. Across the scan, every pair with $i<j$ is counted when `j` is processed. Therefore, the final answer is exactly the requested pair count.

## Complexity detail

Let $n$ be the number of dominoes. The loop performs constant arithmetic and expected constant-time Counter operations per domino, so time is $O(n)$.

There are only unordered pairs drawn from nine endpoint values. At most $9\cdot10/2=45$ canonical keys can exist. Counter storage is therefore bounded by a source-defined constant, giving $O(1)$ space.

The answer can be as large as $n(n-1)/2$, but Python integers represent it without overflow. The problem’s maximum still fits comfortably in normal integer ranges.

Counter is implemented as a dictionary, but its possible key universe remains bounded. Keys range from eleven through ninety-nine with the tens digit no greater than the units digit, and only the forty-five valid canonical combinations can be inserted.

The input list is read sequentially and never copied or modified. Each destructured pair supplies two constant-sized integers.

## Alternatives and edge cases

- **Tuple key:** Use `(min(a,b), max(a,b))`. It generalizes beyond one-digit endpoints and makes canonicalization visually explicit.
- **Sort each domino:** Sorting a two-element list creates the same identity but adds avoidable allocation or mutation.
- **Compare every pair:** Directly test equivalence in $O(n^2)$ time.
- **Count frequencies then combine:** Build all canonical counts, then sum `q * (q - 1) // 2`. It is equally correct but needs a second pass over keys.
- **One domino:** No earlier partner exists, so the answer is zero.
- **All equivalent:** Contributions grow from zero through $n-1$, yielding every index pair.
- **No equivalent keys:** Every lookup is zero and the answer remains zero.
- **Repeated double:** Dominoes such as `[3,3]` canonicalize normally and pair with each other.
- **Rotation:** `[1,9]` and `[9,1]` share key nineteen.
- **Different unordered pairs:** The decimal encoding cannot collide under digits one through nine.
- **Self-pair prevention:** Incrementing after adding ensures an index never pairs with itself.
- **Index order:** Each unordered pair is counted once at its later index, satisfying `i < j`.
