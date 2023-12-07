import pytest
from datetime import datetime, timedelta
from question_model import Question
from quiz_logic import QuizLogic
from time import sleep

@pytest.fixture
def many_sample_questions():
    return [
        Question("What is 2+2?", "4", ["2", "3", "4", "5"], ["math"],
         "Easy", "General"),
        Question("What is the capital of France?", "Paris",
         ["Berlin", "London", "Madrid", "Paris"],
         ["geography", "Europe"], "Medium", "General Knowledge"),
    ]

@pytest.fixture
def one_sample_question():
    return [
        Question("What is 2+2?", "4", ["2", "3", "4", "5"], ["math"], "Easy", "General"),
    ]

def test_has_more_questions(many_sample_questions):
    quiz_logic = QuizLogic(many_sample_questions)
    assert quiz_logic.has_more_questions() == True

def test_has_not_more_questions(one_sample_question):
    quiz_logic = QuizLogic(one_sample_question)
    quiz_logic.next_question()
    assert quiz_logic.has_more_questions() == False

def test_next_question(many_sample_questions):
    quiz_logic = QuizLogic(many_sample_questions)
    assert quiz_logic.next_question() == "Question 1: What is 2+2?"
    assert quiz_logic.next_question() == "Question 2: What is the capital of France?"

def test_check_correct_answer(many_sample_questions):
    quiz_logic = QuizLogic(many_sample_questions)
    quiz_logic.next_question()
    assert quiz_logic.check_answer("4") == True

def test_check_wrong_answer(many_sample_questions):
    quiz_logic = QuizLogic(many_sample_questions)
    quiz_logic.next_question()
    assert quiz_logic.check_answer("5") == False

def test_statistics(many_sample_questions):
    quiz_logic = QuizLogic(many_sample_questions)
    quiz_logic.next_question()
    sleep(1)
    quiz_logic.check_answer("4")
    quiz_logic.next_question()
    sleep(2)
    quiz_logic.check_answer("Berlin")
    score, wrong, score_percent, fastest_time, slowest_time, avg_time = quiz_logic.get_score()

    assert score == 1
    assert wrong == 1
    assert score_percent == 50
    assert fastest_time == "1.00"
    assert slowest_time == "2.00"
    assert avg_time == "1.50"

