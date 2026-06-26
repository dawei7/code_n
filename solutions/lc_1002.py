"""
Description
-----------
Given a list of lowercase words, return all characters that appear in every word. If a character appears multiple times in every word, include it that many times in the result.

Examples
--------
Example 1:
Input:  words = ["bella", "label", "roller"]
Output: ["e", "l", "l"]

Example 2:
Input:  words = ["cool", "lock", "cook"]
Output: ["c", "o"]

Example 3:
Input:  words = ["abc", "def"]
Output: []
"""

def solve(words):
    # Write your code here.
    merged = dict()
    merged_list = list()

    for word in words:
        curr = dict()
        for char in word:
            curr.setdefault(char, 0)
            curr[char] += 1

        if not bool(merged):
            merged = curr.copy()
        else:
            for k,v in merged.items():
                if k in curr:
                    merged[k] = curr[k] if curr[k] < merged[k] else merged[k]
                else:
                    merged[k] = 0
        
    for k,v in merged.items():
        for _ in range(v):
            merged_list.append(k)

    return merged_list













