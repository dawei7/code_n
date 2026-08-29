## General

**Choose the two flowers that must remain**

Removing flowers preserves the relative order of every flower that remains. Therefore, any valid resulting garden can be described by two original indices $l<r$ that become its first and last positions. Validity requires `flowers[l] == flowers[r]`. Every retained flower between those endpoints is optional.

Once the endpoints are fixed, the best interior choice is immediate:

- keep every interior flower with positive beauty, because it increases the sum;
- remove every interior flower with negative beauty, because it decreases the sum;
- keeping or removing a zero makes no difference.

The two endpoints are different. They are mandatory even when their shared beauty is negative, because without both of them the selected garden would not have two equal boundary flowers.

If their common value is $v$, the best beauty for endpoints $l$ and $r$ is

$$
2v+
\sum_{l<j<r}\max(\texttt{flowers}[j],0).
$$

The problem has now become finding the equal-valued endpoint pair that maximizes this expression.

**Prefix sums answer each interior query**

The solution builds an array `s` where `s[i]` is the sum of positive contributions among indices strictly before $i$. It starts with zero, and after processing value `v = flowers[i]` it sets

`s[i + 1] = s[i] + max(v, 0)`.

For endpoints $l$ and $i$, the positive sum strictly between them is `s[i] - s[l + 1]`. The first term includes positive values through index $i-1$. The second includes positive values through index $l$, so subtracting it removes everything before or at the left endpoint. The current right endpoint is not yet in `s[i]` and is therefore also excluded, exactly as required.

Adding `v * 2` then supplies the actual endpoint values. This is important when $v$ is negative: prefix sums deliberately ignore negative interior values, but the two required negative endpoints must still count.

**Why only the first occurrence of each value is stored**

Dictionary `d` maps a flower value to its first index. When value `v` appears for the first time, the solution stores its index. On every later occurrence at index $i$, that first position becomes the proposed left endpoint and $i$ becomes the right endpoint.

Keeping only the first occurrence is sufficient because every prefix contribution is nonnegative. Suppose the same value occurs at two possible left endpoints $l_1<l_2<i$. Extending the interval from $l_2$ leftward to $l_1$ can only add optional positive flowers or add nothing. It never forces any extra interior negative flower to remain. Both choices still use the same two endpoint values $v$, so

$$
\texttt{s}[i]-\texttt{s}[l_1+1]+2v
\geq
\texttt{s}[i]-\texttt{s}[l_2+1]+2v.
$$

Thus the earliest occurrence is always at least as good as any later occurrence for a fixed right endpoint. There is no need to keep a list of positions or search among earlier copies.

The solution still evaluates every later occurrence as a possible right endpoint. It updates `ans` with the largest candidate seen. `ans` starts at negative infinity because a valid garden can have negative maximum beauty; initializing it to zero would be wrong for inputs such as the third example.

**Following the examples**

For `flowers = [1, 2, 3, 1, 2]`, choosing the two flowers of beauty 2 at indices 1 and 4 makes the interior values 3 and 1. Both are positive, so the candidate is `2 + 3 + 1 + 2 = 8`. That becomes the maximum.

For `[100, 1, 1, -3, 1]`, the earliest and latest 1 values can be endpoints. The interior 1 remains, while -3 is removed. The result is `1 + 1 + 1 = 3`. The prefix sum of positive parts performs exactly this keep-or-remove decision without explicitly constructing the subsequence.

For `[-1, -2, 0, -1]`, the two -1 values are the only equal endpoint pair that yields a valid garden. Neither -2 nor 0 adds positive beauty, so the candidate is `-1 + -1 = -2`. Negative-infinity initialization allows this correct negative answer to survive.

**Why the final answer is correct**

Every valid remaining garden has some original first and last indices with equal values. For any fixed pair, removing all negative interior flowers and retaining all positive ones maximizes that pair's beauty; the prefix formula computes exactly this optimum.

For each right endpoint, the first occurrence of its value is the best possible left endpoint because moving the left endpoint earlier can only enlarge the set of optional nonnegative contributions. The scan evaluates that best pair whenever a repeated value appears and takes the maximum over all such right endpoints. Hence every globally optimal endpoint value and right endpoint is represented, and `ans` is the maximum possible beauty.

## Complexity detail

Let $n$ be the number of flowers and $U$ the number of distinct beauty values. The loop visits every flower once. Prefix updates, dictionary membership, dictionary insertion, and candidate evaluation are expected $O(1)$ operations, so total expected time is $O(n)$.

The dictionary stores at most one index per distinct value, using $O(U)$ space. The exact protected solution also stores the full prefix array `s` of length $n+1$, so its auxiliary space is $O(n+U)=O(n)$. The manifest records $O(U)$, but that omits this prefix array. A running positive sum plus a dictionary that stores the prefix level at each value's first occurrence could achieve $O(U)$; the existing source does not use that storage optimization.

## Alternatives and edge cases

- **Try every equal pair:** Enumerating all endpoint pairs and summing their interiors can take $O(n^3)$ time without prefix sums or $O(n^2)$ with them, both slower than the one-pass first-occurrence argument.
- **Keep every interior flower:** This fails when an interior beauty is negative, because removal is optional and can improve the total.
- **Kadane's algorithm:** Maximum-subarray logic forces a contiguous retained range, while this problem allows arbitrary interior removals and requires equal endpoints.
- **Store every occurrence:** Lists of positions are unnecessary because the earliest occurrence always dominates later left endpoints for the same value.
- **Running positive prefix scalar:** Store, for each first occurrence, the positive-prefix total immediately after it. This retains the same formula with $O(U)$ rather than $O(n+U)$ space.
- **Negative endpoints:** They must be counted twice even though negative interior values are removed.
- **Adjacent equal values:** The interior sum is zero, so the candidate is exactly twice the shared value.
- **Zero endpoints:** They can form a valid garden; positive interior flowers can still make its beauty positive.
- **All values negative:** The answer may be negative, so zero is not a safe initial maximum.
- **More than two equal flowers:** The first is best as the left endpoint, while every later occurrence is considered as a right endpoint.
- **Repeated negative value inside the interval:** An intermediate copy may be removed; equality is required only for the retained first and last flowers.
- **Guaranteed feasible input:** At least one value repeats, so some candidate replaces negative infinity before the loop ends.
- **Input preservation:** The algorithm records summaries and never changes the `flowers` array.
