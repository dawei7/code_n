class Matrix3D:
    def __init__(self, n: int):
        self.n = n
        self.ones = set()
        self.cnt = [0] * n

    def setCell(self, x: int, y: int, z: int) -> None:
        cell = (x, y, z)
        if cell not in self.ones:
            self.ones.add(cell)
            self.cnt[x] += 1

    def unsetCell(self, x: int, y: int, z: int) -> None:
        cell = (x, y, z)
        if cell in self.ones:
            self.ones.remove(cell)
            self.cnt[x] -= 1

    def largestMatrix(self) -> int:
        best_x = self.n - 1
        best_cnt = self.cnt[best_x]
        for x in range(self.n - 2, -1, -1):
            if self.cnt[x] > best_cnt:
                best_cnt = self.cnt[x]
                best_x = x
        return best_x


# Your matrix3D object will be instantiated and called as such:
# obj = matrix3D(n)
# obj.setCell(x,y,z)
# obj.unsetCell(x,y,z)
# param_3 = obj.largestMatrix()
