if __name__ == "__main__":
    # read the first input
    # probability of car trouble
    p_c_t = float(input())
    # read the second input
    # probability of reaching office on time
    p_o_t = float(input())
    # read the third input
    # number of available trains
    n = int(input())
    
    p = ( p_o_t * (1 - p_c_t) ) + ( p_c_t * (2/n) )
    print(format(p,".6f"))