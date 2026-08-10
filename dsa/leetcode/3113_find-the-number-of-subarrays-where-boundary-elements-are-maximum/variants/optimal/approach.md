## General

**Count valid subarrays by their right boundary.** For a subarray ending at the current value `x` to qualify, its left boundary must also equal `x`, and every interior value must be at most `x`. The source asks how many earlier equal values are still “visible” from the current position without a greater value blocking them.

Every singleton is valid because its first and last element are the same and are trivially its maximum. Longer valid subarrays pair the current `x` with an earlier `x` whose intervening values never exceed `x`.

**Stack entries group visible equal boundaries.** `stk` contains pairs `[value, count]`. Distinct stack values decrease from bottom to top. The count attached to a value is the number of occurrences of that value that remain eligible as left boundaries for a future equal right endpoint.

Grouping equal values avoids storing and counting them one by one. If three visible copies of five share one entry `[5,3]`, a new five can form three longer valid subarrays with them plus its singleton.

**A larger incoming value removes smaller candidates.** Before handling `x`, the source executes:

`while stk and stk[-1][0] < x: stk.pop()`.

Suppose a smaller stack value `y` remained. Any future subarray beginning at an earlier `y` and ending at another `y` after current position would contain `x > y` internally. Its boundary elements could not be the maximum. Current `x` permanently blocks those candidates, so discarding their groups is correct.

Each smaller group is popped only once over the entire scan.

**A greater top creates a new blocked layer.** After popping smaller values, if the stack is empty or its top value is greater than `x`, the source appends `[x,1]`.

The count begins at one for the current singleton. If a greater value remains on top, any older `x` below that greater barrier cannot pair with the current `x`: the greater value would lie inside and violate the maximum condition. A new group is therefore necessary.

**An equal top extends the visible group.** If the top value equals `x`, every occurrence counted in that group has only values at most `x` between it and the current position. Each can serve as a valid left boundary. The source increments the group count by one to include current `x`.

After either appending or incrementing, `stk[-1][1]` is exactly the number of valid subarrays ending at this position:

- one uses current `x` as both boundaries;
- every other one begins at one of the visible earlier equal occurrences.

The source adds this count to `ans`.

**Trace `[1,4,3,3,2]`.** Value one creates `[1,1]` and contributes one. Value four pops the smaller one, creates `[4,1]`, and contributes one. Value three is below four, so it creates `[3,1]` and contributes its singleton.

The next three matches the top. Its count becomes two, contributing the singleton and subarray `[3,3]`. Final value two is below three and creates a new count-one group. Total contribution is $1+1+1+2+1=6$.

For `[3,3,3]`, counts at the top become one, two, and three. Their sum is six, equal to the number of all subarrays.

**Why a greater blocker can remain in the stack.** A value larger than current `x` is not invalidated by seeing `x`. It may later pair with an equal large value, and current `x` would be an allowed smaller interior element. The new `x` group sits above it. If that larger value reappears, it will pop the smaller group and reconnect with its old equal group.

For example, in `[5,2,5]`, first five stays below the temporary group for two. The final five pops two, finds equal five, and correctly counts `[5,2,5]`.

**A stack invariant.** After each position, every entry represents equal-valued occurrences not separated from the scan frontier by a larger value, and entry values are strictly decreasing. Popping restores this property for a larger incoming value; appending handles a smaller blocked layer; incrementing handles equality. Therefore, the top count gives exactly all legal left boundaries for the current right boundary.

Since every qualifying subarray has one unique right endpoint, summing these ending counts counts every answer once.

## Complexity detail

Every input value is pushed into a group once or merged with the top. A group can be popped at most once. Although popping occurs inside a `while` loop, total pops across all $n$ iterations are $O(n)$. Total time is therefore $O(n)$.

In a strictly decreasing array, every value creates a separate stack entry, so worst-case auxiliary space is $O(n)$.

The answer can be $n(n+1)/2$ when all values are equal. For $n=10^5$, a 64-bit result is required outside Python.

## Alternatives and edge cases

- **Previous-greater boundaries plus frequency maps:** It can count equal endpoints inside valid regions, but the monotonic stack combines both tasks more directly.
- **Enumerate every subarray:** Checking boundary equality and maxima costs at least quadratic time.
- **All equal values:** Top counts grow from one through $n$, counting every subarray.
- **Strictly increasing values:** Each new value pops all smaller groups and contributes only its singleton.
- **Strictly decreasing values:** No group is popped during the scan; every position contributes only one.
- **Greater value between equal endpoints:** It blocks the pair, represented by a separate greater stack layer.
- **Smaller values between equal endpoints:** They are popped when the equal boundary returns and do not prevent validity.
- **Singletons:** Always included through the new occurrence in the top count.
- **Equal top:** Increment rather than append so all mutually visible copies remain grouped.
- **Smaller top:** Pop because current `x` permanently invalidates it for future matching boundaries.
- **Greater top:** Preserve it because current smaller value may legally lie inside a future larger-boundary subarray.
- **Positive values:** The stack logic uses only comparisons and would also work for arbitrary comparable integers.
- **Large answer:** Python integers grow automatically.
- **No input mutation:** `nums` is scanned in original order.
- **Unique right endpoints:** They partition qualifying subarrays and prevent double counting.
