def sum(f,end):
    total=0
    for k in range(f,end+1):
        if(k%2==0):
            total+=k
    return total
def main():
    f,end=eval(input('Enter from number,and end number:'))
    tot=sum(f,end)
    print('Sum of even numbers from %d to %d is %d'%(f,end,tot))
main()

a=100
def main():
    a=200
    print("a=",a)
    
main()
print("a=",a)
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
