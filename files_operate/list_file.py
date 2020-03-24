import os
import subprocess


def dir_list(path, all_file):
    file_list = os.listdir(path)
    all_dir_file = ''
    for filename in file_list:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dir_list(filepath, all_file)
        else:
            if filename.split('.')[-1] in ['rtv', 'gps', 'img', 'py']:
                if all_dir_file == '':
                    all_dir_file = filename
                else:
                    all_dir_file = all_dir_file + ":" + filename
    if all_dir_file != '':
        command = 'meta-generator -i %s --add_bindings_file "%s" --add_bindings_type "rtv:gps"' % (path, all_dir_file)
        print(command)
        subprocess.call(command, shell=True)
    # all_file.append(all_dir_file)

    return all_file


dir_list('../', [])

