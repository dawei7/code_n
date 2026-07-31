## Description

A valid IP address contains exactly four integers separated by single dots. Each integer is between `0` and `255`, inclusive, and has no leading zero unless the integer itself is `0`.

For example, `"0.1.2.201"` and `"192.168.1.1"` are valid. Addresses `"0.011.255.245"`, `"192.168.1.312"`, and `"192.168@1.1"` are invalid because of a leading zero, an out-of-range component, and an invalid separator, respectively.

Given a digit-only string `s`, return every valid IP address obtainable by inserting dots. Digits may neither be removed nor reordered. The valid addresses may be returned in any order.
