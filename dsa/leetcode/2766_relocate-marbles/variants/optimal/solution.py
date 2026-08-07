class Solution:
    def relocateMarbles(
        self,
        nums: List[int],
        moveFrom: List[int],
        moveTo: List[int],
    ) -> List[int]:
        occupied = set(nums)

        for source, destination in zip(moveFrom, moveTo):
            occupied.remove(source)
            occupied.add(destination)

        return sorted(occupied)
