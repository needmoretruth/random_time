import hashlib
import os
import time


def hash_mine():
    print("hi")
    difficulty = int(input("difficulty(0 amount): "))
    if difficulty <= 0:
        print("difficulty need bigger than 0")
        return
    elif difficulty > 64:
        print("difficulty need smaller than 64")
        return
    elif difficulty > 8:
        print("i think this is very hard")
        print("you think it is so slow")
        print("press Ctrl+C to stop")
        time.sleep(2)
    nonce = 0
    data = os.urandom(16).hex()
    block = data + str(nonce)
    hash_result = hashlib.sha256(block.encode()).hexdigest()
    start_time = time.time()
    while hash_result[:difficulty] != "0" * difficulty:
        nonce += 1
        block = data + str(nonce)
        hash_result = hashlib.sha256(block.encode()).hexdigest()
    end_time = time.time()
    run_time = end_time - start_time
    print(f"run time: {run_time:.8f} seconds")
    print(f"count: {nonce}")
    nonce = nonce / run_time
    print("average count per second: ", nonce)
    print(f"hash result: {hash_result}")
    print(f"data: {data}")
