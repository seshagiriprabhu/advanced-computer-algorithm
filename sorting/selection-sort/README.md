Selection sort
==============
The algorithm divides the input list into two parts: the sublist of items already 
sorted, which is built up from left to right at the front (left) of the list, and 
the sublist of items remaining to be sorted that occupy the rest of the list. 
Initially, the sorted sublist is empty and the unsorted sublist is the entire 
input list. The algorithm proceeds by finding the smallest (or largest, depending 
on sorting order) element in the unsorted sublist, exchanging it with the 
leftmost unsorted element (putting it in sorted order), and moving the sublist 
boundaries one element to the right.

Here is an example of this sort algorithm sorting eight elements:
Initial list:   [8, 7, 6, 5, 4, 3, 2, *1*]
While Sorting:  [**1**, 7, 6, 5, 4, 3, *2*, 8]
While Sorting:  [**1**, **2**, 6, 5, 4, *3*, 7, 8]
While Sorting:  [**1**, **2**, **3**, 5, *4*, 6, 7, 8]
While Sorting:  [**1**, **2**, **3**, **4**, *5*, 6, 7, 8]
While Sorting:  [**1**, **2**, **3**, **4**, **5**, *6*, 7, 8]
While Sorting:  [**1**, **2**, **3**, **4**, **5**, **6**, *7*, 8]
While Sorting:  [**1**, **2**, **3**, **4**, **5**, **6**, **7**, *8*]
Sorted list:    [**1**, **2**, **3**, **4**, **5**, **6**, **7**, **8**]

