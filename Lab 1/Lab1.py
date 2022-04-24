keywords=['int', 'float', 'if', 'else']
math_operators=['+', '-', '=']
logical_operators=['>']
numerical_values=['0','1','2','3','4','5','6','7','8','9']
others=[',',';','(',')','{','}']


#reading file

file = open("D:\Downloads\Spring  2022\Spring 2022 submissions\CSE420\CSE420 Lab\Lab 1\input.txt")
lines_List = file.read().split()
file.close()


#output lists

keyword_outputs=[]
math_operator_outputs=[]
logical_operator_outputs=[]
numerical_outputs=[]
identifier_outputs=[]
other_outputs=[]


for i   in  range(len(lines_List)):
    
    #if keyword

    if  lines_List[i]   in keywords:
        if  lines_List[i]   not in  keyword_outputs:
            keyword_outputs.append(lines_List[i])
    
    #if math operator

    elif    lines_List[i]   in math_operators:
        if  lines_List[i]   not in  math_operator_outputs:
            math_operator_outputs.append(lines_List[i])

    #if logical operator
    
    elif    lines_List[i]   in logical_operators:
        if  lines_List[i]   not in  logical_operator_outputs:
            logical_operator_outputs.append(lines_List[i])
    
    #if other operator
    
    elif    lines_List[i][-1]   in others:

        if  lines_List[i][-1]   not in  other_outputs:
            other_outputs.append(lines_List[i][-1])
        
        if  len(lines_List[i])>1:

            #if numerical_values
            if  lines_List[i][0] in   numerical_values:

                if  lines_List[i][0:-1] not in  numerical_outputs:
                    numerical_outputs.append(lines_List[i][0:-1])
            
            #else it's identifier
            else:

                if  lines_List[i][0:-1] not in  identifier_outputs:
                    identifier_outputs.append(lines_List[i][0:-1])


print("Keywords: ", end = '')
print(*keyword_outputs, sep = ", ")

print("Identifiers: ", end = '')
print(*identifier_outputs, sep = ", ")

print("Math Operators: ", end = '')
print(*math_operator_outputs, sep = ", ")

print("Logical Operators: ", end = '')
print(*logical_operator_outputs, sep = " ")

print("Numerical Values: ", end = ''),
print(*numerical_outputs, sep = ", ")

print("Others: ", end = '')
print(*other_outputs, sep = " ")