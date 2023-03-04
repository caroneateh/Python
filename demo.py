#print("My name is Carone")
#print(10 * 20)
#print(f"2 days is {2 * 24 * 60} minutes")
#print("2 days is" + str(2 * 24 * 60) + "minutes")

time_conversion = "minutes"
calculation_to_minutes = 60 * 24


#print(f" 20 days is { 20 * calculation_to_minutes} {time_conversion}")

def days_to_minutes(num_of_days):
    condition_check = num_of_days > 3
    print(type(condition_check))
    if num_of_days > 3:
        print(f" {num_of_days} days is {num_of_days * calculation_to_minutes} {time_conversion}")
    elif num_of_days == 0:
        print("you entered a zero, enter a valid number")
    else:
        print("incorrect number")

def validate_and_execute():
    try:
          user_input_number = int(num_of_days_element)
          if user_input_number > 0:
             days_to_minutes(user_input_number)
          elif user_input_number == 0:
            print("you entered a zero, enter a valid number")
          else:
            print("your input is not a number, don't ruin my program")
    except ValueError:
       print("your input is not a valid number, don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey, enter a number:\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()


