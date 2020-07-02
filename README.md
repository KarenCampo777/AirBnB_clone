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
  
* **create:** creates a new instance of the specified class, sacing it into the JSON file, it also prints the id. 

The *syntax* is: create \<class name\>
* **update** Updates the key value of an instance based on the class name and id by adding an update attribute. 

The *syntax* is: \<class name\> \<id\> \<attribute name\> \<attribute value\>

* **show:** 	Prints all attributes or the string representation of an instance based on the id and class name. 

The *syntax* is: \<class name\> \<id\>

*	**all:**   Print the string representations of every instance based on the class name, if used with no option it prints every instance saved to the file. 

The *syntax* is: all \<class name\> 

* **destroy:**	Deletes all attribues or an instance based on the id and class name. 

The *syntax* is: destroy \<class name\> \<id\>

* **help** 	Displays the use of all available commands. 

The *syntax* is: help \<command\>

* **quit** 	Exit console

* **EOF** 	Exit console

## Examples 

**On destroy**
~~~
$ ./console.py
(hbnb) create BaseModel
1619595d-9691-49e2-925f-abe5ba1da8cb
(hbnb) show BaseModel 1619595d-9691-49e2-925f-abe5ba1da8cb
[BaseModel] (1619595d-9691-49e2-925f-abe5ba1da8cb) {'id': '1619595d-9691-49e2-925f-abe5ba1da8cb', 'created_at': datetime.datetime(2020, 7, 1, 23, 18, 11, 506679), 'updated_at': datetime.datetime(2020, 7, 1, 23, 18, 11, 506734)}
(hbnb) destroy BaseModel 1619595d-9691-49e2-925f-abe5ba1da8cb
(hbnb) show BaseModel 1619595d-9691-49e2-925f-abe5ba1da8cb
** no instance found **
(hbnb)
~~~

**On create and update User**
~~~
$ ./console.py
(hbnb) create User
317a233b-8e8c-4b1b-b279-d6b99ad501ca
(hbnb) updater user b7945aa1-8bc2-4ea2-bc37-80eb34a3200f name Andres
vagrant@vagrant-ubuntu-trusty-64:~/Holberton/AirBnB_clone$ ./console.py
(hbnb) create User
f044a77a-7337-433d-a5f4-751c35fc0950
(hbnb) update User b7945aa1-8bc2-4ea2-bc37-80eb34a3200f name Andres
(hbnb) show User f044a77a-7337-433d-a5f4-751c35fc0950
[User] (f044a77a-7337-433d-a5f4-751c35fc0950) {'updated_at': datetime.datetime(2020, 7, 1, 23, 29, 17, 435363), 'created_at': datetime.datetime(2020, 7, 1, 23, 29, 17, 435317), 'id': 'f044a77a-7337-433d-a5f4-751c35fc0950'}
(hbnb) 
~~~

**On Classes, example made with City but applies for all Classes**
~~~
./console.py
(hbnb) create City
47426c35-a5b4-40b9-8857-71d19629c1e7
(hbnb) update City 47426c35-a5b4-40b9-8857-71d19629c1e7
** attribute name missing **
(hbnb) update City 47426c35-a5b4-40b9-8857-71d19629c1e7 name Cali
(hbnb) all City
["[City] (5d9c717c-c21e-456d-8e03-ba5c48a405a8) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 340176), 'id': '5d9c717c-c21e-456d-8e03-ba5c48a405a8', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 340180)}", "[City] (c143db25-1d92-4367-b5fb-b5b8f8f91776) {'id': 'c143db25-1d92-4367-b5fb-b5b8f8f91776', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 750525), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 750531)}", "[City] (8925eabb-d5ff-4ec4-bf12-a555214f046f) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 340789), 'id': '8925eabb-d5ff-4ec4-bf12-a555214f046f', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 340802)}", "[City] (a6086165-1af1-4a82-9fcc-9d5ba6315f69) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 772169), 'id': 'a6086165-1af1-4a82-9fcc-9d5ba6315f69', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 772176)}", "[City] (64e5851b-b233-4a3f-86dc-604fcee70d90) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 246980), 'id': '64e5851b-b233-4a3f-86dc-604fcee70d90', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 246983)}", "[City] (17fad2ad-609f-443c-a5b8-ef3e8208b7d0) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 229444), 'id': '17fad2ad-609f-443c-a5b8-ef3e8208b7d0', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 229462)}", "[City] (1eacac2b-c109-4c33-896e-b208a16eedda) {'id': '1eacac2b-c109-4c33-896e-b208a16eedda', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 774209), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 774213)}", "[City] (3b6e2bbc-cb87-491c-a97c-609e7a275d3e) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 749500), 'id': '3b6e2bbc-cb87-491c-a97c-609e7a275d3e', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 749514)}", "[City] (d1398b15-72dc-4dba-8fdd-967bfcf3ed53) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 389573), 'id': 'd1398b15-72dc-4dba-8fdd-967bfcf3ed53', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 389580)}", "[City] (f1713580-c1f0-44f8-9fd4-0622d368221c) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 770531), 'id': 'f1713580-c1f0-44f8-9fd4-0622d368221c', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 770544)}", "[City] (7f1d4054-0b57-4b62-bae5-3a85fdf9c48b) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 329801), 'id': '7f1d4054-0b57-4b62-bae5-3a85fdf9c48b', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 329824)}", "[City] (e512870d-2d37-48de-aa68-cbc9cf6002b9) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 229497), 'id': 'e512870d-2d37-48de-aa68-cbc9cf6002b9', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 229500)}", "[City] (dd3f4650-636d-4b71-9e30-c0868aa50128) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 773220), 'id': 'dd3f4650-636d-4b71-9e30-c0868aa50128', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 773224)}", "[City] (4b425ca6-87ae-42a8-ba0b-2765fcb60fa7) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 247767), 'id': '4b425ca6-87ae-42a8-ba0b-2765fcb60fa7', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 247785)}", "[City] (9cc5f9ce-55b7-4484-a7da-3091882871bf) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 187707), 'id': '9cc5f9ce-55b7-4484-a7da-3091882871bf', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 187725)}", "[City] (cbbdf376-d24a-4698-b939-f1b6b27cc125) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 374757), 'id': 'cbbdf376-d24a-4698-b939-f1b6b27cc125', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 374771)}", "[City] (55bb4fb3-d71a-4e81-ba73-c2d25628442d) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 251504), 'id': '55bb4fb3-d71a-4e81-ba73-c2d25628442d', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 251509)}", "[City] (40748e07-686f-44ae-a56e-f12992747d52) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 183630), 'id': '40748e07-686f-44ae-a56e-f12992747d52', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 183634)}", "[City] (807c3994-fcbc-4cdd-8d8c-7e98f02430a7) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 750451), 'id': '807c3994-fcbc-4cdd-8d8c-7e98f02430a7', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 750571)}", "[City] (543eea25-41fe-452a-81c3-a1b069c26b4f) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 249327), 'id': '543eea25-41fe-452a-81c3-a1b069c26b4f', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 249375)}", "[City] (89b11c87-1443-4511-8e13-a3be5ca13cd0) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 375607), 'id': '89b11c87-1443-4511-8e13-a3be5ca13cd0', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 375611)}", "[City] (62c16879-615e-433c-a4ee-1bbc292659cd) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 391283), 'id': '62c16879-615e-433c-a4ee-1bbc292659cd', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 391288)}", "[City] (7dbf01a0-efc8-4aee-846e-4a795c857557) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 340847), 'id': '7dbf01a0-efc8-4aee-846e-4a795c857557', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 340853)}", "[City] (cf280935-3b6a-4236-ae3b-aa8199a22b10) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 770585), 'id': 'cf280935-3b6a-4236-ae3b-aa8199a22b10', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 770589)}", "[City] (6d8e0cf0-7157-4346-a472-c21d7654fede) {'id': '6d8e0cf0-7157-4346-a472-c21d7654fede', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 247841), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 247847)}", "[City] (9fba6072-c15b-4034-8bf2-7a3afc535864) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 188943), 'id': '9fba6072-c15b-4034-8bf2-7a3afc535864', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 188958)}", "[City] (e5a87766-5bb8-4ca4-873a-214cb60e798e) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 342519), 'id': 'e5a87766-5bb8-4ca4-873a-214cb60e798e', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 342525)}", "[City] (8dc699d9-4943-4e76-a3d4-4b370f3a6238) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 230101), 'id': '8dc699d9-4943-4e76-a3d4-4b370f3a6238', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 230388)}", "[City] (a092bc61-c517-47ed-8811-9c3e68ce4a47) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 749568), 'id': 'a092bc61-c517-47ed-8811-9c3e68ce4a47', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 749579)}", "[City] (90611787-0f1a-4d19-8a26-8997805b4268) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 771250), 'id': '90611787-0f1a-4d19-8a26-8997805b4268', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 771265)}", "[City] (34680b26-9e4d-4082-aa38-0d78a47d3451) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 253755), 'id': '34680b26-9e4d-4082-aa38-0d78a47d3451', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 253828)}", "[City] (7f232767-f890-4c47-ba6f-1b49af107450) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 340127), 'id': '7f232767-f890-4c47-ba6f-1b49af107450', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 340140)}", "[City] (14ceb0f3-6fbb-478c-b4aa-dc6ce5c7d5e0) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 773149), 'id': '14ceb0f3-6fbb-478c-b4aa-dc6ce5c7d5e0', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 773171)}", "[City] (2f2479c5-bfd6-48a5-99f6-05998dd9c92a) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 339714), 'id': '2f2479c5-bfd6-48a5-99f6-05998dd9c92a', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 339718)}", "[City] (47426c35-a5b4-40b9-8857-71d19629c1e7) {'name': 'Cali', 'updated_at': datetime.datetime(2020, 7, 1, 23, 48, 21, 953500), 'created_at': datetime.datetime(2020, 7, 1, 23, 47, 52, 98077), 'id': '47426c35-a5b4-40b9-8857-71d19629c1e7'}", "[City] (12878390-05e8-42fc-b99f-e323fd0d1714) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 176980), 'id': '12878390-05e8-42fc-b99f-e323fd0d1714', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 176997)}", "[City] (9c6adada-50e8-4151-a853-db050a3fc089) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 183555), 'id': '9c6adada-50e8-4151-a853-db050a3fc089', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 183573)}", "[City] (4b704e7a-422f-4869-a707-35f2a37adbd1) {'id': '4b704e7a-422f-4869-a707-35f2a37adbd1', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 341570), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 341581)}", "[City] (99e2355a-7e91-47f7-8c89-c589ac9f2ce9) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 375564), 'id': '99e2355a-7e91-47f7-8c89-c589ac9f2ce9', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 375636)}", "[City] (f41778ed-8229-4d4c-8b36-cccb29dff498) {'created_at': datetime.datetime(2020, 7, 1, 23, 38, 55, 342891), 'id': 'f41778ed-8229-4d4c-8b36-cccb29dff498', 'updated_at': datetime.datetime(2020, 7, 1, 23, 38, 55, 342926)}", "[City] (d2c189ec-e014-4cb5-9010-30030384adb2) {'id': 'd2c189ec-e014-4cb5-9010-30030384adb2', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 177039), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 177043)}", "[City] (324a10ac-f553-4865-bf25-8a80b2faddae) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 187425), 'id': '324a10ac-f553-4865-bf25-8a80b2faddae', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 187471)}", "[City] (126f5572-1183-40d7-aaec-1b46e9450d8c) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 329907), 'id': '126f5572-1183-40d7-aaec-1b46e9450d8c', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 329916)}", "[City] (d7c9d83d-1f01-47b1-ab20-8bd39bd3a58c) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 189743), 'id': 'd7c9d83d-1f01-47b1-ab20-8bd39bd3a58c', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 189747)}", "[City] (dabcd013-b9cd-4c92-a431-e4ea12bce56c) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 774144), 'id': 'dabcd013-b9cd-4c92-a431-e4ea12bce56c', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 774160)}", "[City] (6c2b7e55-e517-49d5-97b4-58b79c6f6542) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 341681), 'id': '6c2b7e55-e517-49d5-97b4-58b79c6f6542', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 341687)}", "[City] (30bc4dd1-b96f-42d4-9895-557ae64fedc6) {'name': 'Cali', 'id': '30bc4dd1-b96f-42d4-9895-557ae64fedc6', 'created_at': datetime.datetime(2020, 7, 1, 23, 43, 34, 694537), 'updated_at': datetime.datetime(2020, 7, 1, 23, 45, 4, 775762)}", "[City] (eeb340fb-f4aa-4b8d-b754-ebfd31705077) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 389488), 'id': 'eeb340fb-f4aa-4b8d-b754-ebfd31705077', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 389509)}", "[City] (8f3d9b4e-529b-47d1-baff-abd83433af76) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 374933), 'id': '8f3d9b4e-529b-47d1-baff-abd83433af76', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 374943)}", "[City] (308b1588-30b5-40e5-8111-c0c4b4f015df) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 177576), 'id': '308b1588-30b5-40e5-8111-c0c4b4f015df', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 177642)}", "[City] (3325c8ba-b9c1-4d6c-99dd-e017bc8ff3d4) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 189686), 'id': '3325c8ba-b9c1-4d6c-99dd-e017bc8ff3d4', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 189699)}", "[City] (8b8b72d6-f2e1-43a9-a248-7aa38dd0122e) {'id': '8b8b72d6-f2e1-43a9-a248-7aa38dd0122e', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 177617), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 177620)}", "[City] (93e660b6-bcf5-439b-ac8d-3c3728d6c685) {'id': '93e660b6-bcf5-439b-ac8d-3c3728d6c685', 'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 393263), 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 393270)}", "[City] (14d8b0ee-bbad-4545-9d16-b37c451fb4e9) {'id': '14d8b0ee-bbad-4545-9d16-b37c451fb4e9', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 189000), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 189004)}", "[City] (3b82a7a7-a806-475a-8288-46b75e7ef2bf) {'id': '3b82a7a7-a806-475a-8288-46b75e7ef2bf', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 190471), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 190476)}", "[City] (cc6e2db3-bbd5-4ce3-ade3-845bdc65fa56) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 381812), 'id': 'cc6e2db3-bbd5-4ce3-ade3-845bdc65fa56', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 381817)}", "[City] (79000a03-b599-4c7a-be88-b5bf7ddc39a3) {'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 387845), 'id': '79000a03-b599-4c7a-be88-b5bf7ddc39a3', 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 387906)}", "[City] (f94d221e-2462-4a99-afa4-902aa2888fde) {'id': 'f94d221e-2462-4a99-afa4-902aa2888fde', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 771316), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 771320)}", "[City] (274402af-78e8-41f7-9471-7a46ec04dd11) {'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 339653), 'id': '274402af-78e8-41f7-9471-7a46ec04dd11', 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 339671)}", "[City] (43511909-b338-4237-b1f4-dfaf61e046a2) {'id': '43511909-b338-4237-b1f4-dfaf61e046a2', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 772105), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 20, 772119)}", "[City] (78b41fa9-9be5-4316-b369-72a02270696f) {'id': '78b41fa9-9be5-4316-b369-72a02270696f', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 249661), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 249710)}", "[City] (cd0840b4-3241-4fec-b010-8979b515eab3) {'id': 'cd0840b4-3241-4fec-b010-8979b515eab3', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 330445), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 330526)}", "[City] (4253d590-92ae-4861-b3eb-c870cb437260) {'id': '4253d590-92ae-4861-b3eb-c870cb437260', 'created_at': datetime.datetime(2020, 6, 30, 21, 40, 4, 482775), 'updated_at': datetime.datetime(2020, 6, 30, 21, 40, 4, 482812)}", "[City] (d6c2352a-c508-41dd-b224-1c1f62ecd0da) {'id': 'd6c2352a-c508-41dd-b224-1c1f62ecd0da', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 190413), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 15, 190425)}", "[City] (0e9a84b5-e3e9-4362-83b4-2d4e22db7b55) {'id': '0e9a84b5-e3e9-4362-83b4-2d4e22db7b55', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 246931), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 246944)}", "[City] (4a9c874e-e2c9-455b-a758-36be1e1520b4) {'id': '4a9c874e-e2c9-455b-a758-36be1e1520b4', 'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 381732), 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 381755)}", "[City] (0b9d49fd-d601-4d59-84bc-80f08b73b1ff) {'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 254063), 'id': '0b9d49fd-d601-4d59-84bc-80f08b73b1ff', 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 254089)}", "[City] (fb5d14b7-c954-40af-9b8c-9072de2f3988) {'id': 'fb5d14b7-c954-40af-9b8c-9072de2f3988', 'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 388229), 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 388249)}", "[City] (f7f9fed6-c5fe-494f-b6ec-070283fc974c) {'id': 'f7f9fed6-c5fe-494f-b6ec-070283fc974c', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 342454), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 342468)}", "[City] (91bc8b91-4fcc-40c0-881d-08dd2bffa7f9) {'id': '91bc8b91-4fcc-40c0-881d-08dd2bffa7f9', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 251417), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 251441)}", "[City] (9c7852f1-48a2-4c6b-84f0-aeda678597ad) {'id': '9c7852f1-48a2-4c6b-84f0-aeda678597ad', 'created_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 330491), 'updated_at': datetime.datetime(2020, 7, 1, 20, 19, 57, 330495)}", "[City] (f1acbcbc-1240-445c-9fa6-04bbd7dd8e04) {'id': 'f1acbcbc-1240-445c-9fa6-04bbd7dd8e04', 'created_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 230340), 'updated_at': datetime.datetime(2020, 7, 1, 20, 20, 38, 230348)}", "[City] (4f35bfa3-26ad-449c-8e84-4d06949d7a80) {'id': '4f35bfa3-26ad-449c-8e84-4d06949d7a80', 'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 393179), 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 393203)}", "[City] (8867cc6b-3b5a-4080-84a1-1488fa7e65c5) {'id': '8867cc6b-3b5a-4080-84a1-1488fa7e65c5', 'created_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 391203), 'updated_at': datetime.datetime(2020, 7, 1, 20, 18, 50, 391227)}"]
(hbnb) 
~~~


## Diagram 

[You can check our diagram here](https://drive.google.com/file/d/1oqx5JAtTVLaSI1AP8cRRMZrTtwlj_oGU/view)

## Installation

- git clone 
- cd AirBnB_clone
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Authors:
 * [Andres Bayona](https://github.com/AndrewB4y)
 * [Karen Campo](https://github.com/KarenCampo777)
