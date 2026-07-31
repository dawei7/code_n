from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece_by_first = {piece[0]: piece for piece in pieces}
        index = 0

        while index < len(arr):
            piece = piece_by_first.get(arr[index])
            if piece is None or arr[index : index + len(piece)] != piece:
                return False
            index += len(piece)

        return True
