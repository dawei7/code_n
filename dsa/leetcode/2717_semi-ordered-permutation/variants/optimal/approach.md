## General

**Only the locations of 1 and n matter**

A semi-ordered permutation imposes exactly two requirements: value `1` must occupy index zero, and value `n` must occupy index $n-1$. Every other value may appear in any order. Therefore an optimal solution should not spend effort arranging the middle values; they merely move aside as `1` and `n` pass them through adjacent swaps.

Let `i = nums.index(1)` and `j = nums.index(n)`. Because `nums` is a permutation, both values occur exactly once, so these positions are unambiguous.

**Cost of moving 1 to the front**

Value `1` starts at index `i`. One adjacent swap with the element immediately to its left decreases its index by one. No adjacent swap can decrease its index by more than one. Reaching index zero therefore requires at least `i` swaps, and swapping `1` left exactly `i` times achieves that cost.

Thus `i` is both a lower bound and the exact isolated cost for the first requirement.

**Cost of moving n to the back**

Value `n` starts at index `j`. It is $n-1-j$ positions away from the last index. Moving it right across each intervening element takes exactly one adjacent swap, so its isolated cost is:

$$
n-1-j.
$$

Again, this is unavoidable because a swap moves `n` at most one position right, and it is attainable by repeatedly swapping it with its right neighbor.

**When the two journeys do not overlap**

If `i < j`, value `1` already lies to the left of value `n`. Moving `1` left never crosses `n`, and moving `n` right never crosses `1`. The two sets of required swaps are disjoint, so the total is:

$$
i+(n-1-j).
$$

The implementation sets `k = 1` in this case and returns `i + n - j - k`, which is exactly the same expression.

For `[2,1,4,3]`, `i=1` and `j=2`. The cost is $1+(3-2)=2$: move `1` once left and `4` once right.

**When 1 initially lies to the right of n**

If `i > j`, the paths must cross. A single swap between `1` and `n` makes progress toward both goals simultaneously: `1` moves one position left while `n` moves one position right. Adding the isolated costs would count that crossing as two swaps, once for each value, even though it is one physical operation.

Therefore subtract one shared swap:

$$
i+(n-1-j)-1=i+n-j-2.
$$

The code represents this by setting `k = 2` when `i >= j` and returning `i + n - j - k`. Equality cannot occur because `1` and `n` are different values for $n\ge2$, so this branch really means `i > j`.

Consider `[3,2,1]`. Here $n=3$, `i=2`, and `j=0`. The isolated distances sum to four. A valid adjacent-swap sequence is `[3,2,1]` to `[3,1,2]`, then `[1,3,2]`, and finally `[1,2,3]`. This takes three operations. The middle step swaps `1` with `3`, moving both special values toward their destinations at once. The formula gives $2+2-1=3$, exactly matching the sequence.

**Why no other shared savings are possible**

Each required swap involving `1` moves it left one step, and each required swap involving `n` moves it right one step. A single adjacent swap can involve both special values only when they are next to each other. Since two distinct elements cross at most once, at most one operation can advance both goals.

When `i<j`, they move away from each other and never need to cross, so there is no shared operation. When `i>j`, their final order is the reverse of their initial order, so they must cross exactly once. This proves the adjustment is neither missing a saving nor subtracting too much.

**Why disturbing middle values is harmless**

The middle values are shifted by the movements of `1` and `n`, but the definition places no restrictions on them. Once the endpoints contain the required values, the permutation is semi-ordered regardless of the middle arrangement.

**A direct optimality proof**

The endpoint distances require `i` leftward steps for `1` and $n-1-j$ rightward steps for `n`. One adjacent swap can contribute to both counts only when it swaps `1` with `n`, which happens exactly once if their initial order is reversed and never otherwise. The formula adds both lower bounds and removes precisely that one double count. A sequence that moves `1` left and `n` right achieves the formula, so the returned number is minimal.

## Complexity detail

Let $n$ be the permutation length. Python's `nums.index(1)` scans until it finds `1`, and `nums.index(n)` independently scans until it finds `n`. Each scan is $O(n)$ in the worst case, so total time is $O(n)$; two linear scans remain linear.

The algorithm stores only `n`, `i`, `j`, and `k`. It does not copy or modify the permutation, giving $O(1)$ auxiliary space.

The arithmetic after locating the two values is constant time. Although a constructive simulation would perform exactly the returned number of swaps, the solution computes that count without performing them.

## Alternatives and edge cases

- **Simulate adjacent swaps:** Produces the final permutation but does unnecessary mutations when only the minimum count is requested.
- **One combined scan:** The positions of `1` and `n` can be recorded in one traversal; it keeps the same $O(n)$ time and $O(1)$ space.
- **Breadth-first search over permutations:** Finds a shortest sequence for tiny $n$ but has factorial state growth and ignores the endpoint structure.
- **Already semi-ordered:** When `i=0` and `j=n-1`, the formula returns zero.
- **Reversed special values:** When `n` precedes `1`, subtract exactly one because their crossing swap advances both.
- **Length two:** The only permutations are already ordered with cost zero or reversed with cost one; the formula handles both.
- **Adjacent 1 and n in correct order:** They do not cross, so no discount applies.
- **Adjacent n and 1 in reversed order:** Their one mutual swap is the shared operation counted by the subtraction.
- **Distinctness guarantee:** The permutation property ensures `index` finds one unique position for each special value.
- **Unrestricted middle:** No sorting of values `2` through `n-1` is required.
