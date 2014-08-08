__author__ = 'ddsnowboard'
arr = [1, 1]


def get(num):
    if len(arr) >= num:
        return arr[num-1]
    else:
        for j in range(len(arr), num):
            arr.append(arr[j-1]+arr[j-2])
        return arr[num-1]
while True:
    take = input("What number do you want to get?")
    if take.lower() == "stop":
        break
    else:
        print(get(int(take)))
print(len(arr))