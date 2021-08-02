# Find all missing numbers from a given sorted array
# example =  6, 7, 10, 11, 13
# output = 8,9,12
def find_multiple_missing(data):
    test = []
    start_index = data[0]
    end_index = data[len(data) - 1]
    for i in range(start_index, end_index + 1):
        if i not in data:
            test.append(i)
    return test


if __name__ == "__main__":
    testing_data = [6, 7, 10, 11, 13]
    res = find_multiple_missing(testing_data)
    print(res)
