with open("day6_input.txt", "r") as f:
    all_answers = list(f.read().split('\n\n'))

def get_total_count(all_answers):
    counts = []
    for group in all_answers:
        questions_answered = []
        for person in group:
            for question in person:
                if question not in questions_answered and question != '\n':
                    questions_answered.append(person)
            count = len(questions_answered)
        counts.append(count)
    print("The total count is {}".format(sum(counts)))

get_total_count(all_answers)

def get_all_yes_count(all_answers):
    counts = []
    for group in all_answers:
        questions_answered = []
        all_responses = group.split('\n')

        result = set(all_responses[0]).intersection(*all_responses) # https://www.semicolonworld.com/question/53496/python-intersection-of-multiple-lists
        counts.append(len(result))

    print("The total count is {}".format(sum(counts)))
        
get_all_yes_count(all_answers)
