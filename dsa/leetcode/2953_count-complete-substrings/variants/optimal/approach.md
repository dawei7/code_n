## General

A complete substring has two independent requirements:

1. Every character that appears occurs exactly $k$ times.
2. Every adjacent pair differs by at most two alphabet positions.

The source first handles the adjacency rule globally, then counts exact-frequency windows inside each valid region.

**Split at impossible boundaries**

If neighboring characters `word[p - 1]` and `word[p]` differ by more than two, no complete substring may contain both, because that adjacent pair would violate the rule.

The outer loop partitions `word` into maximal segments where every adjacent difference is at most two. It finds maximal `word[i:j]` by extending `j` while

`abs(ord(word[j]) - ord(word[j - 1])) <= 2`.

Every substring fully inside such a segment automatically satisfies the adjacency requirement. Every substring crossing a segment boundary is invalid. Thus segments can be counted independently and their answers added.

**Possible length for a chosen number of distinct letters**

Suppose a complete substring contains exactly $d$ distinct characters. Each occurs exactly $k$ times, so its length must be

$$
L=d\cdot k.
$$

There are only 26 lowercase letters, so helper `f` tries `d = 1..26`. If `L > m` for segment length $m$, larger $d$ values also cannot fit and the loop breaks.

For each $d$, only windows of the single required length $L$ need examination.

**Track character frequencies inside one window**

`cnt` maps characters to their counts in the current length-$L$ window. `freq` maps a count value to how many character keys currently have that count.

For the initial window:

`cnt = Counter(s[:L])` and `freq = Counter(cnt.values())`.

The window is complete exactly when `freq[k] == d`.

Why is that enough? Those $d$ characters already account for $d\cdot k=L$ positions, the entire window. Therefore no other character can have a positive count. The length equation supplies the otherwise missing “exactly $d$ distinct characters” proof.

**Slide the window in constant time**

When right endpoint `j` enters, the source updates `freq` around the increment:

1. Decrease the number of characters having the incoming character's old count.
2. Increment its count in `cnt`.
3. Increase the number having its new count.

It performs the symmetric operations for outgoing character `s[j - L]`, decrementing its count.

After both updates, `cnt` describes the new window and `freq[k]` again tells how many characters occur exactly $k$ times. The source adds the Boolean comparison to `ans`.

Counter entries whose count falls to zero are not deleted. `freq[0]` may contain bookkeeping values, but only `freq[k]` for positive $k$ is queried, so zero-count keys cannot cause a false complete window.

**Why every complete substring is counted once**

Any complete substring cannot cross an invalid adjacency boundary, so it belongs to one unique maximal segment. If it has $d$ distinct letters, its length is exactly $dk$, and helper `f` examines its endpoint window during the iteration for that $d$.

The frequency test accepts it. Conversely, every accepted window lies in a valid-adjacency segment and has exactly $d$ characters occurring $k$ times, so it is complete.

## Complexity detail

For a segment of length $m$, at most 26 distinct-count choices are tried. Each choice initializes and slides windows in $O(m)$ time, so $O(26m)=O(m)$ because alphabet size is constant. Segments are disjoint, giving total $O(n)$ time.

The counters contain at most 26 character keys and use $O(1)$ logical state for a fixed alphabet. However, the exact Python source creates `word[i:j]` segment slices and `s[:L]` window slices. A slice can contain $O(n)$ characters, so actual peak auxiliary space is $O(n)$, not the manifest's $O(1)$ claim.

## Alternatives and edge cases

- **Check every substring:** Counting letters from scratch is cubic; even incremental enumeration is quadratic.
- **Do not split segments:** Then every window would need a second structure tracking invalid adjacent gaps. Splitting makes adjacency automatic.
- **Window lengths not divisible by $k$:** They cannot have every present character occur exactly $k$ times and are never tested.
- **One distinct character:** Test windows of length $k$; adjacency differences inside repeated letters are zero.
- **Boundary difference exactly two:** Allowed because the rule is “at most” two.
- **Boundary difference three:** Forces a segment break, and no valid substring crosses it.
- **Outgoing and incoming character equal:** Increment then decrement restores its count; the paired `freq` updates remain correct.
- **Zero-count Counter keys:** They do not affect `freq[k]` for positive $k$.
- **Alphabet cap:** Trying beyond 26 distinct characters is impossible for lowercase English input.
- **Space mismatch:** Fixed-size counters are constant, but Python string slicing makes this exact implementation linear-space at peak.
- **Why all valid substrings stay in one segment:** A substring contains every adjacency between its endpoints. Crossing a split necessarily includes the disallowed pair that caused the split.
- **At most 26 passes:** The outer loop inside `f` is alphabet-bounded, so its apparent nested scan remains linear under the fixed lowercase alphabet model.
