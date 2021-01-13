from pymongo import MongoClient
import requests, datetime, pprint

classmate_one = requests.get('https://api.github.com/users/AJStrizzy').json()
classmate_two = requests.get('https://api.github.com/users/JaxonNarramore').json()
classmate_three = requests.get('https://api.github.com/users/alanavery').json()
classmate_four = requests.get('https://api.github.com/users/sschneeberg').json()
classmate_five = requests.get('https://api.github.com/users/zfinnan').json()

obj_one = {
    'name': classmate_one.get('name'),
    'login': classmate_one.get('login'),
    'location': classmate_one.get('location'),
    'company': classmate_one.get('company'),
    'bio': classmate_one.get('bio')
}

obj_two = {
    'name': classmate_two.get('name'),
    'login': classmate_two.get('login'),
    'location': classmate_two.get('location'),
    'company': classmate_two.get('company'),
    'bio': classmate_two.get('bio')
}

obj_three = {
    'name': classmate_three.get('name'),
    'login': classmate_three.get('login'),
    'location': classmate_three.get('location'),
    'company': classmate_three.get('company'),
    'bio': classmate_three.get('bio')
}

obj_four = {
    'name': classmate_four.get('name'),
    'login': classmate_four.get('login'),
    'location': classmate_four.get('location'),
    'company': classmate_four.get('company'),
    'bio': classmate_four.get('bio')
}

obj_five = {
    'name': classmate_five.get('name'),
    'login': classmate_five.get('login'),
    'location': classmate_five.get('location'),
    'company': classmate_five.get('company'),
    'bio': classmate_five.get('bio')
}

print(obj_one)
print(obj_two)
print(obj_three)
print(obj_four)
print(obj_five)