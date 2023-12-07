# PythonQuizApp
[![Python](https://img.shields.io/badge/Python-Backend-blue)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-Ui-yellow)](https://tkdocs.com/) 
[![Pytest](https://img.shields.io/badge/Pytest-Testing-green)](https://docs.pytest.org/en/7.4.x/) 

Welcome to the PythonQuizApp!

"PythonQuizApp" is a Python application designed for creating and taking quizzes. The application includes a comprehensive quiz management system that allows users to load questions from an external <a href=https://the-trivia-api.com/>Trivia Api</a> and adding their own questions. It features a graphical user interface (GUI) for a seamless user experience.


## Table of contents
* [Installation Process](#installation-process)
* [How to Use the Quiz Application](#how-to-use-the-quiz-application)
* [Key Componenets](#key-components)
* [Tests and validation](#tests-and-validation)
* [Future plans](#future-plans)

## Installation Process:

1. Clone the repository to your local computer:

    ```
    $ git clone 'https://github.com/Mrokus95/PythonQuizApp.git'
    ```

2. Navigate to the project directory

3. (Optional) It is recommended to create and activate a Python virtual environment:

    ```
    $ python -m venv venv
    $ python venv/bin/activate
    ```

4. Install the required dependencies:

    ```
    $ pip install -r requirements.txt
    ```

6. Run the application:

    ```
    $ python main.py
    ```

    The application will display a window with questions and start the game simultaneously.


## How to Use the Quiz Application:

  1. Adding Custom Questions:

     At the beginning of the application, it will ask if you want to add your own questions to the question bank.
     Adding custom questions to the database is optional but allows using the application even when the API with questions is unavailable.
     In the question editor tab, users can add multiple questions, specifying the question content, correct answer, answer options, tags, difficulty, and category.
     
     ![pytanie](https://github.com/Mrokus95/PythonQuizApp/assets/59625513/362f3129-b45d-4a52-a694-46c2f6161ae8)
     ![creator](https://github.com/Mrokus95/PythonQuizApp/assets/59625513/7a8493da-723a-4686-bef5-264ad38c7765)

  3. Randomizing Questions:

     Upon starting the quiz, the application randomly selects ten questions from the available pool.
     Each question is multiple-choice, and users must choose one of the four answer options.

     ![quiz](https://github.com/Mrokus95/PythonQuizApp/assets/59625513/30e188f2-7289-4718-9f2e-c4159f7c34aa)

  5. Quiz Results:

     After completing the last question, users receive quiz results.
     Information includes the number of correct and incorrect answers, the fastest and slowest answer times, and the average time needed for a response.
   
     ![result](https://github.com/Mrokus95/PythonQuizApp/assets/59625513/59003884-ccf6-4b4e-ba04-033bd6e5c98c)

  7. Restart or Close:

     At the end of the quiz, users have the option to start a new game or close the application.
     
     ![new_game](https://github.com/Mrokus95/PythonQuizApp/assets/59625513/c5b421b6-0d46-46d7-ac9a-7866d8ea80a3)

## Key components:
    
    The key components of "QuizApp" include:
    
  1. Question Model: Defines the structure of quiz questions, including the question text, correct answer, choices, tags, difficulty level, and category.
  
  2. Quiz Logic: Manages the flow of the quiz, keeps track of the user's score, records answer times, and calculates performance metrics such as fastest and slowest response times.
  
  3. Question Manager: Retrieves questions from an external API, allows users to load their own questions, and provides an interface for editing and adding questions.
  
  4. User Interface (UI): The graphical interface allows users to interact with the application, take quizzes, and edit questions through a dedicated question editor.
  
  5. Exception Handling: The application incorporates error handling to manage cases where questions cannot be loaded, ensuring a robust user experience.
  
  6. Testing: Utilizes the pytest framework for testing, covering question creation and quiz logic.

## Tests and validation

  The project is partly covered by unit tests due to time constraints. I have made efforts to thoroughly validate the process of creating new questions and the quiz logic as it is most critical part of application. Testing the UI will be part of our future plans.

## Future plans

  In the future, it would be worthwhile to consider implementing a user system, allowing users to create their own quizzes and choose difficulty levels.
