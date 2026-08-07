def _containment_and_overlap(first: str, second: str) -> tuple[bool, int]:
    combined = second + "#" + first
    prefix = [0] * len(combined)
    contained = False
    for index in range(1, len(combined)):
        matched = prefix[index - 1]
        while matched and combined[index] != combined[matched]:
            matched = prefix[matched - 1]
        if combined[index] == combined[matched]:
            matched += 1
        prefix[index] = matched
        if index > len(second) and matched == len(second):
            contained = True
    return (contained, prefix[-1])


class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        second_in_first, first_to_second_overlap = _containment_and_overlap(s1, s2)
        if second_in_first:
            return s1
        first_in_second, second_to_first_overlap = _containment_and_overlap(s2, s1)
        if first_in_second:
            return s2
        first_then_second = s1 + s2[first_to_second_overlap:]
        second_then_first = s2 + s1[second_to_first_overlap:]
        return min((first_then_second, second_then_first), key=len)
