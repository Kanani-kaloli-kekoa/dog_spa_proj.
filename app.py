import json

# Import modules here!


SERVICES_FILENAME = "/Users/student/code/dog_spa_practice/dog_spa/services.json"
TRANSACTIONS_FILENAME = "/Users/student/code/dog_spa_practice/dog_spa/transactions.txt"


def print_welcome_message():
    print(
        """
                         .--~~,__
            :-....,-------`~~'._.'
            `-,,,  ,_      ;'~U'
            _,-' ,'`-__; '--.
            (_/'~~      ''''(;
 WELCOME TO LUXURY DOG SERVICES!
    """
    )


print("These are the service we provide")
with open(SERVICES_FILENAME) as services_file:
    services = json.load(services_file)["services"]
    print(services)


def dog_spa():
    print_welcome_message()

    while True:
        choice = input("What would you like today?")

        if choice in services.keys():
            price = services[choice]["price"]
            print(price)

        else:
            print("sorry", choice, "is not an option.")


def transactions():
    with open(TRANSACTIONS_FILENAME, "a") as transactions_file:
        transactions_file.write(f"\n{datetime.datime.now()}, {choice}, {price} ")


def print_exit_message():
    print()


if __name__ == "__main__":
    dog_spa()
