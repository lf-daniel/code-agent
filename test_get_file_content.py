from functions.get_file_content import get_file_content


def lorem_test() -> None:
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    #print(result[:50])
    print(f"lorem.txt truncated: {'truncated' in result}")

def test() -> None:
    test_cases = [
        ('calculator', 'main.py'),
        ('calculator', 'pkg/calculator.py'),
        ('calculator', '/bin/cat'),
        ('calculator', 'pkg/does_not_exist.py'),
    ]

    for test_case in test_cases:
        result = get_file_content(test_case[0], test_case[1])
        print(f'{test_case[1]} length: {len(result)}')
        print(result)
        print()

if __name__ == "__main__":
    lorem_test()
    test()
