"""
get best work
"""


def best_worker(numbers: list):
    if not numbers:
        return None
    best_work = numbers[0]
    for i in range(len(numbers)):
        temp_numbers = numbers[i:]
        temp_best = temp_numbers[0]
        for j in range(1, len(temp_numbers)):
            temp_best = temp_best + temp_numbers[j]
            if best_work >= temp_best:
                best_work = temp_best
    return best_work


print(best_worker([2, -3, -4, 1, -3, 2, -1]))
print(best_worker([0.5, 1]))
print(best_worker([1]))
print(best_worker([]))
print(float('0.814'))
