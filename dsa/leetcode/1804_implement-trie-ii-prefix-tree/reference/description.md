## Description

Design a trie that stores a multiset of lowercase words. Inserting the same word repeatedly creates multiple occurrences rather than leaving a single membership flag. The structure must report both exact-word multiplicity and the number of stored words sharing a requested prefix.

It must also erase one occurrence of a supplied word. Every erase call is guaranteed to name a word currently present, possibly with other occurrences remaining. Erasing one word must update all of its prefix counts without changing unrelated words.
