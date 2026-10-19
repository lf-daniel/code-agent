from profile import run

from functions.run_python_file import run_python_file


def test() -> None:
    test_cases = [
        ('calculator', 'main.py'),
        ('calculator', 'main.py', ['3 + 5']),
        ('calculator', 'tests.py'),
        ('calculator', '../main.py'),
        ('calculator', 'nonexistent.py'),
        ('calculator', 'lorem.txt'),
    ]

    for test_case in test_cases:
        if len(test_case) > 2:
            result = run_python_file(test_case[0], test_case[1], test_case[2])
        else:
            result = run_python_file(test_case[0], test_case[1])

        print(result)
        print()

if __name__ == "__main__":
    test()
