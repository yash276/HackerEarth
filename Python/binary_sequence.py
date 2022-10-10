if __name__ == "__main__":
    # input number of test cases
    test_cases = int(input())
    # get the values of x,y,a,b, for each test case
    # try to find the desired binary sequence for each test case and print the result.
    for test_case in range(0,test_cases):
        input_str=input()
        x = int(input_str.split(" ")[0])
        y = int(input_str.split(" ")[1])
        a = int(input_str.split(" ")[2])
        b = int(input_str.split(" ")[3])
        if x * y == a + b:
            print("Yes")
        else:
            print("No")