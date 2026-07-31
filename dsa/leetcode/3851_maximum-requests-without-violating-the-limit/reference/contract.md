## Function Contract

**Inputs**

- `requests`: A nonempty array of two-element arrays `[user, time]`, one for each request record.
- `k`: The maximum number of retained requests that any one user may have inside an inclusive interval of the prescribed length.
- `window`: The nonnegative span from the first endpoint $t$ to the inclusive endpoint $t+\texttt{window}$.

Records may arrive in any order, different users are checked independently, and multiple records may share the same user and time. Let $N=\lvert\texttt{requests}\rvert$.

For a user's sorted retained times $a_0\le a_1\le\cdots$, validity is equivalent to

$$
a_{i+k}-a_i>\texttt{window}
$$

whenever both indexed times exist. Equality does not suffice because both interval endpoints are included.

**Return value**

Return the maximum possible total number of retained request records across all users.
