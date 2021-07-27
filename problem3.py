# find duplicate numbers from a given integer array
# solving problem using brute force approach
def find_duplicate_number(data):
    test = []
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                test.append(data[i])
    return list(set(test))


if __name__ == "__main__":
    testing_data = [3, 4, 1, 4, 1, 1]
    result = find_duplicate_number(testing_data)
    print(result)
