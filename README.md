# AirBnB_clone: The Console

The Console is the first part of the AirBnB-Clone project.
The first thing is to write a command interpreter for the objects of AirBnB clone.

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

**How does the console work?**

It displays a command prompt or cmd (hbnb) that waits for the user to do an input that can be a command and an argument, then it reads it so it can check internally for the function that is needed... So when we enter a command like "destroy", our console looks for the "do_destoy(self, args):" function to validate it and see if it exits then it can be excecute it or if it does not so the console displays an error menssage. If we want to leave the console to go back to the terminal we can type the commands: or EOF, quit or simply press the keys Ctrl + d.

## Console Usage

**In interactive mode...**
~~~
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$
~~~

**In non-interactive mode...**
~~~
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
~~~

## Supported Commands Syntax
  
* **create:** creates a new instance of the specified class, sacing it into the JSON file, it also prints the id. The *syntax* is: [class_name] or [class_name].create() 
* **update** Updates the key value of an instance based on the class name and id by adding an update attribute. The *syntax* is: [class_name] [object_id] [update_key] [update_value] or [class].update([object_id] [update_key] [update_value]() 	
* **show:** 	Prints all attributes or the string representation of an instance based on the id and class name. The *syntax* is:[class_name] [object_id] or [class_name].show([object_id])() 	Displays all attributes of class_name.object_id
*	**all:**   Print the string representations of every instance based on the class name, if used with no option it prints every instance saved to the file. the *syntax* is: [class_name], [class_name].all() 	
* **destroy:**	Deletes all attribues or an instance based on the id and class name. The *syntax* is [class_name] [object_id] or [class_name].destroy([object_id])() 	
* **count:** 	Counts all the instances based on the id and class name. the *syntax* is: [class_name] or [class_name].count() 	

* **help** 	Displays the use of all available commands. The *syntax* is: [help] [command] 	
* **quit** 	Exit console
* **EOF** 	Exit console

## Examples 

<img src="https://i.ibb.co/k54KKVP/BnBex1.png" alt="BnBex1" border="0" />

<a href="https://ibb.co/GnW77fr"><img src="https://i.ibb.co/k54KKVP/BnBex1.png" alt="BnBex1" border="0">

## Installation

- git clone 
- cd AirBnB_clone
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Authors:
 * [Andres Bayona](https://github.com/AndrewB4y)
 * [Karen Campo](https://github.com/KarenCampo777)
