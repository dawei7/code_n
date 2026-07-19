from typing import List


class Solution:
    def friendRequests(
        self,
        n: int,
        restrictions: List[List[int]],
        requests: List[List[int]],
    ) -> List[bool]:
        parent = list(range(n))
        size = [1] * n

        def find(person: int) -> int:
            while person != parent[person]:
                parent[person] = parent[parent[person]]
                person = parent[person]
            return person

        result = []
        for first, second in requests:
            first_root = find(first)
            second_root = find(second)
            allowed = True

            if first_root != second_root:
                for restricted_first, restricted_second in restrictions:
                    restricted_first_root = find(restricted_first)
                    restricted_second_root = find(restricted_second)
                    if (
                        restricted_first_root == first_root
                        and restricted_second_root == second_root
                    ) or (
                        restricted_first_root == second_root
                        and restricted_second_root == first_root
                    ):
                        allowed = False
                        break

                if allowed:
                    if size[first_root] < size[second_root]:
                        first_root, second_root = second_root, first_root
                    parent[second_root] = first_root
                    size[first_root] += size[second_root]

            result.append(allowed)

        return result
