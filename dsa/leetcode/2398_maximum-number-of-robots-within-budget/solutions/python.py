from collections import deque

def solve(charge_times: list[int], running_costs: list[int], budget: int) -> int:
    n = len(charge_times)
    max_len = 0
    left = 0
    current_running_sum = 0
    # Monotonic queue to store indices of chargeTimes in descending order
    dq = deque()

    for right in range(n):
        # Update running sum
        current_running_sum += running_costs[right]

        # Maintain monotonic decreasing queue for chargeTimes
        while dq and charge_times[dq[-1]] <= charge_times[right]:
            dq.pop()
        dq.append(right)

        # Calculate total cost: max(charge_times in window) + (count * sum(running_costs))
        # count = right - left + 1
        while left <= right:
            window_size = right - left + 1
            max_charge = charge_times[dq[0]]
            total_cost = max_charge + (window_size * current_running_sum)

            if total_cost <= budget:
                break

            # Shrink window from the left
            current_running_sum -= running_costs[left]
            left += 1
            if dq[0] < left:
                dq.popleft()

        max_len = max(max_len, right - left + 1)

    return max_len
