from collections import defaultdict


def solve(students: list[list[int]]) -> int:
    students_by_bench: defaultdict[int, set[int]] = defaultdict(set)

    for student_id, bench_id in students:
        students_by_bench[bench_id].add(student_id)

    return max((len(student_ids) for student_ids in students_by_bench.values()), default=0)
