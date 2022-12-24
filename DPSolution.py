class LIS:
  def __init__(self, nums):
    # Store the input list
    self.nums = nums

    # Create a list to store the LIS lengths at each index
    self.lst = [0] * len(nums)

    # Create a dictionary to store the previously calculated LIS lengths
    self.memo = {}

  def LIS_at_index(self, i):
    # If we have already calculated the LIS length at this index,
    # return it from the memo
    if i in self.memo:
      return self.memo[i]

    # If this is the first element, the LIS length is 1
    if i == 0:
      return 1

    # Set the default LIS length to 1
    self.lst[i] = 1

    # Iterate over the previous elements
    for j in range(0, i):
      # If the previous element is less than the current element,
      # update the LIS length at the current index
      if self.nums[j] < self.nums[i]:
        self.lst[i] = max(self.lst[i], self.LIS_at_index(j) + 1)

    # Store the LIS length at the current index in the memo
    self.memo[i] = self.lst[i]

    # Return the LIS length at the current index
    return self.lst[i]

  def LIS(self):
    # Initialize the maximum LIS length to 0
    max_length = 0

    # Iterate over the elements in the list
    for i in range(len(self.nums)):
      # Update the maximum LIS length
      max_length = max(max_length, self.LIS_at_index(i))

    # Return the maximum LIS length
    return max_length
