## General

**Extend the current part as far as validity permits.** Scan from left to
right while recording the letters already used in the current substring. A
26-bit integer is enough: bit $c$ indicates that the corresponding lowercase
letter has appeared since the last cut.

**A repeated letter forces a boundary.** When the next letter's bit is already
set, the current substring cannot include it. Every valid partition must place
a cut somewhere after that letter's previous occurrence and before the new
one. Cut immediately before the new occurrence, count a new part, clear the
mask, and insert the letter into that new part.

**Why the latest possible cut is optimal.** The greedy first part is the
longest valid prefix. Any valid partition must end its first part no later
than the greedy cut, because including the repeated letter would violate
uniqueness. Moving a cut earlier cannot reduce the number of parts required
for the remaining suffix. Applying the same argument after each forced cut
proves that the greedy partition uses the minimum number of substrings.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Each character is processed once with
constant-time bit operations, so time is $O(n)$. The mask and counters use
$O(1)$ auxiliary space because the lowercase alphabet has exactly 26 letters.
The asymptotic-optimality certificate records the matching $\Omega(n)$
worst-case input-inspection lower bound.

## Alternatives and edge cases

- **Partition dynamic programming:** Test every unique substring ending at
  each position and minimize prior cuts. The fixed alphabet limits each
  backward scan to 26 characters, so it remains linear but uses more state and
  a larger constant.
- **Character set:** A mutable set implements the same greedy boundary rule
  clearly, with $O(1)$ bounded space over the fixed alphabet.
- **All characters unique:** The scan makes no cut and returns one part.
- **All characters equal:** Every character after the first forces a cut, so
  the answer is $n$.
- **Repeat after a cut:** Clearing the mask is essential; letters in earlier
  substrings do not constrain the new substring.
- **Single character:** The initialized partition count of one is already the
  correct answer.
- **Maximum unique-part length:** No valid substring can exceed 26 characters,
  although the full input can contain $10^5$ characters.
