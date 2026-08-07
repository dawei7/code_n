class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        index1 = len(series1) - 1
        index2 = len(series2) - 1
        next_value1 = 0
        next_value2 = 0
        answer = []

        while index1 >= 0 or index2 >= 0:
            if index2 < 0 or (index1 >= 0 and series1[index1][0] > series2[index2][0]):
                timestamp = series1[index1][0]
            elif index1 < 0 or series2[index2][0] > series1[index1][0]:
                timestamp = series2[index2][0]
            else:
                timestamp = series1[index1][0]

            if index1 >= 0 and series1[index1][0] == timestamp:
                next_value1 = series1[index1][1]
                index1 -= 1
            if index2 >= 0 and series2[index2][0] == timestamp:
                next_value2 = series2[index2][1]
                index2 -= 1

            answer.append([timestamp, next_value1 + next_value2])

        answer.reverse()
        return answer
