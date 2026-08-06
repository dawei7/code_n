## Description

Three parallel arrays describe a website-visit log. At index `i`, `username[i]` names the visitor, `website[i]` names the visited site, and `timestamp[i]` gives the visit time.

A pattern is an ordered list of exactly three website names. Its entries do not have to be distinct: `["home","away","love"]`, `["leetcode","love","leetcode"]`, and `["luffy","luffy","luffy"]` are all possible patterns. A user matches a pattern when that user visits its first site, then its second site at a later time, and then its third site later still. The chosen visits need not be consecutive in the user's history; unrelated visits may occur between them.

The score of a pattern is the number of distinct users who match it. Several different choices of visits by one user still add only one to that pattern's score.

Return the three-site pattern with the greatest score. If more than one pattern reaches that score, choose the lexicographically smallest pattern.
