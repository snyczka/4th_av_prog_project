import pandas as pd
from typing import Callable, Any, Dict, List, Tuple, Generator
from functools import wraps
import timeit
from itertools import chain
from random import sample, randint
import datetime


def measure_exe_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        '''Wrapper that measures and then returns the execution time of a decorated function.'''
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        return (result, (end - start))
    return wrapper

def special_bind(func: Callable, value: Tuple[Any, List]) -> Tuple:
    '''Modified Writer Monad to process functions with the Execution Time Wrapper.'''
    new_value = func(value[0])
    value[1].append(new_value[1])
    return (new_value[0], value[1])

def unit(value: str) -> tuple:
    '''Base case for the Writer Monad'''
    return (value, [])

@measure_exe_time
def prep_data(source: str) -> dict:
    '''Returns dictionary with Questions as the key to each Answer.'''
    df = pd.read_csv(source, encoding='latin')
    df['Answer'].fillna(" Null")
    return dict(map(lambda x, y: (x, y), df['Question'], df['Answer']))

@measure_exe_time
def question_generation(possible_questions: Dict[str, str]) -> Dict[str, str]:
    '''Returns a random selection of 20 Answer:Question Pairs from a wider dictionary.'''
    pre_selection = list(sample(list(possible_questions.keys()), 20))
    random_20 = dict(((x, possible_questions[x]) for x in pre_selection))
    return random_20


def correctly_answered(options: Dict[str, str], answer: Tuple[str, str]) -> bool:
    '''Tests whether the option chosen by the player matches the pre-determined answer.'''
    return options.get(
            input(f"\n\n\n{answer[0]}\nSelect Answer:\n1.{options.get('1')}\n2.{options.get('2')}\n3.{options.get('3')}\nAnswer Either\n\t\t1\t\t2\t\t3\n")
            ) == answer[1]

def selection_generator(pre_selection: List[str]) -> Generator:
    for x in range(3):
        yield pre_selection.pop(randint(0,(2-x)))

def recursive_play(remaining_questions: Dict[str, str], accumulator: int) -> int:
    '''Returns the accumulated points as an integer after recursively testing the player.'''
    unselected_questions = remaining_questions
    if(len(unselected_questions.keys()) == 5):
        return accumulator
    else:
        selection = list(chain(selection_generator(list(unselected_questions.keys()))))
        selected_question = (selection[0], unselected_questions.get(selection[0]))
        randomizing_dict = {'1' : unselected_questions.pop(selection.pop(randint(0, 2))), 
                            '2' : unselected_questions.pop(selection.pop(randint(0, 1))), 
                            '3' : unselected_questions.pop(selection.pop(0))}
        if(correctly_answered(randomizing_dict, selected_question)):
            accumulator = accumulator + 10
        return recursive_play(unselected_questions, accumulator)


@measure_exe_time
def question_play(contest: Dict[str, str]) -> int:
    '''Returns the result of the recursive_play function.'''
    return recursive_play(contest, 0)



if __name__ == '__main__':
    new_player = input('Enter player name: ')
    creation_time = datetime.datetime.now().strftime('Time:\t%H:%M:%S\t%d/%m/%Y')
#    (jeo, read_time) = prep_data("JEOPARDY_CSV.csv")
#    (twenty_q, q_time) = question_generation(jeo)
#    (player_score, play_time) = question_play(twenty_q)
    player_score = special_bind(question_play, special_bind(question_generation, special_bind(prep_data, unit("JEOPARDY_CSV.csv"))))
    with open("players.txt", "a") as myfile:
        myfile.write(f"{new_player}:\nScore: {player_score[0]}\n{creation_time}\nFile read in {player_score[1][0]} seconds\nQuestions formed in {player_score[1][1]} seconds\nPlayed for {player_score[1][2]} seconds\n\n\n")

    