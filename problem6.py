# Find multiple missing numbers in a given integer array with duplicates?
# example = [4,3,2,7,8,2,3,1]
# output = 5, 6
def find_missing(data):
    test = []
    for i in range(1, len(data) + 1):
        if i not in data:
            test.append(i)
    return test


if __name__ == "__main__":
    data = [4, 3, 2, 7, 8, 2, 3, 1]
    res = find_missing(data)
    print(res)
