## General

A subsequence becomes invalid only when its selected elements contain three adjacent positions **inside the subsequence** with the same parity. The actual values do not matter beyond whether they are even or odd.

When extending a stable subsequence with a new array element, the entire history is unnecessary. The only information that can determine whether appending is safe is:

- the parity of the subsequence's last selected element; and
- whether the terminal run of that parity currently has length one or length two.

A stable subsequence can never have a terminal same-parity run longer than two. This gives only four states, regardless of the input length.

**Meaning of the four counters**

The source stores:

`endings = [[0, 0], [0, 0]]`

The first index is parity: zero for even and one for odd. The second index distinguishes the terminal run length:

- `endings[p][0]` counts nonempty stable subsequences ending in exactly one consecutive selected element of parity `p`;
- `endings[p][1]` counts nonempty stable subsequences ending in exactly two consecutive selected elements of parity `p`.

“Exactly one” does not mean the whole subsequence has length one. It means the immediately preceding selected element, if one exists, has the opposite parity. For example, parity pattern even-odd-even has a final even run of length one.

Every nonempty stable subsequence belongs to exactly one of these four categories, so summing all four counters after processing the array gives the requested answer. The empty subsequence belongs to none of them and is correctly excluded.

**Processing the current element**

For a current `value`, the source obtains its parity with:

`parity = value & 1`

The least significant bit is zero for even integers and one for odd integers. The opposite parity is:

`other = parity ^ 1`

XOR with one toggles zero to one and one to zero.

The algorithm counts new subsequences that use the current array occurrence as their final selected element. Existing subsequences that skip this occurrence remain in the state because the old counters are never cleared.

There are exactly three valid ways to create a new subsequence ending at the current occurrence.

**Start a singleton**

Selecting only the current element creates one stable subsequence. Its terminal run has length one.

**Append after the opposite parity**

The current element may be appended to every stable subsequence ending with the opposite parity, regardless of whether that old terminal run has length one or two. Changing parity breaks the old run and starts a new run of length one.

Combining the singleton and both opposite-parity states gives:

`new_run_one = 1 + endings[other][0] + endings[other][1]`

The source applies the modulus to this sum immediately.

**Append after one equal-parity ending**

The current element may also be appended to a subsequence whose terminal run consists of exactly one element of the same parity. The new terminal run then has length two:

`new_run_two = endings[parity][0]`

There is deliberately no transition from `endings[parity][1]`. Such a subsequence already ends with two selected elements of the current parity. Appending a third would create the forbidden run of three consecutive equal parities.

**Why the new counts are computed before mutation**

After calculating both values from the old state, the source performs:

`endings[parity][0] = endings[parity][0] + new_run_one`

`endings[parity][1] = endings[parity][1] + new_run_two`

with the modulus applied to each assignment.

The additions retain subsequences that do not select the current element while adding those that do. The opposite-parity row is unchanged because a new subsequence ending at the current element cannot end with the opposite parity.

It is essential that `new_run_two` be read before `endings[parity][0]` receives `new_run_one`. Otherwise, newly created subsequences using the current occurrence could immediately be extended by that same occurrence a second time. Computing both transition values first preserves the zero-or-one choice for each array position.

**A complete trace for three odd values**

For `nums = [1, 3, 5]`, only the odd row changes.

After processing $1$:

- one singleton is created;
- the odd states are `[1, 0]`.

After processing $3$:

- `new_run_one = 1` creates singleton `[3]`;
- `new_run_two = 1` extends `[1]` to `[1, 3]`;
- retained and new states total `[2, 1]`.

After processing $5$:

- `new_run_one = 1` creates singleton `[5]`;
- `new_run_two = 2` extends each prior one-odd-run subsequence, creating `[1, 5]` and `[3, 5]`;
- the states become `[3, 3]`.

Their sum is six. The length-three subsequence `[1, 3, 5]` is absent because extending the run-length-two state was forbidden.

**Why each stable subsequence is counted exactly once**

Take any nonempty stable subsequence and look at the index of its final selected element. When the outer loop reaches that index, remove the final element temporarily.

- If nothing remains, the subsequence is generated by the singleton term.
- If the prior last parity differs, the shorter subsequence lies in one of the two `other` states and is extended into `new_run_one`.
- If the prior last parity is equal, stability guarantees the shorter subsequence's same-parity terminal run has length exactly one; it lies in `endings[parity][0]` and is extended into `new_run_two`.

These cases are mutually exclusive and cover every stable subsequence. The final selected index is unique, so the same index sequence cannot be generated during two different iterations.

Every generated subsequence is also stable. Singleton subsequences are safe; switching parity starts a run of length one; and extending a same-parity run is allowed only from length one to length two. No transition can create length three.

Together, these facts ensure that the four counters contain all and only stable nonempty subsequences after every processed prefix.

**Applying the modulus**

An array of length $n$ has up to $2^n-1$ nonempty subsequences, so the raw count grows far beyond ordinary fixed-width integer ranges. All transitions use only addition, and the requested result is modulo

$$
10^9+7.
$$

Reducing each updated count modulo this number preserves the final remainder while keeping state values bounded. The source also applies one final modulus after summing the four counters.

## Complexity detail

Let $n$ be the length of `nums`.

The algorithm visits each element exactly once. Every iteration performs a constant number of parity operations, additions, state accesses, and modulus operations. Its total running time is $O(n)$.

This is a major reduction from enumerating all $2^n$ subsequences. The four-state compression works because future validity depends only on the final parity run, not on the complete selected history.

The `endings` matrix always contains four counters. All other variables are scalars, so auxiliary space is $O(1)$. The counts remain bounded by the modulus, and no recursion stack or input-sized collection is used.

Reading all elements is necessary: changing the parity of an unexamined final element can change the number of stable subsequences. Therefore, the linear running time is asymptotically optimal.

## Alternatives and edge cases

- **Enumerate every subsequence:** Checking all $2^n-1$ nonempty subsequences is impossible for $n$ up to $10^5$.
- **Store the full ending parity string:** Future transitions need only its final run length capped at two. Keeping more history wastes space and creates many equivalent states.
- **Track only the last parity:** This loses the distinction between a run of length one, which may be extended, and a run of length two, which may not.
- **Count contiguous subarrays:** The restriction concerns consecutive elements inside the selected subsequence, not neighboring positions in `nums`. Skipped array elements do not break a parity run unless an opposite-parity element is selected.
- **All elements have one parity:** Only subsequences of lengths one and two are stable. The transitions count all singleton index choices and all two-index choices while refusing every third same-parity extension.
- **Alternating parities:** Every subsequence is not automatically stable because skipping elements can bring three values of one parity together. The DP evaluates parity adjacency in the selected order correctly.
- **One element:** The singleton term creates exactly one stable subsequence, and the final sum returns one.
- **Repeated numerical values:** Occurrences at different indices define different subsequences. The DP processes each position separately even when values are equal.
- **Large element values:** Only `value & 1` is used. Magnitude has no effect beyond parity.
- **Modulo timing:** Reducing after each update is safe because addition respects modular arithmetic and prevents counters from growing exponentially.
