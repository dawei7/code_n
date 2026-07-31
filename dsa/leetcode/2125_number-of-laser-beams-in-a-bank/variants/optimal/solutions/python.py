def solve(bank: list[str]) -> int:
    previous_devices = 0
    beams = 0
    for row in bank:
        devices = row.count("1")
        if devices:
            beams += previous_devices * devices
            previous_devices = devices
    return beams
