import argparse
import getopt
import os
import pathlib
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("day_number_and_name")

    args = parser.parse_args()
    day_number_and_name = args.day_number_and_name

    with open("Templates/Solver.py.template", "r") as solver_template_file:
        solver_content = solver_template_file.read().format(day_number_and_name)
    with open(f"Solvers/{day_number_and_name}.py", "w") as solver_file:
        solver_file.write(solver_content)

    with open("Templates/SolverTest.py.template", "r") as solver_test_template_file:
        solver_test_content = solver_test_template_file.read().format(day_number_and_name)
    with open(f"Tests/{day_number_and_name}Test.py", "w") as solver_test_file:
        solver_test_file.write(solver_test_content)

    pathlib.Path(f"InputData/Real/{day_number_and_name}.txt").touch()
    pathlib.Path(f"InputData/Examples/{day_number_and_name}").mkdir()
    for part in [1,2]:
        for exemple in [1]:
            pathlib.Path(f"InputData/Examples/{day_number_and_name}/Part{part}-{exemple}.txt").touch()
            pathlib.Path(f"InputData/Examples/{day_number_and_name}/Part{part}-{exemple}A.txt").touch()
