import re
from collections import Counter
import argparse
import sys

parser = argparse.ArgumentParser()

def parsing(filepath):
    users = Counter()
    ips = Counter()

    try:
        with open(filepath, "r") as f:
            for line in f:
                match = re.search(r"Failed password for (\S+) from (\S+) ", line)
    
                if match:
                    users[f"{match.group(1)}"] += 1
                    ips[f"{match.group(2)}"] += 1
            return users, ips
    
    except FileNotFoundError:
        print("File not exist")
        sys.exit()


def threshold(users, ips, thd):
    msg_ip = []
    msg_user = []
    for user in users:
        if users[user] > thd:
            msg_user.append(f"Suspicious! User {user} : {users[user]} attempts")

    for ip in ips:
        if ips[ip] > thd:
            msg_ip.append(f"Brute force attempted by {ip} : {ips[ip]} attempts")

    return msg_user, msg_ip

def main():
    parser.add_argument("filepath")
    parser.add_argument("--output", default="terminal")
    parser.add_argument("--threshold", type=int, default=5) 
    args = parser.parse_args()
    users, ips = parsing(args.filepath)

    res1, res2 = threshold(users, ips, args.threshold)

    if args.output == "terminal":
        for result in res1:
            print(result + "\n")
        for result in res2:
            print(result + "\n")
    
    elif args.output == "file":
        with open("reports.txt", "a") as f:
            for result in res1:
                f.write(result + "\n")
            for result in res2:
                f.write(result + "\n")


if __name__ == "__main__":
    main()