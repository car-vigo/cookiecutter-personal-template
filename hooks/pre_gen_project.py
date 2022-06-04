from distutils.log import ERROR
import os 
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_COLOR = "\x1b[0m"

print(f"{MESSAGE_COLOR} Creting project at {os.getcwd()}{RESET_COLOR}")