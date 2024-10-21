# # Create set using curlybrace
# My_set={1,2,3,4,5}
# # check type of set
# print(type(My_set))
# # show result 
# print(My_set)
# # create set using set constructor
# my_set={1,2,3,4,5,5,1,2,3}
# print(my_set)
# # can't change but we can add it
# my_set={"Dragon","Dragon fly"}
# my_set.add("Bird")
# print(my_set)

# m_set={3,4,5,6,7}
# print(f"My set before remove={m_set}")
# m_set.remove(5)
# # or m_set.discard
# print(f"My set after removed={m_set}")

# item={1,2,3,4,5,6}
# removed_item=item.pop()
# # union use for combine set1 n set2 to one
# # or(|)=union
# set1={1,2,3,4}
# set2={4,5,6,7,8}
# result=set1.union(set2) 
# # or result=set1 |set2
# print(result)

set1={1,2,3,4,5,6}
set2={3,4,5,6,7,7}
result=set1.intersection(set2)
# we use and(&) with intersection
# or result=set1 &set2
print(result)

# set1={1,2,3,4,5,5}
# set2={3,4,5,6,7,8,9}
# result=set1.symmetric_difference(set2)
# print(result)
# we use sym_diff to delet number that have the same
# or we can use one more is we use this (^) symbol


# list1=[1,2,3,4,5,6,4,6,7]
# my_list=list(set[list])
# print(my_list)

# list1=[1,2,3,4,5,6]
# list2=[2,3,4,7,6]
# My_list=list(set(list1)  | set(list2))
# print(My_list)




