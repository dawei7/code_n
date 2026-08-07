from typing import List


class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        length = len(sensor1)
        first = 0
        while first < length and sensor1[first] == sensor2[first]:
            first += 1
        if first == length:
            return -1

        first_faulty = True
        second_faulty = True
        for index in range(first, length - 1):
            if sensor1[index] != sensor2[index + 1]:
                first_faulty = False
            if sensor2[index] != sensor1[index + 1]:
                second_faulty = False

        if first_faulty == second_faulty:
            return -1
        return 1 if first_faulty else 2
