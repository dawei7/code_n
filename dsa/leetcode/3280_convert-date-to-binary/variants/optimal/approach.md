## General

**Convert the three fixed components independently**

Split the input at its two hyphens to obtain decimal strings for the year, month, and day. Convert each string to an integer first; this removes the leading zero used by the fixed-width month or day format.

Format each positive integer in base two. Standard binary formatting introduces no leading zeros, so the three results already satisfy the output rule. Join them with hyphens in their original year-month-day order.

The input guarantee supplies exactly three valid positive components. Each is converted without mixing information from the others, and joining them restores precisely the required separators, so the returned string is the requested representation.

## Complexity detail

Every legal input contains exactly ten characters and three bounded numeric components. The work and produced output length are bounded by constants, giving $O(1)$ time and $O(1)$ space.

## Alternatives and edge cases

- **Repeated division by two:** Manually collecting remainders is correct, but built-in base formatting expresses the same conversion more directly.
- **Convert the entire date string:** Hyphens are separators rather than part of one number, so the three components must remain independent.
- **Preserve component width:** Binary components must not be padded; decimal leading zeros disappear.
- January and days `01` become binary `1`, not `01`.
- Leap days such as `2000-02-29` are already guaranteed valid and need no calendar validation.
- The boundary years `1900` and `2100` are converted by the same rule as every interior year.
- The output keeps exactly two hyphens even though component lengths change.
