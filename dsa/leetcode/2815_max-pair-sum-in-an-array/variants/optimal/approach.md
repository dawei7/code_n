## General

**Use the largest digit as a fixed-size key**

There are only ten possible largest decimal digits. Maintain one bucket for the greatest value previously seen under each key. For each number, inspect its decimal digits to find the maximum.

If that bucket already contains a value, the current number forms an eligible pair with it. Because all numbers are positive, the greatest prior value gives the largest possible sum ending at the current index; update the global answer with that sum. Then replace the bucket value when the current number is larger.

Every valid pair is considered when its later endpoint is processed. At that moment, the bucket stores a value at least as large as the pair's earlier endpoint, so the candidate evaluated is no worse. Conversely, every evaluated candidate consists of two distinct processed indices with equal largest digits. The maximum candidate is therefore exactly the required answer, while untouched or singleton buckets cannot form pairs.

## Complexity detail

Let $n$ be the array length and $V$ its largest value. Inspecting a number's decimal representation costs $O(\log V)$, so total time is $O(n\log V)$. The ten fixed buckets use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Check every pair:** Direct enumeration is correct but takes $O(n^2\log V)$ time after repeated digit inspection.
- **Store complete groups then sort:** This works but retains all values and performs unnecessary sorting; one maximum per group is enough during the scan.
- Equal values at different indices are a valid pair.
- A number such as `10000` has largest digit `1`, not `0`.
- Repeated occurrences of the largest digit do not change the bucket key.
- Return `-1` when every bucket receives at most one number.
- Values are positive, so pairing with the largest prior bucket value always dominates pairing with a smaller one.
