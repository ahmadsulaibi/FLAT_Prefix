# Implement Prefix algorithm
# Example: * 2 + 3 4

def main():
    inp = input("Input your equation: ")
    print("-"*20,end=" Solving ")
    print("-"*20)
    arr = inp.split()
    sum = 0

    count = 0

    while count < len(arr):
        if arr[count] == '+' or arr[count] == '-' or arr[count] == '/' or arr[count] == '*' or arr[count] == '**' or\
                arr[count] == "//" or arr[count] == "%":
            count += 1

        if arr[count] == '+' or arr[count] == '-' or arr[count] == '/' or arr[count] == '*' or\
                arr[count] == '**' or arr[count] == "//" or arr[count] == "%":
            print("The system can not accept two operators next to each other!")
            print("Your input must be a prefix (starting with an operator), as an example:")
            print("* 2 + 3 4")
            print("Please fix it!")
            exit()

        if int(arr[count]):
            break
        else:
            a = " ".join(arr)
            print("Your input must be a prefix (starting with an operator), as an example:")
            print("* 2 + 3 4")
            print(f"What you wrote is {a}, which starts with an operand {arr[count]}.")
            print("Please fix it!")
            exit()

    arr.reverse()

    count = 0
    while count < len(arr):
        if arr[count] == '+':
            if float(arr[count-1]) and float(arr[count - 2]):
                second = float(arr[count - 1]) # <second element>
                last = float(arr[count - 2]) # <last element>
                sum = second + last
                print(f"{arr[count]} "
                      f"{arr[count - 1]} "
                      f"{arr[count - 2]} "
                      f"= {sum}")

                arr.remove(arr[count])
                arr.remove(arr[count - 1])
                arr.remove(arr[count - 2])

                count = 0
                arr.insert(count, str(sum))

                print("My new List", end=": ")
                print(" ".join(arr[::-1]))

                continue

        if arr[count] == '-':
            if float(arr[count -1]) and float(arr[count - 2]):
                second = float(arr[count - 1])  # <second element>
                last = float(arr[count - 2])  # <last element>
                sum = second - last

                print(f"{arr[count]} "
                      f"{arr[count - 1]} "
                      f"{arr[count - 2]} "
                      f"= {sum}")

                arr.remove(arr[count])
                arr.remove(arr[count - 1])
                arr.remove(arr[count - 2])

                count = 0
                arr.insert(count, str(sum))
                print("My new List", end=": ")
                print(" ".join(arr[::-1]))

                continue

        if arr[count] == '*':
            if float(arr[count -1]) and float(arr[count - 2]):
                second = float(arr[count - 1])  # <second element>
                last = float(arr[count - 2])  # <last element>
                sum = second * last

                print(f"{arr[count]} "
                      f"{arr[count - 1]} "
                      f"{arr[count - 2]} "
                      f"= {sum}")

                arr.remove(arr[count])
                arr.remove(arr[count - 1])
                arr.remove(arr[count - 2])

                count = 0
                arr.insert(count, str(sum))

                print("My new List", end=": ")
                print(" ".join(arr[::-1]))

                continue

        if arr[count] == '/':
            if float(arr[count -1]) and float(arr[count - 2]):
                second = float(arr[count - 1])  # <second element>
                last = float(arr[count - 2])  # <last element>
                sum = second / last

                print(f"{arr[count]} "
                      f"{arr[count - 1]} "
                      f"{arr[count - 2]} "
                      f"= {sum}")

                arr.remove(arr[count])
                arr.remove(arr[count - 1])
                arr.remove(arr[count - 2])

                count = 0
                arr.insert(count, str(sum))

                print("My new List", end=": ")
                print(" ".join(arr[::-1]))

                continue

        if arr[count] == '**':
            if float(arr[count -1]) and float(arr[count - 2]):
                second = float(arr[count - 1])  # <second element>
                last = float(arr[count - 2])  # <last element>
                sum = second ** last

                print(f"{arr[count]} "
                      f"{arr[count - 1]} "
                      f"{arr[count - 2]} "
                      f"= {sum}")

                arr.remove(arr[count])
                arr.remove(arr[count - 1])
                arr.remove(arr[count - 2])

                count = 0
                arr.insert(count, str(sum))

                print("My new List", end=": ")
                print(" ".join(arr[::-1]))

                continue

        if arr[count] == '//':
            if float(arr[count -1]) and float(arr[count - 2]):
                second = float(arr[count - 1])  # <second element>
                last = float(arr[count - 2])  # <last element>
                sum = second // last

                print(f"{arr[count]} "
                      f"{arr[count - 1]} "
                      f"{arr[count - 2]} "
                      f"= {sum}")

                arr.remove(arr[count])
                arr.remove(arr[count - 1])
                arr.remove(arr[count - 2])

                count = 0
                arr.insert(count, str(sum))

                print("My new List", end=": ")
                print(" ".join(arr[::-1]))

                continue

        if arr[count] == '%':
            if float(arr[count -1]) and float(arr[count - 2]):
                second = float(arr[count - 1])  # <second element>
                last = float(arr[count - 2])  # <last element>
                sum = second % last

                print(f"{arr[count]} "
                      f"{arr[count - 1]} "
                      f"{arr[count - 2]} "
                      f"= {sum}")

                arr.remove(arr[count])
                arr.remove(arr[count - 1])
                arr.remove(arr[count - 2])

                count = 0
                arr.insert(count, str(sum))

                print("My new List", end=": ")
                print(" ".join(arr[::-1]))

                continue

        count += 1

    print("-"*20, end=" Solution ")
    print("-"*20)
    print(f"The solution to your prefix is: {sum}")
if __name__ == '__main__':
    main()


# Important
# d = {}
# m = ['a','b','c','d']
#
# for i in range(len(m) - 1):
#     d[m[i]] = (m[i],)
#
# for i in sorted(d.keys()):
#     k = d[i]
#     print(k[0])

# d = {'one':'two','three':'one', 'two': 'three'}
# v = d['three']
#
# for k in range(len(d)):
#     v = d[v]
#
# print(v)

# lst = [[x for x in range(3)] for y in range(3)]
#
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print(f"{r} {c}: #")

# d = {}
# d['1'] = (1,2) # position 1
# d['2'] = (2,1) # position 1
#
# for x in d.keys():
#     print(d[x][1])

# m = [x*x for x in range(5)]
#
# print(m[2])
# print(m[m[2]])
#
# def fun(l):
#     del l[l[2]]
#     return l
#
# print(fun(m))