import pandas as pd
import datetime
import smtplib
from email.message import EmailMessage
import os

def sendEmail(to, sub, msg):
    print(f"email to {to} \nsend with subject: {sub}\n message: {msg}")
    email = EmailMessage()
    email['from'] = 'ABhay Parashar'
    email['to'] = f"{to}"
    email['subject'] = f'{sub}'

    email.set_content(f'{msg}')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('Email','password')
        smtp.send_message(email)
        print("Email send")





    pass
if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    #print(type(today))
    update = []
    yearnow =  datetime.datetime.now().strftime("%Y")
    #print(yearnow)
    for index, item in df.iterrows():
        #print(index,item['birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        #print(type(bday))
        if(bday == today) and yearnow not in str(item["Year"]): 
            sendEmail(item['Email'] ,"Happy BIrthday "+item["Name"], item['message'])
            update.append(index)
    for i in update:
        yr = df.loc[i, 'Year']
        #print(yr)
        df.loc[i,'Year'] = f"{yr}, {yearnow}"
        #print((df.loc[i, 'Year'])
    #print(df)
    df.to_excel("data.xlsx", index=False)



    
    
    
