## General

**Turn the allowed alphabet into a lookup structure**

A word is consistent when every one of its characters belongs to `allowed`. Repeatedly searching the original string for each character would work, but a set expresses membership directly.

`s = set(allowed)` stores each allowed character once. The input already guarantees that characters in `allowed` are distinct, but set conversion still provides expected constant-time `c in s` tests.

Because all characters are lowercase English letters, the set contains at most 26 entries.

**Check one complete word**

For a word `w`, the expression

`all(c in s for c in w)`

tests its characters lazily from left to right. The inner generator produces one Boolean membership result at a time. `all` returns true only if every produced value is true.

If an unallowed character is found, `all` short-circuits immediately. Later characters in that word do not matter because one violation is enough to make the entire word inconsistent.

If the generator reaches the end without a false membership test, every character belongs to `s` and `all` returns true.

**Count Boolean results**

The outer generator applies that word check to every string in `words`. Python Booleans act as integers during addition: `True` contributes one and `False` contributes zero. Therefore

`sum(all(...) for w in words)`

counts exactly the words for which the condition succeeds.

No list of per-word results is created. `sum` consumes one Boolean at a time and maintains a numeric accumulator.

**Trace the first example**

For `allowed = "ab"`, the set is `{'a', 'b'}`.

- `"ad"` checks `a` successfully, then fails on `d`;
- `"bd"` fails when it reaches `d`;
- `"aaab"` contains only `a` and `b`, so it contributes one;
- `"baa"` also contributes one;
- `"badab"` fails at `d`.

The Boolean sequence is false, false, true, true, false, whose numeric sum is two.

Repeated characters do not need special handling. If `a` is allowed, every occurrence of `a` passes the same membership test. Consistency is about membership, not uniqueness inside a word.

**Why the result is correct**

For any word, `all` returns true exactly when there is no character outside `s`. Since `s` contains exactly the characters of `allowed`, that condition is identical to the definition of consistency.

The outer generator evaluates every word exactly once. Adding one for true and zero for false produces the number of consistent words and neither omits nor double-counts any entry. Thus the returned integer is exactly the requested count.

**Why short-circuiting is safe**

After one forbidden character appears, the conjunction “all characters are allowed” is permanently false. Skipping the remaining checks changes no result. For a consistent word, however, every character must be examined because an unseen final character could still be forbidden.

The source combines this logical short-circuit with lazy generators at both levels, keeping the implementation compact without hiding any stored intermediate collection.

**How the two lazy layers cooperate**

The inner generator belongs to one word and is consumed only until `all` knows that word’s result. The outer generator does not move to the next word until that result is available. `sum` then immediately incorporates the Boolean and requests the next one. At no point must the implementation store all characters, all membership answers, or all word decisions. This evaluation order explains both the early stopping behavior and the constant working-space claim.

## Complexity detail

Let `A = len(allowed)` and define

$$
S = \sum_{w\in\texttt{words}} \lvert w\rvert.
$$

Building the set takes expected $O(A)$ time. Across all words, at most `S` character membership tests are made; short-circuiting may make the actual number smaller. Expected total time is $O(A+S)$, commonly written as $O(S)$ because `A <= 26`.

The set stores at most 26 lowercase letters, so under the fixed alphabet its space is $O(1)$. The nested generators and sum accumulator also use constant auxiliary state. If the alphabet were unbounded, the set term would instead be $O(A)$.

## Alternatives and edge cases

- **26-element Boolean array:** Map each character to `ord(c)-ord('a')` and test a fixed slot. This gives deterministic constant-time lookup and constant space.
- **26-bit mask:** Store allowed letters in one integer and test character bits. It is compact and matches the fixed alphabet but less immediately readable to beginners.
- **Search `allowed` directly:** `c in allowed` can scan up to 26 characters for every word character. It remains bounded here but repeats work that preprocessing avoids.
- **Explicit nested loops:** They can maintain a counter and break on the first forbidden character. This is semantically identical to the generator and `all`.
- **Every word consistent:** Every inner `all` returns true, so the result equals `len(words)`.
- **No word consistent:** Every word encounters a forbidden character and the sum remains zero.
- **One-character allowed set:** Only words composed entirely of repetitions of that character pass.
- **Repeated characters in a word:** Each occurrence is checked, but repetition is allowed and does not make a word inconsistent.
- **Distinctness of `allowed`:** Set construction would remove duplicates even without the guarantee, so behavior remains natural.
- **Nonempty words:** The constraints avoid the vacuous-empty-word case; mathematically `all` of an empty generator would be true.
- **Lowercase-only guarantee:** It keeps the lookup universe at 26 and makes the constant-space claim valid.
