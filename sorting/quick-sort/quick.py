# /usr/bin/python
# A program to do quick sort using separate list

def quick_sort(inp):
    ''' Quick sort function '''
    lesser = []
    greater = []

    if len(inp) <= 1:
        return inp

    for i in inp[1:]: 
        # 0th element in the list is always the pivot element
        if i < inp[0]:  # if the current element is less than pivot
            lesser.append(i) # Added to the lesser list
        else:          # if the current element is greater than pivot
            greater.append(i) # Added to greater list

    print "While sorting: ", lesser , inp[0:1] , greater
    # Lesser list is again called in depth first manner, greater and pivot elements
    # will be cached in the stack. Once it reaches a single element in lesser list
    # the quick_sort(greater) will be called
    return quick_sort(lesser) + inp[0:1] + quick_sort(greater)

if __name__ =="__main__":
    '''Main function'''

    inp =[]
    s = int(raw_input('How many elements would you like to enter: '))
    for x in range(s):
        inp.append(int(raw_input('Enter element #' + `x+1` + ': ')))
    print "Initial list: ", inp
    output_list = quick_sort(inp)
    print "output list: ", output_list
