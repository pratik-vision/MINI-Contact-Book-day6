while True:
 contact={}
 print('=======☎️WELCOME TO CONTACTBOOK☎️=========')
 print('SELECT,1.ADD CONTACT\n2.SEARCH CONTACT\n3.UPDATE CONTACT\n4.DELETE CONTACT\n5.SHOW ALL\n6.EXITS')
 op=int(input('Enter the choice='))
 if op == 1:
    name=input('Enter name=')
    number=int(input('enter number='))
    contact[name]=number
    print('contact saved')
 elif op==2:
    print('how u  can search by 1.name or 2.number')
    p=int(input('enter='))
    if p==1:
        name=input('enter name=')
        print(contact.get(name))
    if p==2:
        number=int(input('enter number ='))
        print(contact.get(number))
    else:
        print('INVALID')
 elif op==3:
    print('which one upgrade 1.number or 2.name')
    o=int(input('enter='))
    if o==1:
        name=input('enter name=')
        if name in contact:
            n=int(input('enter new number='))
            contact[name]=n
            print('updated')
        else:
            print('INVALID')
    elif o ==2:
        num=int(input('enter number='))
        if num in contact:
            n=input('enter new name=')
            contact[n]=num
            print('updated')
        else:
            print('INVALID')
 elif op ==4:
    name=input('enter name=')
    if name in contact:
        del contact[name]
        print('contact deleted')
    else:
        print('invalid')
 elif op==5:
    for name,number in contact.items():
        print(name,":",number)
 elif op==6:
    print('exiting contact')
else:
    print('invalid choice,try again')