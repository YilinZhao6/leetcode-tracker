class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.hashmap={}
        for index, value in enumerate(nums):
            if value not in self.hashmap:
                self.hashmap[value]=[]
            self.hashmap[value].append(index)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target in self.hashmap:
            return random.choice(self.hashmap[target])
        else:
            return -1
        