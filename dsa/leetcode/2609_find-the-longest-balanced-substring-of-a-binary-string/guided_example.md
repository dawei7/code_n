# Guided Example: Find the Longest Balanced Substring of a Binary String

## 1. The instance, its maximal runs, and the required outcome

The representative input is the fourteen-character string `00110001110001`, read left to right at positions $0$ through $13$, so that position $0$ holds `0`, position $1$ holds `0`, position $2$ holds `1`, and so on up to position $13$, which holds `1`. Compressing the string into maximal runs of equal characters gives the structure the whole lesson depends on.

| Run | Characters | Positions | Length | Character |
|---|---|---|---|---|
| 1 | `00` | 0–1 | 2 | `0` |
| 2 | `11` | 2–3 | 2 | `1` |
| 3 | `000` | 4–6 | 3 | `0` |
| 4 | `111` | 7–9 | 3 | `1` |
| 5 | `000` | 10–12 | 3 | `0` |
| 6 | `1` | 13 | 1 | `1` |

A substring of `s` is **balanced** when, inside that substring, every `0` occurs before every `1` and the two characters occur equally often. The empty substring is balanced by definition, so the answer can never be negative.

For this instance the longest balanced substring is `s[4..9]`, the six characters `000111`, and the required outcome is therefore $6$. Two shorter candidates are visible in the same string: `0011` at positions $0$–$3$ has length $4$, and `01` at positions $10$–$13$ has length $2$. A method must be able to compare candidates that live in different parts of the string, because the best one is not the first one.

## 2. What "balanced" forces: the shape of an admissible substring

The first condition is a shape constraint. If a `1` appeared while a later position still held a `0`, the substring would contain a one before a zero and would be rejected. So every balanced substring has all of its zeroes first and all of its ones last, which means it is literally of the form

$$0^{k}1^{k}$$

for some $k \ge 0$. This single observation collapses a two-condition problem into a one-parameter search: the answer is twice the largest admissible $k$, and therefore always even.

The second consequence is the one that makes an efficient method possible. Suppose a balanced substring uses a block of $k$ zeroes and then a block of $k$ ones. Since the characters are contiguous in `s`, the zero block lies inside **one** maximal zero run — if it spilled out of that run, a `1` would sit between its zeroes. By the same argument the one block lies inside one maximal one run, and it must be the maximal one run that comes immediately after that zero run, because any intervening run is a zero run that would place zeroes after ones.

So the search space is not "all substrings". It is exactly the set of adjacent pairs consisting of a maximal zero run followed by a maximal one run. For each such pair with run lengths $z$ and $o$, the best achievable balance is $k = \min(z, o)$: the substring may use a suffix of the zero run and a prefix of the one run, and it cannot use more than the shorter run supplies.

## 3. Why counting zeroes and ones globally is not enough

The most tempting shortcut is to count every `0` and every `1` in `s` and answer twice the smaller total. For this instance that count is eight zeroes against six ones, suggesting a balanced substring of length $12$ — but the required answer is $6$. The shortcut ignores arrangement, and arrangement is what the shape condition is about.

| Reading of the instance | Zeroes | Ones | Predicted answer | Required answer |
|---|---|---|---|---|
| Counts over the whole string `00110001110001` | 8 | 6 | 12 | 6 |
| Counts inside `000111` at positions 4–9 | 3 | 3 | 6 | 6 |
| Counts over the whole string `01000111` | 3 | 4 | 6 | 6 |

The third row shows why this shortcut is dangerous rather than merely inaccurate: on the sample `01000111` the global counts $3$ and $4$ happen to produce the correct value $6$, so the wrong method passes a test and then fails on this instance. A method must be justified by the shape argument, not by agreement on one input.

A second near-miss is a greedy that grabs the first zero run and the first one run and stops. On this instance that greedy pairs run 1 with run 2 and returns $4$, missing the $6$ built from runs 3 and 4. Candidates must be compared, not accepted on first sight.

## 4. The run-pair reduction

Walk the maximal runs once and consider every index $r$ where a zero run of length $z_r$ is immediately followed by a one run of length $o_r$. The reduction is

$$\text{answer} = 2 \cdot \max_{r} \min(z_r, o_r),$$

where the maximum over an empty family of pairs is $0$. Section 5 will execute this formula; Section 6 proves that no other substring can beat it.

The formula also suggests how to evaluate it without ever storing the run decomposition explicitly. Keep two counters while reading `s` left to right: $z$, the length of the zero run currently being read, and $o$, the length of the one run that follows it. On a `0`, either extend the current zero run or — if $o > 0$, meaning the previous pair has just ended — settle the finished pair with the value $2\min(z, o)$, then begin a fresh zero run. On a `1`, extend the one run. When the string ends, one final pair may still be open and is settled with the same rule. Two counters and one best-so-far value are all the state required.

## 5. Step-by-step scan of the instance

The table records the full state evolution. The column `z`, `o` shows the counters *before* the character at that position is processed, and the action column says what the character triggers.

| Position | Character | `z`, `o` before | Action | Best after |
|---|---|---|---|---|
| 0 | `0` | 0, 0 | no open one run, so open the zero run: `z = 1` | 0 |
| 1 | `0` | 1, 0 | extend the zero run: `z = 2` | 0 |
| 2 | `1` | 2, 0 | open the one run: `o = 1` | 0 |
| 3 | `1` | 2, 1 | extend the one run: `o = 2` | 0 |
| 4 | `0` | 2, 2 | pair closed: candidate $2\min(2,2) = 4$; restart with `z = 1`, `o = 0` | 4 |
| 5 | `0` | 1, 0 | extend the zero run: `z = 2` | 4 |
| 6 | `0` | 2, 0 | extend the zero run: `z = 3` | 4 |
| 7 | `1` | 3, 0 | open the one run: `o = 1` | 4 |
| 8 | `1` | 3, 1 | extend the one run: `o = 2` | 4 |
| 9 | `1` | 3, 2 | extend the one run: `o = 3` | 4 |
| 10 | `0` | 3, 3 | pair closed: candidate $2\min(3,3) = 6$; restart with `z = 1`, `o = 0` | 6 |
| 11 | `0` | 1, 0 | extend the zero run: `z = 2` | 6 |
| 12 | `0` | 2, 0 | extend the zero run: `z = 3` | 6 |
| 13 | `1` | 3, 0 | open the one run: `o = 1` | 6 |
| end | — | 3, 1 | trailing pair settled: candidate $2\min(3,1) = 2$ | 6 |

The three settled pairs are exactly the three adjacent zero-run/one-run pairs of Section 1, and the best value never decreases after position 10.

| Pair settled | Zero-run length $z$ | One-run length $o$ | $\min(z, o)$ | Candidate $2\min(z,o)$ | Running best |
|---|---|---|---|---|---|
| Runs 1 and 2 | 2 | 2 | 2 | 4 | 4 |
| Runs 3 and 4 | 3 | 3 | 3 | 6 | 6 |
| Runs 5 and 6 | 3 | 1 | 1 | 2 | 6 |

The maximum is $6$, attained at the second pair and realised by the substring `000111` spanning positions 4 through 9 — exactly the required outcome. Note that the winning pair is not the pair with the longest runs in aggregate (runs 3, 4 and 5 have lengths 3, 3, 3) but the pair whose two lengths are the most evenly matched, because the shorter side caps the balance.

## 6. Invariant and correctness of the run-pair maximum

**Scan invariant.** After the character at position $i$ has been processed, $z$ equals the length of the maximal zero run ending at $i$ (or $0$ if the character at $i$ is a `1`), $o$ equals the length of the maximal one run that follows that zero run and reaches $i$ (or $0$ if no such one run has started), and the running best equals the largest $2\min(z_r, o_r)$ over all pairs fully contained in `s[0..i]`. Each character updates exactly one counter or settles exactly one pair, so the invariant is restored at every step; the value is never copied from a stale pair because a settled pair is final — a maximal run cannot be extended after the next character changes.

**Every candidate is attainable.** Let a pair have lengths $z$ and $o$, and let $k = \min(z, o)$. The last $k$ zeroes of the zero run and the first $k$ ones of the one run are contiguous in `s` (nothing separates two adjacent runs), and together they spell $0^{k}1^{k}$, which satisfies both balance conditions. So the substring of length $2k$ exists, and the running best never exceeds the true answer.

**No admissible substring is missed.** Take any balanced substring and let $k$ be its number of zeroes. By the shape argument it is $0^{k}1^{k}$, so its zero block lies inside a single maximal zero run and its one block inside the immediately following maximal one run. Those runs therefore have lengths $z \ge k$ and $o \ge k$, which makes $2\min(z, o) \ge 2k$: the pair that contains this substring already yields a candidate at least as long. Hence the maximum over pairs is at least the length of every balanced substring, and combined with the previous paragraph it equals the length of the longest one.

An immediate corollary is the failure condition. If `s` contains no `0` or no `1`, no pair exists, the family of candidates is empty, and the answer is $0$ — which correctly describes both `111` and `000000`, where only the empty substring is balanced.

## 7. Boundary cases and traps

| Situation | Instance | What the run-pair rule returns | Why it is right |
|---|---|---|---|
| Only ones | `111` | 0 | no zero run ever exists to open a pair |
| Only zeroes | `000000` | 0 | the zero run is never followed by a one run |
| Single character | `0` | 0 | the empty substring is the only balanced one |
| Ones outnumber zeroes | `00111` | 4 | the substring keeps `0011`, discarding the surplus `1` |
| Zeroes outnumber ones | `000011` | 4 | the substring keeps `0011`, discarding the surplus prefix `00` |
| Isolated zero between one runs | `01000111` | 6 | the leading `0` cannot join later zeroes, but the pair `000`/`111` still wins |
| Several candidates | `00110001110001` | 6 | the maximum is compared across all pairs, not taken from the first |

Two semantic traps deserve separate mention. First, a balanced substring must satisfy both conditions simultaneously: equal counts alone is not enough, since `10` has one zero and one one but every `1` precedes a `0`. Second, surplus characters are always discarded from the *outside* of a candidate — from the front of a zero run or the back of a one run — never from the middle, because a substring is contiguous. That is precisely why $\min(z, o)$, and not $z + o$ or some other aggregate, is the right quantity to maximize.

The alternatives that were considered and rejected are summarized below.

| Method | Time | Auxiliary space | Verdict |
|---|---|---|---|
| Test every substring directly | $O(n^{3})$ | $O(1)$ | correct but inspects every start, end and interior character |
| Prefix counts plus a shape test | $O(n^{2})$ | $O(n)$ | correct; still quadratic because every start is retried |
| Global totals of zeroes and ones | $O(n)$ | $O(1)$ | wrong: it predicted $12$ on this instance and $6$ on `01000111` where the arrangement differs |
| Pair adjacent maximal runs, keeping the best | $O(n)$ | $O(1)$ | correct and optimal; each character is read once |

## 8. Complexity of the run-pair scan

Let $n$ denote the length of `s`, so $n = 14$ for this instance and $n \le 50$ under the contract. The scan reads every character exactly once. A character either increments one of the two counters or settles one finished pair, and settling a pair performs a constant number of operations ($\min$, a doubling, a comparison with the best). Each pair is settled at most once, and the number of pairs is at most the number of runs, which is at most $n - 1$. The total work is therefore

$$O(n)$$

time, with no dependence on how the runs are distributed.

Auxiliary space is $O(1)$. The entire state is the current zero-run counter, the current one-run counter, and the best candidate seen so far; no array, no run list, and no copy of the string is needed beyond reading it. A direct substring enumeration would instead need $O(n)$ space for prefix counts and $O(n^{2})$ or $O(n^{3})$ time, which the shape argument makes unnecessary.