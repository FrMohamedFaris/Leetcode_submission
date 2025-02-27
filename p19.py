class Solution(object):
    def countTriplets(self, arr):
        n = len(arr)
        prefixXOR = [0] * (n + 1)

        for i in range(n):
            prefixXOR[i + 1] = prefixXOR[i] ^ arr[i]

        count = 0

        for i in range(n):
            for k in range(i + 1, n):
                if prefixXOR[i] == prefixXOR[k + 1]:
                    count += k - i

        return count


arr = [2, 3, 1, 6, 7]
sol = Solution()
print(sol.countTriplets(arr))
