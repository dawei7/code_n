## General

**Reduce operations to nearest-value distance**

Changing an integer `x` into a target `p` using only increments and decrements costs exactly $\lvert x-p\rvert$. Any sequence reaching `p` needs at least that many unit changes, and repeatedly moving toward `p` attains the bound.

Therefore each array element can be solved independently: find the binary-palindromic integer closest to `x` and return their absolute difference.

**Precompute every candidate in a fixed safe range**

Before the `Solution` class is defined, the source enumerates

`range(1 << 14)`,

which is every integer from 0 through 16,383. For each integer `i`, `bin(i)[2:]` removes Python's `"0b"` prefix and leaves its ordinary binary digits. The equality `s == s[::-1]` recognizes exactly those digit strings that read the same forward and backward.

Every matching integer is appended to the global list `p`. Because `i` is visited in increasing numeric order, `p` is automatically sorted; no separate sort is needed. The list contains 255 values, including zero.

The upper limit is safely beyond the legal input domain. Every input is at most 5,000, and 8,191 has binary representation `1111111111111`, which is palindromic and lies above every legal input. Thus each legal `x` has at least one precomputed palindrome at or above it. The list also begins with zero, so a lower-side candidate always exists conceptually, although the code still guards the predecessor index.

This precomputation occurs once when the module is loaded. Multiple calls to `minOperations` reuse the same ordered candidate list.

**Locate the insertion boundary with binary search**

For one value `x`, `bisect_left(p, x)` returns the first index `i` for which `p[i] >= x`.

There are only two possible nearest candidates:

- `p[i]`, the smallest binary palindrome greater than or equal to `x`;
- `p[i-1]`, the largest binary palindrome strictly below `x`, when `i >= 1`.

Any candidate farther left is no larger than the predecessor and therefore has at least as much distance below `x`. Any candidate farther right is no smaller than the successor and therefore has at least as much distance above `x`. No other precomputed value can beat these two neighbors.

The source initializes `times` to infinity, conditionally measures both sides, and keeps their minimum. If `x` itself is a binary palindrome, `bisect_left` points directly to it and `p[i] - x` is zero.

**Preserve each answer in input order**

The loop handles `nums` from left to right and appends one minimum distance per input value. Candidate searches share the read-only list `p` but no per-element state, so one answer cannot affect another.

For `x=6`, whose binary form is `110`, the surrounding palindromes are 5 (`101`) and 7 (`111`). Both are one unit away, so the result is one.

For `x=12`, the predecessor 9 has binary form `1001` and distance three, while the successor 15 has form `1111` and distance three. Either target is optimal, and the returned operation count is three.

For `x=7`, binary search lands on 7 itself because `111` is palindromic, yielding zero operations.

**Why the neighbor comparison is complete**

The candidate generation is complete over the entire numeric interval that can contain a needed lower or upper neighbor for the constrained inputs. Its palindrome test is exact because reversal equality is the definition applied to the no-leading-zero binary representation.

For each `x`, sorted-order reasoning proves the closest candidate lies at the binary-search boundary or immediately before it. The method tests both positions when present and takes the smaller absolute difference. Since absolute difference equals the minimum operation count for a chosen target, each appended value is globally minimal.

**The manifest summary describes a different algorithm**

The manifest says the solution mirrors the leading half of each input's binary representation and compares a constant set of constructed candidates. The exact source does not mirror bits per input. It exhaustively precomputes all palindromes below $2^{14}$ once, then performs binary search.

This distinction matters for explaining both the data flow and complexity. The source's query phase is $O(\log P)$ per value, where $P=255$ is the fixed number of precomputed candidates. The one-time enumeration cost must also be acknowledged.

## Complexity detail

Let $B=14$ be the fixed enumeration bit limit, $P$ the number of discovered binary palindromes, and $N$ the length of `nums`.

Precomputation visits $2^B$ integers. Creating and reversing a binary string costs $O(B)$ in the worst case, so module initialization takes $O(2^B B)$ time and stores $O(P)$ integers. Here $B=14$ and $P=255$, so both are fixed constants under the documented constraints.

Each array element performs `bisect_left` in $O(\log P)$ time and constant additional arithmetic. The method phase is $O(N\log P)$ time. Including initialization, the explicit bound is

$$
O(2^B B + N\log P).
$$

With fixed $B$ and $P$, this simplifies to $O(N)$ time for asymptotic growth in the number of inputs. The manifest's $O(N\log V)$ can serve as a loose search-oriented description, but it accompanies a mirroring summary that is not the executed algorithm.

The returned `ans` list uses $O(N)$ space. Apart from output, each query uses $O(1)$ local space, and the global candidate list uses fixed $O(P)$ storage. If the value limit were generalized, the hard-coded enumeration would first need to be redesigned rather than extrapolated beyond 16,383.

## Alternatives and edge cases

- **Mirror the leading binary half:** Constructing a few same-length and boundary-length palindrome candidates per input avoids exhaustive enumeration and resembles the manifest summary, but it is not the exact source.
- **Search outward one integer at a time:** Testing `x-1`, `x+1`, and so on eventually works but repeats palindrome checks and has no comparably clean per-query bound.
- **Linear scan of all precomputed palindromes:** With only 255 candidates it may be fast in practice, but binary search gives $O(\log P)$ lookup.
- **Generate candidates for every call:** The global list deliberately pays initialization once and reuses it.
- **Value already palindromic:** The successor position equals `x`, so the answer is zero.
- **Equal-distance neighbors:** Either target is optimal; only the distance is returned, so no tie-breaking target is needed.
- **Smallest legal input:** For `x=1`, candidate 1 is present and produces zero.
- **Zero candidate:** The precomputation regards binary `0` as palindromic. Inputs are positive, and candidate 1 is always closer than zero for positive non-palindromic cases where this could matter, so inclusion does not corrupt results.
- **Upper-neighbor guarantee:** Palindrome 8,191 is above the maximum legal value 5,000, ensuring a finite successor for every valid input.
- **Predecessor guard:** When `i=0` there is no `p[i-1]` to inspect; the source checks `i >= 1` before doing so.
- **Successor guard:** The code also checks `i < len(p)`, making the binary-search handling safe even though legal inputs guarantee a successor.
- **Independent array positions:** Duplicate inputs repeat the same search and return duplicate distances; no mutation or shared progress occurs.
- **Hard-coded domain:** Values beyond the supported constraint could exceed the precomputed range, so correctness should not be claimed for an unauthorized generalized domain.
- **Source/manifest strategy mismatch:** The explanation and exact complexity must include enumeration plus binary search, not per-value bit mirroring.
