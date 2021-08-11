

# Excercise_1
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggieSize(array):
    for item in array:
        if item > 0:
            array[array.index(item)] = "big"
    return array


print(biggieSize([-1, 3, 5, -5])) #should return [-1,"big","big",-5]

# Excercise_2
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def countPositives(array):
    positiveNumbers = 0
    for i in range(len(array)):
        if array[i]>0:
            positiveNumbers +=1
    array[len(array)-1]=positiveNumbers
    return array

print(countPositives([-1,1,1,1])) #should return [-1,1,1,3]
print(countPositives([1,6,-4,-2,-7,-2])) #should return [-1,6,-4,-2,-7,2]

# Excercise_3
# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10

def sumTotal(array):
    zum = 0
    for i in range(len(array)):
        zum=zum+array[i]
    return zum

print(sumTotal([1,2,3,4])) #should return 10

# Excercise_4
# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(array):
    zum = 0
    avg = 0
    for i in range(len(array)):
        zum=zum+array[i]
    avg = zum/len(array)
    return avg

print(average([1,2,3,4])) #should return 2.5


# Excercise_5
# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(array):
    counter = 0
    for item in array:
        counter +=1
    return counter

print(length([37,2,1,-9])) #should return 4


# Excercise_6
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def Minimum(array):
    
    if len(array)==0:
        return False
    else:
        min = array[0]
        for item in array:
            if item<min:
                min=item
        return min

print(Minimum([37,2,1,-9])) #should return -9
print(Minimum([])) #should return false

# Excercise_7
# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def Maximum(array):
    
    if len(array)==0:
        return False
    else:
        max = array[0]
        for item in array:
            if item>max:
                max=item
        return max

print(Maximum([37,2,1,-9])) #should return 37
print(Maximum([])) #should return false

# Excercise_8
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimateAnalysis(array):
    
    if len(array)==0:
        return False
    else:
        max = array[0]
        min = array[0]
        leng = len(array)
        zum = 0
        for item in array:
            if item>max:
                max=item
            if item<min:
                min=item
            zum+=item
        avg = zum/leng

        return {'sumTotal': zum, 'average': avg, 'minimum': min, 'maximum': max, 'length': leng }
        
print(ultimateAnalysis([37,2,1,-9])) #should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

print(ultimateAnalysis([])) #should return false

# Excercise_9
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverseList(array):
    # We use mathematical operations for reversing the array (avoid the use of a temporary variable or array). The algorothim consists in three steps for doing the swap operation:
    #1) a = a+b
    #2) b = a-b
    #3) a = a-b

    # the above algorithm is run to the half of the array
    half_length = int(len(array)/2) #range method only accepts integers (not floats)
    for i in range(half_length):
         if i != (len(array)-i-1): #the formula does no work when a and b are the same item.
            array[i]=array[i]+array[len(array)-i-1]
            array[len(array)-i-1]=array[i]-array[len(array)-i-1]
            array[i]=array[i]-array[len(array)-i-1]
    return array
        
print(reverseList([37,2,1,-9])) #should return [-9,1,2,37]