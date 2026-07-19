def solve(difficulty: list[int], profit: list[int], worker: list[int]) -> int:
    jobs = sorted(zip(difficulty, profit))
    abilities = sorted(worker)
    job_index = 0
    best_profit = 0
    total_profit = 0

    for ability in abilities:
        while job_index < len(jobs) and jobs[job_index][0] <= ability:
            best_profit = max(best_profit, jobs[job_index][1])
            job_index += 1
        total_profit += best_profit

    return total_profit
