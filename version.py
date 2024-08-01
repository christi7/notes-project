import argparse
import os

VERSION_FILE = "version.txt"

def read_version():
    if not os.path.exists(VERSION_FILE):
        return [0, 0, 0]
    with open(VERSION_FILE, 'r') as file:
        version = file.read().strip().split('.')
    return [int(v) for v in version]

def write_version(version):
    with open(VERSION_FILE, 'w') as file:
        file.write('.'.join(map(str, version)))

def update_version(part):
    version = read_version()
    if part == "major":
        version[0] += 1
        version[1] = 0
        version[2] = 0
    elif part == "minor":
        version[1] += 1
        version[2] = 0
    elif part == "patch":
        version[2] += 1
    write_version(version)

def get_full_version():
    version = read_version()
    return '.'.join(map(str, version))

def main():
    parser = argparse.ArgumentParser(description="Version Manager")
    parser.add_argument('command', choices=['get', 'update_major', 'update_minor', 'update_patch'], help="Command to execute")
    args = parser.parse_args()

    if args.command == 'get':
        print(get_full_version())
    elif args.command == 'update_major':
        update_version('major')
    elif args.command == 'update_minor':
        update_version('minor')
    elif args.command == 'update_patch':
        update_version('patch')

if __name__ == "__main__":
    main()
