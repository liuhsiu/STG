import unittest

from page_object_functions.recur_fibo import RecurFibo
from page_object_functions.convert_num_to_string import ConvertNumToString



class P1Solution(unittest.TestCase):
    # Given an arry of itnergers numbs and an integer target, retrn indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    # You can return the answer in any order.

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_dict = {}
        nums_len = len(nums)
        for i in range(nums_len):
            complement = target - nums[i]
            if complement in complement_dict:
                return [complement_dict[complement], i]
            else:
                if nums[i] in complement_dict:
                    continue
                complement_dict[nums[i]] = i


    def twoSum3(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []

    # how to create hash table in python
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100


    nums = [2,7,11,15]
    target = 9

    def test_get_hash(self):
        P1Solution.twoSum(self, nums, target)


    def test_two_sum(self):
        P1Solution.get_hash(self, 'm')


if __name__ == '__main__':
    unittest.main()