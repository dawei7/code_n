# Guess the Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 843 |
| Difficulty | Hard |
| Topics | Array, Math, String, Interactive, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-the-word/) |

## Problem Description
### Goal
The array `words` contains unique six-letter strings, and one entry has been chosen as the secret. The interactive helper `Master` accepts `Master.guess(word)` calls. A guess must belong to `words`; otherwise the call returns `-1`. For a valid guess, the result is the number of positions whose letters exactly match the secret.

Each test case supplies an `allowedGuesses` limit from `10` through `30`. Call `Master.guess` with the secret word without exceeding that limit. Success is determined through the helper rather than an ordinary function return, and the cases are generated so that a reasonable non-brute-force strategy can succeed.

### Function Contract
**Inputs**

- `words`: $g$ unique lowercase strings of length six, where $1 \leq g \leq 100$ and the secret is one entry.
- `master`: the interactive helper that reports exact-position matches and enforces the hidden secret and guess budget.

Let $q$ be the case's allowed number of guesses, where $10 \leq q \leq 30$ on LeetCode.

**Return value**

Return no platform value. The interaction succeeds only if `master.guess(secret)` is called at most $q$ times. The app-adapted reference returns its simulated `master` so the local judge can verify that same state transition.

### Examples
**Example 1**

- Input: `secret = "acckzz", words = ["acckzz", "ccbazz", "eiowzz", "abcczz"], allowedGuesses = 10`
- Output: `You guessed the secret word correctly.`

For example, `Master.guess("ccbazz")` reports three exact-position matches, while guessing `"acckzz"` reports six and finds the secret.

**Example 2**

- Input: `secret = "hamada", words = ["hamada", "khaled"], allowedGuesses = 10`
- Output: `You guessed the secret word correctly.`
