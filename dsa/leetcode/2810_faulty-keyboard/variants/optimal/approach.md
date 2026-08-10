## General

**Simulate the faulty key literally.** The input is processed from left to right. For an ordinary character, that character appears at the end of the text currently displayed. When the character is `"i"`, it is not typed into the display; instead, the entire displayed text is reversed.

The solution stores the current displayed characters in a Python list named `t`. Lists support efficient appending and can be joined into one string at the end.

**Maintain the exact displayed text after every input character.** Initially, no keys have been processed and `t` is empty, matching the empty display. For each character `c`:

- If `c == "i"`, the assignment `t = t[::-1]` creates a reversed copy of the current list and rebinds `t` to it.
- Otherwise, `t.append(c)` adds the ordinary character to the right end.

This is a direct simulation rather than a symbolic representation of pending reversals. After every loop iteration, reading `t` from left to right gives exactly the text the faulty keyboard would currently show.

For example, process `"string"`. The characters `s`, `t`, and `r` append to form `str`. The next character is `i`, so the list becomes `rts` and no `i` is retained. Then `n` and `g` append, producing `rtsng`.

**Why the invariant proves correctness.** The base case is correct because both the simulated list and keyboard display are empty. Assume `t` matches the display before processing a character. For an ordinary character, both the keyboard rule and the algorithm append that same character, preserving equality. For `i`, both reverse their existing sequence and omit the key itself, again preserving equality. Induction covers the entire input. Finally, `"".join(t)` converts the correct character sequence into the required string without adding separators.

**Consecutive faulty keys work naturally.** Reversal is its own inverse. Two consecutive `i` characters reverse the display twice and restore its prior order. The implementation performs the two slices and arrives at that result without special handling. If the display is empty, reversing it still yields an empty list.

**The input string itself is never modified.** Python strings are immutable. The loop reads characters from `s` and changes only `t`. The returned value is newly constructed.

**The exact implementation is not the deque-and-parity technique in the manifest.** The variant metadata describes keeping track of whether the logical direction is reversed and using a deque, which can solve the problem in linear time. The exact code performs a physical full-list reversal every time it sees `i`. That difference affects the worst-case time complexity.

Suppose the string begins with many ordinary characters and is followed by many `i` characters. Each faulty key copies and reverses a list whose length is already large. Repeating that operation can copy a quadratic total number of elements. The constraint `len(s) <= 100` keeps this straightforward simulation fast in practice, but it is not asymptotically linear in all inputs.

**Assignment rather than in-place reversal.** `t[::-1]` constructs a new list. The old list becomes eligible for reclamation once `t` is rebound, assuming there are no other internal references to it. Using `t.reverse()` would reverse the same list in place and avoid a second simultaneously live full list, but it would still take linear time per faulty key and therefore have the same quadratic worst-case time.

**The result excludes every `i`.** The special branch does not append `c`. This is easy to overlook: the key triggers an action rather than inserting a character. Ordinary occurrences of every other lowercase letter, including characters repeated many times, are appended exactly once.

**Why a final reversal alone is insufficient.** It might seem possible to count how many `i` keys appear and reverse the final ordinary-character string based only on parity. That loses timing information. Ordinary characters typed after a reversal append to the currently reversed display rather than being moved by earlier reversals. For example, reversing `ab` and then typing `c` gives `bac`, not the reversal of `abc`. Any optimized solution must account for changing insertion direction, not merely total parity.

## Complexity detail

Let $n$ be the input length. Appending an ordinary character is amortized $O(1)$. When a faulty key occurs after $r$ ordinary characters have been retained, `t[::-1]` takes $O(r)$ time and allocates a list of length $r$.

In the worst case, $\Theta(n)$ faulty keys each reverse a list of length $\Theta(n)$, so total time is $O(n^2)$. The final join takes $O(n)$ time and does not change the bound. A matching quadratic pattern is an ordinary prefix of roughly half the input followed by roughly half faulty keys.

At most $n$ ordinary characters are retained. During a slice reversal, the old and new lists can both be live briefly, but each is $O(n)$. The final string is also $O(n)$. Peak auxiliary space is $O(n)$, whether or not the output is counted asymptotically.

The manifest's $O(n)$ time applies to the absent lazy-direction/deque approach, not to this source. With $n \le 100$, the maximum amount of copying is small, but constraints do not change the conceptual worst-case bound in terms of $n$.

## Alternatives and edge cases

- **Deque plus direction flag:** Toggle a Boolean instead of reversing stored characters. Append new characters to the logical back, which is one physical end or the other depending on the flag, and materialize in the correct direction once. This gives $O(n)$ time and $O(n)$ space and matches the manifest.
- **List plus two buffers:** Accumulate runs between faulty keys and combine them with direction awareness. This can also avoid repeated full reversals but is more complex than a deque.
- **In-place `list.reverse`:** It avoids allocating a new list for every reversal but still scans the current output each time, so worst-case time remains $O(n^2)$.
- **No faulty key:** Every character appends, and the result equals the input.
- **Faulty key at the beginning:** The stated contract says the first character is not `i`, but reversing an empty list would still be harmless.
- **Consecutive faulty keys:** Every pair cancels in effect, although the exact source still pays for both reversals.
- **Faulty key after one character:** Reversing a one-element display changes nothing, but the key is still omitted.
- **All later characters ordinary:** They append after whatever orientation the most recent physical reversal produced.
- **Repeated ordinary letters:** Each occurrence is a separate keystroke and is preserved; no set or deduplication is involved.
- **Empty output outside the constraints:** An input consisting only of faulty keys would leave the list empty and return an empty string, though the first-character guarantee prevents that exact valid case.
- **Do not use reversal parity alone:** The positions of ordinary characters relative to reversal events affect the answer, so total count parity lacks enough information without direction-aware insertion.
- **Input preservation:** The immutable input string is only read, while all simulation state lives in the new list.
