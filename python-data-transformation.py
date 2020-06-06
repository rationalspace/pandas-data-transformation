import csv
#read csv1
f = open('attendees1.csv')
csv_f = csv.reader(f)

attendee_emails1 = []

for row in csv_f:
  attendee_emails1.append(row[2])

#read csv 2
f = open('attendees2.csv')
csv_f = csv.reader(f)

attendee_emails2 = []

for row in csv_f:
  attendee_emails2.append(row[2])

#create set out of list - so that we have unique entries
attendee_emails1 = set(attendee_emails1)
attendee_emails2 = set(attendee_emails2)

#find the difference between 2 sets
second_year_attendees = attendee_emails2.difference(attendee_emails1)

#print the difference
print(second_year_attendees)
