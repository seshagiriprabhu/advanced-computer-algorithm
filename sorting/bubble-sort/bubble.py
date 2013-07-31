# /usr/bin/python
# A program to do bubble sort

def bubble_sort(inp_list):
    '''Bubble sort function'''

    j = len(inp_list)-1
    while j != 0:
        for k in range(j):
            if inp_list[k] > inp_list[k+1]:
                temp = inp_list[k]
                inp_list[k] = inp_list[k+1]
                inp_list[k+1] = temp
            print "while sorting", inp_list
        j = j - 1
    return inp_list

def main():
    '''Main function'''

    inp =[]
    s = int(raw_input('How many elements would you like to enter: '))
    for x in range(s):
        inp.append(int(raw_input('Enter element #' + `x+1` + ': ')))
    print "Initial list: ", inp
    output_list = bubble_sort(inp) 
    print "Sorted list: ", output_list

if __name__ == "__main__":
    main()

