import os
import pandas as pd
import datetime
import smtplib

path = os.getwd()
os.chdir(path)

email
pwd


def sendemail(to, sub, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, pwd)
    s.sendmail(email, to, f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == '__main__':
    df = pd.read_excel('data.xlsx')
    today = datetime.datetime.now().strftime("%d-%m")
    currYear = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for ind, item in df:
        if today == item['Birthday'] and currYear not in item['Year']:
            sendemail(item['email'], "Happy Birthday", item['msg'])
            writeInd.append(ind)

    for i in writeInd:
        yr = df.loc[i, 'Year']
        df[i, 'Year'] = f"{yr}, {currYear}"

    df.to_excel('data.xlsx)
