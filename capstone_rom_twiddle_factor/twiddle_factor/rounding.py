import numpy as np
import math

def q_truncate(din_ptr,b_sign,b_int,b_fr):
    if(b_sign==0):
        if(din_ptr<0):
            print("**************** Rounding : Truncate overflow 1 ******************\n")

    max_abs=math.pow(2,b_int)-1
    for i in range(b_fr):
        max_abs+=math.pow(2,i*(-1)-1)
    
    din_sign = 1 if din_ptr > 0 else -1

    din_abs = math.fabs(din_ptr)

    if(din_abs > max_abs):
        print("**************** Rounding : Truncate overflow 2 ******************\n")
        print("din = {0}, max_abs = {1} .... clipping \n".format(din_ptr, max_abs))
        din_abs = max_abs

    din_ext = int(din_abs * math.pow(2,b_fr))

    din_ptr = 0

    for i in range(b_int+b_fr):
        if((din_ext & 0x1)==0x1):
            din_ptr+=math.pow(2,(b_fr*(-1))+i)
        din_ext = din_ext>>1
    
    if(b_sign == 1):
        din_ptr = din_ptr*din_sign
    
    return din_ptr