import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    #check if allowed to operate here
    try:
        wd_abspath = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(wd_abspath, directory))
        valid_target_dir = wd_abspath == os.path.commonpath([wd_abspath, target_dir])
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        #print(f'Success: "{target_dir}" is within the working directory')
    except Exception as err:
        print(f'Error: Unexpected {err=}, {type(err)=}')

    #list content
    try:
        file_infos = []
        for item in os.listdir(target_dir):
            filepath = os.path.join(target_dir, item)
            size_str: str = f'file_size={os.path.getsize(filepath)}bytes'
            dir_str: str = f'is_dir={os.path.isdir(filepath)}'
            file_infos.append(f"- {item}: {size_str}, {dir_str}")
        return '\n'.join(file_infos)
    except Exception as err:
        return f'Error: Unexpected {err=}, {type(err)=}'
