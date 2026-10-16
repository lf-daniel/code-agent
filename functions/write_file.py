import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        wd_abspath = os.path.abspath(working_directory)
        file_abspath = os.path.normpath(os.path.join(wd_abspath, file_path))
        if wd_abspath != os.path.commonpath([wd_abspath, file_abspath]):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_abspath):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        #check/make parent directories
        os.makedirs(os.path.dirname(file_abspath), exist_ok=True)
        #open file in write Mode and write contents
        with open(file_abspath, "w") as f:
            if f.write(content) == len(content):
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            raise Exception('Error: failed to write')

    except Exception as err:
        return f'Error: Unexpected {err=}, {type(err)=}'
