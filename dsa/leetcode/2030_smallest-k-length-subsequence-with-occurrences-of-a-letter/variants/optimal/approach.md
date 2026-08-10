## General

**Combine lexicographic greediness with two feasibility constraints**

A lexicographically small subsequence wants the earliest possible character at each output position. A monotonic stack supports that goal: when a smaller current character arrives, larger characters at the end of the tentative answer may be removed.

This problem adds two restrictions. The final stack must have exactly `k` characters, and at least `repetition` of them must equal `letter`. Every removal and every skipped character must preserve both possibilities.

The source tracks:

- `stack`: the currently selected subsequence, in original index order;
- `selected_letter`: how many selected characters equal `letter`;
- `remaining_letter`: how many copies of `letter` remain at or after the current scan position.

Initially, `remaining_letter = s.count(letter)`. It is decremented only after the current character has been processed, so during the decisions for one iteration it still includes the current character.

**When a larger stack top may be removed**

The `while` loop considers replacing the last selected character with the smaller current `character`. The comparison `character < stack[-1]` is what makes the replacement lexicographically beneficial: the first changed output position becomes smaller.

But a beneficial pop is allowed only when enough source characters remain to refill the output. After popping, there would be `len(stack) - 1` selected characters. The number of characters from the current index through the end is `len(s) - index`. The condition

`len(stack) - 1 + len(s) - index >= k`

guarantees that these together can still produce length `k`. Without it, a late small character could cause the final subsequence to be too short.

**Protect the required copies of `letter`**

If the stack top is not `letter`, popping it does not reduce `selected_letter` and is harmless to the repetition requirement.

If the top is `letter`, the source requires

`selected_letter - 1 + remaining_letter >= repetition`.

The first term is how many required letters would remain selected after the pop. The second term counts every copy still available from the current position onward. Their sum is the greatest number of `letter` copies the final answer could still contain. A pop is safe only when that maximum remains at least `repetition`.

This check is intentionally made before decrementing `remaining_letter` for the current character. If the current character itself equals `letter`, it is a legitimate replacement for the popped copy and must be counted as available.

**Decide whether to append the current character**

After all safe lexicographic pops, the current character can be appended only if `len(stack) < k`. A full stack cannot accept another character unless an earlier pop made space.

If the current character is `letter`, the source always appends it when space exists and increments `selected_letter`. Extra copies beyond the minimum are allowed, and `letter` may itself be lexicographically valuable.

For a non-`letter` character, the condition is

`k - len(stack) > repetition - selected_letter`.

The left side is the number of open output slots. The right side is the number of required `letter` copies still missing. A non-`letter` may use a slot only when there are strictly more slots than mandatory letters. If the two numbers are equal, every remaining slot must be reserved for `letter`, so the current nonrequired character is skipped.

**Why stack order still forms a subsequence**

Characters are appended only as the source scans left to right. Popping removes a previously chosen index but never changes the order of those that remain. Appending the current character places its later index after every retained index.

The stack therefore always spells a subsequence of the processed prefix. Joining it at the end produces a valid subsequence of the full string.

**Trace the main decisions for `"leet"`**

Let `k=3`, `letter="e"`, and `repetition=1`. The first character `l` can be selected because three slots are open and only one is reserved.

The next character `e` is smaller than `l`. There are enough characters left to reach length three after popping, and `l` is not a protected required letter, so `l` is removed. The `e` is appended and becomes the first selected required copy.

The next `e` is appended as well. At `t`, one slot remains, so it is appended. The result is `"eet"`. Although only one `e` was required, retaining two gives the lexicographically smallest feasible result.

**Why the greedy result is lexicographically smallest**

Whenever the source pops, it replaces a larger selected character with an available smaller character while explicitly proving that length and repetition can still be completed. Any feasible answer retaining that larger character at the same first differing position cannot be lexicographically smaller.

Whenever it refuses to pop, at least one reason is decisive: the current character is not smaller, too few source positions remain, or removing a required letter would make the quota impossible. Thus no feasible lexicographic improvement is being rejected.

Whenever it skips a non-`letter` because all open slots are reserved, including that character would force the final answer below `repetition`. Otherwise it appends when space exists, preserving the earliest feasible choice after the stack's improvement phase.

By induction over the scan, `stack` is the lexicographically smallest prefix that can still be completed into a valid length-`k` answer. The global availability guarantee for `letter` ensures such a completion exists. At the end, the stack has length `k` and at least the required number of letters, so it is the desired subsequence.

**Why each character is processed only a constant number of times**

A character can be appended once and later popped once. It never re-enters the stack. Although the `while` loop can pop several elements during one iteration, the total number of pops over the full scan is at most the total number of pushes.

This amortized fact makes the monotonic-stack scan linear rather than quadratic.

## Complexity detail

Let $N=\lvert s\rvert$. Counting `letter` takes $O(N)$ time. The main scan takes amortized $O(N)$ time because each character is pushed at most once and popped at most once. Joining at most `k` characters costs $O(k)$, which is within $O(N)$. Total time is $O(N)$.

The stack holds at most `k` characters, so auxiliary construction space is $O(k)$ and therefore $O(N)$ in the worst case. The returned string also has length `k`. All counters and indices use $O(1)$ additional space.

## Alternatives and edge cases

- **Enumerate subsequences:** There can be exponentially many, so direct comparison is infeasible.
- **Dynamic programming over positions and quota:** It can model feasibility but uses much more time and memory than the monotonic greedy method.
- **Ordinary smallest-subsequence stack:** Ignoring the `letter` quota may pop or skip too many required copies.
- **Exactly `k` source characters:** Nothing can ultimately be omitted; the capacity condition prevents destructive pops.
- **`repetition = k`:** Every output slot is reserved for `letter`, so all non-`letter` characters are skipped.
- **All characters equal `letter`:** The first `k` retained copies form the only value-level answer.
- **More required letters than currently selected:** The non-`letter` append guard reserves enough remaining slots.
- **Popping a required letter:** Allowed only when the current and future suffix can replace it.
- **Extra copies of `letter`:** They are legal because the requirement is at least, not exactly, `repetition`.
- **Equal current and top characters:** No pop occurs because equality cannot create a lexicographic improvement.
- **Late smaller character:** It cannot trigger a pop when too few positions remain to refill length `k`.
- **Duplicate subsequence values:** The task asks for the smallest string, not a unique index selection.
- **Input preservation:** The source reads `s` and builds a separate stack.
