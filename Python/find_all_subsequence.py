import itertools
from operator import index 

def find_subsquence(string: str, subsequence: str, occurence: int)->bool:
    """_summary_

    Args:
        string (str): _description_
        subsequence (str): _description_
        occurence (int): _description_

    Returns:
        bool: _description_
    """
    # assume there are no such sequences available
    output = False
    # create an index tracker to track the indexes of the elements in the subsequence as found in the string
    # the length of this tracker will also be used to count the number of oocurences of subsequence in the string
    index_tracker = []
    # deifine intial values for some variables
    sub_index = 0  # variable to indx in the subsequence
    str_index = 0 # variable to index in the input string
    index = '' # string to keep track of the indces in the string where we found an element from the subsequence
    
    # run a loop until the end to the input string
    while str_index < len(string):
        # if we found a matching element in the string from the given subsequence
        if string[str_index] == subsequence[sub_index]:
            # convert the string index and add it to the index variable for tracking
            index = index + str(str_index)
            # increase the sub index by 1 so that next we can match next character from subsequence
            sub_index = sub_index + 1
            # store the string index of last found element
            last_found_index = str_index
            # if the length of the index string is equal to the subsequence string, it means we have found the subseqence in the string
            # The index where all the elements of the subseqenqce where found in the input string is stored in the index variable
            if len(index) == len(subsequence):
                # if these pair of incdexes are not already present in the index list, then add them
                if index not in index_tracker:
                    index_tracker.append(index)
                    index = index[:-1]
                    str_index = last_found_index
                    sub_index = sub_index - 1
                else:
                    index = index[:-1]
            else:
                print("what to do")
                
        else:
            print("what to do")
                
    
    
    if len(index_tracker) == occurence:
        output = True
                
    return output

def find_sequence(x: int, y: int, a: int, b: int)->str:
    # assume there are no such sequences available
    output = 'No'
    # total number of zero's in the binary sequence
    no_of_zeros = '0' * x
    # total number of ones's in the binary sequence
    no_of_ones = '1' * y 
    # create a single string from the total number of zero's and one's
    binary_string = no_of_zeros + no_of_ones
    # get all the combimations of binary string from this single string
    permutaions = list(itertools.permutations(list(binary_string)))  
    binary_string = sorted([''.join(permutation) for permutation in permutaions])
    # to get the unique values from the binary string list
    # convert the list to set 
    # then convert that set back to list
    tmp_set = set(binary_string)
    binary_string = list(tmp_set)
    # run the loop over all the strings.
    #  if we are able to find the subsequences then change the value of output to Yes and break
    for string in binary_string:
        if find_subsquence(string, "01", a) and find_subsquence(string, "10", b):
            output = 'Yes'
            break  
    return output
    

if __name__ == "__main__":
    # input number of test cases
    test_cases = int(input())
    # get the values of x,y,a,b, for each test case
    # try to find the desired binary sequence for each test case and print the result.
    for test_case in range(0,test_cases):
        x =int(input())
        y =int(input())
        a =int(input())
        b =int(input())
        if x * y == a + b:
            print("Yes")
        else:
            print("No")
        # output = find_sequence(x, y, a, b)
        # print(output)
    # string = "100110010100"
    # subsquence = "10"
    # occurence = 3
    # print(find_subsquence(string,subsquence,occurence))