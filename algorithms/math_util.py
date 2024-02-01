def floor_to_ndp(number, dp):
    mul = 10 ** dp
    return ((number*mul)//1)/(mul)