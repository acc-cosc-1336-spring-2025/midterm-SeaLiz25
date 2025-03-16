#add import

from src.question_a.question_a import get_person_category

def main():              
    age = int(input("Enter a person's age:  "))
    category = get_person_category(age)

    print ("This person is a(n) ", category)

main()