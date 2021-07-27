# How do you find the missing number in a
# given integer array of 1 to 100?
def find_missing_number():
    data = [1, 2, 4, 5, 6]
    n = 6 
    total_sum = n * (n + 1) / 2
    res = total_sum - sum(data)
    return int(res)


if __name__ == "__main__":
    result = find_missing_number()
    print(result)
