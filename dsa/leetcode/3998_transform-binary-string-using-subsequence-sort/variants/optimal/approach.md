## General

**Understand what sorting a binary subsequence can change.**  A selected binary subsequence contains some number of `0` characters followed by some number of `1` characters after it is sorted. Those same characters are written back into the selected indices from left to right. Thus the operation can move selected zeros toward earlier selected positions and selected ones toward later selected positions.

Two facts follow:

1. The total number of ones never changes, because sorting only rearranges existing characters.
2. In every prefix, the number of ones can stay the same or decrease, but it can never increase.

The second fact is the crucial direction. Among the selected positions that lie in any prefix, sorting puts as many selected zeros as possible into those earlier positions. It cannot bring an extra one from a later selected position forward past a zero.

Let `source_prefix[i]` be the number of ones in `s[0..i]`, including index `i`. A fully specified binary target `t` is reachable exactly when:

- `t` contains the same total number of ones as `s`; and
- for every index `i`, the number of ones in `t[0..i]` is at most `source_prefix[i]`.

These conditions are necessary by the two observations above.

They are also sufficient. Think about the positions of the first one, second one, and so on. The prefix inequalities say that the `r`-th one in the target is never to the left of the `r`-th one in the source. Each one only needs to stay in place or move right. Whenever a one must cross a later zero, selecting those two positions gives the subsequence `"10"`; sorting it changes those positions to `"01"`. Repeating such moves constructs the target. Therefore, preserving the total and never exceeding a source prefix's one count completely characterizes reachability.

**First summarize the source string.**  The exact solution scans `s` once. The variable `ones` counts how many ones have appeared so far, and each cumulative value is appended to `source_prefix`. After the loop, `ones` is also the required total number of ones in every completed pattern, so the source stores it as `required_ones`.

**Choose the best possible replacement of question marks.**  A pattern may represent many completed binary strings. Trying all `2^q` assignments for `q` question marks would be far too expensive. The prefix condition reveals one assignment that is at least as easy to reach as every other assignment with the required total.

For one `pattern`, the source computes:

- `fixed_ones`, the number of literal `"1"` characters;
- `question_count`, the number of `"?"` characters;
- `needed_ones = required_ones - fixed_ones`.

Exactly `needed_ones` question marks must become ones so that the completed pattern has the same total number of ones as `s`. If `needed_ones < 0`, the fixed ones already exceed the source total. If `needed_ones > question_count`, there are not enough question marks to supply all required ones. Either case makes the pattern impossible immediately.

When the count is feasible, the remaining

`zero_questions = question_count - needed_ones`

question marks must become zeros.

Where should those zeros and ones be placed? Prefix feasibility becomes easiest when every question-mark one is delayed as far to the right as possible. Equivalently, make the first `zero_questions` question marks zeros and make all later question marks ones. This assignment has the smallest possible number of ones in every prefix among all assignments with the same total.

If this most favorable assignment violates a source prefix limit, moving any chosen one earlier cannot repair the violation. Therefore no assignment works. If the favorable assignment satisfies every prefix limit, it itself is a reachable completed target, so the pattern works.

**How the second scan constructs that favorable assignment without building it.**  The variables have these meanings:

- `pattern_ones` is the number of ones assigned in the current pattern prefix;
- `questions_seen` is the number of question marks encountered before or at the current step;
- `zero_questions` says how many earliest question marks must remain zero.

A literal `"1"` increments `pattern_ones`. A literal `"0"` does not. For a `"?"`, the test

`questions_seen >= zero_questions`

is performed before incrementing `questions_seen`. Thus the first `zero_questions` question marks contribute zero, and every question mark after them contributes one.

After processing each character at `index`, the source compares `pattern_ones` with `source_prefix[index]`. If the pattern prefix contains more ones, the reachability invariant has failed and `possible` becomes false. The scan can stop early because adding later characters cannot change a prefix that already has too many ones.

**Walk through the first example.**  For `s = "101"`, the source prefix counts are `[1, 1, 2]` and `required_ones = 2`.

- Pattern `"1?1"` already has two fixed ones. Its question mark must be zero, producing `"101"`. Its prefix counts `[1, 1, 2]` pass.
- Pattern `"0?1"` has one fixed one, so its question mark must be one, producing `"011"`. Its prefix counts `[0, 1, 2]` never exceed the source counts.
- Pattern `"0?0"` has no fixed ones but only one question mark. It needs two question-mark ones, which is impossible before any prefix scan begins.

The resulting booleans are `[True, True, False]`.

**Important defect in the exact stored source.**  The method annotations use `List[str]` and `List[bool]`, but the file does not import `List` from `typing` and does not define it. In an ordinary Python module, class definition therefore raises

`NameError: name 'List' is not defined`.

The algorithm works as described if the execution harness supplies `List`, but the exact file is not standalone. This documentation records that source dependency rather than silently treating the missing import as present.

## Complexity detail

Let `n` be the length of `s` and let `m` be the number of patterns.

Building `source_prefix` takes `O(n)` time. For each pattern, the two `count` calls each scan `n` characters, and the prefix-feasibility loop scans at most `n` more. A constant number of full scans still gives `O(n)` time per pattern.

- Total time complexity is `O(nm)`.
- Auxiliary space complexity is `O(n)`, excluding the required output array.

The prefix list holds `n` integers. Each pattern is handled with a constant number of counters and booleans; the favorable completed string is never constructed. The returned `answer` contains `m` booleans and therefore uses `O(m)` output space. If output storage is included in the space accounting, the total is `O(n + m)`.

## Alternatives and edge cases

- **Enumerate all question-mark assignments:** A pattern with `q` question marks has `2^q` completions. Assigning the required ones to the latest question marks gives the prefix-minimal completion directly.
- **Simulate arbitrary subsequence sorts:** The operation has exponentially many subsequence choices. Total-one equality and prefix dominance capture the entire reachable set without exploring operations.
- **Move ones with a queue of positions:** One can match source-one positions to target-one positions and check that none moves left. This is equivalent to the prefix test, but the cumulative counts integrate more naturally with wildcard assignment.
- **Too many fixed ones:** When `fixed_ones > required_ones`, question marks cannot delete literal ones, so the pattern is immediately false.
- **Too few available ones:** When `fixed_ones + question_count < required_ones`, even turning every question mark into one cannot preserve the source total.
- **All question marks:** The source assigns zeros first and the required number of ones last. This is the most right-shifted binary string with the correct total and therefore the easiest completion to reach.
- **No question marks:** The count check requires the fixed target to have exactly the source's number of ones, and the prefix scan becomes the ordinary binary reachability test.
- **A prefix violation:** Once `pattern_ones > source_prefix[index]`, later assignments cannot alter that already-fixed prefix. Breaking early is safe.
- **Equal source and completed target:** Every prefix count is equal, so zero operations are allowed and the pattern returns true.
- **Sorting the entire string:** This produces all zeros followed by all ones and is one reachable extreme, but many intermediate targets are also reachable by sorting smaller subsequences.
- **Operation direction:** Sorting is non-decreasing. It can move ones right across zeros, not left. Reversing the prefix inequality would characterize the wrong operation.
- **Boolean arithmetic:** In Python, `char == "1"` is a boolean that behaves as `0` or `1` in addition. This is why `ones += char == "1"` correctly updates the count.
- **Missing `List` import:** The stated algorithmic bounds assume the method can be defined. The exact source needs `List` supplied by the environment or imported separately before those annotations can be evaluated.
