## General

**Treat each bar as a state transition**

Before the first bar, the scan is outside a paired region. Every bar toggles
that state: the first bar opens a region, the second closes it, and the same
pattern repeats for later pairs. When the current character is an asterisk,
increment the answer only if the state is outside.

The state is correct after every prefix because its parity equals the number of
bars already seen: an even count means every opened region has closed, while
an odd count means the scan is inside the current pair. Consequently, the
algorithm counts exactly the asterisks excluded by no pair. The guaranteed even
total number of bars leaves no unmatched opening bar.

## Complexity detail

Let $n$ be the length of `s`. Each character is examined once, giving $O(n)$
time. The outside flag and counter use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Split on vertical bars:** Even-indexed segments are outside regions and their asterisks can be summed in $O(n)$ time, but splitting allocates $O(n)$ space.
- **Rescan every prefix:** Counting preceding bars separately for each asterisk is correct but takes $O(n^2)$ time in an asterisk-heavy string.
- **No bars:** The initial outside state never changes, so every asterisk counts.
- **Empty paired region:** Adjacent bars toggle inside and immediately back outside.
- **Boundary asterisks:** Asterisks before the first bar or after a closing bar count; bars themselves never do.
- **Letters:** Lowercase letters do not affect either the state or the answer.
