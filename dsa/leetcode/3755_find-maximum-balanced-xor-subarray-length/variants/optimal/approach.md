## General

Represent each prefix by two values: its cumulative bitwise XOR and its parity balance, adding one for an even element and subtracting one for an odd element.

Between two equal prefix-XOR values, the intervening subarray has XOR zero because equal values cancel under XOR. Between two equal balances, the intervening subarray adds equally many even and odd elements. Thus, a subarray is valid exactly when the joint state `(prefix_xor, balance)` is identical at its two boundaries.

Store the earliest index at which every joint state occurs, beginning with `(0,0)` at boundary `-1`. When a state repeats at index `i`, its distance from that earliest index is the longest valid subarray ending at `i`; retaining the earliest occurrence maximizes every later distance.

## Complexity detail

Each of the $n$ elements causes one constant-time expected hash-table lookup or insertion, giving expected $O(n)$ time. At most $n+1$ distinct prefix states are stored, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Enumerate all subarrays:** Updating XOR and parity counts for every left endpoint is correct but takes $O(n^2)$ time.
- **Track XOR alone:** Equal XOR prefixes do not guarantee equal counts of even and odd values.
- **Track balance alone:** Equal parity balances do not guarantee that the subarray XOR is zero.
- **Initial state:** Recording `(0,0)` at `-1` allows a valid prefix beginning at index zero to be counted.
- **Zero values:** Zero is even and leaves cumulative XOR unchanged; both effects must be applied.
- **Repeated state:** Never replace its earliest index, because a later stored boundary can only shorten future candidates.
