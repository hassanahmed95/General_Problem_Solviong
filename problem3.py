# find duplicate numbers from a given integer array
# solving problem using brute force approach
def find_duplicate_number(data):
    data = [3, 4, 1, 4, 1]
    test = []

    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            # print(data[j])
            if data[i] == data[j]:
                test.append(data[i])
    return list(set(test))


if __name__ == "__main__":
    result = find_duplicate_number()
    print(result)
