## General

Process `s` from left to right while storing the fully reduced processed prefix in a stack. Before a new character arrives, the stack has no removable adjacent pair: every operation wholly inside that prefix has already been performed in leftmost order.

Appending a character can create only one new eligible pair, between that character and the stack top. Their alphabet positions are consecutive exactly when their absolute difference is $1$, or $25$ for the circular `a`/`z` boundary. If they are consecutive, pop the stack top and discard the new character. Otherwise, push the new character. After either action, the stack is again the final reduced form of the prefix seen so far.

This simulates the required order rather than choosing arbitrary pairs. Any pair lying entirely in an earlier prefix is resolved before a later character is examined, so it is necessarily removed before every pair farther to the right. Each input character is pushed at most once and popped at most once. Joining the stack after the scan yields the final string.

## Complexity detail

Let $n=\lvert s \rvert$. Every character causes one constant-time stack decision and participates in at most one pop, so the time complexity is $O(n)$. The stack can contain all $n$ characters when no pair is removable, giving $O(n)$ auxiliary space; the returned string also has length at most $n$.

## Alternatives and edge cases

- **Repeatedly scan and splice the string:** Literal leftmost simulation is correct, but rescanning from the beginning and rebuilding the string after every deletion can take $O(n^2)$ time.
- **Remove any available pair:** This violates the contract because reductions need not have a unique outcome; for `abc`, removing `ab` leaves `c`, whereas removing `bc` would leave `a`.
- **Compare only code-point difference one:** That misses the circular `az` and `za` pairs, whose code-point difference is $25$.
- **Equal adjacent letters:** Their difference is zero, so they remain in the string.
- **Newly exposed pair:** A deletion may make two characters consecutive in the current string; the stack exposes that relationship naturally to the next processed boundary.
- **Single character or stable input:** Nothing is removed, and the original content is returned unchanged.
