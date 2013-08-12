# /usr/bin/python
# A program to do quick sort using inplace algo

def partition(inp, start, end):
    ''' A function which does partition '''
    
    pivot = inp[end]
    bottom = start - 1
    top = end
    
    done = 0
    while not done:
        while not done:
            bottom = bottom + 1
            if bottom == top:
                done = 1
                break
            if inp[bottom] > pivot:
                inp[top] = inp[bottom]
                break

        while not done:
            top = top - 1
            if top == bottom:
                done = 1
                break
            if inp[top] < pivot:
                inp[bottom] = inp[top]
                break
    print "While sorting: " , inp
    inp[top] = pivot
    return top

def quick_sort(inp, start, end):
    ''' Quick sort function '''
    if start < end:
        split = partition (inp, start, end)
        quick_sort(inp, start, split - 1)
        quick_sort(inp, split + 1, end)
    else:
        return

if __name__ == "__main__":
    ''' Main function '''

    inp = []
    s = int(raw_input('How many elements would you like to enter: '))
    for x in range(s):
            inp.append(int(raw_input('Enter element #' + `x+1` + ': ')))

    print "Initial list: ", inp
    start = 0
    end = len(inp) - 1
    quick_sort(inp, start, end)        
    import string
    print string.join(map(str, inp))

    
