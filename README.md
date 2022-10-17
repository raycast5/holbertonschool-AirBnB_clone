https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221017%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221017T064454Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ad49642a3ff2b9bfcc46b25d5bcde47ff97b011ac505935fa0b618b106ffaa7f![image](https://user-images.githubusercontent.com/104580766/196107893-99867696-ebc0-490e-88d4-bd159ceb841f.png)

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
- Opening
Navigate to the directory containing the console.py file
```
$ ./console.py
(hbnb) 
```

- Using help command
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```
Using help + any of the commands listed above will give you a description of each of the commands.

- Non Interactive Mode
Using the command interpreter in non interactive mode is possible:
```
$echo "show Amenity c4bf43ae-35e9-4d6d-bb7f-b3ca1ca86acd" | ./console.py
(hbnb)
[Amenity] (c4bf43ae-35e9-4d6d-bb7f-b3ca1ca86acd) {'id': 'c4bf43ae-35e9-4d6d-bb7f-b3ca1ca86acd', 'created_at': datetime.datetime(2022, 10, 17, 3, 7, 31, 8283), 'updated_at': datetime.datetime(2022, 10, 17, 3, 7, 31, 8291)}
(hbnb)
```


### Authors

Raymond Colon | [GitHub](https://github.com/raycast5)

