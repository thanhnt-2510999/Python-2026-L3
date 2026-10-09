import os
import string
import random
import time
from typing import TypedDict
# student_id, course_id, mark
Mark = TypedDict('Mark', {'student_id': str, 'course_id': str, 'score': float})
type Marks = list[Mark]
# course_id, course_name
Course = TypedDict('Course', {'course_id': str, 'course_name': str, 'archived': bool})
type Courses = list[Course]
# student_id, name, dob, marks
Student = TypedDict('Student', {'student_id': str, 'name': str, 'dob': str})
# Student = TypedDict('Student', {'student_id': str, 'name': str, 'dob': str, 'marks': Marks})
type Students = list[Student]

STUDENTS: Students = []

COURSES: Courses = []

MARKS: Marks = []

# utility
def id_generator(size=6, chars=string.ascii_uppercase + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def format_input(message: str) -> str:
    user_input = input(message + " Type q to cancel\n")
    if user_input.lower() == 'q':
        raise KeyboardInterrupt
    return user_input

def choice_input(message: str) -> bool:
    exit_flag = False
    cont_choice = input(message + ' (y/n): ')
    if cont_choice.lower() != 'y':
        exit_flag = True
    return exit_flag
    # user_input = input(message + " Type q to cancel\n")
    # if user_input.lower() == 'q':
    #     raise KeyboardInterrupt
    # return user_input

# course function
def find_course(id: str) -> tuple[bool, int]:
    print(f"id: {id}")
    for idx, course in enumerate(COURSES):
        if course['course_id'] == id:
            return (True, idx)
    return (False, -1)

def list_course() -> None:
    for course in COURSES:
        print(f"{course['course_id']}. {course['course_name']}")

    print()
    if len(COURSES) == 0:
        print("There is no course in the list.")
    input("Enter to continue...")

def add_course() -> None:
    while True:
        try:
            course_id = format_input("Enter course ID:")
            course_exist, _ = find_course(course_id)
            if course_exist:
                print(f"Course with ID {course_id} already existed. Try another ID")
                continue
            course_name = format_input("Enter course name:")
            COURSES.append({"course_id": course_id, "course_name": course_name, "archived": False})

            print(f"Course {course_name} with ID {course_id} added successfully")
        except KeyboardInterrupt: # add duplicate error
            break
        exit_flag = choice_input('\nDo you want to add another course?')
        if exit_flag:
            break

def edit_course() -> None:
    while True:
        try:
            course_id = format_input("Enter course ID:")
            course_exist, idx = find_course(course_id)
            if not course_exist:
                print(f"Course with ID {course_id} not found. Try another ID")
                continue
            course_name = format_input("Enter course name:")
            COURSES[idx] = {"course_id": course_id, "course_name": course_name, "archived": False}

            print(f"Course with ID {course_id} edited successfully")
        except KeyboardInterrupt: # add duplicate error
            break
        exit_flag = choice_input('\nDo you want to edit another course?')
        if exit_flag:
            break

# def archive_course() -> None:
#     while True:
#         try:
#             course_id = format_input("Enter course ID:")
#             course_exist, idx = find_course(course_id)
#             if not course_exist:
#                 print(f"Course with ID {course_id} not found. Try another ID")
#                 continue
#             COURSES[idx]["archived"] = not COURSES[idx]["archived"]

#             print(f"Course with ID {course_id} {"archive" if COURSES[idx]["archived"] else "unarchive"} successfully")
#         except KeyboardInterrupt: # add duplicate error
#             break
#         cont_choice = input('\nDo you want to archive another course? (y/n): ')
#         if cont_choice.lower() != 'y':
#             break

# student function
def find_student(id: str) -> tuple[bool, int]:
    print(f"id: {id}")
    for idx, student in enumerate(STUDENTS):
        if student['student_id'] == id:
            return (True, idx)
    return (False, -1)

def list_student() -> None:
    for student in STUDENTS:
        print(f"{student['student_id']}. {student['name']}. {student['dob']}")

    print()
    if len(STUDENTS) == 0:
        print("There is no student in the list.")
    input("Enter to continue...")

def add_student() -> None:
    while True:
        try:
            student_id = format_input("Enter student ID:")
            student_exist, _ = find_student(student_id)
            if student_exist:
                print(f"Student with ID {student_id} already existed. Try another ID")
                continue
            name = format_input("Enter student name:")
            dob = format_input("Enter date of birth (YYYY-MM-DD)")
            STUDENTS.append({"student_id": student_id, "name": name, "dob": dob})

            print(f"Student with ID {student_id} added successfully")
        except KeyboardInterrupt: # add duplicate error
            break
        exit_flag = choice_input('\nDo you want to add another student?')
        if exit_flag:
            break

def edit_student() -> None: # todo edit mark
    while True:
        try:
            student_id = format_input("Enter student ID:")
            student_exist, idx = find_student(student_id)
            if not student_exist:
                print(f"Student with ID {student_id} not found. Try another ID")
                continue
            name = format_input("Enter student name:")
            dob = format_input("Enter date of birth (YYYY-MM-DD)")
            STUDENTS[idx]["name"] = name
            STUDENTS[idx]["dob"] = dob
            
            print(f"Student with ID {student_id} edited successfully")
        except KeyboardInterrupt: # add duplicate error
            break
        exit_flag = choice_input('\nDo you want to edit another student?')
        if exit_flag:
            break

# def delete_student() -> None:
#     while True:
#         student_id = input("Enter student ID: Type q to cancel\n")
#         if student_id == 'q':
#             break
#         student_exist, idx = find_student(student_id)
#         if not student_exist:
#             print(f"Student with ID {student_id} not found. Try another ID")
#             continue
#         del STUDENTS[idx]

#         print(f"Student with ID {student_id} deleted successfully")
#         cont_choice = input('\nDo you want to delete another student? (y/n): ')
#         if cont_choice.lower() != 'y':
#             break

# mark function
def find_mark(student_id: str, course_id: str) -> tuple[bool, int, int]:
    print(f"id: {id}")
    for idx, mark in enumerate(MARKS):
        if mark['student_id'] == student_id and mark['course_id'] == course_id:
            return (True, idx)
    return (False, -1)

def list_mark_by_student_id(student_id: str) -> None:
    for mark in MARKS:
        if mark['student_id'] == student_id:
            print(f"{mark['course_id']}. {mark['score']}")


    input("Enter to continue...")

def list_mark_by_course_id(course_id: str) -> None:
    for mark in MARKS:
        if mark['course_id'] == course_id:
            print(f"{mark['student_id']}. {mark['score']}")
    input("Enter to continue...")

def add_mark() -> None:
    while True:
        try:
            student_id = format_input("Enter student ID:")
            student_exist, idx = find_student(student_id)
            if not student_exist:
                print(f"Student with ID {student_id} not found. Try another ID")
                continue
            
            while True:
                course_id = format_input("Enter course_id:")
                course_exist, _ = find_course(course_id)
                if not course_exist:
                    print(f"Course with ID {course_id} not found. Try another ID")
                    continue
                score = format_input("Enter score:") # check error
                MARKS.append({"student_id": student_id, "course_id": course_id, "score": float(score)})
                exit_flag = choice_input('\nDo you want to add mark of another course?')
                if exit_flag:
                    break
            
            print(f"Marks of student with ID {student_id} added successfully")
        except KeyboardInterrupt: # add duplicate error
            break
        exit_flag = choice_input('\nDo you want to add mark to another student?')
        if exit_flag:
            break

def edit_mark() -> None: # todo
    while True:
        try:
            student_id = format_input("Enter student ID:")
            student_exist, idx = find_student(student_id)
            if not student_exist:
                print(f"Student with ID {student_id} not found. Try another ID")
                continue
            
            while True:
                course_id = format_input("Enter course_id:")
                course_exist, _ = find_course(course_id)
                if not course_exist:
                    print(f"Course with ID {course_id} not found. Try another ID")
                    continue
                score = format_input("Enter score:")
                MARKS.append({"student_id": student_id, "course_id": course_id, "score": float(score)})
                exit_flag = choice_input('\nDo you want to edit mark of another course?')
                if exit_flag:
                    break
            
            print(f"Marks of student with ID {student_id} added successfully")
        except KeyboardInterrupt: # add duplicate error
            break
        exit_flag = choice_input('\nDo you want to edit mark of another student?')
        if exit_flag:
            break

# def delete_mark() -> None:
#     while True:
#         mark_id = input("Enter mark ID:")
#         if mark_id == 'q':
#             break
#         mark_exist, idx = find_mark(mark_id)
#         if not mark_exist:
#             print(f"Student with ID {mark_id} not found. Try another ID")
#             continue
#         del STUDENTS[idx]

#         print(f"Student with ID {mark_id} deleted successfully")
#         cont_choice = input('\nDo you want to delete another mark? (y/n): ')
#         if cont_choice.lower() != 'y':
#             break

# menu
def course_menu() -> None:
    # if number of courses is 0 then add course immediately
    # else display menu 1 to list, 2 to add, 3 to edit by id, 4 to delete by id, q to exit to main menu
    # display success message when course is added
    # display error message when: course with existing id
    # 
    last_message = ""
    while (True):
        clear_screen()
        last_message = """
Courses
1. List course
2. Add course
3. Edit course
4. Exit
--------------------
"""
        print(last_message)
        course_choice = input("Choose one of the options above: ")
        while True:
            try:
                choice = int(course_choice)
                if choice not in range(1, 6):
                    raise ValueError
                break
            except ValueError:
                course_choice = input("Invalid choice! Choose again: ")

        match choice:
            case 1:
                # list course
                list_course()
            case 2:
                # add course
                add_course()
            case 3:
                # edit course
                edit_course()
            # case 4:
            #     archive_course()
            case 4:
                break

def student_menu() -> None:
    # if number of students is 0 then add student immediately
    # else display menu 1 to list, 2 to add, 3 to edit by id, 4 to delete by id, q to exit to main menu
    # display success message when student is added
    # display error message when: student with existing id

    last_message = ""
    while (True):
        clear_screen()
        # add list by courses
        # add list all
        print("""
Students
1. List student
2. Add student
3. Edit student
4. Exit
--------------------
""")
        student_choice = input("Choose one of the options above: ")
        while True:
            try:
                choice = int(student_choice)
                if choice not in range(1, 7):
                    raise ValueError
                break
            except ValueError:
                student_choice = input("Invalid choice! Choose again: ")

        match choice:
            case 1:
                # list student
                list_student()
            case 2:
                # add student
                add_student()
            case 3:
                # edit student
                edit_student()
            case 4:
                # delete_student()
                # print(4)
            # case 5:
                break

def mark_menu() -> None:
    

    last_message = ""
    while (True):
        clear_screen()
        # add list by students
        print("""
Marks
1. List marks by course
2. Add mark
3. Exit
--------------------
""")
        mark_choice = input("Choose one of the options above: ")
        while True:
            try:
                choice = int(mark_choice)
                if choice not in range(1, 7):
                    raise ValueError
                break
            except ValueError:
                mark_choice = input("Invalid choice! Choose again: ")

            continue
        match choice:
            case 1:
                # list mark
                # list_mark_by_student_id(student_id)
            # case 2:
                course_id = format_input("Enter course ID:")
                course_exist, _ = find_course(course_id)
                if not course_exist:
                    print(f"Course with ID {course_id} not found. Try another ID")
                list_mark_by_course_id(course_id)
            case 2:
                # add mark
                add_mark()
            # case 3:
            #     # edit mark
            #     edit_mark()
            case 3:
            #     delete_mark()
            # case 5:
                break

def main() -> None:


    while True:

        print("""
Student mark management
1. Course
2. Student
3. Mark
4. Exit
--------------------
""")

        user_choice = input("Choose one of the options above: ")
        while True:
            try:
                choice = int(user_choice)
                if choice not in range(1, 5):
                    raise ValueError
                break
            except ValueError:
                user_choice = input("Invalid choice! Choose again: ")

        match choice:
            case 1:
                # course
                course_menu()
            case 2:
                # student
                student_menu()
            case 3:
                # mark
                mark_menu()
            case 4:
                break

