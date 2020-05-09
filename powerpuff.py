''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    from decimal import Decimal
    while(True):
        
        inp=input('enter an integer for no of igredients in the range of 1 to 1e7 => ')
        try:
            no_ingred=Decimal(inp)
            if(no_ingred!=int(no_ingred) or no_ingred<1 or no_ingred>1e7):
                continue
            break
        except:
            continue
        
    no_ingred=int(no_ingred)   
    longmaxx=9223372036854775807
    while(True):
        if no_ingred==1:
            ingr=input(f'Enter quantity of the ingredient required to create a Powerpuff girl,\ninput Integers in the range 0 to {longmaxx} => ')
        else:
            ingr=input(f'Enter quantities of the {no_ingred} ingredients required to create a Powerpuff girl,\ninput Integers in the range 0 to {longmaxx} => ')
        ingred=ingr.split()
        if len(ingred)!=no_ingred:
            continue
        
        ingredlist=[]
        for i in range(no_ingred):
            try:
                eachingred=Decimal(ingred[i])
                if(eachingred!= int(eachingred) or eachingred < 0   or   eachingred > longmaxx ):
                    break
                else:
                    ingredlist.append(int(eachingred))
                    
            except:
                break

        if len(ingredlist)!=no_ingred:
            
            continue
        else:
            break

            

    while(True):

        if(no_ingred==1):
            #print(f'\n\nEnter the quantity of the ingredient present in the laboratory to create Powerpuff girls.')
            ingr=input(f'\nEnter the quantity of the ingredient present in the laboratory to create Powerpuff girls.Reqirements to create a powerpuff girl is \n{ingredlist},\ninput Integers in the range 0 to {longmaxx} => ')
        else:    
            
            ingr=input(f'\nEnter the quantity of {no_ingred} ingredients present in the laboratory to create Powerpuff girls.Reqirements to create a powerpuff girl is \n{ingredlist},\ninput Integers in the range 0 to {longmaxx} => ')
        ingred=ingr.split()
        if len(ingred)!=no_ingred:
            continue
        
        labingredlist=[]
        for i in range(no_ingred):
            try:
                eachingred=Decimal(ingred[i])
                if(eachingred!= int(eachingred) or eachingred < 0   or   eachingred > longmaxx ):
                    break
                else:
                    labingredlist.append(int(eachingred))
            except:
                break

        if len(labingredlist)!=no_ingred:
            continue
        else:
            break

    min=longmaxx
    for i in range(no_ingred):
        no=int(labingredlist[i]/ingredlist[i])
        if no<min:
            min=no
    print(f'Maximum PowerPuff girls which can be created is {min}')
    return min

main()