class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx, cy = center
        best_quality = -1
        best_coordinates = [-1, -1]

        for x, y, quality in towers:
            if abs(x - cx) + abs(y - cy) > radius:
                continue

            coordinates = [x, y]
            if quality > best_quality or (quality == best_quality and coordinates < best_coordinates):
                best_quality = quality
                best_coordinates = coordinates

        return best_coordinates
