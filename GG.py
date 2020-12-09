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
