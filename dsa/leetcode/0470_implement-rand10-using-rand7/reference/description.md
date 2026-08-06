## Description

The provided API `rand7()` returns a uniformly random integer from the inclusive range `[1, 7]`. Implement `rand10()` so that it returns a uniformly random integer from `[1, 10]` while calling only `rand7()` for randomness. Do not call another random API or use a language's built-in random generator.

Each source test has an internal integer `n` specifying how many times the judge calls the implemented `rand10()`. This internal value is not an argument to `rand10()` itself.
