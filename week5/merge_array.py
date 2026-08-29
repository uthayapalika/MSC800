dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
merged_dict={**dict1,**dict2}
#print(merged_dict)


dict3={'a':1,'b':2,'c':3}
dict4={'a':1,'b':2,'c':3}

merged_dict={**{k:v for k,v in dict3.items() if k in 'aeiou'},
            **{k:v for k,v in dict4.items() if k in 'aeiou'}}

#print(merged_dict)

Key1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
Value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]

Key2 = ['u', 'b', 'o', 'x', 'e', 'a']
Value2 = [200, 30, 10, 88, 55, 920]

merged_dict = {
    **{k: v for k, v in zip(Key1, Value1) if v % 2 != 0},
    **{k: v for k, v in zip(Key2, Value2) if v % 2 != 0}
}

print(merged_dict)