# /usr/bin/python

def insertion_sort(inp_list):
    "This function is to sort the given input elements"

    for i in range(1, len(inp_list)):
        valueToInsert=inp_list[i]
        holePos=i
        while holePos > 0 and valueToInsert < inp_list[holePos - 1]:
            inp_list[holePos] = inp_list[holePos - 1]
            holePos = holePos -1
        inp_list[holePos] = valueToInsert
        print "While sorting: ", inp_list
    return inp_list

def main():
    "Main function"
    inp =[]
    s = int(raw_input('How many elements would you like to enter: '))
    for x in range(s):
        inp.append(int(raw_input('Enter element #' + `x+1` + ': ')))
    print "Initial list: ", inp
    output_list = insertion_sort(inp) 
    print "Sorted list: ", output_list

if __name__ == "__main__":
    main()


