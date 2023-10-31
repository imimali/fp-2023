from seminar5.domain import (create_student,
                             get_nr, get_name,
                             get_group,
                             get_specialization, set_name, set_group, set_specialisation)


def add_student(students, nr, name, group, specialisation):
    """
    Adds a new student to the list of students
    :param students: lisst of students to add to
    :param nr: student id number
    :param name: name of the student
    :param group: group to which the student belongs
    :param specialisation: specilaireafgdwtrh
    :return:
    """
    student = create_student(nr, name, group, specialisation)
    students.append(student)


def modify_student(students, nr, name, group, specialisation):
    """
     Modify a student identified by id in the list of students
    :param students: lisst of students to add to
    :param nr: student id number of student bound to be modified
    :param name: name of the student
    :param group: group to which the student belongs
    :param specialisation: specilaireafgdwtrh
    :
    """
    for student in students:
        if get_nr(student) == nr:
            set_specialisation(student, specialisation)
            set_name(student, name)
            set_group(student, group)


def copy_student_list(students):
    result = []
    for student in students:
        result.append(
            create_student(get_nr(student), get_name(student), get_group(student), get_specialization(student)))
    return result


def register_for_undo(undo_list, current_entities):
    """
    Registers a new entry in the undo list
    :param undo_list:
    :param current_entities:
    :return:
    """
    undo_list.append(copy_student_list(current_entities))


def pop_undo_list(undo_list):
    if not undo_list:
        raise ValueError("Nothing to undo")
    return undo_list.pop()


def test_add_student():
    students = []
    add_student(students, 1, 'bob', 212, 'mate-info')
    assert len(students) == 1
    assert get_name(students[0]) == 'bob'

    add_student(students, 2, 'bob2', 212, 'mate-info')
    assert get_name(students[0]) == 'bob'
    assert get_name(students[1]) == 'bob2'


def test_modify():
    students = [create_student(1, 'bob', 123, 'mateinfo')]
    modify_student(students, 2, 'bobdated', 124, 'mateinfo2')
    assert get_name(students[0]) == 'bob'
    modify_student(students, 1, 'bobdated', 124, 'mateinfo2')
    assert get_name(students[0]) == 'bobdated'


if __name__ == '__main__':
    test_add_student()
    test_modify()
