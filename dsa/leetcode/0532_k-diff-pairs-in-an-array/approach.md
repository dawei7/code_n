## General

The result counts unique **value pairs**, not pairs of array indices. Duplicate occurrences may prove that a pair exists, especially when `k = 0`, but they must not make the same value pair count multiple times.

Because `k >= 0`, every valid pair can be written canonically as:

$$
(a,a+k).
$$

The smaller endpoint `a` uniquely identifies that pair. The solution stores these smaller endpoints in `ans`, a set, so repeated discoveries automatically collapse into one result.

A second set, `vis`, contains every distinct value encountered earlier in the left-to-right scan.

For each current value `x`, there are two ways it can complete a pair with an earlier value.

**An earlier value is `x - k`.** If `x - k in vis`, then the earlier value and current value form:

$$
(x-k,x),
$$

whose absolute difference is `k`. Its smaller endpoint is `x - k`, so the code adds `x - k` to `ans`.

**An earlier value is `x + k`.** If `x + k in vis`, the earlier value is larger than the current one. The canonical ordered pair is:

$$
(x,x+k).
$$

Its smaller endpoint is `x`, so the code adds `x` to `ans`.

Checking both directions matters because input order is arbitrary. In `[1, 3]` with `k = 2`, the later three finds `3 - 2`. In `[3, 1]`, the later one finds `1 + 2`. Both input orders add the same canonical endpoint one.

Only after both checks does the method execute `vis.add(x)`. This order enforces the distinct-index requirement. The current occurrence cannot pair with itself because it is not considered “previously seen” until its checks are complete.

The order is particularly important for `k = 0`. A zero-difference pair requires two occurrences of the same value. On its first occurrence, `x` is absent from `vis`, so neither check adds it. On its second or later occurrence, `x - 0` and `x + 0` are present, and `x` is added to `ans`. Thus a value contributes exactly when its frequency reaches at least two.

Although both `if` statements are true together when `k = 0`, they add the same `x` to a set. The pair is still counted once.

For `nums = [3, 1, 4, 1, 5]` and `k = 2`:

- three is first and creates no pair;
- one sees earlier three through `1 + 2` and adds endpoint one;
- four finds neither two nor six;
- the repeated one discovers endpoint one again, but the set is unchanged;
- five sees earlier three through `5 - 2` and adds endpoint three.

The final set is `{1, 3}`, representing value pairs `(1, 3)` and `(3, 5)`, so the answer is two.

For `[1, 3, 1, 5, 4]` with `k = 0`, the second one is the only value whose prior duplicate exists. `ans` becomes `{1}` and the method returns one.

**Why every stored endpoint represents a valid pair.** An endpoint is added only after a membership test finds the complementary value in `vis`. That complement came from a strictly earlier array position. The two indices are therefore different, and the canonical values differ by exactly `k`. Set membership cannot introduce a nonexistent pair.

**Why every valid unique pair is found.** Take any valid pair `(a, a + k)` represented by two different occurrences. Whichever of those two occurrences appears later in the scan sees the other value in `vis`. If the later value is `a + k`, the subtraction check adds `a`; if it is `a`, the addition check adds `a`. For `k = 0`, the second equal occurrence sees the first. Thus every valid pair's canonical endpoint enters `ans`.

**Why uniqueness is exact.** Different canonical endpoints describe different ordered value pairs when `k` is fixed. Repeated occurrences of the same pair add the same endpoint, and the set retains one copy. Therefore `len(ans)` is exactly the number of unique k-diff pairs.

The algorithm never sorts or modifies `nums`. Negative values work naturally because Python sets and addition/subtraction do not depend on sign.

## Complexity detail

Let $n$ be the length of `nums`. The solution scans the array once. Each iteration performs a constant number of expected-$O(1)$ set lookups and insertions, giving expected $O(n)$ time.

Both `vis` and `ans` contain at most one entry per distinct input value, so each uses $O(n)$ space in the worst case. Total auxiliary space is $O(n)$, matching the manifest.

The expected-time statement uses the standard hash-set model. Python integers safely handle values such as `x + k` outside the input's stated numeric range.

## Alternatives and edge cases

- **Frequency map:** For `k > 0`, count keys whose `x + k` exists; for `k = 0`, count values with frequency at least two. It has the same asymptotic bounds.
- **Sort and use two pointers:** It can find each distinct difference in $O(n\log n)$ time, but sorting is slower asymptotically and may modify or copy the input.
- **Check every index pair:** It takes $O(n^2)$ time and requires an additional mechanism to deduplicate value pairs.
- **`k = 0`:** A value qualifies only after a second occurrence; the set prevents further duplicates from increasing the result.
- **One array element:** No earlier complement exists, so the answer is zero.
- **Repeated valid pair:** Every discovery adds the same smaller endpoint and counts once.
- **Reverse arrival order:** The two complement checks make discovery independent of which endpoint appears first.
- **Negative values:** Canonical smaller endpoints and set membership remain valid.
- **No valid pair:** `ans` stays empty and `len(ans)` returns zero.
- **Distinct-index rule:** Delaying `vis.add(x)` until after checks prevents an occurrence from pairing with itself.
- **Large `k`:** Complements may lie far outside observed values; failed set membership simply contributes nothing.
