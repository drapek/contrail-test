"""
    Prints out debug information.
"""
import sys


def print_out_all_variables(stdout=sys.stdout):
    print("# DEBUG local()=", locals(), file=stdout)
    print("# DEBUG global()=", globals(), file=stdout)
    print("# DEBUG dir()=", dir(), file=stdout)
