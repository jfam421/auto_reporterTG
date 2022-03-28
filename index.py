import smtplib
from random import choice

users = []
random_text = ["""Inciting hatred. Agitating war. Aiding war

This channel is purposefully spreading false and/or misleading information concerning Russia`s armed invasion on Ukrainian land. Moreover, many posts in this channel are nationalistic, hateful and distasteful. Any disinformation and pro-Russian propaganda about the current war will only lead to more victims and casualties.""", """text2"""]

with open("user_list.txt", "r") as file:
    users = file.readlines()

with open("mail_list.txt", "r") as mail:
    for line in mail:
        email = ""
        passw = ""
        checker = False
        for j in range(len(line)):
            if (checker != True):
                if(line[j]!= ":"):
                    email = email + line[j]
                else:
                    checker = True
            else:
                passw = passw + line[j]

        for user in users:
            text = choice(random_text)
            user_about = user.rstrip("\n")
            email_text = f"""\
From: {email}
To: abuse@telegram.org
Subject: Inciting hatred (user: {user_about})

{text}

Reported user: ({user_about})
"""
            #print(email_text)
            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(email, passw)
                smtp_server.sendmail(email, "abuse@telegram.org", email_text)
                smtp_server.close()
                print ("[#]Email sent successfully[#]\n")
            except Exception as ex:
                print ("Something went wrong: ", ex)
