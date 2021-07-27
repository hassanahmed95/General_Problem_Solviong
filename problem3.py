# find duplicate numbers from a given integer array?
def find_duplicate_number():
    data = [1, 2, 4, 4, 6, 6, 5]
    test = []

    for i in range(0, len(data)):
        # print(data[i])
        for j in range(1, len(data)):
            print(data[j])
            if i == j:
                # if i not in test:
                test.append(data[i])
    return test


find_duplicate_number()
# print(res)
# if __name__ == "__main__":
#     result = find_duplicate_number()
#     print(result)
