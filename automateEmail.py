import os
import pandas as pd
import datetime
import smtplib

path = os.getcwd()
os.chdir(path)

# email
# pwd


def sendemail(to, sub, msg):
    print(f'This work {to} {sub} {msg}')
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls()
    # s.login(email, pwd)
    # s.sendmail(email, to, f"Subject: {sub}\n\n{msg}")
    # s.quit()


if __name__ == '__main__':
    df = pd.read_excel('data.xlsx')
    print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    print(today)
    currYear = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for ind, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")

        if today == bday and currYear not in str(item['Year']):
            sendemail(item['email'], "Happy Birthday", item['msg'])
            writeInd.append(ind)
    print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ',' + str(currYear)

    df.to_excel('data.xlsx')
