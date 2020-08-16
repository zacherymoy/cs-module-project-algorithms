def sliding_window_max(nums, k):
    
    i = 0
    arr = []
    while i + (k - 1) < len(nums):
        arr.append(max(nums[i:(i+k)]))
        i += 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")