import excolour.colourer
import sys
import os

try:
    filename = sys.argv[1]
    # Get rid of the module argument from sys.argv so the target script can use arguments as normal
    sys.argv.pop(0)
    sys.path.insert(0, os.path.dirname(filename))
    exec(open(filename).read())
except IndexError as e:
    print("Missing script to run.")
    print("Correct usage: python -m excolour myscript.py [args]")
    sys.exit()
except FileNotFoundError:
    print("Unable to find script {}".format(filename))
    print("Correct usage: python -m excolour myscript.py [args]")
    sys.exit()
