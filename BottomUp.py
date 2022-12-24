# Function to find length of longest increasing subsequence
def LIS(array):
   
    # Initialize array to store LIS values for each element
    lis = [1] * len(array)

    # Loop through array and compute LIS values
    # The first loop with i starts from index 1 up to the last element
    # The second loop with j starts from index 0 up to the current index of i
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] > array[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Return the maximum LIS value
    return max(lis)