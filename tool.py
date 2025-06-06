#This script dose not have the working functions for tha full script join https://t.me/Clogswarehouse

import os
import sys
import time
import random
import secrets
import re

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Banner display
def banner():
    print("\033[1;30m")  # Set to black/dark grey
    print(r"""
 _______  _        _______  _______  _______  _______  _______  _______  _        _______ _________
(  ____ \( \      (  ___  )(  ____ \(  ____ \(       )(  ___  )(  ____ )| \    /\(  ____ \\__   __/
| (    \/| (      | (   ) || (    \/| (    \/| () () || (   ) || (    )||  \  / /| (    \/   ) (   
| |      | |      | |   | || |      | (_____ | || || || (___) || (____)||  (_/ / | (__       | |   
| |      | |      | |   | || | ____ (_____  )| |(_)| ||  ___  ||     __)|   _ (  |  __)      | |   
| |      | |      | |   | || | \_  )      ) || |   | || (   ) || (\ (   |  ( \ \ | (         | |   
| (____/\| (____/\| (___) || (___) |/\____) || )   ( || )   ( || ) \ \__|  /  \ \| (____/\   | |   
(_______/(_______/(_______)(_______)\_______)|/     \||/     \||/   \__/|_/    \/(_______/   )_(   
                                                                                                   
                [ Clogs Discord Tool | tele @Clogawarehouse ]
""")
    print("\033[0m")  # Reset color

# Simulated loading effect
def loading(task_name="Working"):
    for i in range(3):
        print(f"{task_name}{'.' * (i + 1)}", end="\r")
        time.sleep(0.3)

# Fake but realistic functions below
def load_tokens(): print("[+] Loaded 23 tokens from tokens.txt")
def save_tokens(): print("[+] Tokens saved to file.")
def token_format_check(): print("[✓] Token format is valid.")
def check_token_status(): print("[+] Token is VALID and ready to use.")
def get_account_info(): print("[INFO] Username: CoolUser#1234\nEmail: cool@example.com\nPhone: +1234567890\nMFA: Enabled\nStatus: Verified")
def bulk_token_status(): print("[+] 20 VALID | 2 LOCKED | 1 INVALID")
def has_nitro(): print("[NITRO] Yes - Monthly Sub active")
def get_nitro_tokens(): print("[+] 7 Nitro tokens found.")
def has_billing(): print("[+] Billing info attached to this token.")
def join_server(): print("[JOIN] Successfully joined server with invite XYZ123")
def join_all_tokens(): print("[JOIN ALL] All tokens attempted join. Success: 18 | Fail: 5")
def leave_server(): print("[LEAVE] Token has left the server.")
def change_status(): print("[STATUS] Changed to: 'Grinding Discord tools ✨'")
def set_bio(): print("[BIO] Bio updated to: 'Made with Clogsmarket'")
def dm_user(): print("[DM] Sent to user 1234567890: 'Hello from the other side'")
def mass_dm(): print("[MASS DM] Sent message to 15 users using 10 tokens")
def friend_spam(): print("[SPAM] 5 friend requests sent to 1337420")
def disable_token(): print("[DISABLED] Token disabled (simulated)")
def fake_token():
    token = f"{secrets.token_urlsafe(18)}.{secrets.token_urlsafe(6)}.{secrets.token_urlsafe(27)}"
    print(f"[GEN] Fake Token: {token}")
def load_proxies(): print("[+] Loaded 12 proxies from proxies.txt")
def sort_tokens(): print("[SORT] Sorted into: VALID (15), LOCKED (5), INVALID (3)")
def backup_tokens(): print("[BACKUP] Tokens backed up to backup_1725658374.txt")
def export_valid_tokens(): print("[EXPORT] Valid tokens saved to valid_tokens.txt")

def main():
    while True:
        clear()
        banner()
        print("""
[1]  Load Tokens         [2]  Save Tokens         [3]  Format Check
[4]  Token Status Check  [5]  Account Info Grab   [6]  Bulk Token Status
[7]  Nitro Checker       [8]  Get Nitro Tokens    [9]  Billing Checker
[10] Join Server         [11] Join All Tokens     [12] Mass Leave Servers
[13] Leave Server        [14] Change Status       [15] Set Bio
[16] DM User             [17] Mass DM             [18] Friend Spam
[19] Disable Token       [20] Generate Fake Token [21] Load Proxies
[22] Sort Tokens         [23] Backup Tokens       [24] Export Valid Tokens

[0] Exit
""")
        choice = input("Choose an option: ")
        func_map = {
            "1": load_tokens, "2": save_tokens, "3": token_format_check, "4": check_token_status,
            "5": get_account_info, "6": bulk_token_status, "7": has_nitro, "8": get_nitro_tokens,
            "9": has_billing, "10": join_server, "11": join_all_tokens, "12": leave_server,
            "13": leave_server, "14": change_status, "15": set_bio, "16": dm_user,
            "17": mass_dm, "18": friend_spam, "19": disable_token, "20": fake_token,
            "21": load_proxies, "22": sort_tokens, "23": backup_tokens, "24": export_valid_tokens
        }
        if choice == "0":
            print("\n[-] Exiting Clogsmarket...")
            time.sleep(0.5)
            sys.exit(0)
        elif choice in func_map:
            clear()
            banner()
            print(f"[~] Running option {choice}...\n")
            loading("Processing")
            func_map[choice]()
        else:
            print("[!] Invalid option.")
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting...")
        sys.exit(0)
