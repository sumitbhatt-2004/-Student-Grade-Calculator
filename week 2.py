def calculate_grade(marks):
    """
    Function to determine grade and encouraging message using if-elif-else statements.
    """
    if marks >= 90:
        grade = "A+"
        message = "Outstanding performance! Keep up the exceptional work."
    elif marks >= 80:
        grade = "A"
        message = "Great job! You have a strong understanding of the concepts."
    elif marks >= 70:
        grade = "B"
        message = "Good effort! With a little more practice, you can reach the top."
    elif marks >= 60:
        grade = "C"
        message = "Fair performance. Focus more on areas where you struggled."
    elif marks >= 50:
        grade = "D"
        message = "You passed, but you need to work harder to improve your skills."
    else:
        grade = "F"
        message = "Don't get discouraged! Review the basics and try again."
        
    return grade, message

def main():
    # Student ka name input lena
    student_name = input("Enter student name: ")
    
    # While loop for input validation (0 to 100 only)
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                break
            else:
                print(" Invalid marks! Please enter a value between 0 and 100.")
        except ValueError:
            print(" Invalid input! Please enter a valid number.")
            
    # Function call karke grade aur message nikalna
    grade, encouraging_message = calculate_grade(marks)
    
    # Output display karna
    print("\n-------------------------")
    print(f"Student Name : {student_name}")
    print(f"Marks Scored : {marks}")
    print(f"Grade        : {grade}")
    print(f"Message      : {encouraging_message}")
    print("-------------------------")

if __name__ == "__main__":
    main()
