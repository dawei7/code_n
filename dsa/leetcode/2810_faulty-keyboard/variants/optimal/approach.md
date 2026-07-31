## General

**Represent reversals as orientation changes**

Reversing the entire accumulated string after every trigger can repeatedly copy a growing prefix. Only the parity of the number of reversals matters: an even count preserves the current orientation, while an odd count flips it. Maintain a Boolean `reversed_order` and toggle it whenever the next input character is `i`.

Store ordinary characters in a deque. Under normal orientation, append the character to the right. Under reversed orientation, the logical end of the displayed text corresponds to the deque's left side, so append there instead. These constant-time end operations preserve the same logical text that literal reversal and appending would produce.

**Restore the logical reading direction once**

The deque is stored in normal direction when the final reversal parity is even and backward when it is odd. If the flag remains set, reverse the deque once at the end, then join its characters. Inductively, after every processed prefix, reading the deque according to the flag equals the screen text from literal simulation. Toggling the flag models a trigger, and insertion at the corresponding end models an ordinary keystroke, so the final join is correct.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Each input character causes one constant-time toggle or deque insertion. The optional final reversal and string join are linear, so total time is $O(n)$. The deque and returned string use $O(n)$ space.

## Alternatives and edge cases

- **Reverse a string immediately:** Literal simulation is simple but each trigger may copy a prefix, producing $O(n^2)$ time.
- **Record segments between triggers:** Segment parity can reconstruct the answer, but a deque expresses the same idea with less indexing bookkeeping.
- With no `i`, the output equals the input.
- Two consecutive triggers cancel because reversing twice restores the prior text.
- A trigger never appears in the output; it performs only the reversal action.
- A final trigger changes only the reading direction and is handled by the final parity check.
- The first character is guaranteed to be ordinary, but the method also handles reversals of an empty deque harmlessly.
