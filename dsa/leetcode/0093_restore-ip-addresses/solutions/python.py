def solve(s: str) -> list[str]:
    result: list[str] = []
    segments: list[str] = []

    def restore(index: int) -> None:
        remaining_segments = 4 - len(segments)
        remaining_characters = len(s) - index
        if not remaining_segments <= remaining_characters <= 3 * remaining_segments:
            return
        if len(segments) == 4:
            result.append(".".join(segments))
            return

        for length in range(1, 4):
            end = index + length
            if end > len(s):
                break
            segment = s[index:end]
            if length > 1 and segment[0] == "0":
                break
            if int(segment) > 255:
                break
            segments.append(segment)
            restore(end)
            segments.pop()

    restore(0)
    return result
