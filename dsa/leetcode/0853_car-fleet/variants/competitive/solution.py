from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        fleet_distance = -1
        fleet_speed = 1

        for car_position, car_speed in sorted(zip(position, speed), reverse=True):
            distance = target - car_position
            if fleet_distance < 0 or distance * fleet_speed > fleet_distance * car_speed:
                fleets += 1
                fleet_distance = distance
                fleet_speed = car_speed

        return fleets
