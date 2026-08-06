## Description

Given `n`, consider every permutation of the 1-indexed array
`[1, 2, ..., n]`. A permutation is **self-divisible** when the value placed at
every 1-indexed position $i$ is coprime with $i$; equivalently,
$\gcd(a_i,i)=1$ for all $1\le i\le n$.

Return the number of permutations satisfying this condition. Each value from
`1` through `n` must appear exactly once.
