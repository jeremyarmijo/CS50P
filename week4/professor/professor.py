import random

def main():
    level = get_level()
    problem = [generate_integer(level), generate_integer(level)] 
    nb_problem = 0
    score = 10
    nb_solution = 0
    while nb_problem != 10:
        try:
            print(problem[0], "+", problem[1], "= ", end="")
            result = int(input())
            if nb_solution == 2:
                score -= 1
                result = problem[0] + problem[1]
                print(problem[0], "+", problem[1], "= ", end="")
                print(result
            if (problem[0] + problem[1] == result):
                nb_solution = 0                
                problem[0] = generate_integer(level)
                problem[1] = generate_integer(level)
                nb_problem += 1
            else:
                nb_solution += 1
                raise ValueError
        except ValueError:
            print("EEE")
            pass

    print("Score:", score)

def refresh_problem(problem, result):
    if (problem[0] + problem[1]) == result:
        return True
    else:
        print("EEE")
        return False

def get_level():
    level_autorize = [1, 2, 3]
    while 1:
        try:
            level = int(input("Level: "))
            if level not in level_autorize:
                continue
            return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10 ** (level - 1), 10 ** level - 1)

if __name__ == "__main__":
    main()
