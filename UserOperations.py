class UserOps:
    def __init__(self, library_id, birthdate):
        self.__id = library_id
        self.__birth_date = birthdate


    def user_menu(self):
        while True:
            print("""
               *================*
                User Operations:
               *================* 
                1. Add a new user
                2. View user details
                3. Display all users
            """)

            book_menu = input("Enter a valid option: ")

            if book_menu == "1":
                pass
            elif book_menu == "2":
                pass
            elif book_menu == "3":
                pass