balance=10000
amt=int(input("amt"))
if amt<=balance:
    if amt%100==0:
        print("succes")
    else:
       print("multiple by 100")
    else:
       print("insufficient balance")
