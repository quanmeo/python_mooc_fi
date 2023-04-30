def total_result(person: dict):
    return person['result1'] + person['result2'] + person['result3']

def smallest_average(person1: dict, person2: dict, person3: dict):
    result_p1 = total_result(person1)
    result_p2 = total_result(person2)
    result_p3 = total_result(person3)

    if result_p1 <= result_p2 and result_p1 <= result_p3:
        return person1
    elif result_p2 <= result_p1 and result_p2 <= result_p3:
        return person2
    else:
        return person3

if __name__ == '__main__':
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
