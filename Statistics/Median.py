from Calculator.calculator import addition, subtraction, division


def median(nums):

    med = 0
    num = len(nums)
    sorted_nums = [nums[i] for i in range(num)]
    # sorted_nums = nums.sort()

    if num % 2 == 0:
        median1 = sorted_nums[int(float(division.division(num, 2)))]
        median2 = sorted_nums[int(float(subtraction.subtraction((division.division(num, 2)), 1)))]
        med = division.division(addition.addition(median1, median2), 2)
        # med = sorted_nums[int(float(division.division(addition.addition (median1, median2), 2)))]
    else:
        med = sorted_nums[int(float(division.division(num, 2)))]

    return med
