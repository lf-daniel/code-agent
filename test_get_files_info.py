from functions.get_files_info import get_files_info


def test() -> None:
    test_cases = [
        ('calculator', '.', 'current'),
        ('calculator', 'pkg'),
        ('calculator', '/bin'),
        ('calculator', '../'),
        # ('calculator', 'main.py')
    ]

    for test_case in test_cases:
        result = get_files_info(test_case[0], test_case[1])
        print(f'Result for {test_case[2] if len(test_case) > 2 else f'\'{test_case[1]}\''} directory:')
        print(result)
        print()

#     result = get_files_info("calculator", ".")
#     print("Result for current directory:")
#     print(result)
#     print("")
#
#     result = get_files_info("calculator", "pkg")
#     print("Result for 'pkg' directory:")
#     print(result)
#     print("")
#
#     result = get_files_info("calculator", "/bin")
#     print("Result for '/bin' directory:")
#     print(result)
#     print("")
#
#     result = get_files_info("calculator", "../")
#     print("Result for '../' directory:")
#     print(result)
#     print("")

    # result = get_files_info("calculator", "main.py")
    # print("Result for 'main.py':")
    # print(result)


if __name__ == "__main__":
    test()
