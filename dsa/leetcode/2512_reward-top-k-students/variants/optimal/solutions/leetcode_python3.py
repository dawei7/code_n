from typing import List


class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        word_score = {word: 3 for word in positive_feedback}
        word_score.update((word, -1) for word in negative_feedback)

        ranking = []
        for feedback, identifier in zip(report, student_id):
            score = sum(word_score.get(word, 0) for word in feedback.split())
            ranking.append((-score, identifier))

        ranking.sort()
        return [identifier for _, identifier in ranking[:k]]
