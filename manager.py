from application import app, manager
from flask_script import Server, Command
from www import *
import traceback
import sys

# web server
manager.add_command('runserver', Server(host='0.0.0.0', use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()
