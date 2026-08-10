## General

**Sort so one strict inequality is automatic**

A character is weak only if another character has strictly greater attack and strictly greater defense. The source sorts `properties` by key `(-attack, defense)`:

- larger attack appears earlier;
- among equal attack, smaller defense appears earlier.

During the subsequent left-to-right scan, earlier rows never have smaller attack. The running value `mx` stores the greatest defense seen among those earlier rows.

If current defense `x` is less than `mx`, some earlier row has greater defense. The tie ordering is designed so that this witness must also have strictly greater attack.

**Why equal attack must be ordered by increasing defense**

Characters with equal attack cannot dominate one another, no matter how their defenses compare. They must not create false weak counts.

Within one attack group, defenses are scanned from smallest to largest. Earlier same-attack defenses are therefore at most the current defense. They cannot make `x < mx` true.

If `mx` is greater than the current defense, its value cannot have come solely from an earlier character in the same attack group; it must have been established by a previously scanned group with larger attack. That row has both strictly greater attack and defense, providing a valid witness.

For example, equal-attack characters `(5,3)` and `(5,7)` are scanned in that order. When defense three is seen, defense seven has not yet entered `mx`, so the first character is not incorrectly labeled weak because of an equal-attack peer.

**Update the answer and maximum**

The line `ans += x < mx` relies on Python Booleans behaving as integers: true contributes one and false contributes zero.

After testing, `mx = max(mx, x)` incorporates the current defense for later characters. It is safe to update after the test because a character cannot witness its own weakness.

Defense values are positive, so initializing `mx=0` ensures the first character cannot be counted.

**Trace a mixed example**

Consider `[(5,5),(6,3),(3,6)]`. Sorting by descending attack and ascending tied defense gives `[(6,3),(5,5),(3,6)]`.

Defense three is not below zero, then `mx` becomes three. Defense five is not below three, then `mx` becomes five. Defense six is not below five. The answer is zero, matching the fact that no row has both properties above another.

For `[(2,2),(3,3)]`, the stronger character is scanned first and sets `mx=3`. The second defense two is below three, so it is counted.

**Why every counted character is truly weak**

Suppose current character is counted because `x < mx`. Some earlier character supplied that larger defense. Same-attack earlier characters have defense no greater than `x` because of ascending tie order. Therefore the supplier belongs to a strictly larger-attack group. It has both properties strictly greater, so the current character is weak.

**Why every weak character is counted**

If a character is weak, choose a witness with greater attack and defense. Descending attack order places that witness before the character. By the time the character is scanned, `mx` is at least the witness's defense, which is strictly greater than current defense. The test succeeds.

Together, these two directions prove the count exact.

**Equivalent sorting convention**

A common alternative sorts attack ascending and defense descending, then scans right to left. The exact source reverses both scan direction and primary attack direction: descending attack with ascending defense, scanned left to right. Both conventions isolate equal-attack rows from creating false witnesses.

**Input mutation**

`properties.sort(...)` changes the order of the caller's list in place. It does not change either two-element property row, but the original character order is lost after the call.

## Complexity detail

Let $N$ be the number of characters. Sorting costs $O(N\log N)$ time, and the scan costs $O(N)$, so total time is $O(N\log N)$.

Python's Timsort may use $O(N)$ temporary memory in the worst case. The scan itself uses $O(1)$ space. This matches the manifest's $O(N)$ auxiliary bound and the input is left sorted.

## Alternatives and edge cases

- **Attack-frequency suffix maximum:** Store maximum defense at each attack, build suffix maxima, and test against strictly higher attacks in $O(N+K)$ time and $O(K)$ space.
- **Brute-force pair comparison:** Takes $O(N^2)$ time and repeats dominance checks.
- **Wrong tie order:** Descending attack and descending defense scanned left-to-right can let equal attacks falsely dominate.
- **Equal attack, different defense:** Neither is weak because attack must be strictly greater.
- **Equal defense, different attack:** Lower attack is not weak because defense must also be strictly greater.
- **Duplicate property pairs:** They never dominate one another and are treated identically.
- **One globally strongest character:** It can cause many later weak counts through `mx`.
- **Tradeoff characters:** Higher attack but lower defense does not establish weakness.
- **Strict comparison:** Use `x < mx`, not `x <= mx`.
- **Positive defenses:** Make zero a safe initial maximum.
- **Boolean arithmetic:** In Python, adding the comparison increments by exactly zero or one.
- **Input side effect:** The exact source reorders `properties`.
