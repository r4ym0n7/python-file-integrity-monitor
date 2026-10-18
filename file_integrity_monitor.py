import hashlib
import json
import os

BASELINE_FILE = "baseline.json"
SCAN_DIRECTORY = "test_files"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def scan_directory():
    file_hashes = {}

    for root, directories, files in os.walk(SCAN_DIRECTORY):
        for filename in files:
            filepath = os.path.join(root, filename)

            if filepath == BASELINE_FILE:
                continue

            try:
                file_hashes[filepath] = calculate_hash(filepath)
            except PermissionError:
                print(f"Permission denied: {filepath}")

    return file_hashes


def create_baseline():
    hashes = scan_directory()

    with open(BASELINE_FILE, "w") as file:
        json.dump(hashes, file, indent=4)

    print(f"Baseline created for {len(hashes)} files.")


def check_integrity():
    if not os.path.exists(BASELINE_FILE):
        print("No baseline found.")
        print("Run: python3 file_integrity_monitor.py baseline")
        return

    with open(BASELINE_FILE, "r") as file:
        old_hashes = json.load(file)

    current_hashes = scan_directory()

    modified = []
    new_files = []
    deleted_files = []

    for filepath in current_hashes:
        if filepath not in old_hashes:
            new_files.append(filepath)
        elif current_hashes[filepath] != old_hashes[filepath]:
            modified.append(filepath)

    for filepath in old_hashes:
        if filepath not in current_hashes:
            deleted_files.append(filepath)

    print("\nFILE INTEGRITY MONITOR")
    print("======================")

    if modified:
        print("\nModified files:")
        for filepath in modified:
            print(f"  {filepath}")

    if new_files:
        print("\nNew files:")
        for filepath in new_files:
            print(f"  {filepath}")

    if deleted_files:
        print("\nDeleted files:")
        for filepath in deleted_files:
            print(f"  {filepath}")

    if not modified and not new_files and not deleted_files:
        print("\nNo changes detected.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage:")
        print("  python3 file_integrity_monitor.py baseline")
        print("  python3 file_integrity_monitor.py check")
    elif sys.argv[1] == "baseline":
        create_baseline()
    elif sys.argv[1] == "check":
        check_integrity()
    else:
        print("Unknown command.")
