from pandas import *
from datetime import *
from random import *
from smtplib import *
from tkinter import *

# 1. Update the birthdays.csv
info_dict = {"name": ["Gokulakrishnan", "Thirumalairaaj", "Bala", "Kavin", "Mani"],
             "email": ["example1@gmail.com", "example2@gmail.com",
                       "example3@gmail.com", "example4.com", "example5.com"],
             "year": [2003, 2003, 2002, 2002, 2002],
             "month": [5, 5, 11, 3, 4],
             "day": [4, 24, 9, 31, 28]
             }
df = DataFrame.from_dict(info_dict)
df.to_csv("birthdays.csv", index=False)
# 2. Check if today matches a birthday in the birthdays.csv
today_info = datetime.now()
today_day = today_info.day
current_month = today_info.month
day_list = df["day"].to_list()
month_list = df["month"].to_list()
for day, month in zip(day_list, month_list):
    if day == today_day and month == current_month:
        index = day_list.index(day)
try:
    name = info_dict["name"][index]
    receiver_email = info_dict["email"][index]
except NameError:
    pass
else:
    """ 3. If step 2 is true, pick a random letter from letter templates and 
    replace the [NAME] with the person's actual name from birthdays.csv"""
    letter_paths = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                    "letter_templates/letter_3.txt"]
    with open(choice(letter_paths)) as letter:
        letter_format = letter.readlines()
        birthday_celebrator = letter_format[0].replace("[NAME]", name)
        letter_format[0] = birthday_celebrator
        letter_sent = ""
        for sentence in letter_format:
            letter_sent += sentence
            letter.close()


# 4. Send the letter generated in step 3 to that person's email address.
def generator():
    global letter_sent, receiver_email
    sender_email = "summamail0001@gmail.com"
    passkey = "mbyiydgqkujzppkq"
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=passkey)
        try:
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=f"Subject:Birthday wishes\n\n{letter_sent}")
        except NameError:
            pass


# --------------------UI-----------------------------
window = Tk()
window.title("Birthday Mail Generator")
window.config(width=800, height=600)
background_image = PhotoImage(file="images/background.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas = Canvas(width=318, height=159, bg="white", highlightthickness=0)
foreground_image = PhotoImage(file="images/foreground.png")
canvas.create_image(159, 79, image=foreground_image)
canvas.place(x=250, y=228)
sent_button = Button(text="Generate Birthday Day Wish", command=generator)
sent_button.place(x=322, y=425)
window.eval('tk::PlaceWindow . center')
window.mainloop()
