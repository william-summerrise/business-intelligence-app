from faker import Faker
import csv

fake = Faker()

methods = ['email', 'app', 'sms']

entries = []
for _ in range(50):
    entries.append([
        fake.random_element(methods),
        fake.time('%H:%M'),
        fake.paragraph()
    ])

with open('log/engagement.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(entries)