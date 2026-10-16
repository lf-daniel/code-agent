from functions.write_file import write_file


def test() -> None:
    test_cases = [
        ('calculator', "lorem.txt", "wait, this isn't lorem ipsum"),
        ('calculator', "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ('calculator', "/tmp/temp.txt", "this should not be allowed"),
    ]

    for test_case in test_cases:
        result = write_file(test_case[0], test_case[1], test_case[2])
        print(result)
        print()

if __name__ == "__main__":
    test()
