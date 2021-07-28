# The largest and smallest number in an unsorted integer array?
# firstly sort the array
def find_small(data):
    test = []
    while data:
        min_num = data[0]
        for i in range(0, len(data)):
            if data[i] < min_num:
                min_num = data[i]
        test.append(min_num)
        data.remove(min_num)
    return test[0]


if __name__ == "__main__":
    testing_data = [1, 6, 2, 3, 9, -5]
    result = find_small(testing_data)
    print(result)
