from typing import List


def solve(jobs: List[int], workers: List[int]) -> int:
    ordered_jobs = sorted(jobs)
    ordered_workers = sorted(workers)
    return max(
        (job + worker - 1) // worker
        for job, worker in zip(ordered_jobs, ordered_workers)
    )
