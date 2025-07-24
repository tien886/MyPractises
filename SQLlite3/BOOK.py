class Book:
    def __init__(self, bookname :str = "NULL", author :str = "NULL", ID :int = "00000" ):
        self.bookname = bookname
        self.author = author
        self.ID = ID
    def getInfo(self):
        print(f"Book name: {self.bookname}")
        print(f"Author name: {self.author}")
        print(f"Book's ID: {self.ID}")
    def DataEntry(self):
        self.bookname = input("Enter book name: ")
        self.author = input("Enter author name: ")
        while True:
            try:
                self.ID = int(input("Enter book's ID: "))
                break
            except ValueError:
                print("❌ Please enter a valid integer for ID.")
        
        