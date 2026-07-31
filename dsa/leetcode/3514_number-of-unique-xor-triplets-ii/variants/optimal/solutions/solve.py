def solve(nums: list[int]) -> int:
    width = 1 << max(nums).bit_length()
    spectrum = [0] * width
    for value in nums:
        spectrum[value] = 1

    block = 1
    while block < width:
        step = block * 2
        for start in range(0, width, step):
            for offset in range(block):
                left = spectrum[start + offset]
                right = spectrum[start + block + offset]
                spectrum[start + offset] = left + right
                spectrum[start + block + offset] = left - right
        block = step

    for index in range(width):
        spectrum[index] **= 3

    block = 1
    while block < width:
        step = block * 2
        for start in range(0, width, step):
            for offset in range(block):
                left = spectrum[start + offset]
                right = spectrum[start + block + offset]
                spectrum[start + offset] = left + right
                spectrum[start + block + offset] = left - right
        block = step

    return sum(count != 0 for count in spectrum)
