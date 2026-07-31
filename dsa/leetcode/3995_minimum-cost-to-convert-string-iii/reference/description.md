## Description

You are given equal-length strings `source` and `target`. You are also given parallel arrays `rules` and `costs`. Each rule has the form `[pattern, replacement]`, its base application cost is the corresponding value in `costs`, and its pattern and replacement have the same length.

You may apply any rule any number of times. To apply a rule, choose a starting index `l` whose complete rule-length range exists in the current string and whose positions have never been used by an earlier application. At every offset in that range, the pattern character must either equal the current string character or be `'*'`, which matches any one character. Replace the complete range with the rule's replacement exactly as written; replacements contain no wildcards.

An application costs its listed base cost plus the number of `'*'` characters in its pattern. Afterward, none of the positions in that range may participate in another rule application. All rules preserve length, so character positions never shift.

Return the minimum total cost needed to transform `source` into `target`. Return `-1` when no legal sequence of applications can complete the transformation.
