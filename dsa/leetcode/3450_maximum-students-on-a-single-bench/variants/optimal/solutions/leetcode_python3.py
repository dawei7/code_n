from collections import defaultdict
from typing import List


class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        students_by_bench = defaultdict(set)

        for student_id, bench_id in students:
            students_by_bench[bench_id].add(student_id)

        return max((len(student_ids) for student_ids in students_by_bench.values()), default=0)
