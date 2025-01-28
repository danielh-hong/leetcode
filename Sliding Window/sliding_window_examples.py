# Sliding window examples:

# Easy: Maximum Sum of a Subarray of Size K (can solve)
def max_sum_subarray(arr, k):
    """
    Function to find the maximum sum of a subarray of size k.
    
    Args:
    arr (list): The input array.
    k (int): The size of the subarray.
    
    Returns:
    int: The maximum sum of the subarray of size k.
    """
    if not arr or k <= 0 or k > len(arr):
        return 0

    # Initialize the sliding window
    max_sum = 0
    window_sum = 0

    # Create the initial window
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add next element, remove first element of previous window
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage:
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9




# Medium: Longest Substring with K Distinct Characters
def longest_substring_k_distinct(s, k):
    """
    Function to find the length of the longest substring with at most k distinct characters.
    
    Args:
    s (str): The input string.
    k (int): The maximum number of distinct characters allowed.
    
    Returns:
    int: The length of the longest substring.
    """
    if not s or k <= 0:
        return 0

    char_frequency = {}
    max_length = 0
    window_start = 0

    # Expand the window
    for window_end in range(len(s)):
        right_char = s[window_end]
        char_frequency[right_char] = char_frequency.get(right_char, 0) + 1

        # Shrink the window if the number of distinct characters exceeds k
        while len(char_frequency) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1

        # Update the maximum length
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

# Example usage:
s = "araaci"
k = 2
print(longest_substring_k_distinct(s, k))  # Output: 4 ("araa")



# Hard: Sliding Window Max:
def sliding_window_max(nums, k):
    """
    Function to find the maximum value in each sliding window of size k.
    
    Args:
    nums (list): The input list of integers.
    k (int): The size of the sliding window.
    
    Returns:
    list: A list of the maximum values for each window.
    """
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []
    window = []  # Stores indices of the useful elements in the current window

    for i in range(len(nums)):
        # Remove indices that are out of the current window
        while window and window[0] < i - k + 1:
            window.pop(0)

        # Remove indices of smaller elements as they are not useful
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        # Add the current index to the window
        window.append(i)

        # Add the maximum for the current window to the result
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Example usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))  # Output: [3, 3, 5, 5, 6, 7]
