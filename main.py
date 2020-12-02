Counter = 0


class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        self.FindChildren(locations, start, finish, fuel)
        return Counter % (10**9+7)

    def FindChildren(self, locations, start, finish, fuel):
        global Counter
        for i in range(len(locations)):
            if i == start:
                continue
            else:
                if fuel >= abs(locations[i]-locations[start]):
                    self.FindChildren(locations, i, finish, fuel - abs(locations[i]-locations[start]))
                    if i == finish:
                        Counter = Counter + 1

    def __call__(self, *args, **kwargs):
        print(Counter)

a = Solution()
a.countRoutes([4,3,1], 1, 0, 6)
a()