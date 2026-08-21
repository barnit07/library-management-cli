class Book:
    def __init__(self,book_id, title, author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_issued=False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] {self.title} by {self.author}| Status:({status})"
        
    

class Student:
    def __init__(self,student_id, name):
        self.student_id=student_id
        self.name=name
        self.books_issued=[]
    
    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id}) - Borrowed: {len(self.books_issued)}"

class Library:
    total_books_created=0
    total_students_registered=0

    def __init__(self,name):
        self.name=name
        self.books={}
        self.students={}
    
    @classmethod
    def increase_totalbook_count(cls):
        cls.total_books_created+=1
    
    @classmethod
    def increase_student_count(cls):
        cls.total_students_registered+=1
    
    @staticmethod
    def validate_book_id(book_id):
        return True if book_id and book_id.strip() else False

    @staticmethod
    def validate_student_id(student_id):
        return True if student_id and student_id.strip() else False
    
    def add_book(self,book_id,title, author):
        if not self.validate_book_id(book_id):
            print("[ERROR] Book Id cannot be empty")
            return
        
        if book_id in self.books:
            print(f"[Error] Book ID '{book_id}' already exists.")
            return
        
        new_book= Book(book_id, title, author)

        self.books[book_id]= new_book
        Library.increase_totalbook_count()
        print(f"[Success] Book '{title}' added to catalog.")

    def register_student(self, student_id, name):

        if not self.validate_student_id(student_id):
            print(f"[ERROR] Student Id cannot be empty")
            return
        
        if student_id in self.students:
            print(f"[Error] Student ID '{student_id}' already exists.")
            return
        
        new_student=Student(student_id, name)
        self.students[student_id]=new_student
        Library.increase_student_count()
        print(f"[Success] Student '[{student_id}]':{name} added to catalog.")
        

    def issue_book(self, book_id, student_id):
        book=self.books.get(book_id)
        student=self.students.get(student_id)

        if not book:
            print("[Error] Book ID not found.")
            return
        if not student:
            print("[Error] Student ID not found.")
            return
        if book.is_issued:
            print(f"[Error] '{book.title}' is already issued.")
            return
        
        book.is_issued=True
        student.books_issued.append(book)
        print(f"{book.title} is issued to {student.name}")
    


    def return_book(self, book_id, student_id):
        book=self.books.get(book_id)
        student=self.students.get(student_id)

        if not student or not book:
            print("Incorrect book id or student id")
            return
        
        if book not in student.books_issued:
            print(f"{student.name} has not borrowed {book.title}")
            return
        
        book.is_issued=False
        student.books_issued.remove(book)
        print(f"{book.title} returned successfully by {student.name}")
        return
    
    def display_all_books(self):
        if not self.books:
            print("No books in the library to display")
            return

        print(f"\n--- {self.name} Book Catalog (Total Created: {Library.total_books_created}) ---")

        for book in self.books.values():
            print(book)

    
    def display_all_students(self):
        if not self.students:
            print("No Students are registered")
            return
        print(f"\n--- {self.name} Student Catalog (Total Created: {Library.total_students_registered}) ---")

        for student in self.students.values():
            print(student)



def main():
    lib= Library("Gothatar Library")

    while True:
        print("\n1. Add Book \n2. Register Student \n3. Issue Book \n4. Return Book \n5. Display all books \n6. Display all students \n7. Exit Application")
        choice= input("Enter choice: ").strip()

        match choice:
            case "1":
                book_id= input("Enter Book Id: ").strip()
                title= input("Enter Book Title: ").strip()
                author= input("Enter Author Name: ").strip()
                lib.add_book(book_id,title,author)
            
            case "2":
                student_id= input("Enter Student Id: ").strip()
                student_name= input("Enter Student Name: ").strip()
                lib.register_student(student_id,student_name)
            
            case "3":
                book_id= input("Enter Book Id: ").strip()
                student_id= input("Enter Student Id: ").strip()
                lib.issue_book(book_id,student_id)
            
            case "4":
                book_id= input("Enter Book Id: ").strip()
                student_id= input("Enter Student Id: ").strip()
                lib.return_book(book_id,student_id)
            
            case "5":
                lib.display_all_books()
            
            case "6":
                lib.display_all_students()
            
            case "7" | "exit" | "q":
                print("\nExiting Library Management System. Goodbye!")
                break
                
            case _:
                print("\n[Error] Invalid option. Please enter a number between 1 and 7.")
                


if __name__=="__main__":
    main()
