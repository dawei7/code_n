## General

Every character's score depends on two facts:

1. whether that exact character appears at least once;
2. which of the four character categories contains it.

Its number of repetitions does not matter. The source therefore removes duplicates first with

`st = set(password)`

and then scores each remaining distinct character exactly once.

**Why deduplication is the central operation**

Suppose the password contains `"bbB11#"`. Iterating the original string and adding a score per position would count `b` twice and `1` twice, producing too large a result. The set contains only `{"b", "B", "1", "#"}`, so each identity contributes once.

Uppercase and lowercase versions remain distinct because Python strings are case-sensitive: `"b" != "B"`. This matches the rule that they are different characters and also assigns them different weights.

The order in which a set yields its characters is unspecified, but addition is commutative. The final sum is independent of iteration order.

**Classify one distinct character**

The `if`/`elif` chain assigns exactly one category:

- `ch.islower()` adds one;
- otherwise, `ch.isupper()` adds two;
- otherwise, `ch.isdigit()` adds three;
- otherwise, the source adds five.

Under the contract, the only possible characters are English letters, decimal digits, and `!@#$`. Therefore every character that reaches the final `else` is one of the four allowed special characters.

Using an exclusive chain matters. A character must contribute one category weight, not several independent weights. For the restricted ASCII alphabet, the lowercase, uppercase, digit, and special categories are disjoint.

**Why each contribution is exact**

Take any character appearing in `password`. Set construction places one copy of it in `st` regardless of its frequency. The loop visits that copy once. The category tests select its prescribed weight, so the character contributes exactly once.

Conversely, every member of `st` came from the password. The loop never invents or scores an absent character. Summing the selected weights therefore equals the definition over all and only distinct present characters.

The result begins at zero and increases by a positive category weight for every set member. There are no interactions between characters, so no dynamic programming or position tracking is needed.

**A useful way to view the maximum state**

The allowed alphabet has a fixed size:

- 26 lowercase letters;
- 26 uppercase letters;
- 10 digits;
- 4 special characters.

At most 66 distinct characters can enter `st`, even when the password has length $10^5$. The largest possible score is

$$
26\cdot1+26\cdot2+10\cdot3+4\cdot5=128.
$$

This fixed universe explains why the manifest describes the extra space as constant even though the source uses a set.

**Character methods and the input contract**

Python's `islower`, `isupper`, and `isdigit` understand more Unicode characters than only English ASCII. For example, some non-ASCII letters or digit symbols may satisfy them.

That broader library behavior does not change correctness for this problem because the input contract excludes those characters. Within the allowed set, the methods classify every English lowercase letter, English uppercase letter, and decimal digit as intended.

The final `else` similarly relies on the contract. If an arbitrary punctuation character were supplied, the source would award it five points even though it is not in `"!@#$"`. Such a character is outside the valid input domain; for valid inputs, the branch is exact.

**Why no early termination is used**

The theoretical maximum score is known, so an implementation could return immediately after seeing all 66 allowed characters. The source does not track category masks or use that optimization. It builds the complete set and scores it, which remains linear and straightforward.

Repeated characters can make the password much longer without enlarging the set. Set construction still needs to read every input position, because an unseen character could occur at the end.

## Complexity detail

Let $N$ be the password length and $D$ the number of distinct characters.

Building `set(password)` takes $O(N)$ expected time under normal hash-set behavior. Iterating the set takes $O(D)$ time, with $D\le66$. Total expected time is $O(N)$.

In general terms, the set uses $O(D)$ space. Under this problem's fixed 66-character alphabet, $D$ is bounded by a constant independent of $N$, so auxiliary space is $O(1)$ as reported by the manifest.

The method does not build substrings, copy the password into another length-$N$ sequence, or use recursion. Its scalar accumulator remains bounded by 128 for valid inputs.

## Alternatives and edge cases

- **Score every input position:** This overcounts repeated characters because the rule is based on distinct identities.
- **Use four bitmasks:** One bit per lowercase letter, uppercase letter, digit, and special character can deduplicate using fixed integer state and gives a more literal $O(1)$ representation.
- **Use one 66-entry Boolean table:** Map every allowed character to an index, mark presence, and total marked category weights. This avoids hashing but requires explicit mapping logic.
- **Count category diversity rather than character diversity:** Two different lowercase letters each earn one point. The score is not merely one point for the lowercase category being present.
- **Case-fold the password:** Lowercase and uppercase forms are distinct and have different weights, so normalization would corrupt the result.
- **Repeated character:** Any number of repetitions produces the same one set member and one contribution.
- **Same letter in both cases:** `a` and `A` are distinct; together they contribute $1+2=3$.
- **Repeated special character:** A symbol such as `!` contributes five once, not five per occurrence.
- **All 66 allowed characters:** The score is the maximum 128.
- **One-character password:** The answer is simply that character's category weight.
- **Set iteration order:** It may vary between executions, but integer addition yields the same total.
- **Invalid punctuation:** The source's `else` would score it as special. Correctness relies on the documented restriction to `!@#$`.
- **Non-ASCII characters:** Python classification may accept some, but they are outside the input contract and need no special handling here.
