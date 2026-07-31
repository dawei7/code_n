## General

Represent friends internally by zero-based positions. Friend 1 is position zero, and moving `distance` steps clockwise from `current` reaches `(current + distance) % n`. A boolean array provides constant-time membership tests for who has already received the ball.

Start at position zero with turn number one. While the current position has not been visited, mark it, advance by `turn * k` modulo `n`, and increment the turn. The first position encountered twice is not marked again because that repetition is exactly the stopping condition.

Before each iteration, `current` is the holder for that turn and every true boolean corresponds exactly to an earlier holder. The modular update implements the required clockwise pass distance. Consequently the loop marks precisely the friends who receive the ball before termination. Scanning the boolean array from left to right and returning the false positions plus one produces exactly the losers in ascending order.

## Complexity detail

At most $n$ distinct friends can be marked before a repetition, and the final scan examines all $n$ entries. The running time is $O(n)$ and the visited array uses $O(n)$ space.

## Alternatives and edge cases

- **Set of positions:** A hash set also gives expected $O(1)$ membership and $O(n)$ total time, but a fixed boolean array is simpler for the dense range from 1 through `n`.
- **List membership:** Keeping recipients in a list is correct, but repeated membership tests and loser checks can take $O(n^2)$ time.
- **One friend:** Friend 1 starts with the ball, so nobody is a loser even though the next pass immediately repeats friend 1.
- **Distance divisible by `n`:** A pass whose distance is a multiple of `n` returns to the current holder and ends the game.
- **Output order:** Collect unvisited positions by increasing index rather than by pass order.
