
N = int(input())
Array = []


inputs = input()


for num in inputs.split():
    Array.append(int(num))

count = 0



i = 0
while True:

    if Array[i] % 2 == 0:
        Array[i] = int(Array[i] / 2)
    else:
        break

    if i == N - 1:
        i = 0
        count += 1
    else:
        i += 1


print(count)

# for i in range(N):
#     # print(Array[i])
#     if Array[i] % 2 == 0:
#        
#         Array[i] = int(Array[i] / 2)
#         count += 1

"""
4
6 2 4 1

3
8 12 40

"""

