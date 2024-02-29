# holbertonschool-AirBnB_clone - The Console
![hbnb](https://github.com/zabalae/holbertonschool-AirBnB_clone/assets/142937639/63c0b6bf-eac7-4236-9ae9-255d1f18b5fe)

### Description
The AirBnB clone console project is the first step we take towards building our first web application: the *AirBnB clone*. This step is very important because, what we build during this project, is what we will use with all the other following projects.

Each task is linked and will help us:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place...) that inherit from BaseModel
- create the first abstracted storage engine of the project: *File storage*
- create all unittests to validate all our classes and storage engine

### The Command Interpreter
The command interpreter is just like the shell we created in an earlier project but limited to a specific use-case. In our case, we want it to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

### Execution
The shell should work like this in interactive mode: 
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
The shell should work like this in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: *$ echo "python3 -m unittest discover tests" | bash*
