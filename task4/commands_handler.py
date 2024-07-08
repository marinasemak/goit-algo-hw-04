# add new contact to the dictionary
def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Not enough input values"


# change phone for existed contact
def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated"
        else:
            return "Contact not found"
    except ValueError:
        return "Not enough input values"


# show phone of existed contact
def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"{name} {contacts[name]}"
        else:
            return "Contact not found"
    except ValueError:
        return "Not enough input values"


# show all contacts from the dictionary
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
