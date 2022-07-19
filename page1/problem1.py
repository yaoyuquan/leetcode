class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # key is the num
        # value is the index in nums
        map = {}
        # add number to the map
        for index, num in enumerate(nums):
            compare = target - num
            if compare in map:
                return [map[compare], index]
            else:
                map[num] = index