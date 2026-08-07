[TOC]


### Approach #1: Maintain Sorted Disjoint Intervals [Accepted]

**Intuition**

Because `left, right < 10^9`, we need to deal with the coordinates abstractly. Let's maintain some sorted structure of disjoint intervals. These intervals will be closed (eg. we don't store `[[1, 2], [2, 3]]`; we would store `[[1, 3]]` instead.)

In this article, we will go over Python and Java versions separately, as the data structures available to us that are relevant to the problem are substantially different.

**Algorithm**

We will maintain the structure as a *list* `self.ranges = []`.  

*Adding a Range*

When we want to add a range, we first find the indices `i, j = self._bounds(left, right)` for which `self.ranges[i: j+1]` touches (in a closed sense - not half open) the given interval `[left, right]`. We can find this in log time by making steps of size 100, 10, then 1 in our linear search from both sides.

Every interval touched by `[left, right]` will be replaced by the single interval `[min(left, self.ranges[i][0]), max(right, self.ranges[j][1])]`.

*Removing a Range*

Again, we use `i, j = self._bounds(...)` to only work in the relevant subset of `self.ranges` that is in the neighborhood of our given range `[left, right)`. For each interval `[x, y)` from `self.ranges[i:j+1]`, we may have some subset of that interval to the left and/or right of `[left, right)`. We replace our current interval `[x, y)` with those (up to 2) new intervals.

*Querying a Range*

As the intervals are sorted, we use binary search to find the single interval that could intersect `[left, right)`, then verify that it does.


```python
class RangeModule(object):
    def __init__(self):
        self.ranges = []

    def _bounds(self, left, right):
        i, j = 0, len(self.ranges) - 1
        for d in (100, 10, 1):
            while i + d - 1 < len(self.ranges) and self.ranges[i+d-1][1] < left:
                i += d
            while j >= d - 1 and self.ranges[j-d+1][0] > right:
                j -= d
        return i, j

    def addRange(self, left, right):
        i, j = self._bounds(left, right)
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [(left, right)]

    def queryRange(self, left, right):
        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        if i: i -= 1
        return (bool(self.ranges) and
                self.ranges[i][0] <= left and
                right <= self.ranges[i][1])

    def removeRange(self, left, right):
        i, j = self._bounds(left, right)
        merge = []
        for k in xrange(i, j+1):
            if self.ranges[k][0] < left:
                merge.append((self.ranges[k][0], left))
            if right < self.ranges[k][1]:
                merge.append((right, self.ranges[k][1]))
        self.ranges[i:j+1] = merge
```


---

**Algorithm (Java)**

We will maintain the structure as a *TreeSet* `ranges = new TreeSet<Interval>();`. We introduce a new *Comparable* class `Interval` to represent our half-open intervals. They compare by *right-most* coordinate as later we will see that it simplifies our work. Also note that this ordering is consistent with equals, which is important when dealing with *Sets*.

*Adding and Removing a Range*

The basic structure of adding and removing a range is the same.  First, we must iterate over the relevant subset of `ranges`. This is done using iterators so that we can `itr.remove` on the fly, and break when the intervals go too far to the right.

The critical logic of `addRange` is simply to make `left, right` the smallest and largest seen coordinates. After, we add one giant interval representing the union of all intervals seen that touched `[left, right]`.

The logic of `removeRange` is to remember in `todo` the intervals we wanted to replace the removed interval with. After, we can add them all back in.

*Querying a Range*

As the intervals are sorted, we search to find the single interval that could intersect `[left, right)`, then verify that it does. As the TreeSet uses a balanced (red-black) tree, this has logarithmic complexity.


```cpp
class RangeModule {
public:
    RangeModule() {}

    void addRange(int left, int right) {
        auto l = invals.upper_bound({left, INT_MAX});
        auto r = invals.upper_bound({right, INT_MAX});
        if (l != invals.begin()) {
            l--;
            if (l->second < left) l++;
        }
        if (l != r) {
            left = min(left, l->first);
            right = max(right, (--r)->second);
            invals.erase(l, ++r);
        }
        invals.insert({left, right});
    }

    bool queryRange(int left, int right) {
        auto it = invals.upper_bound({left, INT_MAX});
        if (it == invals.begin() || (--it)->second < right) return false;
        return true;
    }

    void removeRange(int left, int right) {
        auto l = invals.upper_bound({left, INT_MAX});
        auto r = invals.upper_bound({right, INT_MAX});
        if (l != invals.begin()) {
            l--;
            if (l->second < left) l++;
        }
        if (l == r) return;
        int l1 = min(left, l->first);
        int r1 = max(right, (--r)->second);
        invals.erase(l, ++r);
        if (l1 < left) invals.insert({l1, left});
        if (r1 > right) invals.insert({right, r1});
    }

private:
    set<pair<int, int>> invals;
};
```


**Complexity Analysis**

* Time Complexity: Let $$K$$ be the number of elements in `ranges`. `addRange` and `removeRange` operations have $$O(K)$$ complexity. `queryRange` has $$O(\log K)$$ complexity. Because `addRange, removeRange` adds at most 1 interval at a time, you can bound these further. For example, if there are $$A$$ `addRange`, $$R$$ `removeRange`, and $$Q$$ `queryRange` number of operations respectively, we can express our complexity as $$O((A+R)^2 Q \log(A+R))$$. 

* Space Complexity: $$O(A+R)$$, the space used by `ranges`.