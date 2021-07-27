# remove duplicate numbers from a given integer array?
def find_unique_list():
    data = [1, 2, 4, 4, 6, 6, 5]
    test = []
    for i in data:
        if i not in test:
            test.append(i)
    return test


if __name__ == "__main__":
    result = find_unique_list()
    print(result)
