# NeoSOFT_reeneka
def twoSum(nums, target):
    seen = {}
# Iterate through the array with index and value
    for i, num in enumerate(nums):
      # Calculate the number to reach the target
        complement = target - num

        if complement in seen:
          # Return the indices of complement and current number
            return [seen[complement], i]

        seen[num] = i
      
 # Example 1       
nums = [2, 7, 11, 15]
target = 9
# Call the fucntion and print result
print(twoSum(nums, target))

# Example 2       
nums = [3, 2, 4]
target = 6
# Call the fucntion and print result
print(twoSum(nums, target))

# Example 3
nums = [3, 3]
target = 6
# Call the fucntion and print result
print(twoSum(nums, target))
