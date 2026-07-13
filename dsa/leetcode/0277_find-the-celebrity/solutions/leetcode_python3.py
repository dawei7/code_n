class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for person in range(1, n):
            if knows(candidate, person):
                candidate = person
        for person in range(n):
            if person == candidate:
                continue
            if knows(candidate, person) or not knows(person, candidate):
                return -1
        return candidate
