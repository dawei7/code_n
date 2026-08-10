
## Solution

---

### Overview

We are given two sentences, `sentence1` and `sentence2` which are each represented as a string array. We are also given an array of string pairs, `similarPairs` where $\text{similarPairs}[i] = [xi, yi]$ indicates that the two words `xi` and `yi` are similar.

The problem describes two sentences are similar if:

1. They have the same length (i.e., the same number of words).
2. $\text{sentence1}[i]$ and $\text{sentence2}[i]$ are similar (words corresponding to each index are similar).

Our task is to determine whether `sentence1` is similar to `sentence2` or not.

---

### Approach: Using Hash Map and Hash Set

#### Intuition

To check whether `sentence1` is similar to `sentence2`, we would first check the number of words in both sentences. If the number of words in both of the sentences is not equal, the sentences cannot be similar, so we return `false` in such a case.

If the number of words in both sentences is equal, we need to check if all the words corresponding to each index of the sentences are similar, i.e., whether $\text{sentence1}[i]$ and $\text{sentence2}[i]$ are similar. These two words can be similar only if either they are the same word, i.e., $\text{sentence1}[i] = \text{sentence2}[i]$, or $(\text{sentence1}[i], \text{sentence2}[i])$ or $(\text{sentence2}[i], \text{sentence1}[i])$ appear in `similarPairs`.

To keep track of similar words for a word, we can think of creating a hash map, say `wordToSimilarWords` with a word as the key that stores a list of all the words that are similar to the key.

So, for every word at index `i` of the given sentences, we check if the words are the same, i.e., $\text{sentence1}[i] = \text{sentence2}[i]$ or if the words form a similar pair, i.e., $wordToSimilarWords[\text{sentence1}[i]]$ contains $\text{sentence2}[i]$.

How can we check whether $\text{sentence2}[i]$ is present in the list received from $wordToSimilarWords[\text{sentence1}[i]]$? We might have to iterate through the entire list of similar words for $\text{sentence1}[i]$, which could, in the worst case, grow to the number of pairs in `similarPair`. This is definitely not a good approach.

What if we use a hash set, say `set` to store similar words for a given word? The advantage of using a hash set over a list is that searching is much faster. In a list, searching costs $O(n \cdot m)$, where $n$ is the number of similar words and $m$ is the length of the word. With a hash set, it's $O(m)$, where $m$ is the length of the word. We need to spend some time to hash the strings which would also require $O(m)$ time per word.

This takes us to the solution of the problem. We define a hash map where a string is the key and the value is a hash set of strings. For each `word1, word2` pair in `similarPairs`, we add `word2` to $\text{wordToSimilarWords}[word1]$ and `word1` to $\text{wordToSimilarWords}[word2]$.

We then iterate over all the words in one of the sentences, say `sentence1`. For every word at index `i`, we would check if the words in both sentences at this index are the same word, i.e., $\text{sentence1}[i] = \text{sentence2}[i]$ or if they are similar by checking if $\text{sentence2}[i]$ is present in the $wordToSimilarWords[\text{sentence}[i]]$ set.

#### Algorithm

1. Check if the number of words in `sentence1` and `sentence2` are equal. If the number of words is not equal, return `false`.
2. Create a `wordToSimilarWords` hash map with string as the key and hash set of strings as the value such that $\text{wordToSimilarWords}[x]$ contains all the similar words corresponding to the word `x`.
3. For each `pair` in `similarPair`, insert the similar words represented by `pair` in `wordToSimilarWords`.
4. Iterate through each word of `sentence1`. For every word at index `i`:
- If the words are equal, i.e., $\text{sentence1}[i] = \text{sentence2}[i]$, continue to check the next word.
- If the words are similar, i.e., $wordToSimilarWords[\text{sentence1}[i]]$ contains $\text{sentence2}[i]$, continue to check the next word.
- Otherwise, the words are neither equal nor similar, so return `false`. The given sentences cannot be similar.
5. We were able to match all the corresponding words of the sentences, thus we return `true`.

#### Implementation

```python
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False
        wordToSimilarWords = defaultdict(set)
        for word1, word2 in similarPairs:
            wordToSimilarWords[word1].add(word2)
            wordToSimilarWords[word2].add(word1)
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in wordToSimilarWords[sentence1[i]]:
                continue
            return False
        return True
```

#### Complexity Analysis

Here, $n$ is the number of words in `sentence1` and `sentence2` and $k$ is the length of similar pairs. Let $m$ be the average length of words in `sentence1` as well as `similarPairs.`

* Time complexity: $O((n + k) \cdot m)$
- We iterate over all the elements of `similarPairs` and insert a pair twice into `wordToSimilarWords`. To hash each word of length $m$, we need $O(m)$ time, and to put the same length word in the hash set, we need $O(m)$ time again. Because there are $k$ pairs of words, there can be at most $2 \cdot k$ words that can be hashed and added to the set. As a result, we require $O(k \cdot m)$ time.
- We also iterate over all of `sentence1`'s words to see if $\text{sentence1}[i] = \text{sentence2}[i]$. Because each word is $m$ long, checking words at a specific index would take $O(m)$ time. It will take $O(n \cdot m)$ time in total because there are $n$ words. For each word $\text{sentence1}[i]$, we check if this word is present as the key in `wordToSimilarWords` which takes $O(m)$ time per word, and searching for the similar word $\text{sentence2}[i]$ in the $wordToSimilarWords[\text{sentence1}[i]]$ set also takes $O(m)$ time. As a result, for $n$ words, performing the key lookup followed by searching in the set would take $O(n \cdot m)$ time.
- The overall time required is $O((n + k) \cdot m)$.

* Space complexity: $O(k \cdot m)$

- We are using `wordToSimilarWords` to store all the similar words for a given word. There are $k$ pairs of similar words, so there could be $O(k)$ words that are inserted into `wordToSimilarWords`. Because the average length of each word is $m$, the required space is $O(k \cdot m)$.