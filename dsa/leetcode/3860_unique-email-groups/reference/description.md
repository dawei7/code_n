## Description

You are given an array `emails` in which every string is a valid email
address. Two addresses belong to the same group only when both their normalized
local names and their normalized domain names are identical.

Normalize the local name, which is the part before `@`, by applying all of
these rules:

- Ignore every dot (`.`).
- Ignore the first plus sign (`+`) and everything after it, when a plus sign is
  present.
- Convert all remaining letters to lowercase.

The domain name is the part after `@`. Normalize it by converting its letters
to lowercase; dots in the domain remain significant and are not removed.

Return the number of unique email groups represented after every address has
been normalized.
