
def list_max(inlist):
    
    max_value = inlist[0]
    for num in inlist:
        if num > max_value:
            max_value = num
    return max_value

def list_min(inlist):
    
    min_value = inlist[0]
    for num in inlist:
        if num < min_value:
            min_value = num
    return min_value

def list_sum(inlist):
    sum = 0
    for i in inlist:
        sum+=i
    return sum; 

def list_average(inlist):
    
    if not inlist:
        raise ValueError("List is empty")
    return list_sum(inlist) / len(inlist)

def list_median(inlist):
    inlist = sorted(inlist)
    if (len(inlist)%2==0):
        return ((inlist[len(inlist)//2]+inlist[(len(inlist)//2) - 1])/2)
    else:
        return inlist[len(inlist)//2]