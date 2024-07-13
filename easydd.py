import os
import time

print("Please enter your password to continue.")
os.system("sudo e")
os.system("clear")

def warn():
    print(f"You have ran EasyDD. Please note that this tool can wipe your USB drive.")
    print(f"1. Start the tool.")
    print(f"2. Exit")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        custom_iso = input("Enter the path to your own ISO file: ")
        if os.path.exists(custom_iso):
            return custom_iso
        else:
            print("File not found.")
            return None
    else:
        print("Invalid choice.")
        return None

def main():
    iso_path = warn()
    if iso_path is None:
        print("Invalid choice. Exiting.")
        return

    if iso_path.startswith("http"):
        download_iso(iso_path)
        iso_path = os.path.basename(iso_path)

    drive = select_drive()

    confirmation = input(f"WARNING: All partitions on /dev/{drive} will be erased. Continue? (yes/no): ")
    if confirmation.lower() == 'yes':
        os.system(f"sudo wipefs --all /dev/{drive}")
        os.system(f"sudo umount /dev/{drive}*")
        flash_distro(iso_path, drive)
        print("Flashing complete.")
    else:
        print("Operation aborted.")


def select_drive():
    print("Select the drive to flash your ISO:")
    drives = os.listdir('/dev/')
    for i, drive in enumerate(drives):
        print(f"{i+1}. {drive}")
    choice = int(input("Enter the drive number: "))
    selected_drive = drives[choice - 1]
    return selected_drive

def flash_distro(iso_path, drive):
    print("Now flashing...")
    os.system(f"sudo dd if={iso_path} of=/dev/{drive} bs=4M status=progress")




if __name__ == "__main__":
    main()
