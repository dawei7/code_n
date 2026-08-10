## General

**Reduce the global ordering rule to one forbidden local pattern**

The desired strings have the form

$$
a^p b^q
$$

for some nonnegative counts $p$ and $q$. In plain language, there may be an initial block of `a` characters followed by a block of `b` characters, and either block may be empty.

The ordering fails exactly when an `a` appears somewhere after a `b`. In a binary string, that implies there is an adjacent transition `"ba"` at the point where the string moves from a region containing `b` back to `a`.

The exact solution therefore returns

`"ba" not in s`.

**Why an invalid string must contain `ba`**

Suppose a `b` occurs before a later `a`. Consider the first `a` that appears after any `b`. The character immediately before this first resumed `a` cannot be `a`, or then that preceding `a` would itself be an earlier resumed `a`. Since the alphabet contains only `a` and `b`, the preceding character must be `b`.

Thus an invalid global ordering always exposes the adjacent substring `ba`.

**Why finding `ba` proves invalidity**

If the string contains adjacent characters `b` then `a`, that `a` appears after that `b`. It directly violates the statement that every `a` must occur before every `b`.

The forbidden pattern is therefore both necessary and sufficient.

**Trace several shapes**

- `"aaabbb"` has transitions `aa`, `ab`, and `bb` but never `ba`, so it is valid.
- `"abab"` contains `ba` at indices 1 and 2, so it is invalid.
- `"bbb"` contains no `a` and no `ba`, so it is valid by vacuous truth.
- `"aaa"` contains no `b` and is also valid.
- `"b"` and `"a"` are both valid one-character strings.

**Why the binary-alphabet guarantee matters**

The proof that the character before the first resumed `a` must be `b` relies on there being no third character.

If arbitrary characters were allowed, a string such as `"bxa"` would violate the relative order while not containing adjacent `ba`. Under the stated input alphabet, this case cannot occur.

**How Python performs the check**

The `in` operator searches for the fixed two-character substring. Because the pattern length is constant, scanning the input is linear in its length and requires no constructed character collection.

The result is negated by `not`: presence means invalid, absence means valid.

**Connection to a state-machine solution**

An equivalent scan keeps a Boolean saying whether a `b` has been seen. Encountering an `a` after that flag becomes true causes failure.

The substring test compresses this state transition. The first forbidden `a` must be immediately preceded by a `b` at the boundary where the state would fail.

**Why the result is correct**

If the source returns false, `ba` exists and supplies a concrete counterexample pair. If it returns true, no `ba` boundary exists. Once the string first enters a `b` block, it can never return to `a`, so all `a` characters precede all `b` characters.

These two implications prove exact equivalence to the required property.

The string is not modified.

**Another structural characterization**

If `ba` is absent, every adjacent transition is one of `aa`, `ab`, or `bb`. Once an `ab` transition occurs, a later `a` would require the sequence to cross from `b` back to `a` somewhere, creating `ba`. Therefore, at most one category-changing boundary exists, and it can only point from `a` to `b`.

This establishes the block form directly, including the cases where no boundary occurs because the string contains only one character type.

**Why checking non-adjacent pairs is unnecessary**

The original condition quantifies over every `a` and every `b`, which might suggest comparing all index pairs. The first invalid non-adjacent ordering necessarily creates one adjacent forbidden boundary, so a linear substring search is a complete certificate.

This local certificate reduces a potentially quadratic pair interpretation to one scan without weakening the property.

## Complexity detail

Let $n$ be `len(s)`.

Searching for a fixed-length substring takes $O(n)$ time in the worst case. The pattern itself has constant length.

Only constant search state is needed, so auxiliary space is $O(1)$.

The constraints limit $n$ to 100, but the analysis holds for arbitrary length.

## Alternatives and edge cases

- **Seen-`b` flag:** Scan left to right and reject an `a` after the flag becomes true. It has the same $O(n)$ time and $O(1)$ space.
- **Sort and compare:** A sorted binary string has all `a` before `b`, but sorting costs more and constructs or mutates data unnecessarily.
- **Find last `a` and first `b`:** The string is valid when one category is absent or the last `a` precedes the first `b`. This is correct but needs more boundary handling.
- **Only `a` characters:** Valid because there are no `b` characters to be preceded.
- **Only `b` characters:** Valid because there are no `a` characters violating the rule.
- **Single character:** Always valid.
- **Exactly `"ab"`:** Valid boundary direction.
- **Exactly `"ba"`:** Minimal invalid case.
- **Several transitions:** Any transition back from `b` to `a` creates the forbidden substring.
- **Binary alphabet:** Essential to the local-pattern equivalence.
- **Vacuous truth:** Missing one character category satisfies the universal statement.
- **Input preservation:** Substring search is read-only.
- **At most one legal block change:** A valid binary string may transition from `a` to `b` once, but never back.
- **Local certificate:** One adjacent `ba` is enough to disprove the universal ordering.
