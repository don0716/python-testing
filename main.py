from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome Donovan!"}

@app.route('/about')
def about_user():
    information = request.args.get("information")
    email = request.args.get("email")
    return {"contact info": information, "email": email}

# write an api route to greet a person and take the name as an input
@app.route("/contact")
def contact_me():
    name = input("What is your name?")
    age = input("What is your age?")
    return {"message": f"Hey! Your name is {name} and your age is {age}"}

# Write an API route '/check-score' [POST]
#The variable name, score
# if the score is >80, then it should print, you passed
# else, print: you have failed

@app.route('/check-score', methods = ['POST'])
def check_score():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')
    
    if(score > 80):
        return (f"Hey! {name}, Since you have recieved {score}, You have passed")
    else:
        return (f"Hey! {name}, Since you have recieved {score}, You have failed the PCM exam!")
    

### `BookStore`
# Each question below requires you to write a class, create objects, and call methods to test your logic.

## 1. `BookStore`
# Create a class `Book` with attributes `title`, `author`, and `copies`. Add a method `is_available()` that returns `True` if `copies > 0`.
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def is_available(self):
        return self.copies > 0
    
# Test
book1 = Book("1994", "Donovan", 3)
book2 = Book("The Dragon", "Ralph", 4)

@app.route('/books')
def get_books():
    books = [
        {"title": book1.title, "author": book1.author, "available": book1.is_available()},
        {"title": book1.title, "author": book1.author, "available": book1.is_available()}
    ]
    return  {"books": books}

# WheatherCheck
# Create a class Weather with temperature (in Celsius) as a property. Add a method is_hot() that returns True if temp is above 35°C.
class Weather:
    def __init__(self, temperature):
        self.temperature = temperature
    def is_hot(self):
        return self.temperature > 35

@app.route("/temperature")
def get_weather():
    weatherDay1 = Weather(40)
    weatherDay2 = Weather(25)
    return {"weatherDay1":{"temperature": weatherDay1.temperature, "is_hot": weatherDay1.is_hot()}, "weatherDay2": {"temperature": weatherDay2.temperature, "is_hot": weatherDay2.is_hot()}}

# MarksEvaluator
# Define a class Marks with name and score. Write a method grade() that returns:
# "Exellent" for score > 90, "Good" for 70-90, "Average" for 40-69, "Fail" otherwise
class Marks:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def grade(self):
        if self.score > 90:
            return "Excellent"
        elif 70 <= self.score <= 90:
            return "Good"
        elif 40 <= self.score < 70:
            return "Average"
        else:
            return "Fail"

@app.route("/marks")
def marks_evaluator():
    name = request.args.get("name")
    score = int(request.args.get("score"))
    student = Marks(name, score)

    return {
        "name": student.name,
        "score": student.score,
        "Grade": student.grade()
    }

### 4. `TaskManager`
# Create a class `Task` with task name and status. Create 3 task objects. Write a method `mark_done()` to set the status as `"Done"` and print the updated task.
class Task:
    def __init__ (self, taskName, status="Pending"):
        self.taskName = taskName
        self.status = status
    
    def mark_done(self):
        self.status = "Done"
        print(f"Task `{self.taskName}` updated to {self.status}")

task1 = Task("Buy Pens")
task2 = Task("Dog Walk")
task3 = Task("Go for a run")
print(task1.taskName, "-", task1.status)

task1.mark_done()




if __name__ == '__main__':
    app.run(debug=True, port=8000)
