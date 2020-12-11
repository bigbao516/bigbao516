#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
count=1
lottoNumbers=[]
while count<=6:
    n=random.randint
    if n not in lottoNumbers:
        lottoNumbers.append(n)
        count+=1
print('Original data:')
for x in lottoNumbers:
    print(x,end='')
for i in range (len(lottoNumbers)):
    flag=0
    for j in range(len(lottoNumbers)-i-1):
        if lottoNumbers[j]>lottoNumbers[j+1]:
            flag=1
            lottoNumbers[j+1],lottoNumbers[j]=lottoNumbers[j],lottoNumbers[j+1]
    if flag==0:
        break
    print('\n\nAfter sorted data:')
    for x in lottoNumbers:
        print(x,end='')


# In[6]:


import random
def bubblesort(dataArray):
    for i in rande(len(dataAreeay)):
        flag=0
        for j in range(len(dataAreeay)-i-1):
            if dataArray[j]>dataArray[j+1]:
                flag=1
                dataArray[j+1],dataArray[j]=dataArray[j],dataArray[j+1]
        if flag==0:
            break
            
def main():
    count=1
    lottoNumbers=[]
    while count<=6:
     n=random.randint(1,49)
        if n in lottoNumbers:
            lottoNumbers.append(n)
            count+=1
    print('Original data:')
    for x in lottoNumbers:
        print(x,end='')
    bubblesort(lottoNumbers)
    
    print('\n\nAfter sorted data:')
    for x in lottoNumbers:
        print(x,end='')
main()


# In[5]:


import random
count=1
lottoNumbers=[]
while count<=6:
    n=random.randint(1,49)
    if n not in lottoNumbers:
        lottoNumbers.append(n)
    count+=1
print('Original data:')
for x in lottoNumbers:
    print(x,end='')
    lottoNumbers.sort()
print('\n\nAfter sorted data:')
for x in lottoNumbers:
    print(x,end='')
    


# In[ ]:


def binarySearch(dataList,key):
    low=0
    high=len(dataList)-1
    while low<=high:
        mid=(low+high)//2
        if key<dataList[mid]:
            high=mid-1
        elif key==dataList[mid]:
            return mid
        else:
            low=mid+1
    return-1
def main():
    lst=[20,50,12,7,30,8,11,33,56,19]
    
    print('Original data:')
    for x in lst:
        print('%3d'%x,end='')
    print()
    lst.sort()
    print('\nSorted data:')
    for x in lst:
        print('%3d'%x,end='')
        print('\n')
        x=eval(input('What number do you want:'))
        while x!=999
         if x==999:
                break
        ans=binarySearch(lst,x)
        if ans!=-1
         print('%d is at lst[%d]'%(x,ans))
            else:
                print('%d is not found'%(x))
            print('')
            x=eval(input('what number do you want:'))
        print('finish')
main()


# In[ ]:




