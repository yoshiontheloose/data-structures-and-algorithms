# Merge Sort

This _divide and conquer_ algorithm divides an input array (or list for Python) in half, calls itself for the two halves, then merges the two sorted halves.

- Explanation found at [GeeksforGeeks.org](https://www.geeksforgeeks.org/merge-sort/)

## Pseudocode

```markdown
ALGORITHM Mergesort(arr)        # arr = [8,4,23,42,16,15]
    DECLARE n <-- arr.length        # n (length) = 6

    if n > 1
      DECLARE mid <-- n/2               # mid = 3
      DECLARE left <-- arr[0...mid]     # left = [0,1,2] / [8,4,23]
      DECLARE right <-- arr[mid...n]    # right = [3,4,5] / [42,16,15]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0         # these track left, right and entire array

    while i < left.length && j < right.length       # 0 < 3 && 0 < 3
        if left[i] <= right[j]          # if left[0] (8) <= right[0] (42)
            arr[k] <-- left[i]          # array at [k(0)]  will be reassigned to left[i(0)]
            i <-- i + 1                 # adds one to i (increments)
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

Sample list for given pseudocode to process:

`[8,4,23,42,16,15]`

---

"`Mergesort`" function takes in a list as an input (`arr`).

The length of our list is declared as a variable (`n`).

The function will then check if there is a list (`if n > 1`).

If a list is present, the statement assigns `middle`, `left`, and `right` variables.

The `middle` is found by dividing the list length by 2 (cutting the list in half).

The `left` is found by grabbing the list indexes from 0 - middle.

The `right` is found by grabbing the list indexes from the middle to the length of our list (`n`).

A new function named "`Merge`" is created that takes in an input of our new variables: `left` and `right`, and the list itself (`arr`).
This function will be where the Merge logic works it's magic to merge the list sides back together.

Three new variables are declared for the left, right, and array indexes. They are set at 0.

A while loop is then implemented. While left side's index (i) is less than the left _length_ of the list and right side's index (j) are less than the right _length_

An if statement in the while loop is created to check if the left's index (`left[i]`) is less than or equal to the right's index (`right[j]`)

- if this is true: the list index (`arr[k]`) is reassigned to the left index (`left[i]`). The left index (`[i]`) is then incremented.
- If this is false: the array's index (`arr[k]`) is reassigned to the right side's index (`right[j]`). The right index (`j`) is then incremented.

The list index (`k`) is incremented to move onto the next list index in the sequence.

Outside of the while loop, but still in the function, a new if statement is created.
This statement checks the index in the left side's list length. It sets the remaining indexes in the list to the remaining values in the right side.
Otherwise, it sets remaining indexes in the list to the remaining values in the left side.
