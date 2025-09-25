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
    def __init__(self, taskName, status = "Pending"):
        self.taskName = taskName
        self.status = status
    def mark_done(self):
        self.status = "Done"
        return f"{self.taskName} updated status to {self.status}"
task1 = Task("Go for walk")
task2 = Task("Go for a run.")
task3 = Task("Go to gym")

# print(f"{task1.taskName} has status {task1.status}")
# print(f" {task1.mark_done()}")

### 5. `CartItem`
# Create a class `CartItem` with name, price, and quantity. Add a method `get_total_price()` that returns price × quantity.
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_total_price(self):
        totalPrice = self.price * self.quantity
        return totalPrice
cartItem1 = CartItem("Candy", 10, 4)
print(f"{cartItem1.name} price is {cartItem1.price} with {cartItem1.quantity} quantity. Total Price: {cartItem1.get_total_price()}")


### 6. `UserProfile`

# Write a class `User` that accepts `name` and `email`. Add a method `update_email(new_email)` that updates the user's email.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def update_email(self, new_email):
        self.email = new_email
        return f"{self.name} has updated his email to {self.email}"

user1 = User("Donovan", "don@gmail.com")
# print(f"{user1.name} email ID: {user1.email}")
# print(f"{user1.update_email("donovan@gmail.com")}")

### 7. `GymProgress`
# Create a `GymMember` class with attributes: `name`, `sessions_attended`, `goal`. Add method `progress()` that prints how many sessions are left to reach the goal.
class GymMember:
    def __init__(self, name, sessions_attended, goal):
        self.name = name
        self.sessions_attended = sessions_attended
        self.goal = goal
    def progress(self):
        sessions_remaining = self.goal - self.sessions_attended
        return f"Sessions Remaining: {sessions_remaining} to Reach the Goal: {self.goal}"
gymMember1 = GymMember("Dwayne", 50, 100)
gymMember2 = GymMember("Dwayne", 300, 500)
# print(f"{gymMember1.progress()}")
# print(f"{gymMember2.progress()}")

### 8. `RestaurantBill`
# Create a `Bill` class with food_item, price, and tip. Add method `final_amount()` that returns price + tip.
class Bill:
    def __init__(self, food_item, price, tip):
        self.food_item = food_item
        self.price = price
        self.tip = tip
    def final_amount(self):
        total_amount = self.price + self.tip
        return f"Total bill amount: {total_amount}"
bill1 = Bill("Curry", 200, 20)
bill2 = Bill("Sugar", 400, 50)
# print(f"{bill1.final_amount()}")
# print(f"{bill2.final_amount()}")

### 9.  `InvoiceGenerator`
# Create a class `Invoice` with `customer_name`, `items`, and `total_amount`. Add a method `generate_receipt()` that prints a bill-like structure.
class Invoice:
    def __init__(self, customer_name, items, total_amount):
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
    def generate_receipt(self):
        receipt = "===== Invoice =====\n"
        receipt += f"Customer: {self.customer_name}\n"
        receipt += f"Items: {self.items}\n"
        receipt += f"Total Amount: ${self.total_amount}\n"
        receipt += "=============================="
        return receipt
        
invoice1 = Invoice("Donovan", "Daal", 400)
print(f"{invoice1.generate_receipt()}")



if __name__ == '__main__':
    app.run(debug=True, port=8000)
