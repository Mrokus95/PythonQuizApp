import pytest
from question_model import Question

@pytest.fixture
def sample_question_data():
    return {
        "question_text": "What is the capital of France?",
        "correct_answer": "Paris",
        "choices": ["Berlin", "London", "Madrid", "Paris"],
        "question_tags": ["geography", "Europe"],
        "question_difficulty": "Medium",
        "question_category": "General Knowledge"
    }

def test_question_creation(sample_question_data):
    question = Question(**sample_question_data)

    assert question.question_text == sample_question_data["question_text"]
    assert question.correct_answer == sample_question_data["correct_answer"]
    assert question.choices == sample_question_data["choices"]
    assert question.question_tags == sample_question_data["question_tags"]
    assert question.question_difficulty == sample_question_data["question_difficulty"]
    assert question.question_category == sample_question_data["question_category"]

def test_question_str_representation(sample_question_data):
    question = Question(**sample_question_data)

    expected_str = (
        f"Question: {sample_question_data['question_text']}"
    )

    assert str(question) == expected_str

def test_empty_question_text():
    with pytest.raises(ValueError):
        Question("", "Correct Answer",
         ["Choice1", "Choice2", "Choice3", "Choice4"],
         ["Tag1", "Tag2"], "Easy", "Category")

def test_empty_correct_answer(sample_question_data):
    sample_question_data["correct_answer"] = ""
    with pytest.raises(ValueError):
        Question(**sample_question_data)

def test_insufficient_choices(sample_question_data):
    sample_question_data["choices"] = ["Choice1", "Choice2"]
    with pytest.raises(ValueError):
        Question(**sample_question_data)

def test_duplicate_choices(sample_question_data):
    sample_question_data["choices"] = ["Choice1", "Choice1", "Choice2", "Choice3"]
    with pytest.raises(ValueError):
        Question(**sample_question_data)