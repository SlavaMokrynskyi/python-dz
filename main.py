nums = [2,6,8,4]
nums2 = [2,6,8,4,5,3]
def showProduct(list):
    num = 1
    for i in list:
        num = num * i
    print(num)

showProduct(nums)

def findMin(list):
    min = 0
    for i in list:
        if min == 0 and i != 0:
            min = i
        if i < min:
            min = i
    return min

print(findMin(nums))

def is_prime(list):
    for i in list:
        if i != 2 and i % 2 != 0:
            if i != 3 and i % 3 !=0:
                return i
        elif i % i == 0:
            return i
            
print(is_prime(nums))

def delete_num(list):
    delete_num = int(input("Enter num which delete --> "))
    count = 0
    for i in list:
        if delete_num in list:
            list.remove(delete_num)
            count += 1
    return count

print(delete_num(nums))

def getList(list_1,list_2):
    result = list(set(list_1 + list_2))
    return result

print(getList(nums,nums2))

def calculateList(degree,list):
    calculatedList = []
    num = 0
    for i in list:
        num = i ** degree
        calculatedList.append(num)
    return calculatedList

print(calculateList(2,nums))

        
