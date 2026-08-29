## General

The array has length `n`, and every value is guaranteed to lie in the closed range `[1, n]`. That makes the set of possible values completely known before examining the input: the only candidates are `1, 2, ..., n`. The task is therefore a presence test. For each candidate in that range, determine whether it occurs at least once in `nums`.

The exact optimal-branch solution separates this into two simple phases:

1. Build `s = set(nums)`, which records every distinct value that appears.
2. Enumerate every candidate `x` from `1` through `n` and return those for which `x not in s`.

This approach is intentionally based on membership rather than frequency. If `2` occurs once or twenty times, the only relevant fact is that `2` is present. A set stores precisely that yes-or-no information and automatically collapses duplicate occurrences.

**Why the known range matters**

If the possible values were unrestricted, observing the input would not tell us which unobserved integers were supposed to be reported. Here the domain `[1, n]` defines the complete checklist. Once the set of observed values is available, scanning that checklist is sufficient: a candidate is missing exactly when the set does not contain it.

The code uses `range(1, len(nums) + 1)`. Python's upper endpoint is excluded, so this produces `1, 2, ..., n` and includes `n` itself. Starting from `1` also matches the problem's one-based value domain; zero is not a candidate and is never returned.

**How the comprehension forms the answer**

The expression

`[x for x in range(1, len(nums) + 1) if x not in s]`

visits candidates in increasing order. For each candidate, the condition keeps it only when the set has no matching value. Consequently, the result is automatically sorted in ascending order even though the input may be in any order. The problem does not require a special ordering operation, and no final sort is needed.

For `nums = [4,3,2,7,8,2,3,1]`, the set becomes `{1,2,3,4,7,8}`. The candidate scan makes the following decisions:

- `1`, `2`, `3`, and `4` are in the set, so they are skipped.
- `5` and `6` are absent, so they are appended.
- `7` and `8` are present, so they are skipped.

The returned list is `[5,6]`.

In `nums = [1,1]`, the array length is two, so the candidate domain is `{1,2}`. The duplicate `1` creates only one set entry. Candidate `1` is present, while candidate `2` is absent, yielding `[2]`.

**Why duplicates imply missing values but require no special case**

There are exactly `n` array positions and exactly `n` possible values. When one value appears more than once, at least one other value must be absent. The algorithm does not need to match a particular duplicate to a particular missing number. Set construction removes the repeated copies, and the complete domain scan independently identifies every gap.

The same reasoning handles several duplicates or several missing values. If the set has `u` distinct members, exactly `n - u` candidates from `[1, n]` are absent, and the returned list has that length.

**Why every returned value is correct**

Take a value `x` that the comprehension returns. It came from the range `[1, n]`, so it is a valid candidate. Its filter condition was `x not in s`. Because `s` was built from every element of `nums`, absence from `s` means no position of `nums` contains `x`. Thus every returned value really is missing.

Now take any value `y` in `[1, n]` that is missing from `nums`. Set construction cannot insert `y`, because no input occurrence exists. When the candidate loop reaches `y`, `y not in s` is true, so the comprehension includes it. Therefore no missing value is omitted. These two directions establish that the output contains exactly the required values.

**What the implementation does to the input**

The solution reads `nums` to construct a new set and never assigns to an array position. The caller's list therefore remains unchanged. This is a practical advantage over in-place marking methods, especially when the input may be reused after the call.

The solution also avoids relying on arithmetic modification, signs, or index swapping. Its correctness follows directly from set membership, making it approachable and difficult to implement incorrectly.

## Complexity detail

Let $n$ be the length of `nums`. Constructing `set(nums)` processes all $n$ elements. Under the standard expected-cost model for Python hash tables, each insertion takes expected $O(1)$ time, so set construction takes expected $O(n)$ time.

The comprehension checks exactly $n$ candidates. Expected set membership is $O(1)$ per candidate, making this phase expected $O(n)$ as well. Total expected time is $O(n)$.

The set may contain all $n$ distinct input values, so the exact implementation uses $O(n)$ auxiliary space. The returned list can also contain up to $n-1$ values, but the problem explicitly allows the output not to count as extra space.

This is an important fidelity detail: the optimal variant's manifest currently lists $O(1)$ space, but the exact source shown here allocates `set(nums)` and therefore has $O(n)$ auxiliary space. The manifest's bound corresponds to the in-place marking follow-up, not to this exact implementation. The approach document reports the behavior of the actual optimal solution rather than hiding that distinction.

In theoretical worst-case hash-table analysis, adversarial collisions can degrade operations, but the conventional Python and interview analysis uses expected $O(1)$ insertion and membership.

## Alternatives and edge cases

- **In-place sign marking:** For each value `v`, use index `abs(v) - 1` as its presence slot and make that slot negative. A final scan reports positive slots. This satisfies the follow-up in $O(n)$ time and $O(1)$ auxiliary space, but it mutates `nums` and requires `abs` because earlier visits may have changed signs.
- **Cyclic placement:** Repeatedly swap each value `v` toward index `v - 1`; positions that do not contain their canonical values reveal missing numbers. It also uses $O(1)$ auxiliary space and $O(n)$ total swaps, but its duplicate stopping condition is easier to get wrong.
- **Boolean presence array:** A length-`n` Boolean list makes indexing explicit and has deterministic $O(n)$ time, but still consumes $O(n)$ auxiliary space.
- **Sort first:** Sorting allows gaps to be detected, but comparison sorting costs $O(n\log n)$ time and may mutate the input. It provides no advantage over a set for the exact implementation's goals.
- **Every value appears:** The set contains the full domain, every membership test succeeds, and the result is the empty list.
- **One-element input:** The only permitted value is `1`, so `[1]` produces no missing numbers.
- **Many copies of one value:** Duplicates collapse into one set entry; every other candidate is returned once, in increasing order.
- **Output order:** The set itself is unordered, but the solution never iterates over it. Iterating over `range(1, n + 1)` guarantees ascending output.
- **Out-of-range input:** The exact code would ignore an extra out-of-range value when scanning candidates, but the contract guarantees such values never occur; correctness relies on that domain guarantee.
