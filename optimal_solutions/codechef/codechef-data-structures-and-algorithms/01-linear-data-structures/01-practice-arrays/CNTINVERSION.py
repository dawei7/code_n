


def solve():
    def countInversions(arr):
        def merge_and_count(arr, left, mid, right):
            L = arr[left:mid + 1]
            R = arr[mid + 1:right + 1]

            i = j = 0
            k = left
            inv_count = 0

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    inv_count += (len(L) - i)  # Remaining elements in L are inversions
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

            return inv_count

        def merge_sort_and_count(arr, left, right):
            count = 0
            if left < right:
                mid = (left + right) // 2
                count += merge_sort_and_count(arr, left, mid)
                count += merge_sort_and_count(arr, mid + 1, right)
                count += merge_and_count(arr, left, mid, right)
            return count

        return merge_sort_and_count(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    solve()
