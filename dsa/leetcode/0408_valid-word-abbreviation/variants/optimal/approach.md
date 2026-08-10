## General

**Interpret the abbreviation as instructions**

Each abbreviation token is either:

- a literal lowercase letter that must equal the next unconsumed word character;
- a positive decimal number telling how many word characters to skip.

The exact solution scans `abbr` once while tracking where those instructions would place it in `word`.

Its variables are:

- `i`: the number of word characters already consumed;
- `j`: the current abbreviation index;
- `x`: the numeric skip value currently being accumulated from consecutive digits.

The number is applied when the next literal arrives or when the abbreviation ends.

**Build multi-digit lengths correctly**

For a digit, the update

```text
x = x * 10 + int(abbr[j])
```

appends that decimal digit. Reading `1`, then `2` changes `x` from zero to one to twelve. This ensures `12` means skip twelve characters, not skip one and then skip two.

Consecutive digit characters form one number token. This also reflects the non-adjacent replacement rule: two replaced substrings written next to one another would be indistinguishable from one replacement whose length is their sum, so a valid abbreviation treats a maximal digit run as one skip.

**Reject a leading zero immediately**

The condition

```text
if abbr[j] == "0" and x == 0:
    return False
```

detects a zero at the start of a numeric token. At that moment `x == 0` means no nonzero digit has begun the current number.

This rejects both an abbreviation length of zero, such as `"0"`, and a leading-zero form such as `"01"` or `"010"`. Replacing a nonempty substring requires a positive length, and written lengths may not have leading zeros.

A zero after a nonzero prefix is legal. In `"10"`, `x` is already one when the zero arrives, so it becomes ten rather than being rejected.

**Apply a pending skip before a literal**

When `abbr[j]` is a letter, the code first executes `i += x` and resets `x = 0`. This moves past the abbreviated substring so `i` points to the word position that the literal must match.

It then checks:

```text
if i >= m or word[i] != abbr[j]:
    return False
```

The first condition rejects a skip that reaches or passes beyond the word when another literal still needs a position. The second rejects a different literal character.

On a match, `i += 1` consumes that word character. The abbreviation pointer advances once at the end of every iteration.

**Why the skip is delayed**

The method could advance `i` after finishing a digit run, but it does not know the run is finished until it sees a non-digit or reaches the end. Accumulating in `x` avoids lookahead and keeps the loop simple.

The invariant is that `i` accounts for all fully processed tokens except the still-pending numeric value `x`. The effective consumed word position is therefore `i + x` while digits are being read.

**Validate both inputs at the end**

The loop condition is `i < m and j < n`. It stops when either the word is fully consumed or the abbreviation is exhausted.

The final expression is

```text
i + x == m and j == n
```

Both parts are necessary:

- `i + x == m` requires the matched literals plus any trailing numeric skip to consume the word exactly—neither too few nor too many characters;
- `j == n` requires the entire abbreviation to have been processed.

This correctly handles an abbreviation ending in a number. For `word = "substitution"` and `abbr = "12"`, the scan finishes with `i = 0`, `x = 12`, and `j = n`; the final equality accepts it.

It also rejects trailing abbreviation text after the word is already consumed. If a literal makes `i == m` while `j < n`, the loop stops, but `j == n` fails.

**Tracing `i12iz4n`**

For `word = "internationalization"`:

1. Literal `i` matches word index zero, so `i` becomes one.
2. Digits `1` and `2` build `x = 12`.
3. Literal `i` first advances `i` from one to thirteen, resets `x`, matches the word there, and advances to fourteen.
4. Literal `z` matches the next word position.
5. Digit `4` sets a pending skip of four.
6. Literal `n` applies that skip, matches the final word character, and consumes it.

Both pointers finish exactly at their ends, so the abbreviation is valid.

For `word = "apple"`, `abbr = "a2e"`, `a` matches at index zero and `2` skips to word index three, whose character is `l`, not `e`. The literal comparison returns `False`.

**Why every accepted parse is a valid abbreviation**

Every digit run is positive and has no leading zero due to the immediate check. Each such run skips exactly that many contiguous word characters. Every literal is checked at the next position after previous consumption. Because `i` only moves forward, relative order is preserved.

The final equality proves the instructions consume all and only the word, and `j == n` proves no abbreviation instruction is ignored. Therefore a `True` result corresponds to a valid abbreviation.

Conversely, for a valid abbreviation, decimal accumulation recovers every replacement length, skip application moves to each correct literal, and each literal comparison succeeds. Exact total consumption makes the final test true. Thus the method accepts every valid abbreviation.

## Complexity detail

Let $w$ be the word length and $a$ the abbreviation length.

The index `j` advances once per loop iteration and never moves backward, so each abbreviation character is processed at most once. Word access is by direct index, and `i` advances through literals or jumps by numeric lengths without scanning skipped characters. The exact running time is $O(a)$, which is also within the manifest’s looser $O(w+a)$ bound.

Only lengths, three indices/accumulators, and temporary digit conversion are stored, so auxiliary space is $O(1)$. No substring or parsed-token list is created.

All abbreviation integers fit in a 32-bit integer by contract. Python would safely handle larger accumulated values as well; an oversized skip simply fails the final or literal-bound check.

## Alternatives and edge cases

- **Expand the abbreviation:** Replacing numeric tokens with placeholder characters and comparing could use $O(w)$ extra space and unnecessary construction. Pointer arithmetic performs the same validation directly.

- **Regular expression:** A generated pattern could represent skips, but parsing numeric lengths and leading-zero rules explicitly is clearer and avoids regex complexity.

- **Recursive parser:** Recursion over tokens is possible but adds call-stack state without any branching benefit.

- **Whole word abbreviated:** A numeric abbreviation equal to `len(word)` is accepted by the final `i + x` check.

- **No abbreviation:** When `abbr` contains only letters, every character must match and both strings must end together.

- **Leading zero:** Any numeric token starting with `0` is rejected immediately, including `0` itself.

- **Internal zero in a number:** Forms such as `10` and `101` are legal because the token began with a nonzero digit.

- **Skip too far before a literal:** `i >= m` rejects the missing literal position.

- **Trailing skip too far:** The final equality rejects `i + x > m`.

- **Trailing skip too short:** The same equality rejects `i + x < m`.

- **Word consumed before abbreviation:** The loop exits and `j == n` detects unprocessed abbreviation characters.

- **Adjacent numeric-looking replacements:** A run such as `12` is one length twelve, not lengths one and two. This canonical interpretation matches the rule forbidding adjacent replaced substrings.

- **Literal mismatch:** The method returns immediately because no alternative parse exists under the valid token grammar.
