contacts = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "This user does not exist in the database"
    return inner

@input_error
def add_contact(*args):
    name, phone = args

    if name in contacts:
        raise KeyError

    contacts[name] = phone
    return f"Added contact: {name}, {phone}"

@input_error
def change_phone(*args):
    name, phone = args

    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Changed phone number for contact {name} to {phone}"

@input_error
def show_phone(*args):
    name = args

    if name not in contacts:
        raise IndexError
    return f"The phone number for {name} is {contacts[name]}"

@input_error
def show_all():
    if not contacts:
        return "No contacts found"
    result = "Contacts:\n"

    for name, phone in contacts.items():
        result += f"{name}, {phone}\n"

    return result.strip()

def main():
    while True:
        message = 'Unknown command'
        command, *arguments = input("Enter command: ").split(' ')

        if command == "hello":
            message = "How can I help you?"
        elif command.startswith("add"):
            message = add_contact(*arguments or [''])
        elif command.startswith("change"):
            message = change_phone(*arguments or [''])
        elif command.startswith("phone"):
            message = show_phone(*arguments or [''])
        elif len(arguments) > 0 and f"{command} {arguments[0]}" == "show all":
            message = show_all()
        elif command in ["good bye", "close", "exit", "."]:
            print('Good bye!')
            break

        print(message)

if __name__ == "__main__":
    main()
