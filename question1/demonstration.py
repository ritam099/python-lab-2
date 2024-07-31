import module_ListFunction
demolist = [(x**2) for x in range(1, 7)]
print("original list : ", demolist)
print("max of list is : ", module_ListFunction.list_max(demolist))
print("minimum of list is : ", module_ListFunction.list_min(demolist))
print("sum of the list is : ", module_ListFunction.list_sum(demolist))
print("average of the list is : ", module_ListFunction.list_average(demolist))
print("median of the list is : ", module_ListFunction.list_median(demolist))