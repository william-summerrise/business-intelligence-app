from faker import Faker
import csv

fake = Faker()

services = ['IT Support', 'Website Creation', 'App Development', 'Maintenance', 'Software Integration']
sectors = ['Health', 'Biotechnology', 'Education', 'Government']

entries = []
for _ in range(50):
    entries.append([
        fake.name(),
        fake.random_element(services),
        fake.random_element(sectors),
        fake.date_between(start_date='-2w')
    ])

with open('log/service-data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(entries)