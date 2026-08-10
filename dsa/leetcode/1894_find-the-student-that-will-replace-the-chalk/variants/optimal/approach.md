## General

**One full class round always costs the same amount.** Let `s = sum(chalk)`. Starting at student zero and visiting every student once consumes exactly `s` pieces and returns the turn order to student zero. Therefore, any number of complete rounds can be removed from `k` without changing which student eventually encounters insufficient chalk.

**Use modulo to skip all complete rounds.** `k %= s` replaces the initial supply with its remainder after division by one-round consumption. The new `k` satisfies `0 <= k < s`. It represents the chalk remaining at the start of the final partial round after every affordable complete cycle has been performed. This turns a potentially billion-step simulation into one pass.

All `chalk[i]` values are positive, so `s` is positive and modulo is safe. Positivity also guarantees that within this final round, cumulative consumption will eventually exceed the remainder; some student must be the replacer.

**Simulate only the final partial round.** The loop visits students in index order. Before student `i` uses chalk, variable `k` is the remaining supply. If `k < x` for `x = chalk[i]`, the student lacks enough and their index is returned. The comparison is strict: if `k == x`, the student has exactly enough, uses it, and leaves zero for the next student.

If enough chalk remains, `k -= x` models that student's use and advances to the next index. Because the modulo remainder is less than total round consumption, this pass must return before or at the final student. The source has no explicit return after the loop, but that control path is unreachable under the stated positive constraints.

**Trace the first example.** One round costs `5 + 1 + 5 = 11`. Initial `k = 22` becomes zero after modulo, representing two complete rounds with nothing left. Student zero requires five, and `0 < 5`, so index zero is returned immediately. This exactly matches the detailed turn simulation but avoids replaying both rounds.

For `chalk = [3, 4, 1, 2]` and `k = 25`, the round total is ten and the remainder is five. Student zero consumes three, leaving two. Student one requires four, so two is strictly insufficient and index one is returned.

**Why a zero remainder means student zero.** If initial `k` is an exact multiple of `s`, the class completes that many rounds and exhausts the chalk precisely after the final student. The next turn belongs to student zero, who sees zero pieces. Modulo produces zero, and the first comparison returns zero because every requirement is positive.

**Why modulo preserves the answer.** Suppose `k = q s + r` with `0 <= r < s`. The first `q` complete rounds consume `q s` and return to the same student-zero state. No replacement occurs during those rounds because their consumption is included in the number of fully affordable cycles represented by the quotient; if chalk reaches exactly zero, replacement happens only when the next student is asked to use chalk. The remaining process is exactly the process starting with `r`, which the final loop simulates.

**The method does not need prefix storage.** A prefix sum array could locate the first cumulative requirement greater than the remainder by binary search, but creating it still costs linear preprocessing. Since one linear scan is already optimal for reading the input and uses constant extra state, the source subtracts requirements directly.

**Inputs are read-only.** `sum` and iteration inspect `chalk` without sorting or changing it. Preserving order is essential because student sequence is part of the problem; unlike many array problems, rearrangement would change the answer.

## Complexity detail

Let $n$ be the number of students. `sum(chalk)` scans all $n$ requirements once. The final loop scans at most $n$ elements and usually stops earlier. Total time is $O(n)$.

The method stores only the round sum, reduced remainder, loop index, and current requirement. Auxiliary space is $O(1)$, matching the manifest. The input list and returned scalar are not copied.

The round total can be as large as $10^{10}$ under the constraints. Python integers handle it. A fixed-width implementation must use a 64-bit integer for `s` and `k` even though each individual requirement fits in 32 bits.

## Alternatives and edge cases

- **Prefix sums plus binary search:** Build cumulative chalk usage, reduce `k` modulo the total, and find the first prefix strictly greater than the remainder. This remains $O(n)$ overall because building prefixes dominates and uses $O(n)$ space.
- **Repeated direct simulation:** Cycling and subtracting without modulo can require work proportional to the original `k` and is too slow for large supplies.
- **Early total accumulation:** One may stop summing once the partial total exceeds `k` because no full round can then be skipped. The exact source uses the simpler full sum and still remains linear.
- **Exact equality with a requirement:** If `k == chalk[i]`, student `i` consumes it and the next student replaces. Using `<=` in the test would be an off-by-one error.
- **`k` is a multiple of the round total:** Modulo gives zero, and student zero correctly replaces the chalk.
- **One student:** Reduce by that student's requirement, then the only index zero is returned for the final insufficient turn.
- **All requirements positive:** This guarantees a positive divisor and guarantees that the final partial-round loop finds an answer.
- **Large round sum:** Use wide integer arithmetic outside Python; overflow in `sum(chalk)` would corrupt modulo and the result.
- **No post-loop return:** Under the contract the loop must return because the remainder is smaller than the positive total. The implicit `None` path is unreachable.
