import random
from typing import List


def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

def in_order(numbers: List[int]) -> bool:
    """
    リストが昇順になっているかをチェックする
    """
    return all(numbers[i]<numbers[i+1] for i in range(len(numbers)-1))

    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bogo_sort(nums))
