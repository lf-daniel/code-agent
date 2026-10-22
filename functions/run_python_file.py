import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        wd_abspath = os.path.abspath(working_directory)
        file_abspath = os.path.normpath(os.path.join(wd_abspath, file_path))
        if wd_abspath != os.path.commonpath([wd_abspath, file_abspath]):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_abspath):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_abspath.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ['python', file_abspath]
        if args:
            command.extend(args)
        complete = subprocess.run(
            command,
            cwd = working_directory,
            capture_output = True,
            text = True,
            timeout = 30,
            check = True
        )
        out_str: list[str] = []
        if complete.returncode != 0:
            out_str.append(f"Process exited with code {complete.returncode}")
        if not complete.stdout and not complete.stderr:
            out_str.append('No output produced')
        else:
            if complete.stdout:
                out_str.append(f'STDOUT: {complete.stdout}')
            if complete.stderr:
                out_str.append(f'STDERR: {complete.stderr}')

        return "\n".join(out_str)

    except Exception as err:
        return f'Error: Unexpected {err=}, {type(err)=}'

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "run a python file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of the script to execute, relative to working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type":"string"
                    },
                    "description": "arguments to pass into the function",
                }
            },
            "required": ["file_path"],
        },
    },
}
