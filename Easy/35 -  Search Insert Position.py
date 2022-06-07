def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
                if num >= target:
                        return i

        return len(nums)

print(searchInsert([1,3,5,6], 0))