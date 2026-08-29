### 1. Description

You are given a 2D integer array `requests`, where $\text{requests}[i] = [\text{user}_{i}, \text{time}_{i}]$ indicates that $\text{user}_{i}$ made a request at $\text{time}_{i}$.

You are also given two integers `k` and `window`.

A user violates the limit if there exists an integer `t` such that the user makes strictly more than `k` requests in the inclusive interval `[t, t + window]`.

You may drop any number of requests.

Return an integer denoting the **maximum** number of requests that can **remain** such that no user violates the limit.

### 2. Function Contract

**Inputs**

- `requests`: A nonempty array of two-element arrays `[user, time]`, one for each request record.
- `k`: The maximum number of retained requests that any one user may have inside an inclusive interval of the prescribed length.
- `window`: The nonnegative span from the first endpoint $t$ to the inclusive endpoint $t+\texttt{window}$.

Records may arrive in any order, different users are checked independently, and multiple records may share the same user and time. Let $N=\lvert\texttt{requests}\rvert$.

For a user's sorted retained times $a_0\le a_1\le\cdots$, validity is equivalent to

$a_{i+k}-a_i>\texttt{window}$

whenever both indexed times exist. Equality does not suffice because both interval endpoints are included.

**Return value**

Return the maximum possible total number of retained request records across all users.

### 3. Examples

#### Example 1

- **Input:** requests = [[1,1],[2,1],[1,7],[2,8]], k = 1, window = 4

- **Output:** 4

- **Explanation:** 

- For user 1, the request times are `[1, 7]`. The difference between them is 6, which is greater than $window = 4$.

- For user 2, the request times are `[1, 8]`. The difference is 7, which is also greater than $window = 4$.

- No user makes more than $k = 1$ request within any inclusive interval of length `window`. Therefore, all 4 requests can remain.

#### Example 2

- **Input:** requests = [[1,2],[1,5],[1,2],[1,6]], k = 2, window = 5

- **Output:** 2

- **Explanation:** 

- For user 1, the request times are `[2, 2, 5, 6]`. The inclusive interval `[2, 7]` of length $window = 5$ contains all 4 requests.

- Since 4 is strictly greater than $k = 2$, at least 2 requests must be removed.

- After removing any 2 requests, every inclusive interval of length `window` contains at most $k = 2$ requests.

- Therefore, the maximum number of requests that can remain is 2.

#### Example 3

- **Input:** requests = [[1,1],[2,5],[1,2],[3,9]], k = 1, window = 1

- **Output:** 3

- **Explanation:** 

- For user 1, the request times are `[1, 2]`. The difference is 1, which is equal to $window = 1$.

- The inclusive interval `[1, 2]` contains both requests, so the count is 2, which exceeds $k = 1$. One request must be removed.

- Users 2 and 3 each have only one request and do not violate the limit. Therefore, the maximum number of requests that can remain is 3.

### 4. Constraints

- $1 \le \text{requests.length} \le 10^{5}$

- $\text{requests}[i] = [\text{user}_{i}, \text{time}_{i}]$

- $1 \le k \le \text{requests.length}$

- $1 \le \text{user}_{i}, \text{time}_{i}, window \le 10^{5}$
