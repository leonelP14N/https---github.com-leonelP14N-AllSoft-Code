#TODO: Complete os espaços em branco com uma possível solução para o problema.

while  True :
    x , y  = map(int, input('Digite novamente: ').split())
    if  x  ==  y:
        break
    elif  x  >  y :
        print ( 'Decrescente' )
    else :
        print ( 'Crescente' )