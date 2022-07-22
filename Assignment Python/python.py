##############ASSIGNMENT-1##########DATA TYPES############################
#Q-1
#a)
list1 = [25,25.67,'Ayyappa',2+3j,3<7]   #1st list
list2 = [50,1.234,'Ayyappa',6+9j,59>56] #2nd list  
list3 = list1 + list2   #conatenating 2 lists
list3

#b)
import collections
freq = collections.Counter(list3)
print(dict(freq)) #frequency of the list

#c)
list3.reverse() #list in reverse order
print(list3)

#Q-2)
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}

#a)
set = set1.intersection(set2) #common elements
set

#b)
set3 = set1.union(set2) 
set4=set3 - set #not common elements
set4

#c)
set1.remove(7)
set1
set2.remove(7)
set2

#Q-3)

dict1 = {'Banglore': 2342,'Andhra pradesh': 5432,'Kerala':6700,'Chennai':8990,'Mumbai':'10991'}#create dicyionary

#a)
dict1.keys()#print only keys from dict

#b)
dict1['China'] = 55679
dict1

######################ASSIGNMENT-2#####OPERATORS######################################
#1
#a)
x = 12345
y = 543
z = 399

equa = 22*y + z

if x == equa:
    print("the equation is valid")
    
#b)
a = 5
b = 3
x = a//b #  quotient gives output 1
x
y = a%b    # remainder gives output 2
y    
    
 #2
#a)   
a = 5
b = 3
c = 10
a/=b  
a #result is 1.66   
    
 #b)
c*=5
c   #result is 50
    
#3
#a)
word = "data science"
word.find("s")
's' in "data science"  # gives a boolean output

#b)
x = 4 ** 3
x              #x =64 ,thus we can obtain the solution

#############module-3######variables################
#1
#a)
Age1 = 5 #output is possible
Age1    
#b)
5age=55     # output not possible number cannot be assigned to another number

#2  
#a)
Age_1=100 #can

#b)       
age@1=100     #cannot special characters cannot ne assigned

#c)
del(Age_1)
Age_1 

#3)
# variable can be deleted using del keyword  
a=5
del(a)
a  

###############module-4######conditional statement###############
#1)
age = int(input("enter the age of the person"))

if age <= 10:
    print("children")
elif age >= 60:
    print("senior citizen")
elif age > 10 & age < 60:
    print("normal citizen")

#2)
is_male = 'True'
senior_citizen = 'True'

if is_male and senior_citizen:
    print("fare is 70% applicable")
    
elif not is_male and senior_citizen:
    print("fare is 50% applicable")
elif not is_male and not senior_citizen:
    print("70% fare is applicable")
else:
    print("100% fare is applicable")

#3)
num = int(input("enter a number"))

if num > 0 and num%5==0:
    print("satisfies given condition")
else:
    print("given number doesnot satisfy given condition")

###########################module-5##########loops and functions################

list1=[1,5.5,(10+20j),'data science'] 

#1
#a) 
def func(list1):
    for i in list1:
        print(i)
        
func(list1)        
dir(list1)
#b)
def seq_num(x):
    for i in range(x):
        print(i)
        
seq_num(10) 

#c)

range = int(input("enter the range"))

i=0
while i<=range:
    print(i)
    i=i+1
    
    
#2
list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = ['zero','one','two','three','four','five','six','seven','eight','nine']

res={}

for key in list1:
    for value in list2:
        res[value] = key
        list2.remove(value)
        break
    
print("the resultant dictionary is :  ",str(res))    

#3)
list = [3,4,5,6,7]

new_list = [item + 10 if item % 2== 0 else item * 5 for item in list]
    
print(new_list)

#4)
#1)
def greet(name,message):
    print(" hello",name,message)
    
greet('Ayyappa','how r u')    
#2)
def greet(name,message='how r u'):
    print("hello",name,message)

greet('Ayyappa')

#################module-6############packages#########################
import pandas as pd
#1
df = pd.read_csv("E:/Data Science 18012022/Assignment Python/Indian_cities.csv")
df.describe()
df.info()
#a)
gp1 = df.groupby('state_name').mean()
sex_ratio = gp1[['sex_ratio']].sort_values("sex_ratio",ascending=False)
sex_ratio.head(10)
#b)
gp2 = df.groupby('name_of_city').mean()
graduates = gp2[['total_graduates']].sort_values('total_graduates',ascending=False)
graduates.head(10)

#c)
df1 = df[['name_of_city','location','effective_literacy_rate_total']]
df1
df1.nlargest(10,'effective_literacy_rate_total')

#2
#a)
import matplotlib.pyplot as plt
plt.hist(df['literates_total']) #data is right skewed or positive skewed 
plt.xlabel('literates_total')  
  "# Inferences from histogram:\n",
"#•\tThe data represented on the histogram is not symmetrical.\n",
"#•\tIt has a long positive tail. It has a positive skewness.\n",
"#•\tMore than 90% of the data is confined in the range 56998 to 416998.\n",
"#•\tOutliers are present in the dataset."

#b)
 plt.scatter(df['male_graduates'], df['female_graduates'])   

#3
#a)
plt.boxplot(df['effective_literacy_rate_total'])  #outliers are present
"#•\tThe data represented on the boxplot is not symmetrical.\n",
"#•\tIt has negative skewness as the median of the data is close to the upper end of the boxplot.\n",
"#•\tOutliers are present in the dataset beyond the lower whisker.\n",
"#•\tThe median of the data is approximately 85.\n",
"#•\tThe spread of the data is not much and majority of the data is confined between the range 80% to 90%."
#b)







































































