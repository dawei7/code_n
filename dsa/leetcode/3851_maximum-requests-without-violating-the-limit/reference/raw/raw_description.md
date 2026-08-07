## Description

You are given a 2D integer array `requests`, where `requests[i] = [user_i, time_i]` indicates that `user_i` made a request at `time_i`.

You are also given two integers `k` and `window`.

A user violates the limit if there exists an integer `t` such that the user makes strictly more than `k` requests in the inclusive interval `[t, t + window]`.

You may drop any number of requests.

Return an integer denoting the **maximum**​​​​​​​ number of requests that can **remain** such that no user violates the limit.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">requests = [[1,1],[2,1],[1,7],[2,8]], k = 1, window = 4</span>

**Output:** <span class="example-io">4</span>

**Explanation:**​​​​​​​

	- For user 1, the request times are `[1, 7]`. The difference between them is 6, which is greater than `window = 4`.

	- For user 2, the request times are `[1, 8]`. The difference is 7, which is also greater than `window = 4`.

	- No user makes more than `k = 1` request within any inclusive interval of length `window`. Therefore, all 4 requests can remain.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">requests = [[1,2],[1,5],[1,2],[1,6]], k = 2, window = 5</span>

**Output:** <span class="example-io">2</span>

**Explanation:**​​​​​​​

	- For user 1, the request times are `[2, 2, 5, 6]`. The inclusive interval `[2, 7]` of length `window = 5` contains all 4 requests.

	- Since 4 is strictly greater than `k = 2`, at least 2 requests must be removed.

	- After removing any 2 requests, every inclusive interval of length `window` contains at most `k = 2` requests.

	- Therefore, the maximum number of requests that can remain is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">requests = [[1,1],[2,5],[1,2],[3,9]], k = 1, window = 1</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- For user 1, the request times are `[1, 2]`. The difference is 1, which is equal to `window = 1`.

	- The inclusive interval `[1, 2]` contains both requests, so the count is 2, which exceeds `k = 1`. One request must be removed.

	- Users 2 and 3 each have only one request and do not violate the limit. Therefore, the maximum number of requests that can remain is 3.

</div>

**Constraints:**

	- `1 <= requests.length <= 10^5`

	- `requests[i] = [user_i, time_i]`

	- `1 <= k <= requests.length`

	- `1 <= user_i, time_i, window <= 10^5`
