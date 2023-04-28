# Birthday Mail Generator

A simple birthday mail generator with a graphical user interface built with tkinter in python that allows users to generate and send birthday mail to recipients on their birthdays. 

![Screenshot (16)](https://user-images.githubusercontent.com/87391223/235068885-9f08402c-98bf-44e8-816e-8567ea16f0f6.png)


## Features
- Generate and send a birthday mail to the recipient's email address.
- Randomly select from multiple letter templates to send a personalized message.
- Read the recipient's information from a CSV file and store it in a pandas dataframe.

## Getting Started
To get started with this program, simply clone the repository and run the `main.py` file. 

### Prerequisites
- Python 3.x
- pandas
- tkinter
- smtplib

### Installation
1. Clone the repository: 
   ```
   git clone https://github.com/your_username/birthday-mail-generator.git
   ```
2. Install dependencies:
   ```
   pip install pandas
   ```
3. Run the program:
   ```
   python main.py
   ```

## Usage
1. Update the `birthdays.csv` file with the name, email, year, month, and day of each recipient.
2. Click the `Generate Birthday Day Wish` button to generate and send a birthday mail to the recipient's email address.

## File structure
```
├── main.py                    # Main program file
├── birthdays.csv              # CSV file to store recipient information
├── letter_templates           # Folder containing multiple letter templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── images                     # Folder containing background and foreground images for GUI
    ├── background.png
    └── foreground.png
```

## Functions:
Generating and Sending a Birthday Mail:
```python
    def generator():
        global letter_sent, receiver_email
        sender_email = "summamail0001@gmail.com"
        passkey = "mbyiydgqkujzppkq"
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=passkey)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=f"Subject:Birthday wishes\n\n{letter_sent}")
```

Checking If Today Matches a Birthday in the CSV file:
```python
    today_info = datetime.now()
    today_day = today_info.day
    current_month = today_info.month
    day_list = df["day"].to_list()
    month_list = df["month"].to_list()
    for day, month in zip(day_list, month_list):
        if day == today_day and month == current_month:
            index = day_list.index(day)
```

Selecting and Personalizing a Letter Template:
```python
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
```

## Contributing
Contributions to this project are welcome. To contribute, follow these steps:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make and commit your changes (`git commit -am "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
