from typing import List


def solve(buses: List[int], passengers: List[int], capacity: int) -> int:
    buses.sort()
    passengers.sort()
    occupied = set(passengers)
    passenger_index = 0
    boarded = 0

    for bus in buses:
        boarded = 0
        while boarded < capacity and passenger_index < len(passengers) and passengers[passenger_index] <= bus:
            passenger_index += 1
            boarded += 1

    if boarded < capacity:
        candidate = buses[-1]
    else:
        candidate = passengers[passenger_index - 1] - 1

    while candidate in occupied:
        candidate -= 1
    return candidate
