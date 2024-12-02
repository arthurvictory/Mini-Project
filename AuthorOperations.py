author_dict = {}
class AuthorOps:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
    
    # set getters
    def get_name(self):
        return self.__name
    
    def get_biography(self):
        return self.__biography
    
def add_author():
    name = input("Enter the Author's name: ") 
    biography = input("Enter the Author's Biography: ")
        
    author_dict[name] = {
        "Name": name,
        "Biography": biography
    }

    print(f"{name} has been added to the list!")
    print(f"Author: ", author_dict[name], sep="\n")

def view_author():
    name = input("Enter Author's name: ")
    if name in author_dict:
        print(f"Author: ", author_dict[name])
    else:
        print("There is no such Author in the system!")

def display_authors():
    if author_dict:
        print("Your current Author's list:", author_dict, sep="\n")
    else:
        print("No authors are in the current list")

def user_menu():
    while True:
        print("""
           *================*
            User Operations:
           *================* 
            1. Add a new Author
            2. View author details
            3. Display all authors
            4. Back to main menu
        """)

        book_menu = input("Enter a valid option: ")

        if book_menu == "1":
            add_author()
        elif book_menu == "2":
            view_author()
        elif book_menu == "3":
            display_authors()
        elif book_menu == "4":
            break
        else:
            print("That's not a valid option, try again!")
    
user_menu()