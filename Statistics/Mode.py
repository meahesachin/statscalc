from collections import Counter


def mode(nums):

    count = Counter(nums)

    return [k for k, v in count.items() if v== count.most_common(1)[0][1]]

