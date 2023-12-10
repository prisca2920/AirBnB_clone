#!/usr/bin/python3
"""Command interpreter to execute the hbnb console"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """Hbnb console"""

    prompt = "(hbnb) "
    classes = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }

    def do_quit(self, arg):
        """command to exit the program"""
        return True

    def do_EOF(self, arg):
        """what to do at end of file"""
        return True

    def emptyline(self):
        """if an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance and saves it"""
        if not self.check_class(arg):
            return
        instance = HBNBCommand.classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """prints a str rep of an instance"""

        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in HBNBCommand.classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance based on cls name and id"""
        try:
            if not line:
                raise SyntaxError()
            the_list = line.split(" ")
            if the_list[0] not in HBNBCommand.classes:
                raise NameError()
            if len(the_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = the_list[0] + '.' + the_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all str rep of all instances"""
        the_list = []

        if line == "":
            for value in storage.all().values():
                the_list.append(str(value))
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in storage.all().keys():
                if line in key:
                    the_list.append(str(storage.all()[key]))

        print(the_list)

    def do_update(self, line):
        """updates an attr"""
        try:
            if not line:
                raise SyntaxError()
            the_list = split(line, " ")
            if the_list[0] not in HBNBCommand.classes:
                raise NameError()
            if len(the_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = the_list[0] + '.' + the_list[1]
            if key not in objects:
                raise KeyError()
            if len(the_list) < 3:
                raise AttributeError()
            if len(the_list) < 4:
                raise ValueError()
            value = objects[key]
            try:
                value.__dict__[the_list[2]] = eval(the_list[3])
            except Exception:
                value.__dict__[the_list[2]] = the_list[3]
                value.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, line):
        """counts no. of instances"""
        counter = 0
        try:
            the_list = split(line, " ")
            if the_list[0] not in HBNBCommand.classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == the_list[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
