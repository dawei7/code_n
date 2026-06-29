import math
import sys

class WeightedKDTree:

    def __init__(self, points, weights=None):
        if weights is None:
            rows = [(x, y, 0.0) for x, y in points]
        else:
            rows = [(x, y, float(w)) for (x, y), w in zip(points, weights)]
        self.x = []
        self.y = []
        self.w = []
        self.left = []
        self.right = []
        self.xmin = []
        self.xmax = []
        self.ymin = []
        self.ymax = []
        self.minw = []
        self.root = self._build(rows, 0)

    def _build(self, rows, depth):
        if not rows:
            return -1
        axis = depth & 1
        rows.sort(key=lambda row: row[axis])
        mid = len(rows) // 2
        px, py, weight = rows[mid]
        idx = len(self.x)
        self.x.append(px)
        self.y.append(py)
        self.w.append(weight)
        self.left.append(-1)
        self.right.append(-1)
        self.xmin.append(px)
        self.xmax.append(px)
        self.ymin.append(py)
        self.ymax.append(py)
        self.minw.append(weight)
        left = self._build(rows[:mid], depth + 1)
        right = self._build(rows[mid + 1:], depth + 1)
        self.left[idx] = left
        self.right[idx] = right
        for child in (left, right):
            if child == -1:
                continue
            if self.xmin[child] < self.xmin[idx]:
                self.xmin[idx] = self.xmin[child]
            if self.xmax[child] > self.xmax[idx]:
                self.xmax[idx] = self.xmax[child]
            if self.ymin[child] < self.ymin[idx]:
                self.ymin[idx] = self.ymin[child]
            if self.ymax[child] > self.ymax[idx]:
                self.ymax[idx] = self.ymax[child]
            if self.minw[child] < self.minw[idx]:
                self.minw[idx] = self.minw[child]
        return idx

    def _box_distance(self, qx, qy, idx):
        dx = 0
        if qx < self.xmin[idx]:
            dx = self.xmin[idx] - qx
        elif qx > self.xmax[idx]:
            dx = qx - self.xmax[idx]
        dy = 0
        if qy < self.ymin[idx]:
            dy = self.ymin[idx] - qy
        elif qy > self.ymax[idx]:
            dy = qy - self.ymax[idx]
        return math.hypot(dx, dy)

    def nearest_value(self, point):
        qx, qy = point
        best = float('inf')
        stack = [self.root]
        while stack:
            idx = stack.pop()
            if idx == -1:
                continue
            lower = self.minw[idx] + self._box_distance(qx, qy, idx)
            if lower >= best:
                continue
            value = self.w[idx] + math.hypot(qx - self.x[idx], qy - self.y[idx])
            if value < best:
                best = value
            left = self.left[idx]
            right = self.right[idx]
            if left != -1 and right != -1:
                left_lower = self.minw[left] + self._box_distance(qx, qy, left)
                right_lower = self.minw[right] + self._box_distance(qx, qy, right)
                if left_lower < right_lower:
                    if right_lower < best:
                        stack.append(right)
                    if left_lower < best:
                        stack.append(left)
                else:
                    if left_lower < best:
                        stack.append(left)
                    if right_lower < best:
                        stack.append(right)
            elif left != -1:
                stack.append(left)
            elif right != -1:
                stack.append(right)
        return best

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def minimum_run(start, first, second, finish):
    finish_tree = WeightedKDTree(finish)
    first_tree = WeightedKDTree(first, [dist(start, point) for point in first])
    second_tree = WeightedKDTree(second, [dist(start, point) for point in second])
    answer = float('inf')
    for point in second:
        candidate = first_tree.nearest_value(point) + finish_tree.nearest_value(point)
        if candidate < answer:
            answer = candidate
    for point in first:
        candidate = second_tree.nearest_value(point) + finish_tree.nearest_value(point)
        if candidate < answer:
            answer = candidate
    return answer

def read_points(data, idx, count):
    points = [(data[idx + 2 * i], data[idx + 2 * i + 1]) for i in range(count)]
    return (points, idx + 2 * count)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        start = (data[idx], data[idx + 1])
        idx += 2
        n, m, k = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        first, idx = read_points(data, idx, n)
        second, idx = read_points(data, idx, m)
        finish, idx = read_points(data, idx, k)
        out.append(f'{minimum_run(start, first, second, finish):.10f}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
