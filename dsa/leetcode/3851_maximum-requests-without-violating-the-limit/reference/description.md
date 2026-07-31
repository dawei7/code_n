## Description

You are given a list of request records. Each record `requests[i] = [user_i, time_i]` says that a particular user made one request at the specified integer time.

Two additional integers, `k` and `window`, define the limit. A user violates it when some inclusive interval `[t, t + window]`, for an integer $t$, contains strictly more than `k` of that user's retained requests.

You may discard any number of request records. Return the largest number of records that can remain while ensuring that no user violates the limit.
