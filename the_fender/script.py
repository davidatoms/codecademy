import csv


compromised_users = []

with open('passwords.csv') as password_file:
    password_csv - csv.DictReader(password_file)
    for row in password_csv:
        print(row['Username'])
    