## General

The competitive implementation performs a depth-first choice of each IPv4 component. A state records the next unread digit, the dotted prefix built so far, and how many components have already been added. It combines two forms of pruning:

- a remaining-length feasibility test rejects states that cannot possibly fill the remaining component slots; and
- `isValid` rejects illegal component text before recursion.

The source names the component count `dots`. Despite that name, it is incremented once per component, including the fourth; it is not the number of separator characters already finalized in the returned address.

**Meaning of the state**

`restoreIpAddressesRecur(result, s, start, current, dots)` maintains these facts:

- `s[:start]` has been divided into exactly `dots` valid components;
- `current` contains those components in order, each followed by a dot; and
- `s[start:]` is the unconsumed suffix.

Keeping a trailing dot makes extension simple: append the next component and `'.'`. At a complete solution, `current[:-1]` removes exactly that final extra separator.

**Why the digit-count prune is correct**

There are `4 - dots` components still to choose. Each needs at least one digit and can use at most three. If `remaining = len(s) - start`, a solution can exist only when

$$
4-\texttt{dots}\le\texttt{remaining}\le3(4-\texttt{dots}).
$$

The code returns when either inequality fails. This cannot discard a valid address: too few remaining digits would leave an empty component, and too many would force some component beyond three digits. At the initial call, it instantly rejects every source shorter than four or longer than twelve characters.

The same test also guides deeper levels. For example, after two components, six remaining digits are still feasible, while seven are not because only two components remain.

**Trying the next component**

The loop considers endpoints `start`, `start + 1`, and `start + 2`, representing candidate lengths one through three. `len(s) > i` prevents slicing beyond the actual string. The candidate is `s[start:i + 1]`.

`isValid` first rejects an empty candidate, though this caller never supplies one. It then rejects a multi-character substring beginning with `0`; the exact string `"0"` is allowed. Finally, `int(s) < 256` accepts numerical values from zero through 255. Nonnegativity is automatic because the Reference guarantees digits only.

For an accepted component, the code extends `current`, recurses from `i + 1` with one more component, and restores `current` afterward. The removal length is `i - start + 2`: the component length `i - start + 1` plus one trailing dot. This exact arithmetic restores the prefix string to its value before that branch.

Python strings are immutable, so `current += ...` actually binds the local variable to a new string. The recursive call receives that new value, and later slicing rebinds the caller's local variable to the prior text. Sibling calls cannot mutate one another's strings.

**The success condition**

A result is recorded only when `start == len(s)` and `dots == 4`. Therefore all digits have been used and exactly four valid components were chosen. The feasibility prune runs before this condition, but at a complete state both remaining counts are zero, so neither rejection inequality holds.

If the state is not complete, the loop attempts another component. A state with four components but unread digits is already rejected by the prune because zero remaining components cannot hold a positive number of digits. A state that consumed all digits too early is similarly rejected because positive remaining component slots cannot be filled by zero digits.

**Why every answer appears once**

Any valid restored address has a unique ordered tuple of four component lengths. Each length lies between one and three, so the corresponding loop choice exists. Each component passes `isValid`, and every intermediate suffix satisfies the necessary digit-count bounds. The recursion therefore follows that tuple and records the address.

Every recorded path uses four validated components and consumes the string exactly, making it sound. Two paths with different endpoint choices place a dot differently and cannot create the same dotted string, so no set-based deduplication is needed.

## Complexity detail

At most three candidate lengths are explored for each of four fixed component positions. Thus there are at most a constant multiple of $3^4$ recursive states. Validation converts at most three digits, and prefix strings never exceed the fixed maximum address length of fifteen characters. For the specific IPv4 contract, time is therefore $O(1)$ with respect to `len(s)`.

Recursion depth is at most four. `current` has bounded length, and all candidate strings have bounded length. Excluding the returned list, auxiliary space is $O(1)$. The output is also bounded by the finite number of ways to place three dots among at most twelve digits, so even output size is constant in this problem's formal input domain.

If the pattern were generalized to $P$ components of at most $L$ digits, the search would have up to $L^P$ choice paths and carry strings of length $O(PL)$. Calling the present method constant space and time is justified only because IPv4 fixes $P=4$ and $L=3$.

## Alternatives and edge cases

- **Index-path backtracking:** Store chosen component substrings in a list and join only at success. It avoids repeatedly rebuilding `current` strings and is often clearer about restoration.
- **Iterative cut enumeration:** Use three bounded loops for the first three component lengths and let the fourth consume the suffix. It has identical fixed complexity and no recursion.
- **Integer accumulation:** Build a component digit by digit and stop as soon as its value exceeds `255`. This avoids repeated substring conversion and generalizes well to larger segment limits.
- **Trailing-dot invariant:** `current[:-1]` is safe only at success, where four components guarantee a trailing dot exists. Removing it earlier would corrupt the prefix representation.
- **All zeros:** Multi-character zero components are rejected, leaving only `0.0.0.0` for `0000`.
- **Leading zero:** `01` and `00` are invalid even though their parsed integer values are small. The textual check must precede or accompany the numeric check.
- **Numeric ceiling:** `255` passes because it is less than `256`; `256` and larger three-digit strings fail.
- **Impossible lengths:** The initial feasibility test returns immediately for lengths below four or above twelve, including the permitted input lengths thirteen through twenty.
- **Digit-only guarantee:** `int` conversion assumes no sign, dot, whitespace, or letter appears in the source. The challenge contract supplies that guarantee.
- **Any result order:** Shorter next components are attempted first, but the judge accepts any ordering and no sort is necessary.
