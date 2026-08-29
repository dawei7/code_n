## General

Only vowels may move. Every consonant must remain at its original index. The source therefore separates the task into:

1. determine the required order of vowel types;
2. expand each type according to its frequency; and
3. refill only the original vowel positions from left to right.

There are only five possible vowel types, so their sorting cost is constant with respect to the string length.

**Collecting frequency and first-occurrence order together**

The set `st = set("aeiou")` provides constant-time vowel membership checks.

While scanning `s` from left to right, the source maintains:

- `cnt[c]`, the total number of occurrences of vowel `c` seen so far; and
- `vowels`, the distinct vowel types in order of first appearance.

When a vowel `c` is encountered for the first time, `c not in cnt` is true and the source appends it to `vowels`. Every occurrence then increments `cnt[c]`.

At the end:

$$
\texttt{cnt}[c]=\operatorname{frequency}(c)
$$

for each present vowel, and the list order records exactly the first-occurrence tie-breaker.

Consonants are ignored during this stage because neither their identities nor positions influence vowel frequencies.

**Why a stable frequency sort gives both ordering rules**

The source sorts `vowels` with key `-cnt[c]`. Negating the count makes higher frequencies receive smaller keys and therefore appear first.

Only frequency is included in the explicit key. The first-occurrence tie rule is preserved by Python's stable sort: when two vowel types have equal keys, their relative order after sorting is the same as before sorting. Since the original `vowels` list was built in first-occurrence order, tied types remain in precisely the required order.

For example, in `"baeiou"` every vowel count is one. The key ties all five types, so stable sorting leaves `[a,e,i,o,u]` unchanged.

**What the sorted type list means**

Suppose the sorted type order is

$$
c_1,c_2,\ldots,c_t.
$$

The final vowel sequence must contain:

- `cnt[c1]` copies of $c_1$;
- then `cnt[c2]` copies of $c_2$;
- and so on.

All occurrences of a more frequent type come before all occurrences of a less frequent type because ordering is defined by the type's global frequency, not by individual occurrence positions. Equal-frequency types appear in first-occurrence order as entire groups.

The source does not explicitly allocate this expanded sequence. It generates the groups while refilling.

**Refilling the original vowel positions**

The result begins as `ans = list(s)`, so every character is initially preserved.

The second scan again skips consonants. At each vowel index `k`:

1. `vowels[i]` is the current vowel type whose group is being emitted.
2. The source writes that type into `ans[k]`.
3. It decrements the remaining `cnt` for that type.
4. When the remaining count reaches zero, it advances `i` to the next sorted type.

Because this loop modifies only indices whose original character is a vowel, every consonant stays exactly where it began. Because it visits those indices from left to right, the emitted grouped vowel sequence occupies them in required order.

The assignment `ans[k] = c = vowels[i]` simultaneously stores the replacement and binds `c` to the chosen type for the counter update. It does not use the original vowel `c` from the loop after replacement.

**A trace**

For `s = "leetcode"`:

- present vowel frequencies are $e:3$ and $o:1$;
- first occurrence order is `[e,o]`;
- sorting by negative count keeps `[e,o]`;
- the emitted vowel stream is `e,e,e,o`.

The original vowel positions occur at indices 1, 2, 5, and 7. Replacing only those positions gives `"leetcedo"`.

For `"aeiaaioooa"`, the counts are $a:4$, $o:3$, $i:2$, and $e:1$. Their distinct frequencies determine order `a,o,i,e`, and the expanded stream is `aaaaoooiie`.

**Why no vowel is lost or duplicated**

The counter initially contains exactly the number of vowel positions of each type. Every refill consumes one remaining count from the current type. The pointer advances only after that type's count becomes zero.

Therefore each type is emitted exactly its original frequency, the total emitted count equals the number of original vowel positions, and the scan ends only after all required vowel occurrences have been placed. Consonants never enter the counter or emission stream.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. The source scans the string twice and joins an $N$-character list once, costing

$$
O(N)
$$

time.

At most five distinct vowel types are sorted. That step costs $O(5\log5)=O(1)$ relative to $N$.

The mutable result list `ans` contains $N$ characters and is needed because Python strings are immutable. It uses

$$
O(N)
$$

space. The vowel set, counter, distinct-type list, and scalar pointer are bounded by five entries and use $O(1)$ additional space.

The returned joined string itself also has length $N$.

## Alternatives and edge cases

- **Build an explicit vowel pool:** Repeating each sorted type by its count and consuming that list is straightforward but allocates another $O(N)$ sequence; the source reuses the counter as group state.
- **Sort every vowel occurrence:** This costs $O(V\log V)$ for $V$ vowels and needs a tie key per occurrence, while sorting at most five types is enough.
- **Fixed five-element arrays:** Counts and first positions can be stored by vowel index instead of a `Counter`, with the same asymptotic bounds.
- **No vowels:** `vowels` remains empty, the refill loop changes nothing, and the original string is returned.
- **One vowel type:** Sorting is trivial, and every vowel position receives that same type.
- **Equal frequencies:** Stable sorting preserves first-occurrence type order.
- **Repeated consonants:** They are never touched, regardless of their frequencies.
- **All characters vowels:** Every position is refilled, producing the complete grouped vowel stream.
- **Frequency order is non-increasing:** Higher counts come first because the key is negative; using the positive count would reverse the requirement.
- **Lowercase contract:** The membership set contains only lowercase vowels, matching the documented alphabet.
- **Required library name:** Standalone execution needs `Counter` from Python's `collections` module.
