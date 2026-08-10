## General

An additive partition has only two free choices: where the first number ends and where the second number ends. Once those first two values are fixed, every later value is forced. If the previous values are $a$ and $b$, the next value must be exactly $a+b$.

The source enumerates every possible pair of first-number and second-number boundaries. For each pair, a recursive helper attempts to consume the remaining digits as successive forced sums. A candidate succeeds only when the recursion consumes the entire string.

**Enumerating the first two numbers**

Let the complete digit string have length $n$. The outer boundary `i` ranges from 1 through $n-2$, so `num[:i]` is nonempty and at least two digits remain for the second number and a third number.

For each `i`, boundary `j` ranges from `i + 1` through $n-1$. Thus:

- the first term is `num[:i]`;
- the second term is `num[i:j]`;
- the suffix `num[j:]` is nonempty and must contain at least the third term.

These ranges enforce the requirement of at least three numbers. The helper cannot report success merely after choosing two terms because its initial suffix always contains at least one digit.

Every legal placement of the first two boundaries appears in these loops. There is no need to choose later boundaries independently because their numeric values are determined by addition.

**Rejecting leading zeros in the chosen first terms**

A multi-digit number cannot begin with zero.

If the first number has length greater than one and `num[0] == '0'`, the source breaks the inner loop. Changing `j` cannot repair the first term because its boundary `i` is fixed. For subsequent larger values of `i`, the first term still begins with zero and remains invalid.

If the second number has length greater than one and `num[i] == '0'`, the source continues to the next `j`. The one-digit second value `"0"` is allowed, but extending it to `"01"`, `"012"`, or any other multi-digit zero-prefixed text is not.

After these checks, converting the two slices with `int` gives valid first values `a` and `b`.

**Meaning of the recursive helper**

`dfs(a, b, remaining)` asks whether all digits in `remaining` can continue a sequence whose previous two numeric values are $a$ and $b$.

If `remaining` is empty, every earlier forced term matched and consumed the complete input, so the helper returns `True`.

Otherwise, the required next value is $a+b$. The helper tries each nonempty prefix `remaining[:i]`, converts it to an integer, and compares it with that required value. On equality, it recurses with:

- old second value $b$ as the new first value;
- matched sum $a+b$ as the new second value;
- the suffix after the matched prefix as the new remaining text.

This shifts the additive window from $(a,b)$ to $(b,a+b)$.

If a recursive match eventually consumes everything, success propagates immediately. If no tried prefix leads to complete consumption, the current state returns `False`.

**Why complete consumption matters**

Matching several additive terms is insufficient if extra digits remain. For example, a prefix of the input might form `1, 1, 2, 3`, but unrelated trailing digits would make the complete string non-additive under that partition.

Only the `if not num: return True` base case accepts a candidate. It is reached after a matched next term passes the remaining suffix onward and eventually consumes its last digit. Therefore, every character belongs to exactly one sequence term.

**Tracing `112358`**

The boundaries `i = 1` and `j = 2` select $a=1$ and $b=1$, leaving `"2358"`.

- Required sum is 2. Prefix `"2"` matches, so recurse with $(1,2)$ and `"358"`.
- Required sum is 3. Prefix `"3"` matches, so recurse with $(2,3)$ and `"58"`.
- Required sum is 5. Prefix `"5"` matches, so recurse with $(3,5)$ and `"8"`.
- Required sum is 8. Prefix `"8"` matches, leaving the empty suffix.

The empty-suffix base case returns `True`, so the method accepts the string.

For `199100199`, the successful first boundaries select 1 and 99. The helper finds prefix 100 because $1+99=100$, then consumes 199 because $99+100=199$.

**Why trying all first pairs is complete**

Suppose a valid additive partition exists. Its first and second terms end at some legal indices `i` and `j`; the nested loops necessarily examine that pair, and the leading-zero checks do not reject it because valid terms obey the rule.

For that pair, each later term equals the sum of the two preceding terms. The helper tries every nonempty prefix, so it eventually tries the exact textual span of each valid next term. Following those matching branches consumes the entire input and returns `True`.

Conversely, a successful recursive chain begins with two legal nonempty terms, matches every subsequent numeric term to the preceding sum, includes at least one subsequent term, and consumes every digit. Subject to the zero handling discussed next, it witnesses an additive sequence.

**The exact helper's special handling of zero**

Before trying prefixes, the source rejects a remaining suffix beginning with zero only when $a+b>0$. This is safe for a positive expected sum: no valid decimal representation of a positive number begins with zero.

When $a+b=0$, both preceding nonnegative values must be zero. The valid next representation is the single digit `"0"`. However, `int("00")`, `int("000")`, and longer all-zero prefixes also equal zero, so the loop may recursively explore those multi-digit prefixes even though they violate the no-leading-zero rule.

This does not create a false Boolean acceptance. If a branch made only of zero-valued terms consumes the suffix, that suffix consists entirely of zeros, and the same suffix can be consumed as a sequence of legal one-digit zero terms. If any nonzero digit remains, grouping preceding zeros into longer terms cannot make the required sum stop being zero, so the branch still fails. Nevertheless, the redundant partitions materially affect runtime.

## Complexity detail

Let $n$ be the digit-string length. There are $O(n^2)$ choices for the first two boundaries.

The manifest's intended $O(n^3)$ analysis assumes that, for each first pair, verification computes the one forced sum text and advances through the suffix in linear total time. The exact helper does something broader: at each recursive suffix, it loops over every possible prefix and repeatedly slices and parses those prefixes.

For positive expected sums, a conservative unit-cost bound is higher than the manifest: one first-pair verification can visit $O(n)$ recursive suffixes and scan $O(n)$ prefixes at each, giving $O(n^2)$ prefix tests and up to $O(n^4)$ tests across all first pairs. Counting the cost of copying and parsing length-$O(n)$ prefixes raises a conservative character-work bound further.

More importantly, when the expected sum is zero and a suffix contains many zeros followed by a failure-causing digit, many different all-zero prefix lengths compare equal to zero. The helper can explore the compositions of that zero run, producing exponentially many redundant recursive paths. Thus, the exact source's worst-case time is exponential in $n$, with another polynomial factor for slicing and integer conversion. The stated $O(n^3)$ bound describes the direct forced-text verifier, not this precise loop behavior.

Recursion depth is $O(n)$ because each recursive call consumes at least one digit. In an index-based implementation, the active call stack and numeric state would use $O(n)$ space. This source passes sliced suffix strings; ancestor frames retain progressively shorter strings whose total character storage can reach $O(n^2)$ along one branch. Python's arbitrary-precision integers also avoid overflow but may occupy space proportional to their digit counts.

## Alternatives and edge cases

- **Direct forced-sum matching:** Compute `expected = str(a + b)` and require the remaining suffix to start with exactly that text. Then advance by `len(expected)`. This removes the prefix loop, enforces the zero representation automatically, and realizes the intended polynomial verification.
- **Index-based verification:** Keep one original string plus a current offset instead of passing `num[i:]` slices. It avoids retaining copied suffixes and makes space usage closer to the recursion depth.
- **Manual decimal-string addition:** In a language with fixed-width integer overflow, add the two previous terms digit by digit as strings and compare the resulting text. Python integers already grow as needed, so the exact source needs no overflow workaround.
- **Backtrack every boundary:** Choosing a cut or no cut at every digit gap explores exponentially many partitions even when most later values are already forced. Enumerating only the first two cuts is the central reduction.
- **Stop after three matching numbers:** A valid prefix is not enough; every digit of the original string must be consumed.
- **Allow a multi-digit leading zero:** Terms such as `"01"` are invalid even though integer conversion yields 1. The first two loop checks and positive-sum suffix check prevent these cases.
- **All zeros:** Strings such as `"000"` are valid as `0, 0, 0`. Longer all-zero strings are valid as additional one-digit zero terms.
- **`"101"`:** It is valid as `1, 0, 1`; a one-digit zero is allowed.
- **Too-short input:** With fewer than three digits, the boundary ranges generate no candidate pair, so the method returns `False`.
- **Exactly three terms:** The first recursive match may consume the complete suffix and reach the empty base case immediately.
- **A valid prefix plus extra digits:** The recursion eventually fails unless those extra digits equal further forced sums.
- **Large terms:** A term may contain many digits. Python's `int` conversion and addition remain exact, satisfying the overflow follow-up in this environment.
- **First number begins with zero:** Only the one-digit first term zero may be tried; longer first slices are rejected.
- **Second number begins with zero:** Only the one-digit second term zero is legal; longer choices are skipped.
- **At least three numbers:** Because `j < n`, every initial candidate leaves a nonempty suffix that must match at least one sum.
- **Return on first witness:** The problem asks only whether a partition exists, so the source safely stops when any boundary pair succeeds.
