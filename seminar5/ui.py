from seminar5.business import (
    add_student,
    modify_student,
    register_for_undo,
    pop_undo_list,
)
from seminar5.domain import get_name, get_specialization, create_student


def print_menu():
    print(
        """
    1. Add new student
    3. View all
    4. modify
    5. undo
    0. exit
    """
    )


def read_valid_string(message: str):
    """
    Returns a non-empty stripped string read from the console
    :param message: input prompt
    :return:
    """
    value = input(message)
    if value.strip() == "":
        print("Invalid input! Try again:")
        return read_valid_string(message)
    return value.strip()


def read_valid_number(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Try again")


def read_student_data():
    nr = read_valid_number("Enter student id ")
    name = read_valid_string("Enter name ")
    group = read_valid_string("Enter group ")
    spec = read_valid_string("Enter specialisation ")
    return nr, name, group, spec


def print_student(student):
    print(f"name: {get_name(student)}, specialization: {get_specialization(student)}")


def run():
    students = [
        create_student(1, "bob", 123, "mate-info"),
        create_student(2, "bob2", 125, "teologie"),
        create_student(3, "bo3", 123, "mate-info"),
        create_student(4, "bob4", 126, "mate-info"),
    ]
    undo_list = []
    print_menu()
    while True:
        try:
            command = input("Enter command")
            if command == "1":
                register_for_undo(undo_list, students)
                id_student, name, group, spec = read_student_data()
                add_student(students, id_student, name, group, spec)
                print("student added successfully")

            elif command == "3":
                for student in students:
                    print_student(student)
            elif command == "4":
                register_for_undo(undo_list, students)
                print(
                    "You will be asked to enter the data of the student to be modified"
                )
                id_student, name, group, spec = read_student_data()
                modify_student(students, id_student, name, group, spec)
                print("Modified successfully")

            elif command == "5":
                students = pop_undo_list(undo_list)
                print("undo successful")

            elif command == "0":
                print("Bye")
                break
            else:
                print("Invalid option")

        except ValueError as e:
            print(e)
