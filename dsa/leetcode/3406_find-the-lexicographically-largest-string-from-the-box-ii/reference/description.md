## Description

Alice plays a game with `numFriends` friends using the lowercase string `word`. In every round, she splits `word` into exactly `numFriends` non-empty contiguous strings. A round may use any placement of the cuts that has not appeared in an earlier round, and every resulting piece is placed into a box.

After all distinct splits have been used, return the lexicographically largest string that ever entered the box. At the first position where two strings differ, the string with the later lowercase letter is larger. If one string is a prefix of the other, the longer string is larger.
