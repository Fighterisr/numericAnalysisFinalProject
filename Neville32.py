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


x_list = [0.35,0.4, 0.55, 0.65, 0.7, 0.85,0.9]
y_list = [-213.5991,-204.4416, -194.9375, -185.0256, -163.8656,-152.6271]
print("n | m |      x")
print("---------------------")
print('\nFinal :',"%.6f"%(NevilleInterpolation(0.75,x_list,y_list,0,5)))



