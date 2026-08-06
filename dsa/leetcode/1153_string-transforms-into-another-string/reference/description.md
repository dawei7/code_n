## Description

Two strings, `str1` and `str2`, have the same length. Decide whether a sequence of zero or more conversions can change `str1` into `str2`.

One conversion selects a lowercase English character and replaces all of its current occurrences in `str1` with any other lowercase English character. The replacement is global: occurrences that have merged into the selected character are changed together by a later operation. Because every step acts on the string produced by the preceding steps, conversion order can affect whether the target can be reached.

Return `true` exactly when some allowed sequence transforms `str1` into `str2`; otherwise, return `false`.
