import  re
import  pandas  as  pd

#reading file

file=open("/content/input.txt")
input=file.read()
file.close()

input=input.replace("\n", " ")
input=re.split('{|}', input)


# Regular expressions

accessSpecifier="((public|protected|private)( )+)?"
static="((static( )+)?)"
returnType="(int|float|char|boolean|String|byte|short|long|double|void)( )+"
variableName="[a-z|A-Z|$|_]+(0-9|a-z|A-Z|$|_)*( )*"
startingBracket="(\()( )*"
singleParameter="(int|float|char|boolean|String|byte|short|long|double)( )+"+variableName
multipleParameters=singleParameter+"(,( )*"+"(int|float|char|boolean|String|byte|short|long|double)( )+"+variableName+")*"
endingingBracket="(\))( )*"

finalRegEX=accessSpecifier+static+returnType+variableName+startingBracket+"("+singleParameter+"|"+multipleParameters+")?"+endingingBracket


# Storing methods in list

methodsList=[]

for i in  range(len(input)):
  result=re.search(finalRegEX,input[i])

  if  result:
    methodsList.append(result.group())


for i in  range(len(methodsList)):

  # Spliting into before ( and after ( "

  beforeBracket=methodsList[i].split('(')[0]
  afterBracket=methodsList[i].split('(')[1]
  
  returnTypeOfMethod=re.search(returnType,  beforeBracket).group()
  
  # Splitting beforeBracket by returnTypeOfMethod to get method name

  methodName=beforeBracket.split(returnTypeOfMethod)[1]

  print(methodName+"("+afterBracket+" , return type:"+returnTypeOfMethod)