def has_33(nums):
    '''
    This function can detect if there's any equivalnet adjacent entries
    in a list
    '''
    result = []
    for n in range(len(nums)-1):
        if nums[n] == 3.0 and nums[n+1] == 3.0:
            result.insert(n, 'True')
        else:
            result.insert(n, 'False')
    if 'True' in result:
        print(True)
    else:
        print(False)

has_33([1, 3, 1, 3, 1, 2, 1, 2, 3, 2, 3, 2, 3, 2, 3, 23, 2, 3, 2, 3, 31, 13, 1])