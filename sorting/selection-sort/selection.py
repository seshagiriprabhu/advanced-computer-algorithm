# /usr/bin/python
# A program to do selection sort

def selection_sort(inp_list):
    '''The selection sort function'''

    for i in range (len(inp_list)):
        iMin = i
        for j in range(i+1, len(inp_list)):
            if inp_list[j] < inp_list[iMin]:
                iMin = j

        if iMin != i:
            temp = inp_list[i]
            inp_list[i] = inp_list[iMin]
            inp_list[iMin] = temp
        print "While Sorting: ", inp_list
    return inp_list
            
def main():
    '''Main function'''

    inp =[]
    s = int(raw_input('How many elements would you like to enter: '))
    for x in range(s):
        inp.append(int(raw_input('Enter element #' + `x+1` + ': ')))
    print "Initial list: ", inp
    output_list = selection_sort(inp) 
    print "Sorted list: ", output_list

if __name__ == "__main__":
    main()
