import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    #check if allowed to operate here
    try:
        wd_abspath = os.path.abspath(working_directory)
        file_abspath = os.path.normpath(os.path.join(wd_abspath, file_path))
        if wd_abspath != os.path.commonpath([wd_abspath, file_abspath]):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_abspath):
            return f'Error: "{file_path}" is not a file or is missing'

    #return content as string
        with open(file_abspath, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_abspath}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as err:
        return f'Error: Unexpected {err=}, {type(err)=}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Return content from a file, truncated at MAX_CHARS from config.py",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of the file to explore content of, relative to working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}
