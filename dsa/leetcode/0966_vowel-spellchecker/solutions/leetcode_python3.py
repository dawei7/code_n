from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def vowel_key(word):
            return "".join("*" if character in vowels else character for character in word.lower())

        exact = set(wordlist)
        lowercase = {}
        vowel_errors = {}
        for word in wordlist:
            lowercase.setdefault(word.lower(), word)
            vowel_errors.setdefault(vowel_key(word), word)

        answer = []
        for query in queries:
            if query in exact:
                answer.append(query)
            elif query.lower() in lowercase:
                answer.append(lowercase[query.lower()])
            else:
                answer.append(vowel_errors.get(vowel_key(query), ""))
        return answer
