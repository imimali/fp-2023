def get_nr(student):
    # return student['nr_matricol']
    return student[0]


def get_name(student):
    return student[1]


def get_group(student):
    return student[2]


def get_specialization(student):
    return student[3]


def set_name(student, name):
    student[1] = name


def set_group(student, group):
    student[2] = group


def set_specialisation(student, specialisation):
    student[3] = specialisation


def create_student(nr, name, group, specialization):
    """
    Create a new student
    :param nr: student id number
    :param name: name of the student
    :param group: group to which the student belongs
    :param specialization: specilaireafgdwtrh
    :return:
    """
    return [nr, name, group, specialization]
    # return dict(
    #     nr_matricol=nr,
    #     nume=name,
    #     grupa=group,
    #     specializare=specialization
    # )
