def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Not enough arguments"
    return inner

@input_error
def add_contact(contact, contacts):
    name, phone = contact.split(" ")
    contacts[name] = phone
    return f"Added contact: {name}, {phone}"

@input_error
def change_phone(contact, contacts):
    name, phone = contact.split(" ")
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Changed phone number for contact {name} to {phone}"

@input_error
def show_phone(contact, contacts):
    if contact not in contacts:
        raise KeyError
    return f"The phone number for {contact} is {contacts[contact]}"

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found"
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}, {phone}\n"
    return result.strip()

def main():
    contacts = {}
    while True:
        command = input("Enter command: ")
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            print(add_contact(command[4:], contacts))
        elif command.startswith("change "):
            print(change_phone(command[7:], contacts))
        elif command.startswith("phone "):
            print(show_phone(command[6:], contacts))
        elif command == "show all":
            print(show_all(contacts))
        elif command in ["good bye", "close", "exit", "."]:
            print("Good bye!")
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
