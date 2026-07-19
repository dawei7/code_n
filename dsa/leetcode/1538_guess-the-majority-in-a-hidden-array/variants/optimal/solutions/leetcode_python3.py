class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        baseline = reader.query(0, 1, 2, 3)
        comparison = reader.query(0, 1, 2, 4)

        same = 1
        different = 0
        different_index = -1

        if comparison == baseline:
            same += 1
        else:
            different += 1
            different_index = 4

        for index in range(5, n):
            if reader.query(0, 1, 2, index) == baseline:
                same += 1
            else:
                different += 1
                different_index = index

        checks = (
            (reader.query(0, 1, 3, 4), 2),
            (reader.query(0, 2, 3, 4), 1),
            (reader.query(1, 2, 3, 4), 0),
        )
        for result, index in checks:
            if result == comparison:
                same += 1
            else:
                different += 1
                different_index = index

        if same == different:
            return -1
        return 3 if same > different else different_index
