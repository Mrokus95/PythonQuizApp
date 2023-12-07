class Question:

    def __init__(
        self,
        question_text: str,
        correct_answer: str,
        choices: list,
        question_tags: list,
        question_difficulty: str,
        question_category: str,
    ):
        self.validate_question(question_text, correct_answer, choices, question_tags, question_category)
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.choices = choices
        self.question_tags = question_tags
        self.question_difficulty = question_difficulty
        self.question_category = question_category
    
    def validate_question(self, question_text, correct_answer, choices, question_tags, question_category):
        if not question_text:
            raise ValueError("Question text is required.")
        
        if not correct_answer:
            raise ValueError("Correct answer is required.")
        
        if len(choices) != 4:
            raise ValueError("Please provide 4 unique choices.")
        
        if len(set(choices)) != 4:
            raise ValueError("Please provide 4 unique choices.")
        
        if correct_answer not in choices or choices.count(correct_answer) != 1:
            raise ValueError("Correct answer must be one of the provided choices and be unique.")
        
        if not question_tags:
            raise ValueError("Please provide at least one tag.")
        
        if not question_category:
            raise ValueError("Please provide at least one category.")

    def __str__(self):
        return f"Question: {self.question_text}"