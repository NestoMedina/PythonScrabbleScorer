# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85

old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.
def transform(dictionary):
    new_dictionary = {}
    i = 1
    for item in dictionary.values():
        for char in item:
            new_dictionary[char.lower()] = i
        if i == 5:
            i += 2
        elif i == 8:
            i += 1
        i += 1
    return new_dictionary

new_point_structure = transform(old_point_structure)

def initial_prompt():
   print("Let's play some Scrabble!\n")
   user_input = input("Enter a word: ")
   return user_input


def simple_scorer(word):
    word = word.upper()
    points = str(len(word))
    format = ""
    for char in word:
        format += 'Points for {char}: 1 point. \n'.format(char = char)
    final = format + '\n Your overall score is: {points}'.format(points = points)
    return final

vowels = ['A', 'E', 'I', 'O', 'U']
def vowel_bonus_scorer(word):
    word = word.upper()
    points = 0
    format = ""
    for char in word:
        if char in vowels:
            points += 3
            format += "\n Points for {char}: 3".format(char = char)
        else:
            points += 1
            format += "\n Points for {char}: 1".format(char=char)
    final = format + '\nYour overall score is: {points}.'.format(points = str(points))
    return final


def scrabble_scorer(word):
    word = word.lower()
    points = 0
    format = ""
    for char in word:
        if char in new_point_structure.keys():
            points += new_point_structure[char]
        format += "\nPoints for {char}: {value}.".format(char = char, value = new_point_structure[char])
    final = format + '\nYour overall score is: {points}'.format(points = str(points))
    return final


old_scrabble_scorer_dict = {
    'name': 'Scrabble',
    'description': 'The traditional scoring algorithm.',
    'score_function': old_scrabble_scorer
}
simple_scorer_dict = {
    'name': 'Simple Score',
    'description': 'Each letter is worth 1 point. A function with a parameter for user input that returns a score.',
    'score_function': simple_scorer
}
vowel_bonus_scorer_dict = {
    'name': 'Bonus Vowels',
    'description': 'Vowels are 3 pts, consonants are 1 pt.',
    'score_function': vowel_bonus_scorer
}

scoring_algorithms = (
    old_scrabble_scorer_dict,
    simple_scorer_dict,
    vowel_bonus_scorer_dict
)

def scorer_prompt():
    score_prompt = 'Which scoring algorithm would you like to use?'
    user_selection = 3

    while user_selection > 2:
        for index, algorithm in enumerate(scoring_algorithms):
            print(f'{index} - {algorithm["name"]}: {algorithm["description"]}')

        user_selection = int(input('Enter 0, 1, or 2:'))

    selected_score_algorithm_dict = scoring_algorithms[user_selection]

    return selected_score_algorithm_dict
    

def run_program():
    word = initial_prompt()

    selected_score_algorithm_dict = scorer_prompt()

    print(selected_score_algorithm_dict['score_function'](word))

