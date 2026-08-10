## General

**Reduce variance to an ordered pair of characters**

For any chosen substring, its variance is the greatest difference between the occurrence counts of two characters present in it. If one character `a` is treated as the more frequent character and another character `b` as the less frequent one, the relevant difference is

$$
\#a - \#b.
$$

The solution examines every ordered pair `(a, b)` of distinct lowercase letters. Order matters: `(a, b)` maximizes “count of `a` minus count of `b`,” while `(b, a)` maximizes the opposite difference.

Once the pair is fixed, each `a` contributes plus one, each `b` contributes minus one, and every other letter contributes zero. The task becomes finding a maximum-sum substring under one extra rule: it must contain at least one `b`, because both characters used in the difference must be present.

**Why all ordered pairs cover the original definition**

Take a substring that achieves the global largest variance. Choose within it a most frequent character as `a` and the compared less frequent character as `b`. The permutations loop eventually examines this orientation, and the transformed substring's sum is exactly its count difference.

Conversely, every value accepted for an ordered pair comes from a contiguous substring containing `b`, and any positive accepted value necessarily contains `a` as well. It is therefore a legitimate difference between two present characters. The initial answer zero covers cases where no positive difference exists, including strings whose letters all appear at most once and the definition's allowance to compare a character with itself.

**Give the two DP states precise meanings**

For one ordered pair, `f = [0, -inf]` holds two best scores while scanning left to right:

- `f[0]` is the greatest score of a suffix of the processed text that contains no `b`. Because only `a` has positive weight, it is effectively the number of `a` characters since the most recent `b`, with an empty suffix of score zero always allowed.
- `f[1]` is the greatest score of a suffix that contains at least one `b`. This is the state eligible to update the answer.

Initializing `f[1]` to negative infinity marks “no valid substring containing `b` has been formed yet.” It prevents an `a`-only prefix from being mistaken for a valid two-character candidate.

Letters other than `a` and `b` have weight zero. The code leaves both states unchanged on them, which is equivalent to extending the current candidate across a zero-weight character. Such characters may appear inside the chosen substring without affecting the two counts.

**Update when the current character is** `a`

When `c == a`, appending it increases both kinds of candidate by one:

`f[0], f[1] = f[0] + 1, f[1] + 1`.

The first state remains free of `b` and gains one `a`. The second already contains `b` and also gains one `a`. A new `a`-only candidate cannot enter `f[1]` because it still lacks the required minor character.

Python's tuple assignment computes both right-hand values from the old state before assigning either left-hand entry, although here sequential additions would yield the same numbers.

**Update when the current character is** `b`

Appending `b` subtracts one from the pair score and offers two ways to form the best valid state:

`f[1] = max(f[1] - 1, f[0] - 1)`.

The first option extends a candidate that already contained a `b`. The second option takes the best recent suffix containing no `b` and uses the current character as its first `b`. Both results now satisfy the required-minor condition.

Afterward, `f[0] = 0`. No non-empty suffix ending at the current position can be free of `b`, so the only permitted zero-`b` suffix is the empty one that begins after this character. Future `a` characters can grow that fresh state.

This transition is a constrained form of Kadane's algorithm. The `f[0] - 1` option performs the restart precisely when a new minor character arrives, while `f[1]` preserves a previous minor when keeping it is better.

**Why no remaining-minor counter is needed**

A common solution tracks counts and resets a negative segment only when another minor remains later. The exact source instead allows `f[1]` to stay negative. A lone `b` creates score minus one rather than being discarded. Later `a` characters can raise that valid state to zero and then to a positive answer.

At a later `b`, the maximum between extending `f[1]` and starting from `f[0]` decides whether retaining the earlier minor is useful. Because the required negative contribution is represented directly in `f[1]`, the algorithm never loses the last available `b` and does not need advance frequency counts.

**Update the global answer only from the valid state**

After processing each character, the code compares `ans` with `f[1]`. It never uses `f[0]` because that state explicitly contains no `b`. Before the first `b`, `f[1]` remains negative infinity and cannot update the answer.

Once a `b` has appeared, `f[1]` may be negative, zero, or positive. Since `ans` begins at zero, negative one-character candidates do not reduce it. A positive `f[1]` represents a substring with more `a` than `b` and at least one of each.

**Trace the state around a minor character**

For ordered pair `(a, b)` and a relevant sequence `"aababb"`, start with `[0, -inf]`:

- two `a` characters make `f[0] = 2` while `f[1]` is still invalid;
- the first `b` sets `f[1] = 2 - 1 = 1` and resets `f[0]` to zero;
- the next `a` raises the states to `[1, 2]`;
- the next `b` chooses between extending the valid score to one and introducing this `b` after the one-`a` suffix for score zero, so `f[1] = 1`;
- the last `b` again subtracts one, leaving the best valid score zero.

The global answer retains the earlier value two even when later extensions reduce the current best ending score.

**Why the states remain optimal**

Assume the two states hold their stated best scores before a character. A zero-weight character changes no candidate score. On `a`, every relevant suffix gains exactly one, and no state changes validity. On `b`, every now-valid suffix either already contained `b` or obtains its first `b` from the current character; the two terms in the maximum cover these exhaustive cases. Resetting `f[0]` to the empty suffix is forced because the current suffix cannot otherwise exclude `b`.

By induction, `f[1]` is the best valid pair score ending at the current scan frontier. Taking its maximum over all frontiers finds the best substring for that pair, and taking the maximum over all ordered pairs finds the largest variance.

**Interpret the fixed alphabet loop**

`permutations(ascii_lowercase, 2)` generates 26 times 25 ordered pairs and never repeats a character within a pair. The explicit `if a == b` is therefore redundant but harmless. The code scans `s` even for pairs whose letters are absent; those scans cannot improve `ans`, but the alphabet size is fixed and the asymptotic bound remains linear in `n`.

## Complexity detail

Let `n` be the string length and `A = 26` the alphabet size. There are `A(A-1) = 650` ordered pairs, and each pair performs one `O(n)` scan. Time is `O(A^2 n)`, which simplifies to `O(n)` for the fixed lowercase-English alphabet.

For each pair, the algorithm stores two DP values and loop characters. The permutations iterator also has size bounded by the fixed alphabet. Auxiliary space is `O(1)` with respect to `n`. If the alphabet were variable, the time should remain written `O(A^2 n)`.

The string is never copied per pair and is not modified.

## Alternatives and edge cases

- **Modified Kadane with major/minor counts:** Track both counts and the number of remaining minor characters before resetting. It is correct but uses a different state formulation from the exact two-value DP.
- **Enumerate every substring:** Counting all characters in all `O(n^2)` substrings is too slow for `n = 10^4`.
- **Prefix counts for every pair:** They make a fixed substring query quick but still leave quadratically many substrings to test.
- **Only unordered pairs:** That can miss which character is the positive side of the difference; both orientations must be considered.
- **Ordinary Kadane without a required-minor state:** It may choose a substring of only `a` characters, which is invalid for comparing two present characters.
- **One distinct character:** No ordered pair can form a positive valid difference, so `ans` remains zero.
- **All characters distinct:** Any substring has equal maximum relevant counts, and the returned variance is zero.
- **Minor appears before all majors:** `f[1]` is allowed to begin negative and then grow, preserving this valid optimal pattern.
- **Minor appears only once:** The state never discards the requirement; later majors can use that single occurrence.
- **Other letters inside a candidate:** They have zero pair weight and may remain in the substring without changing its score.
- **Equal counts:** A valid pair score of zero does not exceed the initialized answer but is correctly represented.
- **Negative infinity:** It marks an impossible “contains minor” state and remains impossible under added majors until a minor creates a real candidate.
- **Redundant equality check:** `permutations(..., 2)` already yields distinct letters, so the check never triggers.
- **Absent pair characters:** Scanning them is wasted constant-factor work but cannot create an incorrect positive state.
- **Input preservation:** The method reads `s` 650 times and performs no mutation.
