## General

**Reject odd length immediately**

Every valid parentheses string contains one opening and one closing parenthesis per pair, so its length must be even. Editable positions cannot change the length.

The source checks `n & 1` and returns false for odd `n` before scanning. This handles the one-character example even when that character is unlocked.

**Forward scan: every prefix needs enough possible openings**

In the first pass, `x` counts parentheses that can currently act as unmatched openings:

- a locked `'('` definitely supplies an opening, so increment;
- an unlocked position can be chosen as `'('`, so also increment;
- a locked `')'` must consume one available opening.

If a locked closing parenthesis appears when `x == 0`, no earlier position can be assigned as an opening for it. A valid string can never have a prefix with more forced closings than possible openings, so the method returns false.

This pass deliberately treats every unlocked character as the most helpful choice for satisfying closing-prefix constraints. It is a feasibility count, not a final assignment.

**Backward scan: every suffix needs enough possible closings**

Passing the first scan is not sufficient. A string such as too many locked openings near the end may have no later positions available to close them.

The second pass moves right to left and uses the symmetric interpretation:

- a locked `')'` supplies a closing parenthesis, so increment `x`;
- an unlocked position can be chosen as `')'`, so increment;
- a locked `'('` must consume one available closing.

If no closing is available, that locked opening cannot be matched anywhere to its right, so return false.

Together, the scans enforce both directions of valid-parentheses structure.

**Why unlocked characters can play different hypothetical roles**

An unlocked position may be counted as a possible opening in the forward scan and as a possible closing in the backward scan. This does not mean the final string assigns it both characters.

Each scan checks a necessary capacity condition:

- prefixes must have enough flexibility to match forced closes;
- suffixes must have enough flexibility to match forced opens.

For an even-length string, satisfying both families of conditions means the flexible positions can be assigned consistently so the final balance is zero without any prefix becoming negative. The two extreme hypothetical uses establish that neither direction is overconstrained.

**Trace a failing prefix**

If the first character is a locked `')'`, the forward `x` is zero and cannot be decremented. No future editable character can appear before this closing, so failure is final.

By contrast, an unlocked first character increments `x` because it may become `'('` and support a later close.

**Trace a failing suffix**

If the final character is a locked `'('`, the backward scan begins with zero available closings and fails. No earlier character can close an opening that occurs after it.

An unlocked final character can instead become `')'` and provides the needed suffix capacity.

**Why both scans prove feasibility**

A valid assignment clearly passes both tests: scan its actual characters forward to match closes and backward to match opens; treating unlocked positions flexibly cannot reduce capacity.

Conversely, the forward test guarantees no prefix has an unavoidable closing deficit, while the backward test guarantees no suffix has an unavoidable opening deficit. These are exactly the interval constraints on how many unlocked positions must become openings. Since the total length is even, one can choose half the positions as openings within those lower and upper bounds. The remaining unlocked positions become closings, producing balance zero and valid prefixes.

Thus even length plus both successful scans is sufficient, and the final return true is correct.

The strings are read-only; the method decides existence without constructing an assignment.

## Complexity detail

Let $n$ be the common string length.

The forward and backward scans each inspect every index once. Total time is $O(n)$.

Only `n`, `x`, and the loop index are stored. Auxiliary space is $O(1)$.

The early odd-length return can stop immediately, but worst-case work remains linear.

## Alternatives and edge cases

- **Explicit stack of positions:** Storing locked openings and unlocked positions can solve matching but uses $O(n)$ space. The two capacity scans are constant-space.
- **Low/high balance interval:** Track the minimum and maximum feasible unmatched-open counts in one forward pass. This is another $O(n)$, $O(1)$ formulation.
- **Only the forward scan:** It misses unmatched locked openings near the end. The backward symmetry is essential.
- **Odd length:** Impossible regardless of editability.
- **All positions unlocked:** Every even length is feasible.
- **All positions locked:** The scans reduce to ordinary valid-parentheses checks.
- **Locked close at the beginning:** Forward scan rejects it unless an earlier possible opening exists, which it cannot at index zero.
- **Locked open at the end:** Backward scan rejects it.
- **Unlocked original character:** Its current `s[i]` value is irrelevant because it may be changed either way.
- **Equality of counts:** Even length ensures the final assignment can contain equal numbers of opens and closes.
- **No constructed output:** The task asks only whether an assignment exists.
- **Input preservation:** Neither `s` nor `locked` is changed.
