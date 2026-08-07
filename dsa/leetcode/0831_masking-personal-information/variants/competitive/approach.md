## General
Given a personal information string `s`, representing either an **email address** or a **phone number**. Return *the **masked** personal information using the below rules*, the algorithm solves **Masking Personal Information** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
