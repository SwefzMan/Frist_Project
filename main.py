MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resource_machine = {"water" : 300,
                    "milk" : 200,
                    "coffee" : 100,
                    }



def calculate_coin():
    """that value return in dollar $ , for quater = 0.25$ ,dime = 0.10$, nikle = 0.05$, pennie = 0.01$"""
    print("Please insert coins ")
    user_quarters = int(input("How many quarters? : "))
    user_dimes = int(input("How many dimes? : "))
    user_nickles = int(input("How many nickles? : "))
    user_pennies = int(input("how many pennies? : "))
    return (0.25*user_quarters) + (0.10*user_dimes) + (0.05*user_nickles) + (0.01*user_pennies)
def print_report(resource,profit):
    # this function return print water , milk coffee and money
    print(f"water {resource['water']} ml")
    print(f"milk {resource['milk']} ml")
    print(f"coffee {resource['coffee']} g")
    print(f"money {profit} $")
def is_resouce_sufficient(order_resouce) :
    """check is ingrediant if enoght for make a coffee return that value True or False"""
    for item in order_resouce :
        if resource_machine[item] < order_resouce[item] :
            print(f"sorry that is not enough {item}")
            return False
        return True
def is_transition_success(money_recieve, drink_cost) :
    """check that money recieve enough for make a coffee , return True and False"""
    if money_recieve >= drink_cost :
        chance = money_recieve - drink_cost
        print(f"Here is {chance} in chance")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that not enough money, money refund")
        return False
def make_coffee(drink_coffee_name,order_resource):
    for item in order_resource :
        resource_machine[item] -= order_resource[item]
    print(f"Here you are {drink_coffee_name}! ENJOY !")

is_machine_on = True

while is_machine_on :
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off" :
        is_machine_on = False
    elif user_choice == "report" :
        print_report(resource_machine,profit)
    else:
        drink_name = MENU[user_choice]
        if is_resouce_sufficient(drink_name["ingredients"]) :
            payment = calculate_coin()
            if is_transition_success(payment,drink_name["cost"]):
                make_coffee(user_choice,drink_name["ingredients"])


