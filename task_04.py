# Decorator for handling errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Enter name and phone please."
        except IndexError:
            return "Invalid command format."
    return inner

# Dictionary to store contacts
contacts = {}

# Function to add a contact
@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Function to get the phone number by name
@input_error
def get_phone(args):
    name = args[0]
    return contacts[name]

# Function to show all contacts
@input_error
def show_all(args):
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

# Main function to interact with the user
def main():
    while True:
        command = input("Enter a command: ").strip()
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "add":
            try:
                args = input("Enter the argument for the command (name phone): ").strip().split()
                if len(args) != 2:
                    raise ValueError
                print(add_contact(args))
            except ValueError:
                print("Enter name and phone please.")
        elif command == "phone":
            try:
                args = input("Enter the argument for the command (name): ").strip().split()
                if len(args) != 1:
                    raise IndexError
                print(get_phone(args))
            except IndexError:
                print("Enter user name.")
        elif command == "all":
            print(show_all([]))
        else:
            print("Invalid command. Please try again.")

# Start the main function
if __name__ == "__main__":
    main()
