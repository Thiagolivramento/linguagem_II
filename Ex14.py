def tabuada(x):
    for cont in range(1,11):
        print('{0} x {1} = {2}'.format(x,cont,x*cont))

if __name__=='__main__':
    tabuada(8)