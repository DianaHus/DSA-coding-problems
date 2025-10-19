'''
You are required to construct a Python function titled minimal_max_block(). 
This function should accept an array as an input and compute an intriguing 
property related to contiguous blocks within the array.

More specifically, you must select a particular integer, k, from the array. 
Once you've selected k, the function should remove all occurrences of 'k' from the array, 
thereby splitting it into several contiguous blocks, or remaining sub-arrays. 
A unique feature of k is that it is chosen such that the maximum length among these blocks is minimized.

For instance, consider the array [1, 2, 2, 3, 1, 4, 4, 4, 1, 2, 5]. 
If we eliminate all instances of 2 (our k), the remaining blocks would be [1], [3, 1, 4, 4, 4, 1], [5],
with the longest containing 6 elements. 
Now, if we instead remove all instances of 1, the new remaining blocks would be 
[2, 2, 3], [4, 4, 4], [2, 5], the longest of which contains 3 elements. As such, 
the function should return 1 in this case, as it leads to a minimal maximum block length
'''

def minimal_max_block(arr):
    last_occurrance = {}
    max_block_size = {}
    for i in range(len(arr)):
        new_max_block_size = i
        if last_occurrance.get(arr[i]) is not None:
            new_max_block_size = (i - last_occurrance[arr[i]] - 1)
        if max_block_size.get(arr[i]):
            if new_max_block_size > max_block_size[arr[i]]:
                max_block_size[arr[i]] = new_max_block_size
        else:
            max_block_size[arr[i]] = new_max_block_size
        last_occurrance[arr[i]] = i
    final = min(max_block_size, key=max_block_size.get)
    return final

print(minimal_max_block([1, 2, 2, 3, 1, 4, 4, 4, 1, 2, 5]))