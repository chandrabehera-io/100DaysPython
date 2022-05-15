age = int(input("what is your current age? "))
totalAge = 90

days = 365
weeks = 52
months = 12

age_left = totalAge-age
num_days = age_left * 365
num_weeks = age_left * 52
num_months = age_left * 12

print(
    f"You have {num_days} days, {num_weeks} weeks and {num_months} months left")
