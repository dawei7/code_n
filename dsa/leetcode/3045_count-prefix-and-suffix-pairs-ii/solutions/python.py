from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def solve(words: list[str]) -> int:
    root = TrieNode()
    total_pairs = 0
    
    for word in words:
        # A word is a prefix and suffix of another if the sequence of 
        # pairs (word[k], word[n-len(word)+k]) matches.
        # We traverse the Trie using these character pairs.
        node = root
        n = len(word)
        
        for i in range(n):
            char_pair = (word[i], word[n - n + i]) # This logic simplifies to (word[i], word[i])
            # Actually, the condition is: word[i] is prefix and suffix of word[j].
            # This means word[i] == word[j][:len(word[i])] AND word[i] == word[j][-len(word[i]):]
            # We can represent the state by the pair of characters at the current index
            # relative to the start and end of the word.
            pair = (word[i], word[n - len(word) + i]) # Placeholder logic for Trie path
            
        # Correct approach: Use a Trie to store the prefix-suffix pairs.
        # For each word, we check how many times this specific word structure 
        # has appeared as a prefix/suffix combination.
        
        # Re-implementing with a simpler Trie approach:
        # Since we need prefix AND suffix, we store the word in the Trie.
        # But wait, the constraint is word[i] is prefix AND suffix of word[j].
        # This is equivalent to saying word[i] is a prefix of word[j] 
        # AND word[i] is a suffix of word[j].
        
        # Using a Trie to store the words:
        curr = root
        for i in range(n):
            pair = (word[i], word[n - n + i]) # This is just word[i]
            # Actually, the standard approach for this specific problem:
            # Insert (word[i], word[n-1-i]) into Trie.
            pass
            
    # Optimized implementation using a Trie of (prefix, suffix) pairs
    root = {}
    ans = 0
    for w in words:
        n = len(w)
        curr = root
        for i in range(n):
            pair = (w[i], w[n - 1 - i])
            if pair not in curr:
                curr[pair] = {}
            curr = curr[pair]
            if 'count' in curr:
                ans += curr['count']
        
        # After traversing, increment the count at the end of this word's path
        curr['count'] = curr.get('count', 0) + 1
        
    return ans
