## Description

You are given an integer `n`.

Begin with the prime number `2` and form cumulative sums of consecutive primes: first `2`, then `2 + 3`, then `2 + 3 + 5`, and so on. A qualifying value must be one of these sums, must itself be prime, and must not exceed `n`. The sequence always starts at `2`; a sum beginning at a later prime does not qualify.

Return the greatest qualifying prime. If no cumulative prime sum satisfies the conditions, return `0`.
