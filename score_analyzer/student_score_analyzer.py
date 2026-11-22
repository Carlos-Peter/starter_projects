def read_scores(scores):
    scores_dict = {}
    list_of_scores = scores.split()
    if all(score.isdigit() for score in list_of_scores):
        for i in range(1, len(list_of_scores) + 1):
            scores_dict[f"student {i}"] = list_of_scores[i - 1]
        return scores_dict
    else:
        return 0


def average_score(scores_dict):
    total = 0
    if scores_dict:
        for key in scores_dict:
            total += int(scores_dict.get(key, 0))
        average = total / len(scores_dict)
        return average
    else:
        return 0


def highest(scores_dict):
    highest = 0
    if scores_dict:
        for key in scores_dict:
            highest = max(highest, int(scores_dict.get(key)))
        return highest
    else:
        return 0


def lowest(scores_dict):
    lowest = 100
    if scores_dict:
        for key in scores_dict:
            lowest = min(lowest, int(scores_dict.get(key)))
        return lowest
    else:
        return 0


def pass_rate(scores_dict, pass_mark):
    passed = 0
    if scores_dict:
        for key in scores_dict:
            if int(scores_dict.get(key)) >= pass_mark:
                passed += 1
        return passed / len(scores_dict)
    else:
        return 0


def letter_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def print_report(scores_dict):
    if not scores_dict:
        print("no scores")
        return

    print("-" * 40)
    for student, score in scores_dict.items():
        grade = letter_grade(int(score))
        print(f"| {student:<18} {score:>5} Grade: {grade:>4} |")
    scores_average = average_score(scores_dict)
    lowest_score = lowest(scores_dict)
    highest_score = highest(scores_dict)
    pass_rate_of_class = pass_rate(scores_dict, 50)
    print(f"| class average: {scores_average:>21.2f} |")
    print(f"| lowest score: {lowest_score:>22} |")
    print(f"| highest score: {highest_score:>21} |")
    print(f"| pass rate: {pass_rate_of_class:>9.2f} students passed |")
    print("-" * 40)


def main():
    while True:
        user_input = input("Enter student scores separated by spaces: ")
        scores_dict = read_scores(user_input)
        if scores_dict != 0:
            break
        else:
            print("Invalid input. Please enter only numbers separated by spaces.")

    print_report(scores_dict)


main()
