def solve(positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
    pos_set = set(positive_feedback)
    neg_set = set(negative_feedback)
    
    student_scores = []
    
    for i in range(len(student_id)):
        score = 0
        words = report[i].split()
        for word in words:
            if word in pos_set:
                score += 3
            elif word in neg_set:
                score -= 1
        
        # We store (-score, id) to use Python's default sort/heap behavior:
        # Sort by score descending (via negative score) and ID ascending.
        student_scores.append((-score, student_id[i]))
    
    student_scores.sort()
    
    return [student_scores[i][1] for i in range(k)]
