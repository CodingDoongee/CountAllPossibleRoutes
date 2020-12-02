Counter = 0


def IncreaseCounter():
    global Counter
    Counter = Counter + 1


class Node:
    def __init__(self, parent, value, Index, fuel):
        self.value = value
        self.Index = Index
        self.remainFuel = fuel

    def FindChildren(self, locations, start):
        for i in range(len(locations)):
            if i == self.Index:
                continue
            else:
                if self.remainFuel >= abs(locations[i]-self.value):
                    Child = Node(self.Index, locations[i], i, self.remainFuel - abs(locations[i] - self.value))
                    Child.FindChildren(locations, start)
                    if Child.Index == start:
                        IncreaseCounter()

                else:
                    pass


class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        FinishNode = Node(-1, locations[finish], finish, fuel)
        FinishNode.FindChildren(locations, start)
        return Counter

    def __call__(self, *args, **kwargs):
        print(Counter)

a = Solution()
a.countRoutes([4,3,1], 1, 0, 6)
a()