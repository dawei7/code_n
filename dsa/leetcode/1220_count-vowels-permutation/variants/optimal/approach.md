## General

**Count strings by their final vowel**

Trying to generate every valid length-\(n\) string would create an exponential search tree. Most partial strings, however, do not need to be distinguished by their full contents. To decide which vowel may be appended next, only the current final vowel matters. Two strings of the same length that end in the same vowel have exactly the same set of legal next choices.

This allows dynamic programming with five states. In the exact code, the list `f` uses the fixed order `a, e, i, o, u`. For the current string length, `f[0]` counts valid strings ending in `a`, `f[1]` counts those ending in `e`, and so forth.

For length one, each vowel forms exactly one string by itself. Therefore, `f = [1] * 5` is the complete base case. When `n == 1`, the transition loop runs zero times and the final sum correctly returns five.

**Reverse each following rule to obtain the recurrence**

The statement describes which character may follow a given vowel. To count strings ending in a particular new vowel, it is more useful to ask the reverse question: which old final vowels are allowed immediately before this new vowel?

The allowed transitions are:

- `a` can be followed only by `e`.
- `e` can be followed by `a` or `i`.
- `i` can be followed by every vowel except `i`.
- `o` can be followed by `i` or `u`.
- `u` can be followed only by `a`.

Reversing those arrows gives the five assignments in the implementation:

- A new string ending in `a` can come from an old string ending in `e`, `i`, or `u`, so `g[0] = f[1] + f[2] + f[4]`.
- A new string ending in `e` can come from `a` or `i`, so `g[1] = f[0] + f[2]`.
- A new string ending in `i` can come from `e` or `o`, so `g[2] = f[1] + f[3]`.
- A new string ending in `o` can come only from `i`, so `g[3] = f[2]`.
- A new string ending in `u` can come from `i` or `o`, so `g[4] = f[2] + f[3]`.

This reversal is a common source of confusion. For example, the rule “`a` may only be followed by `e`” does not mean that a new `a` can follow only an old `e`. The latter fact comes from looking at every rule that permits `a` as its next character: `e`, `i`, and `u` all do.

**Why a separate next list is necessary**

Each value for length \(L+1\) must be calculated from counts for length \(L\). The code creates `g = [0] * 5` and fills it from `f`. If it overwrote `f` in place from left to right, later assignments could accidentally combine counts from two different lengths. Only after all five new counts are complete does `f = g` advance the DP to the next length.

The loop executes `n - 1` times. It begins with length one, and every iteration appends exactly one character, so after \(t\) iterations `f` represents length \(1+t\). After the final iteration, it represents length \(n\).

**Why addition counts every valid string exactly once**

Consider strings of the new length that end in `a`. Partition them according to their penultimate vowel. The allowed predecessor groups `e`, `i`, and `u` are disjoint because a string has exactly one penultimate character. Removing the final `a` gives a valid old string in exactly one of those groups. Conversely, appending `a` to any old string in one of the three groups creates a valid new string. Thus adding their counts includes every valid new string ending in `a` once and only once.

The same partition argument proves each of the other four transitions. By induction on string length, every entry of `f` has its stated meaning. Every valid length-\(n\) string ends in exactly one of the five vowels, so `sum(f)` gives the total number of valid strings.

**Following the length-two example**

Starting from `[1, 1, 1, 1, 1]`:

- the new `a` count is \(1+1+1=3\), representing `ea`, `ia`, and `ua`;
- the new `e` count is \(1+1=2\), representing `ae` and `ie`;
- the new `i` count is \(1+1=2\), representing `ei` and `oi`;
- the new `o` count is \(1\), representing `io`;
- the new `u` count is \(1+1=2\), representing `iu` and `ou`.

The list becomes `[3, 2, 2, 1, 2]`, whose sum is ten, matching the ten valid two-character strings.

**Modulo arithmetic**

Counts grow exponentially with \(n\), so the result is required modulo \(10^9+7\). The code applies `% mod` to every sum used in a transition. `g[3]` copies `f[2]` without a new remainder operation, which is safe because every stored value in `f` was already reduced. The final `sum(f) % mod` reduces the total of the five states.

Reducing intermediate counts does not change the required answer because modular addition satisfies \((a+b)\bmod M=((a\bmod M)+(b\bmod M))\bmod M\). It also keeps stored integers bounded.

## Complexity detail

Let \(n\) be the requested string length. Initialization handles five states, and each of the \(n-1\) iterations performs a fixed number of additions and assignments across those same five states. The running time is therefore \(O(n)\).

The two lists `f` and `g` each contain exactly five integers, independent of \(n\). At reassignment, an old five-element list becomes reclaimable. Thus auxiliary space is \(O(1)\). Python integers remain bounded by the modulus, so their representation size does not grow with \(n\).

## Alternatives and edge cases

- **Full table by length:** Store all five counts for every length. It uses the same recurrence and \(O(n)\) time but \(O(n)\) space, even though only the preceding row is needed.
- **Matrix exponentiation:** Express the five transitions as a fixed \(5\)-by-\(5\) matrix and raise it to power \(n-1\). This reduces time to \(O(\log n)\) with constant-sized matrices, but it is more algebraically involved and unnecessary for \(n\leq20000\).
- **Top-down memoization:** Cache answers by remaining length and final vowel. It has \(O(n)\) states but also \(O(n)\) cache space and recursion depth, offering no advantage over the iterative five-state form.
- **Brute-force generation:** Enumerating strings branches several ways at each position and grows exponentially. Counting equivalent suffix states is the essential optimization.
- **Length one:** No adjacency restriction is relevant. The initialized five ones sum to five.
- **Modulo placement:** Applying the modulus only at the very end is mathematically correct in Python but creates enormous integers. Reducing each transition keeps arithmetic efficient.
- **Index-to-vowel mapping:** The recurrence is correct only with the order `a, e, i, o, u`. Changing the order without changing every index would silently count the wrong transitions.
- **Outgoing versus incoming rules:** Building `g` requires predecessors of each ending vowel, not successors of that vowel. Reversing the statement’s arrows carefully prevents the most common recurrence error.
