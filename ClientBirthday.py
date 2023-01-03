import datetime

# Get today's date
today = datetime.date.today()

# Get the client's birthday
client_birthday = datetime.date(year=2023, month=1, day=3)

# Check if today is the client's birthday
if today == client_birthday:
  # If it is, print "Happy Birthday"
  print("Happy Birthday")
