## General

Two closed intervals intersect exactly when the later start is no later than the earlier end:

$$
\max(s_1,s_2)\le\min(e_1,e_2).
$$

The time strings can be compared directly. Fixed-width 24-hour `"HH:MM"` format places hour digits first, then minute digits, with leading zeros present. Lexicographic order is therefore identical to chronological order within the day.

Apply the closed-interval inequality to the two start strings and two end strings. The non-strict comparison is essential because an endpoint shared by both events is a non-empty intersection under the inclusive contract.

If the inequality holds, the later start itself is no later than both ends and belongs to both events. If it fails, whichever event starts later begins strictly after the other event has ended, so no common moment exists.

## Complexity detail

The input always contains exactly four strings of fixed length five. A constant number of bounded-length comparisons takes $O(1)$ time and $O(1)$ space.

The verified `bounded_domain` certificate records why runtime scaling is inapplicable to this fixed-shape, single-day contract.

## Alternatives and edge cases

- **Convert to minutes:** Mapping `"HH:MM"` to `60 * hour + minute` and applying the same interval test is correct but unnecessary.
- **Check two separation conditions:** The equivalent expression `event1[1] >= event2[0] and event2[1] >= event1[0]` may be easier to recognize.
- **Touching endpoints:** `["01:00", "02:00"]` conflicts with `["02:00", "03:00"]`.
- **One-minute gap:** An event ending at `"08:59"` does not conflict with one beginning at `"09:00"`.
- **Containment:** If one event lies wholly inside the other, the intersection is non-empty.
- **Point event:** Equal start and end times form a valid one-moment interval.
- **Midnight and final minute:** `"00:00"` and `"23:59"` preserve chronological string order.
- **Same day only:** The contract has no overnight interval whose end wraps into another day.
