## General

**Each query asks for one target value**

The equation in a query is

$$
\textit{val}\mathbin{\char94}\textit{first}=\textit{second}.
$$

XOR is its own inverse: XORing both sides with `first` cancels that operand. Therefore the substring's required value is uniquely determined:

$$
\textit{val}=\textit{first}\mathbin{\char94}\textit{second}.
$$

Instead of searching the string separately for up to $10^5$ queries, the solution preprocesses substring values once. It builds dictionary `d` so that `d[x]` is the best pair of endpoints for decimal value $x$. Each query then needs one XOR and one dictionary lookup.

**Build binary values incrementally**

For every start index $i$, the inner loop begins with `x = 0` and extends the substring one character at a time. Appending a binary digit $b$ to the right of an existing binary number $x$ produces

$$
2x+b.
$$

The code writes the same operation with bits:

`x = x << 1 | int(s[i + j])`.

Left shift multiplies the old value by two, and bitwise OR inserts the new bit in the now-empty least-significant position. This avoids converting every substring from scratch.

When $s[i:i+j+1]$ has been processed, `x` is exactly its decimal value, and its inclusive endpoints are `[i, i + j]`.

**Why at most 32 characters are examined**

Each query operand is at most $10^9$, which is below $2^{30}$. Their XOR is also below $2^{30}$, so every relevant positive target fits in at most 30 binary digits. A substring with more significant nonzero bits would represent a larger value and could never answer a query.

The code uses a conservative bound of 32 extensions per start. That constant safely covers every possible target. Hence preprocessing examines at most $32n$ substrings rather than all $O(n^2)$ substrings.

The loop also stops when `i + j >= n`, preventing access beyond the end of the string.

**Why zero is handled specially**

If the running value becomes zero, the scanned bits so far are all zeros. The shortest substring representing zero is one character, `"0"`. Extending it with more leading zeros still represents zero but makes a longer answer. Extending until a later one would produce a positive number with leading zeros; the same positive value can be represented by the shorter substring beginning at that later one.

Therefore, after recording zero if needed, `if x == 0: break` safely stops the current start. It discards only candidates that can never beat a shorter representation.

This early break also establishes an important property for positive values: every positive substring examined begins with `"1"`. A positive integer's binary representation without leading zeros has a unique length. Thus two substrings representing the same positive value have the same length.

**Why the first dictionary entry is the required one**

The outer loop visits start indices in ascending order. The assignment occurs only when `x not in d`. For zero, the first recorded occurrence is a one-character zero, which is the shortest possible and has the minimum start.

For a positive value, all examined representations have the same no-leading-zero length. Since starts are visited left to right, the first occurrence automatically has the smallest left endpoint among all shortest occurrences. Later occurrences cannot be preferable, so the dictionary entry must not be overwritten.

This explains both tie-breaking rules: shortest length is guaranteed by eliminating leading-zero extensions, and earliest left endpoint is guaranteed by first insertion.

**Answer queries by direct lookup**

For each `[first, second]`, the list comprehension computes `first ^ second` and asks `d.get(...)` for its endpoints. If no preprocessed substring has that value, `get` returns a fresh `[-1, -1]` default.

For `s = "101101"` and query `[0,5]`, the target is $0\mathbin{\char94}5=5$. Starting at index $0$, the bits `"101"` build value $5$, so the dictionary contains `5: [0,2]`. For query `[1,2]`, the target is $3$, and `"11"` at endpoints `[2,3]` supplies it.

**Why the result is complete**

Every relevant nonzero target has at most 30 significant bits and must be represented by a substring beginning with one after unnecessary leading zeros are removed. The preprocessing starts at every index and extends far enough to inspect that representation. Zero is inspected at every zero start before stopping. Thus every value that can be answered is inserted.

The stored endpoints have the correct value by incremental construction, and the insertion-order reasoning proves they satisfy shortest-length and earliest-start priorities. Dictionary lookup therefore returns exactly the required answer.

## Complexity detail

Let $n$ be the length of `s` and $q$ the number of queries. Each start examines at most 32 characters, so preprocessing takes $O(32n)=O(n)$ time. Each query uses constant-time XOR and expected constant-time dictionary lookup, giving $O(q)$ expected time. Total expected time is $O(n+q)$.

At most 32 values are considered per start, so the dictionary has at most $O(n)$ distinct entries. The answer requires $O(q)$ output space. Excluding required output, auxiliary space is $O(n)$; including it, storage is $O(n+q)$.

## Alternatives and edge cases

- **Search per query:** Scanning all substrings for every target repeats enormous work and is infeasible for $10^5$ queries.
- **Enumerate every substring:** Precomputing all $O(n^2)$ substrings ignores the 30-bit target bound and uses too much time and space.
- **Convert slices with `int(..., 2)`:** This is simpler syntactically but repeatedly copies and reparses characters; incremental shifting reuses the previous value.
- **Target zero:** The correct answer is the earliest one-character `"0"`, never a longer run of zeros.
- **All ones:** Value zero is absent, while positive values are still indexed up to the length cap.
- **Leading zeros:** They never help a positive target because removing them preserves the value and shortens the substring.
- **Duplicate value occurrences:** Positive canonical representations have equal length, so retaining the first start satisfies the tie rule.
- **No occurrence:** Dictionary `get` returns `[-1, -1]` without a separate branch.
- **String shorter than 32:** The boundary check ends extension at the string's last character.
- **XOR inversion:** The target must be `first ^ second`; XORing either operand twice cancels it, which is why no equation solving beyond that is needed.
