from helper import *
from operator import itemgetter

def get_block(path):
    block = read_json(path)
    return block

def get_values(path):
    values = []
    sorted_files = get_list_of_files_of_dir_sorted(path)
    totals = dict()
    totals['total_size'] = 0
    totals['nonce'] = 0
    totals['free_size_in_KB'] = get_free_size()
    for i in reversed(sorted_files):
        block = get_block(path + str(i))
        block['block'] = i

        size_of_block = get_size_of_file_by_path(path + str(i))
        totals['total_size'] += size_of_block
        totals['nonce'] += block['nonce']

        block['size'] = size_of_block
        values.append(block)
    return values, totals

def get_hash_of_block(path):
    file = read_file(path)
    return calculate_hash_of_json_block(path)

def check_block(current_block, next_path, dificulty):
    hash_next_block = read_json(next_path)['prev_hash']
    hash_of_current_block = calculate_hash_of_json_block(current_block)
    return "Ok" if hash_next_block == hash_of_current_block and hash_of_current_block.startswith(dificulty) else "Corrupted"

##### Integrity
# def blockchain_integrity_verification(path, dificulty):
#     sorted_files = get_list_of_files_of_dir_sorted(path)
#     blocks_integrity = []
#     if len(sorted_files) < 1:
#         return list(blocks_integrity)
#     else:
#         for i in sorted_files[1:]:
#             if i > 1 and get_block(path + str(i))['nonce'] != 0:
#                 block_number = str(i - 1)
#                 block_result = check_block(path + str(i), calculate_hash_of_file_by_path(path + str(i - 1)), dificulty)
#                 blocks_integrity.append({'block': block_number, 'result': block_result})
#     return list(blocks_integrity)
def blockchain_integrity_verification(path, dificulty):
    sorted_files = get_list_of_files_of_dir_sorted(path)
    blocks_integrity = []
    if len(sorted_files) < 1:
        return list(blocks_integrity)
    else:
        for i in reversed(sorted_files):
            current_block = get_block(path + str(i))
            if current_block['nonce'] == 0:
                continue
            if i < sorted_files[-1] and get_block(path + str(i + 1))['nonce'] != 0:
                blocks_integrity.append({'block': i, 'result': check_block(current_block, path + str(i + 1), dificulty)})
                continue
            if calculate_hash_of_json_block(current_block).startswith(dificulty):
                blocks_integrity.append({'block': i, 'result': 'Ok'})
            else:
                blocks_integrity.append({'block': i, 'result': 'Corrupted'})
    return list(blocks_integrity)

##### MAINING

def calculate_nonce(block, dificulty):
    complete = False
    n = 0
    print(block.items())
    while complete == False:
        n = n + 1
        block['nonce'] = n
        curr_hash = calculate_hash_of_json_block(block)
        if curr_hash.startswith(dificulty):
            complete = True
    return block

def block_chain_maining(path, dificulty):
    sorted_files = get_list_of_files_of_dir_sorted(path)
    values = []
    block_mined = []
    for i in sorted_files:
        block = get_block(path + str(i))
        if block['nonce'] != 0:
            continue
        if i <= 1:
            block['prev_hash'] = ""
        else:
            block['prev_hash'] = calculate_hash_of_file_by_path(path + str(i-1))
        block = calculate_nonce(block, dificulty)
        block_mined.append(block)
        write_to_file(path + str(i), block)
    return block_mined

def create_block(path, block):
    file_name = get_last_file_name(path)
    file_name += 1
    if "nonce" not in block:
        block["nonce"] = 0
    write_to_file(path + str(file_name), block)

def vefirfic_need_mining(values):
    for value in values:
        if value['nonce'] == 0:
            return True
    return False
