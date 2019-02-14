import os
import json
import hashlib
import time

def read_json(path):
    return json.load(open(path))

def get_size_of_file_by_path(path):
    return os.path.getsize(path)

def get_list_of_files_of_dir(blockChain_dir):
    return os.listdir(blockChain_dir)

def get_list_of_files_of_dir_sorted(path):
    return sorted([int(i) for i in get_list_of_files_of_dir(path)])

def get_last_file_name(blockChain_dir):
    files = get_list_of_files_of_dir_sorted(blockChain_dir)
    return 0 if files == [] else files[-1]

def write_to_file(path, data):
        with open(path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)

def calculate_hash_of_json_block(block):
    return hashlib.md5(json.dumps(block, indent=4, sort_keys=True).encode('utf-8')).hexdigest()

def read_file(path):
    return open(path, 'rb').read()

def calculate_hash_of_file_by_path(path):
    file = read_file(path)
    return hashlib.md5(file).hexdigest()

def get_free_size():
    return int(os.popen("df / --output=avail| tail -1").read())

def get_time():
    return time.time()
