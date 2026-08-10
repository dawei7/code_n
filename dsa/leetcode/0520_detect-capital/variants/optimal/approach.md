## General

There are exactly three accepted capitalization patterns:

- every letter is uppercase;
- every letter is lowercase;
- the first letter alone is uppercase.

Instead of checking those patterns with three separate scans, the solution summarizes the entire word by counting its uppercase letters.

The expression:

`sum(c.isupper() for c in word)`

visits each character `c`. For the guaranteed English-letter input, `c.isupper()` is `True` exactly when `c` is uppercase and `False` when it is lowercase. In Python arithmetic, `True` contributes one and `False` contributes zero to `sum`. Consequently, `cnt` is exactly the number of uppercase characters in `word`.

Let `n = len(word)`. Once `cnt` is known, each valid pattern has a simple numeric signature.

**All letters are lowercase.** This case has no uppercase letters, so `cnt == 0`. Because the input contains only English letters, every character not counted as uppercase is lowercase. No second lowercase scan is necessary.

**All letters are uppercase.** This case has one uppercase letter at every position, so `cnt == len(word)`. Conversely, if the count equals the word length, every character must have contributed one and must be uppercase.

**Only the first letter is uppercase.** This case requires two facts together:

- there is exactly one uppercase letter, expressed by `cnt == 1`;
- that one uppercase letter is at index zero, expressed by `word[0].isupper()`.

The conjunction is essential. A word such as `"fLag"` also has exactly one uppercase letter, but it is not the first character and must be rejected.

The return statement joins these three mutually understandable conditions with `or`:

`cnt == 0 or cnt == len(word) or (cnt == 1 and word[0].isupper())`.

If any accepted pattern holds, its corresponding condition is true. If none holds, the expression is false.

Consider `"USA"`. All three characters contribute one, so `cnt` is three, equal to the word length; the method returns true. For `"leetcode"`, every contribution is zero and the first condition succeeds. For `"Google"`, the count is one and the first character is uppercase, so the third condition succeeds.

Now consider `"FlaG"`. Its uppercase letters are `F` and `G`, making `cnt` equal to two. The count is neither zero nor four nor one, so all conditions fail. For `"flaG"`, the count is one, but the only capital is not at the first position, so the third condition fails as required.

**Why a count is sufficient.** At first glance, reducing a word to one number appears to lose positional information. The first two accepted patterns depend only on whether the uppercase count is zero or the full length, so they need no positions. The only remaining valid pattern has exactly one uppercase letter, and a single direct check identifies whether that letter is at the only allowed position. Thus the solution retains precisely the positional fact that matters and discards the rest.

**Why no special branch is needed for a one-letter word.** A single lowercase character gives `cnt == 0`. A single uppercase character gives `cnt == len(word) == 1`. Either form is valid, and one of the first two conditions accepts it. Although the third condition is also true for the uppercase form, overlapping true conditions do not matter under logical OR.

The source guarantees the word is nonempty, so accessing `word[0]` is safe. Python also short-circuits `or` and `and`, but correctness does not depend on avoiding the access here because index zero always exists.

**Why the boolean expression is complete.** Suppose the method returns true. If the first condition caused that result, every letter is lowercase. If the second did, every letter is uppercase. Otherwise the third condition guarantees exactly one uppercase letter and places it first, so all remaining letters are lowercase. Every true result therefore matches an allowed pattern.

In the other direction, an all-lowercase word produces count zero, an all-uppercase word produces count `n`, and a first-capital-only word produces count one with an uppercase first character. Every allowed word activates at least one condition. Together, these two directions show that the method accepts exactly the requested words.

The generator expression does not construct a transformed copy such as an uppercase or lowercase version of the word. It streams boolean results into `sum`, which keeps the implementation compact and its auxiliary state constant.

## Complexity detail

Let $n$ be the length of `word`. The uppercase-count generator examines every character once. Each `isupper` test and boolean addition is constant work for the constrained English letters, so the running time is $O(n)$.

The variables `cnt` and the loop's current character use constant auxiliary storage. A generator expression yields one boolean at a time rather than building a list of $n$ booleans, so auxiliary space is $O(1)$. The input string itself is not counted as working memory.

Even though the final return conditions are constant-time checks, an asymptotically faster general solution is not possible: a late character can change a valid word into an invalid one, so a correct method may need to inspect all $n$ characters.

## Alternatives and edge cases

- **Inspect the first two characters:** For length at least two, their cases determine whether all later characters must be uppercase or lowercase. This also runs in $O(n)$ time but needs a separate one-character branch.
- **Three direct pattern scans:** Check all-uppercase, all-lowercase, and title-style forms separately. It remains $O(n)$ because three is constant, but repeats traversal logic.
- **Built-in whole-string methods:** `word.isupper()`, `word.islower()`, and `word.istitle()` can express the three cases compactly, though their exact language semantics should be understood.
- **Regular expression:** A full match against uppercase, lowercase, or first-capital patterns works, but introduces regex machinery for a simple linear property.
- **Exactly one capital in the middle:** `cnt == 1` alone is insufficient; checking `word[0]` rejects this invalid arrangement.
- **Several capitals but not all:** The count is between one and `n` and cannot satisfy an accepted signature.
- **Single lowercase letter:** Its uppercase count is zero, so it is valid.
- **Single uppercase letter:** Its uppercase count equals the length, so it is valid.
- **All-uppercase and one character:** More than one condition may describe it, but logical OR still produces the correct boolean result.
- **Nonempty guarantee:** It makes the direct first-character check safe.
- **English-letter guarantee:** It ensures every character is classified as either lowercase or uppercase; digits or punctuation would require more careful semantics.
