# capitalize() function
def format_name(first_name, last_name):
    if(first_name == "" or last_name == ""):
        return "You didn't provide valid inputs"
    return (f"{first_name} {last_name}").title()


capitalizedName = format_name("", "")
print(capitalizedName)
