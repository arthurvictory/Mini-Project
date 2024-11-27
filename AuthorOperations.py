class AuthorOps:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
    
        
    
    def user_menu(self):
        while True:
            print("""
               *================*
                User Operations:
               *================* 
                1. Add a new Author
                2. View author details
                3. Display all authors
            """)

            book_menu = input("Enter a valid option: ")

            if book_menu == "1":
                pass
            elif book_menu == "2":
                pass
            elif book_menu == "3":
                pass