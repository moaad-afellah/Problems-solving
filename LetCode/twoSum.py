def twoSum(nums, target):
    main = []
    for mainNumber in range(0, len(nums)):
        for theNumberOfList in range(mainNumber + 1, len(nums)):
            if nums[mainNumber] == target:
                main.append(mainNumber)
            if nums[mainNumber] + nums[theNumberOfList] == target:
                return [theNumberOfList, mainNumber]
    return main

res = twoSum([0, 4, 3, 0], 0)
print(res)












