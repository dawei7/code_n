## General

**Two separate facts determine the answer**

A character qualifies only when both of these statements are true:

1. it occurs exactly once in the entire string;
2. its index is smaller than the index of every other character that also occurs exactly once.

The first fact is global. When the scan sees a character near the beginning, it cannot know that the character is unique until it knows whether the same character appears later. The second fact depends on original position, so merely knowing which character frequencies equal one is not enough; the algorithm must still respect the string’s left-to-right order.

The exact solution cleanly separates these responsibilities into two linear passes. `Counter(s)` computes the total frequency of every character. Then `enumerate(s)` visits the original positions from smallest to largest and returns the first index whose character has count one.

**First pass: count total occurrences**

`cnt = Counter(s)` builds a mapping from each character to the number of positions containing it. If `s = "loveleetcode"`, for example, the counter records that `l` appears twice, `o` appears twice, `v` appears once, and so on.

The exact order in which those dictionary entries are stored is irrelevant. This phase answers only the global uniqueness question. For any index `i`, the character `s[i]` is non-repeating if and only if `cnt[s[i]] == 1`.

Counting before choosing an answer prevents a common one-pass mistake. Seeing the first `l` in `"leetcode"` does not by itself prove that `l` is unique; only a complete count can establish that no later `l` exists. Here, the counter shows `l` has total frequency one, so it qualifies. In `"loveleetcode"`, the first `l` does not qualify because another `l` occurs later.

**Second pass: recover the earliest qualifying position**

The loop `for i, c in enumerate(s)` produces each index `i` and its character `c` in increasing index order. The test `cnt[c] == 1` asks whether that character occurs at exactly one position in the whole string.

As soon as the test succeeds, the method returns `i`. This early return is safe because every smaller index was already examined and failed the same test. Therefore no earlier non-repeating character exists.

If the loop ends, every character occurrence belongs to a character with frequency at least two. No qualifying index exists, so `-1` is the required sentinel.

**Why “count equals one” is the exact condition**

A frequency of zero cannot occur for the character currently read from `s`; its own position contributes at least one. A frequency greater than one means there is at least one other position containing the same character, so it repeats. Only frequency one means the current position is the sole occurrence.

This is a property of the character across the complete string, not a property of the prefix processed so far. The counter remains unchanged during the second pass, so every lookup refers to the same complete-string facts.

**Tracing the examples**

For `s = "leetcode"`, the relevant counts include `l: 1`, `e: 3`, and `t: 1`. The second pass begins at index `0`, sees `l`, and finds count one. Since index zero is the first possible index, it immediately returns `0`.

For `s = "loveleetcode"`, the second pass behaves as follows:

| Index | Character | Total count | Decision |
|---:|:---:|---:|---|
| `0` | `l` | `2` | repeats, continue |
| `1` | `o` | `2` | repeats, continue |
| `2` | `v` | `1` | unique, return `2` |

There may be other unique characters later, but they cannot be the first because index `2` has already qualified.

For `s = "aabb"`, both `a` and `b` have frequency two. Every lookup fails, so the loop finishes and returns `-1`.

**A direct correctness argument**

Suppose the method returns an index `i`. The return condition says `cnt[s[i]] == 1`, and the counter contains exact total frequencies, so the character at `i` is non-repeating. Because indices were visited in increasing order and none returned earlier, every index smaller than `i` has a repeating character. Thus `i` is exactly the first unique-character index.

Now suppose the method returns `-1`. That can happen only after it tests every position and finds a count other than one. Every character at every position therefore repeats, so no valid index exists. The sentinel is correct.

These two cases cover every possible execution, proving that the method returns the smallest qualifying index when one exists and `-1` otherwise.

**Why the answer cannot be found from the counter alone**

Even if the counter exposes all keys with frequency one, selecting an arbitrary such key does not necessarily identify the first occurrence. The order of a frequency map is not the semantic order requested by the problem. The second scan through `s` restores that positional information directly and avoids storing a separate index for every character.

For the fixed lowercase alphabet, one could remember each character’s first index during counting. That works, but a second string scan is simple, linear, and uses no meaningful additional space.

## Complexity detail

Let $n$ be the length of `s`.

Constructing the counter examines all $n$ characters once. The second loop examines at most all $n$ characters once, although it may stop early. Counter creation and expected constant-time lookups give total time

$$
O(n) + O(n) = O(n).
$$

This is asymptotically optimal because, in the worst case, any correct algorithm must inspect the complete string. An unseen final character could repeat an earlier candidate and change the answer.

Let $k$ be the number of distinct characters. The counter uses $O(k)$ entries. The contract restricts `s` to the 26 lowercase English letters, so $k \le 26$; this is a constant independent of $n$. The auxiliary-space bound is therefore $O(1)$ under the stated alphabet. If the problem were generalized to an unbounded alphabet, the precise bound would be $O(k)$.

The input string is read-only, and the integer index and current character use constant additional storage. No output collection is allocated because the method returns only one integer.

## Alternatives and edge cases

- **Fixed 26-element array:** Use `ord(c) - ord('a')` as an index, count into an integer array, then scan the string. This has the same $O(n)$ time and explicit $O(1)$ space. `Counter` is shorter and expresses the frequency idea directly.

- **Repeated `s.count(c)`:** Testing the total count separately for each character is concise but each `count` scans the string. In the worst case this costs $O(n^2)$ time.

- **Queue of provisional unique characters:** During one pass, keep first-seen characters in a queue and mark repeats in a count map, removing repeated entries from the front when possible. It can be linear but maintains more moving state and is easier to get wrong than the two-pass method.

- **Sort characters:** Sorting groups equal letters but destroys their original positions unless indices are stored too. It also costs $O(n\log n)$, while counting is linear.

- **Unique character at index zero:** The second pass returns immediately. No special branch is necessary.

- **Unique character at the final index:** The algorithm must scan the entire second pass before finding it. This is still linear and is necessary to establish that all earlier characters repeat.

- **No unique character:** Every frequency exceeds one, the loop naturally ends, and `-1` is returned.

- **One-character string:** Its only character has count one, so the method returns `0`, which is both the first and only index.

- **Several unique characters:** Only the earliest index matters. The increasing-order scan returns the first and deliberately ignores later candidates.

- **Long runs of one letter:** A string such as `"aaaaa"` gives that character count five. Every position fails, correctly producing `-1`.

- **Fixed-alphabet qualification:** Calling the memory bound $O(1)$ relies on the lowercase-English constraint. With arbitrary Unicode input, the same code remains correct but could store up to $n$ distinct counter keys.

- **Case sensitivity:** The contract contains lowercase letters only. In a generalized string, `A` and `a` would be distinct counter keys, which is the natural behavior unless normalization were explicitly requested.
