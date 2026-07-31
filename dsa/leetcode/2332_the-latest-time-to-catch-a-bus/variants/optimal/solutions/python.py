from typing import List


def solve(buses: List[int], passengers: List[int], capacity: int) -> int:
    ordered_buses = sorted(buses)
    ordered_passengers = sorted(passengers)
    occupied = set(ordered_passengers)
    passenger_index = 0
    boarded = 0

    for bus in ordered_buses:
        boarded = 0
        while (
            boarded < capacity
            and passenger_index < len(ordered_passengers)
            and ordered_passengers[passenger_index] <= bus
        ):
            passenger_index += 1
            boarded += 1

    if boarded < capacity:
        candidate = ordered_buses[-1]
    else:
        candidate = ordered_passengers[passenger_index - 1] - 1

    while candidate in occupied:
        candidate -= 1
    return candidate
