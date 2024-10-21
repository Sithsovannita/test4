pt=[1001,202,3003,6006,404]
cpp=[202,100,804,502]
jv=[3003,202,101,303]
pt=set(pt)
cpp=set(cpp)
jv=set(jv)
# python class only
# pt_only=pt.difference(cpp)
# pt_only=pt.difference(jv)
# print(pt_only)
pt_only=list(pt.difference(cpp,jv))
cpp_only=list(cpp.difference(pt,jv))
java_only=list(jv.difference(pt,cpp))
print(pt_only)
print(cpp_only)
print(java_only)
# cpp class only
# cpp_only=cpp.difference(pt)
# cpp_only=cpp.difference(jv)
# print(cpp_only)
# java class only
# java_only=jv.difference(pt)
# java_only=jv.difference(cpp)
# print(java_only)
# python and cpp
result=pt.intersection(cpp)
print(result)
#cpp and java
result=cpp.intersection(jv)
print(result)
# java and python
result=jv.intersection(pt)
print(result)
