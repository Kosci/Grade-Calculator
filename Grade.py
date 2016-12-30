__author__ = 'Brett'

# Enter grades here, as a list.


def remove_lowest(grade_list, dropped):
    """
    :param grade_list: a list of grades
    :param dropped: an int representing the amount of grades to drop
    :return: a list with the lowest x amount of graded dropped
    """

    grade_list.sort(reverse=True)
    count = 0
    while count < dropped:
        grade_list.pop()
        count += 1

    return grade_list


def calc_grade_score(grade_list):
    """
    :param grade_list: a list of grades
    :return: the final grade, unweighted
    """

    return sum(grade_list) / len(grade_list)


def apply_weight(grade_list, weight):
    """
    :param grade_list: a list of grades
    :param weight: the weight it has
    :return: the final grade, weighted
    """

    return calc_grade_score(grade_list) * weight


def calc_final_grade(grade_list, weight, lowest):
    """
    :param grade_list: the list of grades
    :param weight: the weight it has
    :param lowest: the amount to be dropped
    :return: final grade for that topic
    """

    remove_lowest(grade_list, lowest)
    return apply_weight(grade_list, weight)


def exam_grade_weighted(grade_list, weight):
    return round(apply_weight(grade_list, weight), 2)


def in_class_total(grade_lists):
    return round(calc_final_grade(grade_lists[0], 4, 2) + calc_final_grade(grade_lists[1], 4, 2) +\
            calc_final_grade(grade_lists[2], 15, 1) + calc_final_grade(grade_lists[3], 3, 2) +\
            calc_final_grade(grade_lists[4], 9, 0), 2)


if __name__ == '__main__':
    print("----------------------------------")
    print("SE 342:")
    print("Grade to date: ")