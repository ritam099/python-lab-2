import module_set 

setA= {5*x for x in range(5)}
setB={10*x for x in range(7)}

print(setA)
print(setB)

#a
print("set before adding : ", setA)
module_set.Element_add(setA,16)
print("set after adding : ", setA)


#b
print("set before removing : ", setA)
module_set.Element_remove(setA, 15)
print("set after removing : ", setA)

#c
setC = module_set.Set_union(setA, setB)
print(setC)

setEmpty = set()
setD = module_set.Set_union(setA, setEmpty)
print(setD)

setIntersection = module_set.Set_intersection(setA, setB)
print(setIntersection)

print(module_set.Set_intersection(setA, setEmpty))

#d
print(module_set.diffSet(setA,setB))

print(module_set.diffSet(setB, setA))


print(setA)
print(module_set.diffSet(setA, setEmpty))

print(module_set.diffSet(setEmpty, setA))

#e

print("set A is : ", setA)
print(module_set.checkSubset({0,5,10},setA))

print(module_set.checkSubset(set(),setA))


print("set A is : ", setA)
print("powerset of set A is : ", module_set.powerSet(setA))


print("set is : ", {1,2,3})
listOfSubsets = module_set.getAllSubsets({1,2,3})
print("the subsets are : ")
for i in listOfSubsets:
    print(i)





