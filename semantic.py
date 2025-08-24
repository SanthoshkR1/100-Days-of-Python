# # insertion sort
# def ins_sort(arr):
#     for i in range(1, len(arr)):
#         curr = arr[i]
#         j = i - 1
#         while j >= 0 and curr < arr[j]:
#             arr[j + 1] = arr[j]
#             j = j - 1
#         arr[j + 1] = curr
#     return arr

# arr = [40, 60, 30, 70, 20, 10, 120]
# print(ins_sort(arr))
# def sel_sort(arr):
#     for i in range(len(arr)):
#         s = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[s]:
#                 s = j
#         arr[i], arr[s] = arr[s], arr[i]
#     return arr

# arr = [40, 60, 30, 70, 20]
# print(sel_sort(arr))

# def bub_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr) - 1):
#             if arr[j + 1] < arr[j]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# arr = [40, 60, 30, 70, 20, 10]
# print(bub_sort(arr))
#

#returning two variables 
def fun():
    str ="mrcet college"
    x = 20
    return str,x;
str, x=fun()
print(str)
print(x)