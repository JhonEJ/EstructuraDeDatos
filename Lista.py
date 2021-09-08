def viewList(Lista,datos):
    if datos != len(Lista): #Len determina la longitud de la lista 
        print(Lista[datos])
        viewList(Lista,datos +1)

Lista=[1,2,3,4,5,6,7,8,9,10]
viewList(Lista,0)