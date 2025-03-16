#add import

from src.question_a.question_a import get_person_category

def main():
    
    while True:
        age = int(input("Enter a person's age (or type 'q' to quit): "))
        category = get_person_category(age)      
        print(f"This person is a(n) {category}.")
        user_input = input("Type 'q' to quit or any other key to continue: ")
        if user_input == 'q':
                print("Thank you for using the program. Goodbye!")
               
  
        