## General

**Track the two largest distinct digits while scanning**

The answer depends on distinct numerical digits, not on how many times each digit appears. The protected solution keeps two variables:

- `a` is the largest distinct digit seen so far;
- `b` is the second-largest distinct digit seen so far.

Both start at -1. Every valid digit is between 0 and 9, so -1 is smaller than any possible digit and also serves as the required return value when a second distinct digit never appears.

The loop reads every character `c` in `s`. Letters are ignored. When `c.isdigit()` is true, `int(c)` converts the one-character digit to its numerical value `v`.

**Update when a new largest digit appears**

If `v > a`, the new value becomes the largest. The old largest does not disappear; it becomes the best candidate for second largest. The simultaneous assignment

`a, b = v, a`

stores the new largest in `a` and the previous value of `a` in `b`.

For example, if the tracked digits are `a = 5` and `b = 3` and the scan finds 8, the state becomes `a = 8` and `b = 5`. Value 3 is no longer among the top two.

Simultaneous assignment matters conceptually: Python evaluates the right-hand values before changing either variable, so `b` receives the old `a` rather than the new `v`.

**Update when a value belongs strictly between them**

If `v` is not greater than `a`, it cannot replace the largest. It replaces the second largest only when

`b < v < a`.

Both inequalities are strict. The upper inequality excludes another copy of the largest, because the second-largest digit must be distinct. The lower inequality excludes values that cannot improve `b`, including another copy of the current second largest.

If neither update applies, the digit is a duplicate of an existing maximum or is too small to affect the top two.

**Following the first example**

For `s = "dfa12321afd"`, letters are skipped. The digit 1 first changes the state from `(-1, -1)` to `(1, -1)`. Digit 2 becomes the new largest, producing `(2, 1)`. Digit 3 produces `(3, 2)`.

The later 2 is not greater than 3 and does not satisfy `b < v` because `b` is already 2, so it is ignored. The later 1 is also ignored. The final second-largest value is 2.

For `"abc1111"`, the first 1 sets `a = 1` while `b` remains -1. Every later 1 equals `a` and is ignored. Since only one distinct digit occurred, returning -1 is correct.

**The invariant after every processed prefix**

After any prefix of the string:

- if that prefix contains at least one digit, `a` is its greatest distinct digit; otherwise `a = -1`;
- if it contains at least two distinct digits, `b` is the second greatest; otherwise `b = -1`.

The invariant is initially true for the empty prefix. A letter changes nothing. For a digit, there are three exhaustive cases:

1. it exceeds `a`, so it becomes the largest and the old largest becomes second;
2. it lies strictly between `b` and `a`, so only the second-largest position changes;
3. it is equal to an existing top value or no greater than `b`, so the top two remain correct.

Thus the invariant remains true after each character. At the end, `b` is exactly the requested second-largest distinct numerical digit, or remains -1 when fewer than two distinct digits exist.

**Why no set or sorting is necessary**

There are only ten possible digits, but even storing all ten is more state than needed for this question. Any digit below the current second largest can never matter later: future characters may raise the top values, but an already inferior value cannot become second unless larger values vanish, and scanned values never vanish.

The two-variable state is therefore sufficient for a streaming solution. The string need not be filtered, copied, or revisited.

**Character classification under the input contract**

Python's `str.isdigit()` recognizes some digit characters beyond ASCII. The problem guarantees only lowercase English letters and ordinary digits, so every accepted digit here is exactly one of `'0'` through `'9'` and `int(c)` is appropriate. The broader library behavior does not affect valid inputs.

## Complexity detail

Let $n$ be the length of `s`. The loop examines every character once and performs constant work, giving $O(n)$ time. It may not stop early because a larger digit near the end can change both tracked positions.

Only `a`, `b`, `c`, and `v` are used as scalar state. Auxiliary space is $O(1)$, matching the manifest. The returned integer is not additional growing storage.

The source constraint $n\leq500$ is small, but the streaming bound remains linear for longer strings.

## Alternatives and edge cases

- **Boolean array of ten digits:** Mark each encountered digit and scan from 9 downward afterward. This is also $O(n)$ time and $O(1)$ space, but uses more explicit state.
- **Set plus sorting:** Collecting distinct digits and sorting them works, yet it obscures the one-pass top-two invariant.
- **Sort all digit occurrences:** Duplicates must then be skipped, and copying plus sorting is unnecessary.
- **Convert every character directly:** Calling `int` on a letter would fail, so classification must occur first.
- **No digits:** Both variables remain -1, and returning -1 correctly reports no second largest digit.
- **Exactly one distinct digit:** The largest is tracked in `a` while `b` remains -1.
- **Repeated largest digit:** Strict comparison prevents it from being mistaken for the second-largest distinct digit.
- **Repeated second-largest digit:** It leaves `b` unchanged and is counted only as the same value.
- **Digit zero:** Zero is greater than the -1 sentinel and is handled normally.
- **Digits zero and one only:** The final state becomes `a = 1` and `b = 0`, so zero can be a valid answer.
- **Descending encounter order:** A smaller digit can fill `b` without changing `a`.
- **Ascending encounter order:** Every new maximum shifts the old maximum into `b`.
- **Letters between digits:** They have no effect on the invariant.
- **ASCII input guarantee:** It makes `isdigit` followed by `int` safe for every valid digit character.
- **Input preservation:** The solution reads the string without constructing a modified copy.
