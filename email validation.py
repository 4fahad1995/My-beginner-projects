email=input('Enter email:')
k,j,d=0,0,0
if len(email)>=6:#check whether no. of characters are more than 6 characters
    if email[0].isalpha():    #check whether first email char is capital or not
        if ('@' in email) and (email.count('@')==1): #check how many @ symbols are used
            if (email[-4]=='.') ^ (email[-3]=='.'):  # check where '.' comes after domain extensions
                for i in email:
                    if i==i.isspace():    #check whether email contains blank spaces
                        k=1
                    elif i.isalpha():    
                        if i==i.upper():  #check whether email contains any capital letters
                            j=1
                    elif i.isdigit():      #check whether email contains any digits
                        continue
                    elif i=='_' or i=='.' or i=='@':   #check whether email contains characters like '_' , '.' , '@'
                        continue
                    else:
                        d=1 

                if k==1 or j==1 or d==1:
                    print('Wrong email 5')
                else:
                    print('Right email')
            else:
                print('Wrong email 4')
        else:
            print('Wrong email 3')
    else:
        print('Wrong email 2')
else:
    print('Wrong email 1')
