for i in range(1,10):

    for k in range(i):

        print('      ',end=' ')

    for j in range(i,10):

        w='{0:1}x{1:1}={2:<2}'.format(i,j,i*j)

        print(w,end=' ')

    print()
