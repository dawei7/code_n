## General

**There are only two possible alternating targets**

Once the first character of a binary alternating string is chosen, every later character is forced. A target beginning with zero must be:

`010101...`

and a target beginning with one must be:

`101010...`.

There are no other possibilities because every adjacent character must differ and the alphabet contains only zero and one. The task therefore reduces to counting how many positions differ from each of these two targets and taking the smaller count.

The exact solution explicitly counts mismatches with only the zero-starting target. It derives the other count as a complement.

**Generate the expected character from index parity**

The two-character string `'01'` acts as a tiny lookup table. Expression `i & 1` is zero when index `i` is even and one when it is odd:

- At an even index, `'01'[0]` is `'0'`.
- At an odd index, `'01'[1]` is `'1'`.

Thus `'01'[i & 1]` is exactly the expected character of the alternating target that begins with zero.

Using bitwise AND with one is equivalent to `i % 2` for nonnegative indices. It extracts the least significant bit, which records parity.

**Count mismatches lazily**

The generator:

`c != '01'[i & 1] for i, c in enumerate(s)`

examines every input position. The comparison is `True` exactly when the current character must be flipped to match the zero-starting target.

Python's `sum` treats true as one and false as zero, so:

`cnt = sum(...)`

is the number of required operations for target `0101...`. The generator is lazy and does not allocate a separate expected string or Boolean list.

Each mismatched position costs exactly one operation because an operation flips one chosen binary character. Positions are independent: changing one character neither changes another nor shifts indices.

**Derive the second target's cost by complement**

At every index, the one-starting target expects the opposite character from the zero-starting target. Since the input character is also either zero or one, it matches exactly one of the two targets and mismatches exactly the other.

Therefore, if `cnt` positions mismatch the zero-starting pattern, the remaining `len(s) - cnt` positions mismatch the one-starting pattern.

This complementary relationship is why the source does not need a second pass or second mismatch counter. It returns:

`min(cnt, len(s) - cnt)`.

The smaller value is the fewest flips needed to reach either legal alternating string.

**Trace an example**

For `s = "0100"`, expected zero-starting characters are zero, one, zero, one. The first three positions match, while the last input zero differs from expected one. Hence `cnt = 1`.

The opposite target would mismatch the other three positions, so its cost is `4 - 1 = 3`. The minimum is one, matching the operation that flips only the final character.

For `s = "1111"`, the zero-starting target differs at even indices zero and two, giving `cnt = 2`. The one-starting target differs at odd indices one and three, and its complementary cost is also two.

**Why local adjacent fixes are less direct**

One might scan for equal adjacent pairs and flip a character whenever a violation appears. A flip affects both its left and right adjacencies, so greedy local choices can require careful tie handling.

Comparing against the only two complete valid targets avoids that interaction. Every position's required action is known independently once a target is chosen.

**Why the returned value is correct**

Any alternating binary string must be one of the two parity patterns. For a fixed pattern, every mismatched position must be changed at least once, and flipping each mismatch once is sufficient. Its mismatch count is therefore the exact minimum cost to reach that pattern.

`cnt` is the exact cost of the zero-starting pattern, and `len(s) - cnt` is the exact cost of the one-starting pattern. Taking their minimum examines every possible alternating result, so the returned number is globally optimal.

## Complexity detail

Let $n$ be the string length. `enumerate` visits each character once. Index-parity calculation, a two-character lookup, comparison, and Boolean addition are all $O(1)$ per position. Total time is $O(n)$.

The solution stores only `cnt` plus generator iteration state. It does not construct either target string or a mismatch array, so auxiliary space is $O(1)$, matching the manifest.

The input string is immutable and is never copied or modified. `len(s)` is constant time in Python.

## Alternatives and edge cases

- **Count both targets explicitly:** Maintain two counters in one pass. It is correct but redundant because the counts sum to $n$.
- **Construct target strings:** Comparing with materialized `0101...` and `1010...` strings uses $O(n)$ extra space unnecessarily.
- **Greedy adjacent repair:** It can be made correct, but changes influence two neighboring relationships and obscure the two-target structure.
- **Dynamic programming:** Tracking the previous chosen bit is excessive because only two deterministic patterns exist.
- **One-character string:** Both possible characters are alternating; one target costs zero, so the answer is zero.
- **Already alternating:** One mismatch count is zero and is returned.
- **All zeros:** Roughly half the odd or even positions must flip, depending on the chosen start.
- **All ones:** The symmetric half-position result applies.
- **Odd length:** The two targets have different counts of zeros and ones, but complementarity still holds position by position.
- **Even length:** Each target contains equally many zeros and ones; mismatch costs still need not differ.
- **Equal costs:** Either target is optimal, and only the operation count is returned.
- **Bitwise parity:** `i & 1` is safe because enumerate indices are nonnegative integers.
- **Binary alphabet:** Complementary mismatch counts rely on each input character being exactly zero or one.
- **No mutation needed:** The method calculates the minimum count without constructing the changed string.
