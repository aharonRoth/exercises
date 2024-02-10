def SingleNumber(nums):
    SingleNumber = nums[0]
    nums = nums[1:]
    newNums = []
    while SingleNumber in nums or SingleNumber in newNums:
        newNums.append(SingleNumber)
        SingleNumber = nums[0]
        nums = nums[1:]
    return SingleNumber

nums  = [1, 3, 1, -1, 3]
print(SingleNumber(nums))