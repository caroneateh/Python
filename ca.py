calculation_to_minutes = 60 * 24
time_conversion = "minutes"

def days_to_minutes(num_of_days):
    condition_check = 30.98
    print(type(condition_check))
    if num_of_days > 0:
        print(f" {num_of_days} days is {num_of_days * calculation_to_minutes} {time_conversion}")
    elif num_of_days == 0:
        print("you entered a 0, please enter a valid positive number")
    else:
        print("you entered a negative value")


#days_to_minutes(25)
#days_to_minutes(30)
#days_to_minutes(35)
 
def validate_and_execute():
    try: 
          user_input_int = int(num_of_days_element)
          if user_input_int > 0:
            days_to_minutes(user_input_int)
          elif user_input_int == 0:
             print("you entered a 0, please enter a valid positive number")
          else: print("user entered a wrong number")
    except ValueError:
        print("carone is a girl")
user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number\n")
    set_of_days = user_input.split(", ")
    #print(list_of_days)
    print(set(set_of_days))
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()


    
#print(f" 20 days is { 20 * calculation_to_minutes} {time_conversion}")  
#print(f" 20 days is { 20 * calculation_to_minutes} {time_conversion}")
#print(f" 20 days is { 20 * calculation_to_minutes} {time_conversion}")