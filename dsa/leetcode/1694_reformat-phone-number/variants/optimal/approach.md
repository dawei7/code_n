## General

**Remove formatting before creating new formatting**

The original spaces and dashes carry no grouping meaning. The chained replacements first remove every dash and then every space, leaving a string containing only digits:

`number = number.replace("-", "").replace(" ", "")`.

Digit order is unchanged. Starting from this clean sequence prevents old separators from interfering with index calculations.

**Create provisional blocks of three**

Let `n` be the number of cleaned digits. The list comprehension creates `n // 3` slices:

`number[i * 3 : i * 3 + 3]`.

These are consecutive three-digit blocks beginning at positions zero, three, six, and so on. When `n` is divisible by three, they cover the entire string and already form the final grouping.

When a remainder exists, the final behavior depends on whether it is one or two.

**Handle a remainder of two**

If `n % 3 == 2`, the provisional blocks cover the first `n - 2` digits. `number[-2:]` is exactly the remaining pair, so the source appends it.

For eight digits, the initial list contains the first six as two blocks of three, and the last two become one final block. No block has length one.

**Repair the dangerous remainder of one**

If `n % 3 == 1`, blindly taking all possible groups of three would leave one final digit, which the rules forbid. The correct ending is two blocks of two.

The provisional list’s last three-digit block contains the first three of the final four digits. The source changes:

`ans[-1] = ans[-1][:2]`,

keeping only its first two digits. It then appends `number[-2:]`, the final two digits. Together these cover the last four digits as `2 + 2`.

For seven cleaned digits, provisional blocks are positions `0..2` and `3..5`, with position six left over. Shortening the second block to positions three and four, then appending positions five and six, produces lengths `3, 2, 2`.

The smallest remainder-one cleaned length is four because at least two digits exist. Therefore `ans` has a provisional block and `ans[-1]` is always safe in this branch.

**Join blocks with exactly one dash**

`"-".join(ans)` inserts one dash between adjacent blocks and none at either end. Since every list entry has length two or three after the remainder logic, the result satisfies all grouping constraints.

At most two length-two blocks appear: only the four-digit ending creates two, while a two-digit remainder creates one.

**Trace the examples**

`"1-23-45 6"` cleans to `"123456"`. Its remainder is zero, so blocks `"123"` and `"456"` join as `"123-456"`.

`"123 4-567"` cleans to seven digits. Provisional blocks `"123"` and `"456"` are repaired to `"123"`, `"45"`, `"67"`.

`"123 4-5678"` cleans to eight digits. Blocks `"123"` and `"456"` plus final `"78"` give `"123-456-78"`.

**Why the result is correct**

Cleaning preserves exactly the digit sequence. Every complete block before the final four-or-fewer region has length three. The remainder branches implement the only legal endings: one block of two, one block of three through the divisible case, or two blocks of two.

Slices are contiguous and cover each cleaned digit exactly once after the remainder-one adjustment. Joining preserves block order, so the returned string is precisely the required reformatting.

The quotient-and-remainder split is exhaustive because division by three can leave only zero, one, or two digits. The zero case needs no branch, the two case can be appended directly, and the one case is repaired. Consequently there is no unhandled cleaned length and no route that can produce a forbidden one-digit group.

## Complexity detail

Let `N` be the original string length. Each `replace` scans and constructs a string, costing $O(N)$ time. The block slices collectively copy $O(N)$ digits, and joining also costs $O(N)$. Total time is $O(N)$.

Immutable cleaned strings, the block list and its slice strings, and the returned string use $O(N)$ space. Peak auxiliary space is therefore $O(N)$.

No numeric conversion occurs, so long phone numbers and leading digit zeros are preserved exactly.

## Alternatives and edge cases

- **Character filtering:** Build the clean digits with a comprehension testing `c.isdigit()`. It is a single conceptual pass but still uses $O(N)$ output storage.
- **Manual scanner and block builder:** It can emit blocks as digits arrive, though recognizing the final four requires buffering or knowing the cleaned length.
- **Regular expression removal:** It works but is unnecessary for two literal separator characters.
- **Exactly two digits:** No provisional three-block exists; the remainder-two branch appends the full pair.
- **Exactly three digits:** One three-digit block is returned.
- **Exactly four digits:** One provisional block is shortened to two and the final two digits are appended.
- **Multiple spaces or dashes:** Every occurrence is removed by `replace`, regardless of adjacency.
- **Leading and trailing separators:** Cleaning removes them without affecting digit order.
- **Leading zero digit:** String slicing preserves it; integer parsing would not.
- **Remainder one:** It must never be emitted as a one-digit block, which is why the last provisional triple is rebalanced.
- **At most two two-blocks:** Only the final four digits create two such blocks, and earlier blocks remain length three.
