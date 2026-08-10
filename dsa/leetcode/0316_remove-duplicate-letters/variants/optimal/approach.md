## General

The result must satisfy three requirements at once:

- it is a subsequence, so chosen characters keep their original relative order;
- every distinct letter from `s` appears exactly once;
- among all subsequences meeting those rules, it is lexicographically smallest.

Lexicographic order is decided at the first position where two strings differ. Therefore, placing a smaller feasible character earlier is more important than any choices made later. The challenge is deciding when an already chosen letter can safely be moved to a later occurrence.

The source uses a greedy stack `stk`, a membership set `vis`, and a last-occurrence map `last`.

**Why last occurrences are needed**

`last = {c: i for i, c in enumerate(s)}` records the final index of every letter. Repeated assignments for the same key naturally leave its greatest index.

Suppose a letter is currently in the partial result but a smaller current letter would look better before it. Removing the old letter is safe only if another copy appears later. The test

`last[letter] > i`

answers exactly that question at current index `i`.

If the old letter's last occurrence has already been reached, removing it would make it impossible to include that required letter at all. Lexicographic improvement cannot justify producing an invalid result.

**The stack as a chosen subsequence**

Characters are appended while scanning `s` from left to right. Hence, the stack always corresponds to characters chosen at increasing original indices and is a valid subsequence of the processed prefix.

Popping only removes a previous choice. Appending the current character after those removals still preserves index order. The algorithm never moves a later character before an earlier index artificially; it simply chooses not to use some earlier occurrences.

`vis` contains exactly the letters currently in `stk`. When a letter is appended, it is added to `vis`. When a letter is popped, it is removed from `vis`. Keeping these two structures synchronized allows constant-time duplicate checks.

**Skipping an already selected letter**

If current character `c` is already in `vis`, the source immediately continues. Adding it would violate the requirement that each letter appear once.

Keeping the earlier selected occurrence is safe. Any later decisions that might pop that letter can still use an occurrence after the pop only when the last-occurrence condition permits it. The current duplicate does not need to replace the existing copy merely because it has been encountered.

This skip also prevents equal letters from appearing twice in the stack. The stack contains at most one copy of each lowercase letter at any moment.

**The three conditions for popping**

For a character not already selected, the source repeatedly examines the stack top. It pops only while all of these conditions hold:

1. `stk` is nonempty, so a previous choice exists.
2. `stk[-1] > c`, so placing `c` before that top letter makes the result lexicographically smaller.
3. `last[stk[-1]] > i`, so the removed letter occurs again after the current index and can be restored later.

The first condition is structural. The second establishes a strict improvement. The third preserves feasibility.

After a pop, a new top may also be larger than `c` and safely postponable, so the test repeats. This can remove an entire decreasing suffix of replaceable choices.

**Why one safe pop improves the answer**

Let the current stack end with letter `x`, where `x > c`, and suppose `x` occurs again later. Compare two feasible choices:

- keep this early `x` before `c`;
- discard this occurrence of `x`, place `c` now, and use a later `x` if needed.

Both choices can still contain every required letter because a later `x` exists. They agree before the stack position occupied by `x`. At their first differing position, the second choice has `c` while the first has larger `x`. Therefore, the second choice is lexicographically smaller regardless of what follows.

This is an exchange argument: any optimal result that unnecessarily keeps the earlier larger `x` can exchange it for the current smaller `c` without losing feasibility and become better. Such a result was not truly optimal, so popping is mandatory for the smallest answer.

**Why the loop stops at the correct barrier**

The loop stops for one of three meaningful reasons.

If the stack is empty, `c` can become the earliest currently chosen character.

If the top is smaller than `c`, moving `c` before it would make the first differing position larger, not smaller. That top should remain.

If the top has no later occurrence, it is mandatory at its current position. Removing it would lose a distinct letter, so `c` must come after it even when `c` is smaller.

Equality does not arise for a new `c` because `c not in vis`; if an equal copy were already on the stack, the earlier duplicate check would skip the current occurrence.

After all safe improvements, the source appends `c` and adds it to `vis`.

**Tracing `cbacdcbc`**

The final occurrences include `a` at 2, `d` at 4, `b` at 6, and `c` at 7.

| Index and character | Action | Stack afterward |
| --- | --- | --- |
| `0: c` | append | `c` |
| `1: b` | pop `c` because `c > b` and `c` appears later; append `b` | `b` |
| `2: a` | pop `b` because `b > a` and `b` appears later; append `a` | `a` |
| `3: c` | append | `ac` |
| `4: d` | append | `acd` |
| `5: c` | skip because `c` is already selected | `acd` |
| `6: b` | `d > b`, but `d` has no later copy; keep `d` and append `b` | `acdb` |
| `7: c` | skip because `c` is already selected | `acdb` |

The inability to pop `d` at index 6 explains why `ab...` is not feasible while retaining every distinct letter. The answer is `"acdb"`.

**Why every distinct letter appears at the end**

A letter is appended the first time it is encountered while absent from the stack. It can later be popped only if `last[letter] > i`, proving another occurrence remains. At that later occurrence, it can be appended again if still absent.

Eventually, the scan reaches the letter's final occurrence. If the letter is absent, it is appended. Once that final occurrence has been used, it can never be popped by a later character because `last[letter] > i` will be false. Thus, no required letter disappears permanently.

The membership check ensures no letter appears more than once. The final joined stack therefore contains each distinct input letter exactly once.

**Why the complete result is globally smallest**

At every index, the while loop removes every suffix letter that is both larger than the current letter and safely postponable. The exchange argument proves that retaining any such letter would make the result lexicographically worse. The loop never removes a smaller prefix letter or a mandatory last copy, because doing so would worsen order or destroy feasibility.

Consequently, after each processed prefix, the stack is the smallest feasible chosen prefix that can still be completed using the unprocessed suffix. When scanning ends, no future choices remain and that feasible prefix is the complete answer. It is therefore the lexicographically smallest valid distinct-letter subsequence.

## Complexity detail

Let $n$ be the string length. Building `last` takes $O(n)$ time, and the main loop visits every character once.

Although the main loop contains a `while`, each occurrence can be pushed at most once during its iteration and popped at most once later. Across the entire scan, the total number of stack pushes and pops is $O(n)$. Set operations are expected $O(1)$. Total time complexity is $O(n)$.

The string contains only 26 lowercase English letters. `last`, `vis`, and `stk` each hold at most 26 entries, so auxiliary space is $O(26)=O(1)$ with respect to $n$. The returned string also has at most 26 characters.

For an unbounded alphabet, the same algorithm would use $O(u)$ space for $u$ distinct characters, but the stated alphabet makes the constant-space manifest bound exact.

## Alternatives and edge cases

- **Recursive smallest-feasible-first-letter selection:** Find the smallest character whose suffix still contains every needed letter, choose it, remove later duplicates, and recurse. It is correct and linear under the fixed 26-letter alphabet, but repeated slicing is less direct than the stack.
- **Sort the distinct letters:** This ignores subsequence order. The alphabetically sorted set may not be obtainable from `s` while preserving indices.
- **Keep the first occurrence of every letter:** It guarantees uniqueness but can be lexicographically suboptimal when a larger early letter safely appears later.
- **Keep the last occurrence of every letter:** It may also produce a larger prefix and does not greedily optimize the order of selected occurrences.
- **Pop whenever the top is larger:** Without checking for a later copy, this can permanently remove a required letter.
- **Pop whenever a later copy exists:** Without requiring `top > c`, this may remove a smaller letter and make the result lexicographically larger.
- **Forget to remove a popped letter from `vis`:** Its later occurrence would be skipped, causing the final result to omit that letter.
- **Forget the duplicate check:** Repeated letters would be appended, violating exactly-once output.
- **One character:** It is appended and returned unchanged.
- **All characters equal:** The first occurrence is appended and every later occurrence is skipped, yielding one letter.
- **Already strictly increasing distinct letters:** No top is greater than the next character, so the input is returned unchanged.
- **Strictly decreasing distinct letters:** No letter has a later duplicate, so none can be popped; the original order is the only feasible distinct-letter subsequence.
- **A smaller letter arrives late:** Larger suffix letters are popped only when each has another future occurrence; mandatory letters form a barrier.
- **Repeated smallest letter:** Once selected, later copies are skipped. Earlier larger letters may already have been removed when its first useful occurrence appeared.
- **Lowercase guarantee:** Lexicographic character comparisons match alphabetical order directly.
