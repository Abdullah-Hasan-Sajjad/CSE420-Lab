import re

# TAKING RE INPUT

re_amount=int(input())
re_list=[]

for i in  range(re_amount):
  re_list.append(input())


# TAKING STRINGS INPUT

string_amount=int(input())
string_list=[[]]

for i in  range(string_amount):
  string_list[i].append(input())

  if (i < string_amount-1):
    string_list.append([])


for i in  range(string_amount):
  
  for j in  range(re_amount):

    if  re.match(re_list[j], string_list[i][0]):
      string_list[i].append(j+1)


# Output

for i in  range(len(string_list)):

  if  len(string_list[i]) > 1:
    print("yes, ",string_list[i][1:])
  
  else:
    print("NO, 0")