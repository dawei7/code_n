## Description

There are `n` houses labeled from `0` through `n - 1` around a circle. Two directed road systems connect neighboring houses. Moving forward from house `i` to `(i + 1) % n` covers `forward[i]` meters. Moving backward from house `i` to `(i - 1 + n) % n` covers `backward[i]` meters.

You walk at one meter per second and begin at house `0`. Visit the houses listed in `queries` in their given order. For every move from the current house to the next requested house, either direction around the circle may be used, independently of earlier moves.

Return the minimum total number of seconds required to complete all visits.
