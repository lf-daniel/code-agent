import os


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        wd_abspath = os.path.abspath(working_directory)
        file_abspath = os.path.normpath(os.path.join(wd_abspath, file_path))
        if wd_abspath != os.path.commonpath([wd_abspath, file_abspath]):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_abspath):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_abspath.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'


    except Exception as err:
        return f'Error: Unexpected {err=}, {type(err)=}'
