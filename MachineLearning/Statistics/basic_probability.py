if __name__ == "__main__":
    # read the first input
    # probability of mike taking bus
    p_m_b = float(input())
    # read the second input
    # probability of alice taking bus
    p_a_b = float(input())
    # read the third input
    # probability of raining
    p_r = float(input())
    # output
    # probability of mike and alice meeting on lake in rain
    p_r_s = p_r * ( p_a_b + p_m_b - 2 * p_a_b * p_m_b )
    print(format(p_r_s, '.6f'))