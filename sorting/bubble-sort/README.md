Bubble sort
===========

Bubble sort works by repeatedly stepping through the list to be sorted, comparing 
each pair of adjacent items and swapping them if they are in the wrong order. The 
pass through the list is repeated until no swaps are needed, which indicates that 
the list is sorted. It only uses comparisons to operate on elements, it is a 
comparison sort.

Example
-------

Input list: [8, 7, 5, 4, 3, 2, 1]


[*8*, *7*, 5, 4, 3, 2, 1]

[7, *8*, *5*, 4, 3, 2, 1]

[7, 5, *8*, *4*, 3, 2, 1]

[7, 5, 4, *8*, *3*, 2, 1]

[7, 5, 4, 3, *8*, *2*, 1]

[7, 5, 4, 3, 2, *8*, *1*]

[*7*, *5*, 4, 3, 2, 1, **8**]

[5, *7*, *4*, 3, 2, 1, **8**]

[5, 4, *7*, *3*, 2, 1, **8**]

[5, 4, 3, *7*, *2*, 1, **8**]

[5, 4, 3, 2, *7*, *1*, **8**]

[*5*, *4*, 3, 2, 1, **7**, **8**]

[4, *5*, *3*, 2, 1, **7**, **8**]

[4, 3, *5*, *2*, 1, **7**, **8**]

[4, 3, 2, *5*, *1*, **7**, **8**]

[*4*, *3*, 2, 1, **5**, **7**, **8**]

[3, *4*, *2*, 1, **5**, **7**, **8**]

[3, 2, *4*, *1*, **5**, **7**, **8**]


[*3*, *2*, 1, **4**, **5**, **7**, **8**]

[2, *3*, *1*, **4**, **5**, **7**, **8**]

[*2*, *1*, **3**, **4**, **5**, **7**, **8**]

[*1*, **2**, **3**, **4**, **5**, **7**, **8**]


Sorted list:  [**1**, **2**, **3**, **4**, **5**, **7, **8**]

