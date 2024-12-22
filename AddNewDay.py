import argparse
import getopt
import json
import os
import pathlib
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("day_number_and_name")

    args = parser.parse_args()
    day_number_and_name = args.day_number_and_name

    if not pathlib.Path(f"Solvers/{day_number_and_name}.py").exists():
        with open("Templates/Solver.py.template", "r") as solver_template_file:
            solver_content = solver_template_file.read().format(day_number_and_name)
        with open(f"Solvers/{day_number_and_name}.py", "w") as solver_file:
            solver_file.write(solver_content)

    if not pathlib.Path(f"Tests/{day_number_and_name}Test.py").exists():
        with open("Templates/SolverTest.py.template", "r") as solver_test_template_file:
            solver_test_content = solver_test_template_file.read().format(day_number_and_name)
        with open(f"Tests/{day_number_and_name}Test.py", "w") as solver_test_file:
            solver_test_file.write(solver_test_content)

    pathlib.Path(f"InputData/Real/{day_number_and_name}.txt").touch()
    pathlib.Path(f"InputData/Examples/{day_number_and_name}").mkdir(exist_ok=True)
    for part in [1,2]:
        for exemple in [1]:
            pathlib.Path(f"InputData/Examples/{day_number_and_name}/Part{part}-{exemple}.txt").touch()

    with open("InputData/Examples/Tests.json", "r") as input_data_json_file:
        input_data_json = json.loads(input_data_json_file.read())
    if not day_number_and_name in input_data_json:
        input_data_json[day_number_and_name] = {
            f"Part{n}": [{"filename": f"InputData/Examples/{day_number_and_name}/Part{n}-1.txt","answer": None}] for n in [1, 2]}
        with open("InputData/Examples/Tests.json", "w") as input_data_json_file:
            input_data_json_file.write(json.dumps(input_data_json, indent=2))