def solve(row: list[int]) -> int:
    seating = row[:]
    position = [0] * len(seating)
    for seat, person in enumerate(seating):
        position[person] = seat

    swaps = 0
    for first_seat in range(0, len(seating), 2):
        person = seating[first_seat]
        partner = person ^ 1
        second_seat = first_seat + 1
        if seating[second_seat] == partner:
            continue

        partner_seat = position[partner]
        displaced = seating[second_seat]
        seating[second_seat], seating[partner_seat] = partner, displaced
        position[partner] = second_seat
        position[displaced] = partner_seat
        swaps += 1

    return swaps
