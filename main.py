from functools import lru_cache


class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        @lru_cache(None)
        def FindChildren(start, finish, fuel):
            ans = 0
            if start == finish:
                ans += 1
            for i in range(len(locations)):
                if i != start:
                    if fuel >= abs(locations[i] - locations[start]):
                        ans += FindChildren(i, finish, fuel - abs(locations[i] - locations[start]))
            return ans
        return FindChildren(start=start, finish=finish, fuel=fuel) % (10 ** 9 + 7)


a = Solution()
print(a.countRoutes([4, 3, 1], 1, 0, 6))
