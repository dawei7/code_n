## General

**Enumerate exactly the legal choices**

The operation must remove exactly one occurrence of the character `digit` from `number`. The solution scans `number` with `enumerate`, so each loop item provides both the position `i` and the character `d` stored there. The condition `if d == digit` filters the scan to precisely the positions that are legal to delete.

For every legal position, the expression

`number[:i] + number[i + 1:]`

constructs the result of deleting that one character. The first slice contains every character before position `i`. The second starts immediately after `i` and contains all later characters. Joining them omits exactly `number[i]` and preserves the relative order of every other digit. It cannot accidentally remove two occurrences, reorder digits, or substitute a different character.

The problem guarantees that `digit` appears in `number` at least once. Therefore, the generator passed to `max` always produces at least one candidate, and `max` is never applied to an empty sequence.

**Why comparing the candidates as strings is valid**

Python's `max` compares strings lexicographically. At first glance, that might seem different from choosing the greatest integer, but all candidates have exactly the same length: each begins with the same length-`n` input and removes exactly one character. For two equal-length decimal strings, lexicographic order and numeric order agree.

To see why, consider the first position where two candidates differ. Every earlier digit is equal, so those shared positions contribute the same amount to both numbers. At the first differing position, the candidate with the larger digit is numerically larger because that digit has a higher place value than all later positions combined can overturn. Lexicographic comparison makes exactly the same decision at that first difference.

The input consists of decimal digits from `'1'` through `'9'`, so removing a character cannot create an ambiguous leading-zero representation. Even if zero were present, equal length would still be the central comparison fact, but the stated digit range makes the representation especially direct.

**How deleting one copy changes the remaining alignment**

When occurrence `i` is removed, every digit before `i` remains in the same position and every digit after it shifts one place to the left. Thus, different deletion choices often share a long prefix. The first point at which their retained sequences differ determines which candidate is larger.

For example, suppose two copies of the target occur at positions `i < j`. Deleting the earlier occurrence causes `number[i + 1]` to move into position `i`. Deleting the later occurrence leaves `digit` at position `i`. If the character immediately after the earlier occurrence is greater than `digit`, deleting the earlier copy produces a larger digit at the first differing position and must be better. If it is smaller, preserving the earlier `digit` is better. This observation leads to a greedy alternative, but the exact implementation does not need to encode or prove all such cases: it materializes every legal result and asks `max` to compare them.

**Why the maximum is the required answer**

Let the set of indices containing `digit` be `D`. Every valid operation selects one index from `D`, and the generator creates the corresponding result. Therefore, no legal answer is missing from the candidates.

Conversely, every yielded candidate comes from an index in `D` and deletes exactly the character at that index, so no illegal answer is included. The generated set is exactly the set of all possible results. Because equal-length lexicographic order matches numeric order, `max` returns the numerically greatest legal result. These two facts establish correctness without relying on a local heuristic.

**A small trace with repeated occurrences**

Take `number = "1231"` and `digit = "1"`. The matching indices are zero and three.

- Removing index zero gives `"231"`.
- Removing index three gives `"123"`.

Both strings contain three digits, so string comparison examines their first characters. Since `'2' > '1'`, `"231"` is also the greater integer and is returned.

Now consider repeated adjacent target digits. Removing either of two indistinguishable adjacent copies can produce the same string. The generator may yield that identical candidate more than once, but this does not affect correctness: the maximum of a collection is unchanged by duplicates.

**The generator controls how candidates are retained**

The candidates are written as a generator expression rather than a list comprehension. A generator creates one deletion result at a time as `max` asks for it. Python's `max` retains the best candidate seen so far instead of storing every candidate simultaneously.

This distinction matters for space, but it does not make candidate construction free. Slicing a Python string creates new strings, and concatenation creates the combined candidate. Each candidate has length `n - 1` and therefore takes linear work to build. The generator limits the number of candidates alive at once; it does not change the total amount of slicing work.

**Why the exact code is intentionally simple**

The input length is at most one hundred, so evaluating all legal deletion positions is comfortably small. The implementation trades the more delicate proof and branching of a greedy scan for a direct correspondence between legal choices and generated strings. Its one return expression expresses the entire argument: construct every permitted result, compare them under an equivalent ordering, and keep the greatest.

This is also why the complexity description must follow the actual operations rather than merely label the idea as a linear greedy algorithm. The code is exhaustive over occurrences and copies strings for each occurrence. It is reliable and concise under the given constraint, but its worst-case running time is quadratic rather than linear.

## Complexity detail

Let `n` be the length of `number` and let `k` be the number of occurrences of `digit`. The scan itself visits `n` characters. For each of the `k` matching positions, two slices and one concatenation construct a length-`n - 1` candidate, taking `O(n)` time. Comparing that candidate with the current maximum can also examine up to `O(n)` characters when the strings share a long prefix.

The total running time is therefore

$$
O(n + kn) = O(kn).
$$

Because `k \le n`, the worst case is `O(n^2)`. This worst case occurs when the target digit appears throughout much or all of the string. The small source constraint keeps that amount of work practical.

The generator does not collect all `k` candidates. At any moment, `max` needs the current candidate and the best candidate retained so far, each of length `O(n)`. Temporary slices and the returned string are also linear in length. Consequently, the auxiliary memory used by the exact Python expression is `O(n)`, not `O(kn)`. If the unavoidable returned string is excluded from an auxiliary-space convention, candidate construction still requires `O(n)` temporary storage.

## Alternatives and edge cases

- **Greedy first improving deletion:** Scan target occurrences from left to right and remove the first one whose following digit is larger than `digit`; if none exists, remove the last occurrence. This can run in `O(n)` time, but it is an alternative to the submitted enumeration, not what the exact solution executes.
- **Build a list of every candidate:** A list comprehension would make the same choice but retain all generated strings, increasing peak space to `O(kn)`.
- **Convert every candidate to an integer:** Numeric conversion is unnecessary because all candidates have equal length. It adds work and obscures the useful ordering argument.
- **Delete a globally smallest digit:** The removable character is fixed by `digit`, and position affects the remaining place values. Choosing by digit magnitude alone does not solve the problem.
- **Only one target occurrence:** The generator yields one candidate, so `max` returns the uniquely legal result.
- **Target at the first position:** `number[:0]` is the empty string, and concatenating the remaining suffix correctly removes the first character.
- **Target at the final position:** `number[i + 1:]` is empty, and the prefix is the complete result.
- **Adjacent target occurrences:** Two deletion positions may produce identical strings. Duplicate candidates are harmless.
- **Every character equals the target:** Every deletion produces the same length-`n - 1` string, which is necessarily the answer.
- **Long common prefixes:** String comparison may inspect nearly the entire candidate, which is included in the `O(kn)` time bound.
- **Guaranteed occurrence:** The source guarantee is essential to this concise use of `max`; without it, the generator would be empty and Python would raise `ValueError`.
- **Exactly one deletion:** Returning the original number is never considered, even when it would be numerically larger due to having an extra digit, because it is not a legal result.
- **String immutability:** The input is not modified. Every slice and concatenation creates a new string.
- **Lexicographic ordering:** It is safe specifically because all candidates contain exactly `n - 1` decimal digits. Comparing arbitrary unequal-length numeric strings lexicographically would not generally be valid.
- **No leading-zero complication:** The stated characters range from `'1'` to `'9'`, so every candidate remains an ordinary length-`n - 1` decimal representation.
- **Small input bound:** With `n \le 100`, the enumeration's quadratic worst case is modest, which supports the solution's preference for transparency.
