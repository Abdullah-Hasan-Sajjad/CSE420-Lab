
from pickle import FALSE, TRUE



def	checkWeb(string):



###################################

# Constrains :

# same domain types multiple type not allowed 
# web starts with www
# web's last part is a valid domain type
# no domain type allowed after www
# everything have to domain type after occuring first domain type
# in the body after www has characters A-Z a-z and numbers 0-9 only

###################################


	domainTypes=['com','org','edu','net','int','gov','mil']

	webchecker=string.split('.')


#############################################
#same domain types multiple type not allowed 
#############################################

	thisStringDomains=[]

	for	i	in	range(len(webchecker)):

		if	webchecker[i]	in	domainTypes:

			if	webchecker[i]	not	in	thisStringDomains:

				thisStringDomains.append(webchecker[i])

			else:
				return	False



##################################################################

# web starts with www
# web's last part is a valid domain type
# no domain type allowed after www

##################################################################



	# web starts with www

	if(webchecker[0]=='www'):
		
		#web's last part is a valid domain type

		if(webchecker[-1]	in	domainTypes):
			
			#check no domain type after www

			if(webchecker[1]	not	in	domainTypes):
				pass
			else:
				return	False
		else:
			return	False

	else:
		return	False


########################################################################
# everything have to domain type after occuring first domain type
########################################################################
	
	firstDomainIndex=int(-1)
	checker=FALSE
	c=0

	# geting first domain type's index

	while	checker==FALSE	and	c<len(webchecker):

		if	webchecker[c]	in	domainTypes:
			
			firstDomainIndex=c
			checker=TRUE

		c=c+1

	# checking if after firstDomainIndex are domain type

	c=firstDomainIndex

	while	checker==TRUE	and	c<len(webchecker):

		if	webchecker[c]	not	in	domainTypes:
			checker=FALSE
			return	False
			
		c=c+1


	


##########################################################
#in the body after www has characters A-Z a-z and 
# numbers 0-9 only
##########################################################
	
	# storing ascii values for A-Z a-z and 0-9 only

	ascii=[]

	for i   in  range(3):

		if  i==0:

			for j   in  range(65,91):
				ascii.append(j)

		elif    i==1:

			for j   in  range(97,123):
				ascii.append(j)

		else:

			for j   in  range(48,58):
				ascii.append(j)



	#checking ascii value

	for i	in	range(1,firstDomainIndex):

		for	j	in	range(len(webchecker[i])):

			if	ord(webchecker[i][j])	in	ascii:
				pass
			else:
				return	False

	return	True
		

def	checkEmail(string):


###################################

# Constrains :

# have to exist a @
# all are upper or lower letter or number or special characters before @
# all are upper or lower letter or number after @
# one hyphen acceptable after @
# hyphen not placed at the beginning or end of the domain 
# local-part may be up to 64 characters long 
# each domain part may be up to 64 characters long
# must exist a domain and local part

###################################

	
#######################
# have to exist a @ 
#######################

	if	string.count('@')==1:
		pass
	else:
		return	False


	atList=string.split('@')
	
	local=atList[0].split('.')
	email_domain=atList[1].split('.')


###############################################################
# all are upper or lowercase letter or number or 
# special characters ! % $ # ‘ & + * – / = ? ^ _`. { | } ~ 
# before @
###############################################################


	# storing ascii values for A-Z a-z and 0-9 only

	ascii=[]
	characters=['!','%','$','#','‘','&','+','*','–','/','=','?','^','_','`','.','{','|','}','~']

	for i   in  range(3):

		if  i==0:

			for j   in  range(65,91):
				ascii.append(j)

		elif    i==1:

			for j   in  range(97,123):
				ascii.append(j)

		else:

			for j   in  range(48,58):
				ascii.append(j)


	#checking ascii value or special characters

	for i	in	range(len(local)):

		for	j	in	range(len(local[i])):

			if	ord(local[i][j])	in	ascii:
				pass

			elif	local[i][j]	in	characters:
				pass

			else:
				return	False
	


###############################################################
# all are upper or lowercase letter or number or hyphen after @
###############################################################	


	#checking ascii value or special characters

	for i	in	range(len(email_domain)):

		for	j	in	range(len(email_domain[i])):

			if	ord(email_domain[i][j])	in	ascii:
				pass
			elif	email_domain[i][j]=='-':
				pass
			else:
				return	False


#############################################################
# one hyphen acceptable after @
# hyphen not placed at the beginning or end of the domain
#############################################################

	hyphen=0
	hyphen_index=[]
	for	i	in	range(len(email_domain)):

		for	j	in	range(len(email_domain[i])):

			if	email_domain[i][j]=='-':
				hyphen=hyphen+1
				hyphen_index.append(str(i)+str(j))

	last_pos_l=len(email_domain)-1
	last_pos_s=len(email_domain[last_pos_l])-1
	last_pos=str(last_pos_l)+str(last_pos_s)
	

	if	hyphen<=1	and	00	not	in	hyphen_index	and	last_pos	not	in	hyphen_index:
		pass
		
	else:
		return	False



################################################
# local-part may be up to 64 characters long 
################################################

	if	len(local)<=64:
		pass
	else:
		return	False



#####################################################
# each domain part may be up to 64 characters long
#####################################################

	for	i	in	range(len(email_domain)):

		if	len(email_domain[i])<=64:
			pass
		else:
			return	False



#############################################
# must exist a domain and local part
#############################################

	if	len(atList)==2	and	len(atList[0])>0	and	len(atList[1])>0:
		pass
	else:
		return	False


	return	True









##################
# Taking input
##################

value=int(input())
list=[[]]

for	i	in	range(value):
	
	list[i].append(input())
	
	if i <value-1:

		list.append([])




for	i	in	range(len(list)):

	bool_web=checkWeb(list[i][0])
	bool_email=checkEmail(list[i][0])

	if	bool_web==True:

		list[i].append('Web')

	elif	bool_email==True:

		list[i].append('Email')

	else:

		list[i].append('invalid')


for	i	in	range(len(list)):

	if	list[i][1]!='invalid':

		print(list[i][1],',',i+1)