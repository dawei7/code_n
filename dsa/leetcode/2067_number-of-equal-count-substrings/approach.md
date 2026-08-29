## General

**Enumerate the possible number of unique letters**

Suppose a valid substring contains exactly `i` distinct letters and each appears exactly `count` times. Its length must be

$$
k=i\cdot\texttt{count}.
$$

There are only 26 lowercase letters, so the source tries `i` from one through 26. For each `i`, it counts valid windows of the corresponding fixed length `k`.

If `k > len(s)`, larger `i` values only make `k` larger, so the loop stops.

**Maintain one fixed-length sliding window**

For a chosen `k`, `cnt` stores frequencies in the current suffix window ending at index `j`. The source adds `s[j]`, and once the scan has more than `k` characters, removes `s[j-k]`.

After removal, the active window contains exactly the latest `k` characters. Before the first full window, it contains the entire processed prefix.

The same frequency structure is reused as the window moves one position at a time.

**Track how many letters currently have the target frequency**

Variable `t` is the number of character types whose current frequency equals `count`.

When incoming character `c` is incremented:

- if its new frequency becomes `count`, `t` increases;
- if its new frequency becomes `count+1`, it has just left the exact target and `t` decreases.

Other frequency changes do not affect whether that character belongs to the exact-count set.

Python Boolean arithmetic implements these crossings with two compact updates.

**Update the tracker when a character leaves**

After decrementing outgoing character frequency:

- if its new frequency becomes `count`, it crossed down from `count+1` and re-enters the exact set, so `t` increases;
- if its new frequency becomes `count-1`, it crossed down from `count` and leaves the exact set, so `t` decreases.

These four threshold crossings keep `t` synchronized without scanning all 26 counts after every window shift.

**Why `t == i` is sufficient**

For a full window, length is `i * count`. If `t==i`, then `i` character types each consume exactly `count` positions, accounting for all `i*count` characters.

There is no room for an extra character with another frequency. Therefore the window has exactly `i` unique letters and every unique letter appears exactly `count` times.

Conversely, any valid window with `i` unique letters makes exactly those `i` counters equal `count`, so `t==i`.

**Why early short prefixes cannot be counted accidentally**

Before the first full length-`k` window, the source still evaluates `ans += i == t`.

If `t==i`, at least `i*count=k` characters would be required to supply those exact frequencies. A shorter prefix cannot satisfy the equality. Thus the compact loop needs no separate `j+1>=k` guard.

**Trace a simple target**

Let `count=2` and `i=2`, so window length is four. Window `"aabb"` has counts two and two, giving `t=2` and one answer.

Sliding to `"abbb"` changes `a` from two to one, removing it from the exact set, and `b` from two to three, also removing it. `t` becomes zero and the new window is rejected.

**Why every equal-count substring is found**

Take a valid substring with `i` unique characters. Its length is necessarily `i*count`, so the outer loop chooses exactly that `i` and `k`.

The sliding scan visits its start-end window once. All its unique counters equal `count`, making `t==i`, so it is counted.

Every counted window satisfies the reverse argument above, so no invalid substring is added.

**Constant alphabet makes the outer factor constant**

The source performs up to 26 full scans. This is not one literal scan, but 26 is fixed by the lowercase English alphabet and does not grow with input length.

Therefore `O(26N)` simplifies to `O(N)`.

## Complexity detail

Let $N=len(s)$. At most 26 choices of unique-letter count are tried, and each performs one $O(N)$ sliding scan. Counter updates are expected constant time, so total time is $O(26N)=O(N)$.

Each Counter holds at most 26 lowercase keys, and all other state is scalar. With the fixed alphabet, auxiliary space is $O(26)=O(1)$.

## Alternatives and edge cases

- **Recount every window:** Scanning 26 frequencies per shift is still linear under a fixed alphabet but has a larger constant.
- **Enumerate all substrings:** Costs $O(N^2)$ before frequency validation.
- **Prefix counts for 26 letters:** Answer a window's frequencies by subtraction, using $O(26N)$ space.
- **`count=1`:** Valid substrings contain no repeated letter.
- **One unique letter:** Windows are runs of exactly `count` copies with no other character.
- **All 26 letters:** Considered only when `26*count<=N`.
- **Target window longer than string:** Outer loop breaks immediately for that and all larger `i`.
- **Frequency rises above target:** The incoming update removes that letter from `t`.
- **Frequency falls back to target:** The outgoing update adds it back.
- **Short initial window:** Cannot make `t==i` before reaching required length.
- **Duplicate valid values at different positions:** Each start-end substring is counted separately.
- **Input preservation:** Only Counter state changes; `s` remains untouched.
