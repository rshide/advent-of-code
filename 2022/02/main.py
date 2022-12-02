import os


def solution1(data):

    choice_map = {
        'op': {
            'A': 'rock',
            'B': 'paper',
            'C': 'scissors'
        },
        'my': {
            'X': 'rock',
            'Y': 'paper',
            'Z': 'scissors'
        }
    }
   
    # k is my choice
    # v is a tuple
    # v[0] is the score of my choice
    # v[1] is a win for me & v[1] is a loss
    outcome_map = {
        'rock': (1, 'scissors', 'paper'),
        'paper': (2, 'rock', 'scissors'),
        'scissors': (3, 'paper', 'rock'),
    }

    outcome_score = {
        'lose': 0,
        'draw': 3,
        'win': 6
    }

    total_score = 0

    for round in data:
        op = choice_map['op'].get(round.split(' ')[0])
        my = choice_map['my'].get(round.split(' ')[1])

        choice = outcome_map.get(my)

        if not choice:
            continue

        outcome = ''

        if my == op:
            # draw
            outcome = outcome_score['draw']
        elif outcome_map[my][1] == op:
            # win
            outcome = outcome_score['win']
        elif outcome_map[my][2] == op:
            # lose
            outcome = outcome_score['lose']

        total_score += choice[0] + outcome

    return total_score


def solution2(data):

    op_map = {
            'A': 'rock',
            'B': 'paper',
            'C': 'scissors'
        }

    outcome_map = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
    }

    score_map = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }

    outcome_score = {
        'lose': 0,
        'draw': 3,
        'win': 6
    }    

    # k is op choice
    # v is tuple 
    # v[0] is my choice to win
    # v[1] is my choice to lose
    choice_map = {
        'rock': {
            'win': outcome_score['win'] + score_map['paper'],
            'lose': outcome_score['lose'] + score_map['scissors']
        },
        'paper': {
            'win': outcome_score['win'] + score_map['scissors'],
            'lose': outcome_score['lose'] + score_map['rock']
        },
        'scissors': {
            'win': outcome_score['win'] + score_map['rock'],
            'lose': outcome_score['lose'] + score_map['paper']
        },        
    }

    total_score = 0
    for round in data:
        op = op_map.get(round.split(' ')[0])
        outcome = outcome_map.get(round.split(' ')[1])
        
        if outcome == 'draw':
            total_score += score_map[op] + outcome_score['draw']
        else:
            total_score += choice_map[op][outcome]


    return None


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(f'Part 1: {solution1(data)}')
    print(f'Part 2: {solution2(data)}')