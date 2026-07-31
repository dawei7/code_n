def solve(positive_feedback, negative_feedback, report, student_id, k):
    word_score = {word: 3 for word in positive_feedback}
    word_score.update((word, -1) for word in negative_feedback)

    ranking = []
    for feedback, identifier in zip(report, student_id):
        score = sum(word_score.get(word, 0) for word in feedback.split())
        ranking.append((-score, identifier))

    ranking.sort()
    return [identifier for _, identifier in ranking[:k]]
