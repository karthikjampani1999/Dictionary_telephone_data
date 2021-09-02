Telephone_Data = {'karthik':'98485','krishna':'637285','Dilip':'2939405'}

while True:
    print("Please enter your contact name: ")
    contact_name = input()
    if contact_name=='':
            break
    if contact_name in Telephone_Data:
        print(Telephone_Data[contact_name] + " is contact number of "+ contact_name )
    else:
        print("Sorry there is no data in our directory")
        print("Please enter your phone number"+ contact_name)
        Telephone_num = input()
        Telephone_Data[contact_name]  =Telephone_num
        print("The telephone data has updated Sucessfully !  Thankyou")