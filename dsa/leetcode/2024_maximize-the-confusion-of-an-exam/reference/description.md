## Description

A teacher is writing a test with `n` true/false questions, with `'T'` denoting true and `'F'` denoting false. He wants to confuse the students by **maximizing** the number of **consecutive** questions with the **same** answer (multiple trues or multiple falses in a row).

You are given a string `answerKey`, where $\text{answerKey}[i]$ is the original answer to the $$i^{\text{th}}$$ question. In addition, you are given an integer `k`, the maximum number of times you may perform the following operation:

- Change the answer key for any question to `'T'` or `'F'` (i.e., set $\text{answerKey}[i]$ to `'T'` or `'F'`).

Return *the **maximum** number of consecutive* `'T'`s or `'F'`s *in the answer key after performing the operation at most* `k` *times*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $answerKey = "TTFF", k = 2$
- **Output:** `4`
- **Explanation:** We can replace both the 'F's with 'T's to make answerKey = "<u>TTTT</u>".
There are four consecutive 'T's.
#### Example 2

- **Input:** $answerKey = "TFFT", k = 1$
- **Output:** `3`
- **Explanation:** We can replace the first 'T' with an 'F' to make answerKey = "<u>FFF</u>T".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "T<u>FFF</u>".
In both cases, there are three consecutive 'F's.
#### Example 3

- **Input:** $answerKey = "TTFTTFTT", k = 1$
- **Output:** `5`
- **Explanation:** We can replace the first 'F' to make answerKey = "<u>TTTTT</u>FTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTF<u>TTTTT</u>".
In both cases, there are five consecutive 'T's.
### Constraints

- $n = \text{answerKey.length}$

- $1 \le n \le 5 * 10^{4}$

- $\text{answerKey}[i]$ is either `'T'` or `'F'`

- $1 \le k \le n$