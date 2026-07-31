## Description

Given two version strings, `version1` and `version2`, compare them. Each version is a dot-separated sequence of **revisions**. A revision's value is its integer conversion, so leading zeroes do not change that value.

Compare revision values from left to right. When one version has fewer revisions, treat each missing revision as `0`.

Return:

- `-1` if `version1 < version2`;
- `1` if `version1 > version2`;
- `0` otherwise.
