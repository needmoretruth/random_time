import hashlib
import os
import random
import sys
import time


def get_version():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                return lines[-1].strip()
    except Exception:
        return ""
    return ""


def menu():
    version = get_version()
    while True:
        try:
            width = os.get_terminal_size().columns - 5
        except Exception:
            width = 40

        print("\n" + "=" * width)
        title = f"NMT Test {version}".center(width)
        print(title)
        print("-" * width)
        print(" 1. run")
        print(" 2. setting")
        print(" 3. debug")
        print(" 4. exit")
        print("=" * width)

        choice = input("select option >> ").strip()

        if not choice:
            print("please enter number")
            time.sleep(1)
            continue

        if choice == "1":
            run()
        elif choice == "2":
            setting()
        elif choice == "3":
            debug()
        elif choice == "4":
            print("bye bye")
            sys.exit()
        else:
            print(f"'{choice}' is wrong please try other number")
            time.sleep(1)


def run():
    while True:
        print("\n--- run menu ---")
        print(" 1. random generation")
        print(" 2. sum loop")
        print(" 3. power loop")
        print(" 4. odd even")
        print(" 5. hash mine")
        print(" 6. back")

        choice = input("select run option >> ").strip()

        if choice == "1":
            random_generation()
        elif choice == "2":
            sum_loop()
        elif choice == "3":
            power_loop()
        elif choice == "4":
            odd_even()
        elif choice == "5":
            hash_mine()
        elif choice == "6":
            break
        else:
            print("wrong choice")


def random_generation():
    a = 0
    count = 0
    max_num = int(input("max number: "))
    if max_num <= 0:
        print("max number need bigger than 0")
        return
    answer = int(input("how many times: "))
    if answer <= 0:
        print("answer need bigger than 0")
        return
    start_time = time.time()
    while answer > a:
        random_num = random.randint(1, max_num)
        count += 1
        if random_num == 1:
            a += 1
    end_time = time.time()
    run_time = end_time - start_time
    print(f"run time: {run_time:.8f} seconds")
    run_time = run_time / answer
    print(f"average time: {run_time:.8f} seconds")
    print(f"count: {count:,}")
    count = count // answer
    print(f"average count: {count:,}")


def sum_loop():
    a = 0
    max_num = int(input("max number: "))
    if max_num <= 0:
        print("max number need bigger than 0")
        return
    start_time = time.time()
    while max_num > a:
        a += 1
    end_time = time.time()
    run_time = end_time - start_time
    print(f"run time: {run_time:.8f} seconds")


def power_loop():
    print("comming soon")
    input("\npress enter to go back")


def odd_even():
    print("comming soon")
    input("\npress enter to go back")


def hash_mine():
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
    hash_result = hashlib.sha256(str(nonce).encode()).hexdigest()
    start_time = time.time()
    while hash_result[:difficulty] != "0" * difficulty:
        nonce += 1
        hash_result = hashlib.sha256(str(nonce).encode()).hexdigest()
    end_time = time.time()
    run_time = end_time - start_time
    print(f"run time: {run_time:.8f} seconds")
    print(f"count: {nonce}")
    nonce = nonce / run_time
    print("average count per second: ", nonce)
    print(f"hash result: {hash_result}")


def setting():
    print("\ncomming soon")
    input("\npress enter to go back")


def debug():
    print("\ncomming soon")
    input("\npress enter to go back")


if __name__ == "__main__":
    print("welcome to nmt-test")
    time.sleep(0.5)
    menu()
