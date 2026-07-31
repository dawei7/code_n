## General

The interval contains at most one thousand values, so inspect every integer directly. Convert the current value to its ordinary decimal string and place those characters in a set. A set contains one entry per distinct digit, so the value qualifies exactly when the set size equals the string length.

Increment the answer for every qualifying value. Iterating with `range(a, b + 1)` is important because both endpoints belong to the requested interval. The conversion also naturally uses the standard representation without artificial leading zeros.

## Complexity detail

The scan examines $R$ integers. Converting and checking one representation touches at most $D$ digits, giving $O(RD)$ time and $O(D)$ temporary set space. Under the stated limit $b \le 1000$, $D \le 4$.

## Alternatives and edge cases

- **Digit bit mask:** Track the ten possible digits in an integer bit mask while repeatedly taking remainders modulo `10`; this has the same $O(RD)$ time and $O(1)$ space.
- **Digit dynamic programming:** Counting qualifying values up to each endpoint can avoid enumerating a much larger interval, but the legal upper bound of `1000` makes that machinery unnecessary here.
- **Repeated prefix recomputation:** Recounting every prefix of the interval before returning the final total is correct but wastes $O(R^2D)$ time.
- **Inclusive endpoints:** A qualifying `a` or `b` must be counted; the upper endpoint cannot be omitted from the loop.
- **Singleton intervals:** When `a == b`, the answer is either `1` or `0` according to that one number.
- **No leading zeros:** Values such as `8` are checked as `"8"`, not as a padded form such as `"008"`.
