## Description

Given the **API** `rand7()` that generates a uniform random integer in the range `[1, 7]`, write a function `rand10()` that generates a uniform random integer in the range `[1, 10]`. You can only call the API `rand7()`, and you shouldn't call any other API. Please **do not** use a language's built-in random API.

Each test case will have one **internal** argument `n`, the number of times that your implemented function `rand10()` will be called while testing. Note that this is **not an argument** passed to `rand10()`.
### Function Contract

**Inputs**

- $\text{rand7}_{values}$: A nonempty deterministic cyclic stream of integers from `1` through `7` that the app adapter uses in place of LeetCode's random API. When `draws` is positive, the stream must eventually produce an accepted pair on every requested output.
- `draws`: The nonnegative number of deterministic `rand10` outputs to generate for the app trace.

**Return value**

- Return the generated list of `draws` values, each in the range `1` through `10`.

The immutable native form instead exposes `Solution.rand10()` with no arguments and calls LeetCode's independently uniform `rand7()` API. The app stream exists only to make the same control flow reproducible.

### Examples

#### Example 1

- **Input:** $n = 1$
- **Output:** `[2]`
#### Example 2

- **Input:** $n = 2$
- **Output:** `[2,8]`
#### Example 3

- **Input:** $n = 3$
- **Output:** `[3,8,10]`
### Constraints

- $1 \le n \le 10^{5}$

**Follow up:**

- What is the <a href="https://en.wikipedia.org/wiki/Expected_value" target="_blank">expected value</a> for the number of calls to `rand7()` function?

- Could you minimize the number of calls to `rand7()`?