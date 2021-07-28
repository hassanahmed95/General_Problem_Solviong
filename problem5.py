# Find all pairs of integer array whose sum is equal to a given number?
def find_pairs(data, summ):
    result = []
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == summ:
                result.append((data[i], data[j]))
    return result


if __name__ == "__main__":
    testing_data = [2, 5, 17, -1]
    # We are supposed to find all pairs, whose sum is equal to total_sum
    total_sum = 7
    res = find_pairs(testing_data, total_sum)
    print(res)
