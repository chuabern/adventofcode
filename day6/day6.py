with open("day6_input.txt", "r") as f:
    all_answers = list(f.read().split('\n\n'))

counts = []

def get_total_count(all_answers):
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