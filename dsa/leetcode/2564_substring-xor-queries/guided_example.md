# Guided Example: Substring XOR Queries

## 1. Turning every query into a target value

Each query supplies two integers, `first` and `second`, and asks for a substring whose decimal value $val$ satisfies

$$
val \oplus \text{first} = \text{second}
$$

Bitwise XOR is its own inverse: applying the same mask twice restores the original bits. XORing both sides of the equation by `first` therefore isolates the unknown on the left and turns the equation into a plain value request:

$$
val = \text{first} \oplus \text{second}
$$

Every query is thus resolved to a single integer target, and the whole problem becomes: given a binary string and a list of integers, report where each integer occurs as the decimal value of a substring, choosing the shortest occurrence and breaking ties by the smallest left index.

Two consequences follow immediately. Queries do not interact — two different queries can produce the same target and must then receive the same endpoints. And the query stage needs no knowledge of the string beyond a lookup, so all the work belongs to a single preprocessing pass.

## 2. Reading a substring's value, and the 30-bit ceiling

The decimal value of the bits `s[i]` through `s[j]` is a positional sum:

$$
val(i, j) = \sum_{k=i}^{j} s[k] \cdot 2^{\,j-k}
$$

which can be built incrementally as the window grows to the right: appending one bit $b$ to a value $x$ shifts it left by one place and adds the new bit,

$$
x \leftarrow 2x + b
$$

That single recurrence means the value of every window starting at a fixed position can be produced in one left-to-right sweep, with no re-reading of earlier bits.

The bit ceiling is decided by the constraints. Both `first` and `second` are at most $10^9$, and $2^{30} = 1\,073\,741\,824$ exceeds $10^9$, so each operand fits in 30 bits and so does their XOR. Any substring of **31 or more** bits has a value of at least $2^{30}$, which can never equal a target. Extending each start by at most 30 bits is therefore not a heuristic cut-off but an exact bound: nothing that could answer a query is skipped.

## 3. The three rules that build the dictionary

The preprocessing is a dictionary from substring value to its answer endpoints. Three design rules make the stored entry the correct one rather than merely *an* occurrence.

| Rule | Effect on the dictionary | Why it gives the right answer |
|---|---|---|
| Sweep every start position, extending up to 30 bits | every substring that could match a target is visited, and every visited value is offered for storage | completeness: no target that occurs is missed |
| Store a value only the first time it is produced | the earliest discovery wins, and discovery order is by increasing start position and then by increasing length | leftmost tie-break: among occurrences of equal length, the survivor has the smallest left index |
| Stop extending as soon as the running value is `0` | a window that begins with `0` is never grown past that single bit | shortest-first: every recorded occurrence starts with `1`, so its length equals the bit length of its value, which no other occurrence can beat |

The third rule deserves the emphasis it gets. A window beginning with `0` and continuing with more bits has the same value as the window with that leading `0` removed, and the shortened window is strictly shorter and starts further right. If such windows were allowed into the dictionary, a four-character match with a small left index could displace a two-character match with a larger one, and the "shortest first" requirement would be violated. Since the dictionary is scanned by increasing start position, the very first entry written for a value is the one at the smallest left index among all canonical occurrences — and every canonical occurrence of a nonzero value has exactly the same length, namely its bit length.

## 4. Worked instance: the first official sample

Take `s = "101101"` with `queries = [[0, 5], [1, 2]]`, whose required output is `[[0, 2], [2, 3]]`. The two targets are $0 \oplus 5 = 5$ and $1 \oplus 2 = 3$.

Reading the string as positions $0 \dots 5$ holding the bits `1 0 1 1 0 1`, the preprocessing sweep behaves as follows:

| Start $i$ | Bits read from $i$ | Values produced in order | Entries recorded by this start | Note |
|---|---|---|---|---|
| 0 | `1`, `10`, `101`, `1011`, `10110`, `101101` | 1, 2, 5, 11, 22, 45 | 1 → `[0, 0]`, 2 → `[0, 1]`, 5 → `[0, 2]`, 11 → `[0, 3]`, 22 → `[0, 4]`, 45 → `[0, 5]` | six distinct values, all new, because this is the first start |
| 1 | `0` | 0 | 0 → `[1, 1]` | the bit itself is `0`, so the extension stops before a longer window can be formed |
| 2 | `1`, `11`, `110`, `1101` | 1, 3, 6, 13 | 3 → `[2, 3]`, 6 → `[2, 4]`, 13 → `[2, 5]` | the value `1` is already owned by the smaller left index 0 |
| 3 | `1`, `10`, `101` | 1, 2, 5 | none | every value here already has a leftmost occurrence |
| 4 | `0` | 0 | none | zero was recorded at index 1 and is not overwritten |
| 5 | `1` | 1 | none | the single bit repeats a known value |

The dictionary that results maps `0 → [1, 1]`, `1 → [0, 0]`, `2 → [0, 1]`, `3 → [2, 3]`, `5 → [0, 2]`, `6 → [2, 4]`, `11 → [0, 3]`, `13 → [2, 5]`, `22 → [0, 4]`, and `45 → [0, 5]`.

## 5. Answering the queries

Each query now costs one XOR and one lookup:

| Query | Target $val = \text{first} \oplus \text{second}$ | Dictionary entry | Reported endpoints |
|---|---|---|---|
| `[0, 5]` | $0 \oplus 5 = 5$ | value 5 is stored at `[0, 2]` | `[0, 2]` |
| `[1, 2]` | $1 \oplus 2 = 3$ | value 3 is stored at `[2, 3]` | `[2, 3]` |

The first answer corresponds to the substring `"101"`, whose value is $4 + 1 = 5$, and $5 \oplus 0 = 5$ as required. The second corresponds to `"11"`, whose value is 3, and $3 \oplus 1 = 2$ as required. Neither endpoint pair needed any scanning of the string at query time; the string was fully digested during preprocessing.

Note how the two answers are found at different scales: value `5` was recorded at start 0 as the third window of that start, while value `3` was only produced at start 2, because the substring `"11"` does not occur earlier. The dictionary does not care about the order in which values were discovered, only that the first discovery of each is the correct one.

## 6. Why the stored entry is exactly the required answer

The correctness argument has three parts, one per requirement.

*Existence.* If a substring has the target value, its length is at most 30 bits, because the target is at most 30 bits and a longer window would exceed it. The sweep visits that start position and extends far enough to build it, so the value enters the dictionary, and the lookup succeeds. When no substring matches, every start position has been exhausted and the value is genuinely absent, so `[-1, -1]` is correct rather than a premature giveaway.

*Minimal length.* A stored occurrence is always a window whose first bit is `1`, except for the single-bit window holding `0`. Removing a leading `0` from any other window leaves a shorter window with the same value, so the shortest occurrence of a nonzero target never starts with `0`, and the sweep's stop rule guarantees that no `0`-prefixed window with more than one bit is ever stored. Consequently the stored occurrence of a nonzero value has the smallest possible length.

*Leftmost tie-break.* All canonical occurrences of one value have identical length, so the shortest-length requirement no longer separates them. The sweep reaches start positions in increasing order and stores a value only when it is first produced, so the surviving occurrence is the one with the smallest left index among those canonical occurrences.

The invariant that unifies the three parts is this: at the end of preprocessing, for every value $x$ present in the dictionary, the stored pair is the leftmost occurrence of the shortest window whose decimal value is $x$. That invariant is exactly what each query asks for, so a single lookup settles each query — and queries sharing a target are answered identically without any extra work.

## 7. Boundary behaviour

| Instance | `s` | Query | Target | Answer | Why it is instructive |
|---|---|---|---|---|---|
| Leading zeroes lose | `"0011"` | `[0, 3]` | 3 | `[2, 3]` | The window `"0011"` also has value 3 but spans four characters; `"11"` spans two, and shorter wins |
| Equal lengths, leftmost wins | `"10101"` | `[0, 5]` | 5 | `[0, 2]` | `"101"` occurs at two window positions of equal length, so the smaller left index is reported |
| Zero target | `"1010"` | `[7, 7]` | 0 | `[1, 1]` | Only the single bit `0` is ever stored for value 0; longer runs of zeroes have the same value and are never shorter |
| Target absent | `"0101"` | `[12, 8]` | 4 | `[-1, -1]` | No window of `"0101"` has value 4, and the sweep proves it rather than guessing |
| Single-bit string | `"1"` | `[4, 5]` | 1 | `[0, 0]` | The dictionary holds one entry, and the target happens to be it |
| Single-bit string, missing target | `"1"` | `[0, 5]` | 5 | `[-1, -1]` | The only value present is 1, so nothing can satisfy the query |
| Repeated bits | `"111"` | `[1, 2]` | 3 | `[0, 1]` | `"11"` first appears at left index 0 and is not displaced by the later copy |

The first two rows are the ones that decide whether an implementation is correct. A dictionary built from every window without the `0`-prefix rule still answers `"0011"` with a four-character window if that window is discovered first, and a dictionary that overwrites on every discovery would move the answer for `"10101"` from `[0, 2]` to `[2, 4]`.

## 8. Other strategies and their trade-offs

| Strategy | Preprocessing | Per query | Total cost | Assessment |
|---|---|---|---|---|
| Value dictionary over windows up to 30 bits | $O(30n)$ | expected $O(1)$ hash lookup | $O(30n + q)$ | The method derived here; the bit ceiling keeps preprocessing linear |
| Scan the string afresh for every query | none | $O(30n)$ window values examined | $O(30nq)$ | Correct but with $q$ up to $10^5$ it repeats the same work hundreds of thousands of times |
| Dictionary of all $O(n^2)$ windows | $O(n^2)$ | $O(1)$ | $O(n^2)$ time and memory | At $n = 10^4$ this is $10^8$ entries, almost all of them longer than any possible target |
| Sort all recorded windows and binary search per query | $O(30n \log(30n))$ | $O(\log n)$ | $O(30n \log n + q \log n)$ | Same information as the dictionary with an extra logarithmic factor on both sides |
| Trie or suffix automaton over the bits | $O(n)$ | $O(30)$ walk per query | $O(n + 30q)$ | Correct, but it solves a harder problem (arbitrary pattern matching) than the one asked |

## 9. Traps this instance exposes

- **Solving for the wrong unknown.** The equation is $val \oplus \text{first} = \text{second}$, and the substring's value is isolated by XORing with `first` again, not by XORing `first` with itself or by subtracting. Because XOR is self-inverse and commutative, the target is `first ^ second` — the same whichever operand is treated as the mask.
- **Letting leading zeroes win the length comparison.** A window such as `"0011"` has the value 3 but is not the shortest representative of 3. Storing it because it was discovered first, or comparing only `right - left`, gives the wrong endpoints when the query asks for a value that has both a padded and an unpadded occurrence.
- **Overwriting a stored value.** The first discovery is the leftmost canonical occurrence; a later discovery of the same value is either the same length at a larger left index or a padded window without the stop rule. Overwriting can only make the answer worse.
- **Capping the extension length too low.** Targets can reach $2^{30} - 1$, so a cap of, say, 16 bits silently loses every target with more than 16 significant bits and reports `[-1, -1]` for queries that are answerable.
- **Extending windows without a bound.** Without the 30-bit ceiling the preprocessing visits $O(n^2)$ windows, which is quadratic in the string length.
- **Skipping the zero rule while also treating the empty window as legal.** A value of 0 must be stored with a one-character window; a dictionary that starts from empty windows or that forces value 0 to have length 0 produces endpoints that are not a valid non-empty substring.
- **Recomputing per query when queries repeat.** Multiple queries can reduce to the same target, and the dictionary answers them all from one entry; recomputation is wasted work.
- **Assuming `first ^ second` is small.** The XOR of two values below $10^9$ can be larger than either operand, for example when their bit patterns disagree in the high bits, so the ceiling must be derived from the bit width of the operands rather than from their magnitudes.

## 10. Time and auxiliary space

Let $n$ be the length of `s`, $q$ the number of queries, and $B = 30$ the maximum number of bits a target can occupy.

- **Preprocessing.** Every start position is extended for at most $B$ bits, and each extension performs a shift, an OR, and one dictionary probe: $O(Bn)$ time.
- **Query resolution.** One XOR and one expected-constant-time lookup per query: $O(q)$ expected.
- **Total time complexity.** $O(Bn + q)$, which is linear in the input size because $B$ is a fixed constant of the constraints. For $n = 10^4$ and $q = 10^5$ this is a few hundred thousand operations.
- **Auxiliary space complexity.** The dictionary holds at most one entry per window visited, so at most $O(Bn)$ value-to-endpoints pairs, each of constant size. The output list adds $O(q)$ pairs. Everything else — the running value, the two window ends, and the target — is constant state.
