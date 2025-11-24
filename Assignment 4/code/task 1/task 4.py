import subprocess
import platform
import os
import getpass

def system_info():
    print("===== System Information =====")
    
    # Kernel version
    kernel = platform.uname().release
    print(f"Kernel Version: {kernel}")
    
    # Current user
    user = getpass.getuser()
    print(f"Current User: {user}")
    
    # CPU / Hardware info (Virtualization)
    try:
        output = subprocess.check_output("lscpu", text=True)
        for line in output.splitlines():
            if "Virtualization" in line:
                print(f"{line.strip()}")
    except Exception as e:
        print(f"Could not fetch CPU info: {e}")

def detect_vm():
    print("\n===== VM Detection =====")
    try:
        virt = subprocess.check_output("systemd-detect-virt", text=True).strip()
        if virt != "none":
            print(f"Virtual Machine detected: {virt}")
        else:
            print("No VM detected. Running on physical machine.")
    except Exception as e:
        print(f"Could not detect VM: {e}")

if __name__ == "__main__":
    system_info()
    detect_vm()
