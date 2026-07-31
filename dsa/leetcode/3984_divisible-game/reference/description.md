## Description

Alice receives a nonempty integer array `nums` and chooses three values: an integer $k>1$ and two indices `l` and `r` with $0 \le l \le r < n$. The chosen indices describe one nonempty, inclusive subarray.

Starting from zero scores, inspect every value in that subarray. A value divisible by $k$ is added to Alice's score; every other value is added to Bob's score. The resulting score difference is Alice's score minus Bob's score.

Alice first maximizes this difference over every legal subarray and every legal $k$. If several values of $k$ attain the same maximum difference, she uses the smallest such $k$. Return the maximum difference multiplied by that selected $k$, reduced modulo $10^9+7$.
