## General

The score requested at index $i$ is the prefix sum of conversion values through that index. When the scan reaches `nums[i]`, only two pieces of earlier information matter: the greatest value seen so far and the sum of all conversion values already produced. There is no need to revisit the prefix.

Maintain `maximum` and `score`. Update the maximum with the current value, add the current value plus that maximum to the score, and append the new score to the answer. After processing index $i$, `maximum` equals `max(nums[0..i])`. The newly added term is therefore exactly `conver[i]`, and `score` is the sum of `conver[0..i]`, which is precisely the answer required at that index. This remains true after every iteration, so the completed array contains all prefix scores.

## Complexity detail

The algorithm performs constant work for each of the $n$ input values, giving $O(n)$ time. The returned answer contains $n$ scores and therefore uses $O(n)$ space. Excluding that required output, the running maximum and score use $O(1)$ auxiliary space. Scores can exceed 32-bit range because both $n$ and the values are large, so fixed-width implementations need a 64-bit integer type.

## Alternatives and edge cases

- **Recompute every prefix maximum:** Scanning `nums[0..i]` separately for each index is correct but takes $O(n^2)$ time in the worst case.
- **Separate conversion and prefix arrays:** Building the full conversion array and then prefix-summing it also takes $O(n)$ time, but it stores an unnecessary additional $O(n)$ array.
- A single element $x$ converts to $2x$, so the only returned score is also $2x$.
- Repeated or decreasing values do not lower the running maximum; they still contribute their own value plus that earlier maximum.
- The positive-value guarantee allows the running maximum to start at zero.
