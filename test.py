

original_list =  [11,45,8,11,23,45,23,45,89]
def CountFrequency(my_list):
    # Creating an empty dictionary
    count = {}
    for i in original_list:
        count[i] = count.get(i, 0) + 1
    return count
# Driver function
if __name__ == "__main__":
    my_list = original_list
    print(CountFrequency(my_list))
'''
import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)
sorted_array_row = sampleArray[:, sampleArray[1].argsort()]
print(sorted_array_row)
coloum_index = 1
sorted_array_coloumn = sampleArray[sampleArray[:,coloum_index].argsort()]
print(sorted_array_coloumn)
'''