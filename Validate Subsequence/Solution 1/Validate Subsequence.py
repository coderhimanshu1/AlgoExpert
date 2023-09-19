 # def(array1, array2):


#   input: non-empty arrays
#   output: boolean: true/ false


#   is array2 subsequence of array1?
    #        p1
#  array [1, 2, 3, 4]
    #        p2
#  sequence [1,  3,  4]


#  edge cases:
#  - any multiple occurrences?
#  - will it always be sorted?
#  - will array2 length always be smaller than array 1 length?




  
def isValidSubsequence(array, sequence):
    
    # Check if the length of the array or sequence is 0 and return false
    if len(array) == 0 or len(sequence) == 0:
        return False
    
    # Check if length of sequence is greater than length of array and return false
    if len(array) < len(sequence):
        return False
  
    # Set pointers to 0
    arrIdx = 0
    seqIdx = 0
  
    # Loop over subsequence
    while arrIdx < len(array) and seqIdx < len(sequence):
        # If sequence[pointer2] == array[pointer1] then increment pointer2
        if array[arrIdx] == sequence[seqIdx]: 