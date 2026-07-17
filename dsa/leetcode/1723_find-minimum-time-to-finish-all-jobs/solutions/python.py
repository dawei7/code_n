def solve(jobs: list[int], k: int) -> int:
    jobs = sorted(jobs, reverse=True)
    workloads = [0] * k
    best = sum(jobs)

    def search(index: int) -> None:
        nonlocal best
        if index == len(jobs):
            best = min(best, max(workloads))
            return

        duration = jobs[index]
        seen_loads: set[int] = set()
        for worker in range(k):
            if workloads[worker] in seen_loads:
                continue
            if workloads[worker] + duration >= best:
                continue
            seen_loads.add(workloads[worker])
            workloads[worker] += duration
            search(index + 1)
            workloads[worker] -= duration
            if workloads[worker] == 0:
                break

    search(0)
    return best
