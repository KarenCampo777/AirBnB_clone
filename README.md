# AirBnB_clone: The Console

The Console is the first part of the AirBnB clone project.
1. Write a command interpreter for the objects of AirBnB clone.
The command interpreter manages the Airbnb clone objects. The first part of building full Airbnb clone.

## Steps:

1. A BaseModel class (parent) does the initialization, serialization, and deserialization of the upcoming instances.
2. Serialization and deserialization flow: Instance <-> Dictionary <-> JSON string <-> File
3. Classes for Airbnb: State, City, Place, Amenity, Review and User.
4. The First abstracted storage engine of the project: The file storage.
5. The unittests that validates all of the classes and the storage engine.

**Our Command Interpreter can actually...**

* Create a new object like a new Amenity, a new Place or a new User)
* Update object attributes
* Destroy the objects that we want to destroy


## Installation

git clone 
cd AirBnB_clone

## Console Usage

**In interactive mode...**

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$

**In non-interactive mode...**

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$

## Supported Commands Syntax




