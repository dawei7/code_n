## General

**Record multiplicity before testing neighbors**

Whether a value is lonely depends on facts about the complete array: its total
frequency and the presence of two other keys. Build a frequency map in one
pass so all three facts are available through direct lookups.

For each distinct value $x$ in the map, include it exactly when its frequency
is one and neither $x-1$ nor $x+1$ is a key. These conditions are precisely the
definition of lonely, so every included value qualifies. Conversely, every
lonely value is a distinct map key that passes all three tests and is therefore
included. Iterating distinct keys also prevents duplicate output entries.

## Complexity detail

Let $n$ be the length of `nums`. Building and scanning the frequency map takes
$O(n)$ expected time under standard hash-table behavior and $O(n)$ space. The
result itself can also contain $O(n)$ values.

## Alternatives and edge cases

- **Sort then inspect runs:** Sorting exposes frequencies and neighboring
  distinct values in $O(n \log n)$ time; it may also modify the input.
- **Compare every pair:** Counting a value and searching for both neighbors by
  scanning the array is correct but takes $O(n^2)$ time.
- A single array element is lonely because both neighboring values are absent.
- A duplicated value is never lonely, even if neither adjacent integer occurs.
- The presence of only one of $x-1$ or $x+1$ is sufficient to disqualify $x$.
- Values at `0` and `1000000` use the same integer-neighbor tests; a neighbor
  outside the allowed input range is simply absent.
- The answer order is unrestricted.
