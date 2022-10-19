if __name__=="__main__":
    # read the input
    # probability that alice will drop her phone
    p = float(input())
    e_x = p/(1-p)**2
    print(format(e_x,'.6f'))