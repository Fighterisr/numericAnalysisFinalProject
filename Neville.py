def NevilleInterpolation(x, x_list, y_list,m,n):

    if(n-m == 1):
        result = (((x-x_list[m])*y_list[n])-((x-x_list[n])
            *y_list[m]))/(x_list[n]-x_list[m])
        print(m,'|',n,'|',"%.7f"%(result))
        return result
    result =(((x-x_list[m])*NevilleInterpolation(x,x_list,y_list,m+1,n))-((x-x_list[n])
            *NevilleInterpolation(x,x_list,y_list,m,n-1)))/(x_list[n]-x_list[m])
    print(m,'|',n,'|',"%.7f"%(result))
    return result





