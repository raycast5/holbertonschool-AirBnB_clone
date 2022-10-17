![image](https://user-images.githubusercontent.com/104580766/196107893-99867696-ebc0-490e-88d4-bd159ceb841f.png)

# Project: AirBnB clone - The console

- This project is the first phase of the AirBnB clone project where we will be handling the console.

## Description

First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Command Interpreter
We will use it to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object



## Usage of Command Interpreter
- Opening: Navigate to the directory containing the console.py file
```
$ ./console.py
(hbnb) 
```

- Using help command:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```
Using help + any of the commands listed above will give you a description of each of the commands.

- Non Interactive Mode: Using the command interpreter in non interactive mode is possible:
```
$echo "show Amenity c4bf43ae-35e9-4d6d-bb7f-b3ca1ca86acd" | ./console.py
(hbnb)
[Amenity] (c4bf43ae-35e9-4d6d-bb7f-b3ca1ca86acd) {'id': 'c4bf43ae-35e9-4d6d-bb7f-b3ca1ca86acd', 'created_at': datetime.datetime(2022, 10, 17, 3, 7, 31, 8283), 'updated_at': datetime.datetime(2022, 10, 17, 3, 7, 31, 8291)}
(hbnb)
```
## Implemented Commands:

- `quit` and `EOF`: Exits the program
- `help`: Gives description of commands
- `create`: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: `$ create BaseModel`
  - If the class name is missing, print ** class name missing ** (ex: `$ create`)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex: `$ create MyModel`)
- `show`: Prints the string representation of an instance based on the class name and id. Ex: `$ show BaseModel 1234-1234-1234`.
  - If the class name is missing, print ** class name missing ** (ex: `$ show`)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex: `$ show MyModel`)
  - If the id is missing, print ** instance id missing ** (ex: `$ show BaseModel`)
  - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: `$ show BaseModel 121212`)
- `destroy`: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234.`
  - If the class name is missing, print ** class name missing ** (ex: `$ destroy`)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex:`$ destroy MyModel`)
  - If the id is missing, print ** instance id missing ** (ex: `$ destroy BaseModel`)
  - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: `$ destroy BaseModel 121212`)
- `all`: Prints all string representation of all instances based or not on the class name. Ex: $ `all BaseModel` or `$ all`.
  - The printed result must be a list of strings
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
- `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
  - Usage: `update <class name> <id> <attribute name> "<attribute value>"`
  - Only one attribute can be updated at the time
  - You can assume the attribute name is valid (exists for this model)
  - The attribute value must be casted to the attribute type
  - If the class name is missing, print ** class name missing ** (ex: `$ update`)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex: `$ update MyModel`)
  - If the id is missing, print ** instance id missing ** (ex: `$ update BaseModel`)
  - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ `update BaseModel 121212`)
  - If the attribute name is missing, print ** attribute name missing ** (ex: `$ update BaseModel existing-id`)
  - If the value for the attribute name doesn’t exist, print ** value missing ** (ex: `$ update BaseModel existing-id first_name`)
All other arguments should not be used (Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)

### Authors

Raymond Colon | [GitHub](https://github.com/raycast5)

