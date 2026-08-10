## General

The forbidden patterns are subsequences, not necessarily contiguous substrings. Their common feature is that both contain exactly two ones and one zero:

- `011` places the zero before two later ones;
- `110` places the zero after two earlier ones.

The source relies on a complete structural characterization of coherent strings. Every coherent binary string belongs to at least one of three families:

1. it contains at most one `1`;
2. it consists entirely of `1` characters; or
3. it has exactly two ones, one at each endpoint, with only zeros between them.

The method computes the Hamming-distance cost to each family and returns the minimum.

**Strings with at most one one are always coherent**

Both forbidden subsequences require two occurrences of `1`. If a string contains zero or one one, neither `011` nor `110` can be formed, regardless of where its zeros occur.

If the original string contains `ones` ones, the cheapest target in this family keeps one existing one when possible and flips every other one to zero. Its cost is

$$
\max(0,\texttt{ones}-1).
$$

There is no reason to flip a zero to one: that would add cost without helping the “at most one” condition.

**All-one strings are coherent**

Without a zero, neither forbidden pattern can occur. Transforming the input into all ones requires flipping every zero:

$$
n-\texttt{ones}.
$$

These are the first two candidates in:

```text
answer = min(max(0, ones - 1), n - ones)
```

**What happens when a coherent string has a zero and at least two ones**

Suppose a zero occurs at some position. To avoid `110`, at most one one may appear before that zero. To avoid `011`, at most one one may appear after it.

Therefore, if any zero exists, a coherent string can contain at most two ones in total.

The cases with zero or one one are already covered. Consider exactly two ones.

- No zero may occur before the first one, because that zero would have two ones after it and form `011`.
- No zero may occur after the second one, because that zero would have two ones before it and form `110`.
- Zeros between the two ones are safe: each has only one one before and one one after.

Thus a coherent string with exactly two ones and at least one zero must have form

$$
1\,0^*\,1.
$$

The two ones are the first and last characters, and every interior character is zero. For length two, this form is simply `11` and overlaps the all-ones family.

**Cost of the endpoint pattern**

For $n\ge2$, the unique target of the third family is:

```text
1 + ("0" repeated n - 2 times) + 1
```

Its flip cost has three parts:

- one if the first character is currently zero;
- one if the last character is currently zero; and
- one for every interior character currently equal to one.

The source computes:

```text
(s[0] == "0") + (s[-1] == "0") + s[1:-1].count("1")
```

In Python, Booleans behave as integers in addition: true contributes one and false contributes zero.

The method compares this cost with the first two families and keeps the minimum.

**Why these families are exhaustive**

Take any coherent target.

- If it has at most one one, it belongs to family 1.
- If it has at least two ones and no zero, it is all ones and belongs to family 2.
- If it has at least two ones and at least one zero, the earlier argument forces it to have exactly two ones, with no zero outside them. It belongs to family 3.

No other coherent shape exists. Therefore the closest coherent string must be the closest member of one of these families.

Within family 1, keeping one existing one minimizes flips. Family 2 has one unique target. Family 3 also has one unique target for fixed length. The three computed costs are exact family minima, so their minimum is the global answer.

**Examples**

For `s = "1010"`, there are two ones.

- Reducing to at most one one costs one.
- Making all ones costs two.
- Making endpoint pattern `"1001"` costs two.

The answer is one, matching a flip to `"0010"`.

For `"0110"`:

- at-most-one-one cost is one;
- all-ones cost is two;
- endpoint-pattern `"1001"` costs four.

Again the answer is one.

For `"1000"`, there is already only one one, so the first candidate is zero.

**Why subsequence scope matters**

Checking only contiguous occurrences would be insufficient. A zero and two ones can form a forbidden subsequence even with other characters between them. The global count-and-position characterization accounts for every possible choice of three increasing indices at once.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. `s.count("1")` scans the full string in $O(N)$ time. For $N\ge2$, `s[1:-1].count("1")` scans the interior, adding another $O(N)$ pass.

Total time is

$$
O(N).
$$

The manifest states $O(1)$ space, but the exact Python source creates `s[1:-1]`. String slicing allocates a new string of length $N-2$, so peak auxiliary space is

$$
O(N)
$$

as written.

The same arithmetic could be implemented in $O(1)$ auxiliary space by deriving the interior-one count from `ones` and the two endpoints, but that optimization is not present in `solution.py`.

All other variables are scalar integers or Booleans.

## Alternatives and edge cases

- **Dynamic programming over forbidden-subsequence automata:** This can minimize flips for arbitrary forbidden patterns, but the three-family characterization makes this instance much simpler.
- **Enumerate all coherent targets:** There are only structured families, so explicit exponential enumeration is unnecessary.
- **Avoid the slice:** Compute interior ones as `ones - (s[0] == "1") - (s[-1] == "1")` to retain $O(1)$ auxiliary space.
- **Length one:** Every one-character string is coherent; the source skips the endpoint-pattern calculation and returns zero.
- **Length two:** No length-three subsequence exists, so every string is coherent. The three candidate costs always include zero.
- **No ones:** The first family costs zero.
- **Exactly one one:** The first family costs zero regardless of its position.
- **All ones:** The second family costs zero.
- **Exactly two endpoint ones:** The third family costs zero when every interior character is zero.
- **Two ones with an outside zero:** That zero creates `011` or `110`, so at least one flip is necessary.
- **Three or more ones plus any zero:** The zero has at least two ones on one side or the other, making a forbidden subsequence unavoidable.
- **Subsequence versus substring:** Characters need not be adjacent, so local window checking alone cannot establish coherence.
- **Manifest mismatch:** Runtime is linear as declared, but Python's interior slice makes actual auxiliary space linear rather than constant.
