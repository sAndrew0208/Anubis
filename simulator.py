from attacker.attacker import AttackerAI
import hashlib
import time
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def simulate_battle():
    # ASCII art for drip :)
    print(Fore.CYAN + r"""
     █████  ███    ██ ██    ██ ██████  ██ ███████ 
    ██   ██ ████   ██ ██    ██ ██   ██ ██ ██      
    ███████ ██ ██  ██ ██    ██ ██████  ██ ███████ 
    ██   ██ ██  ██ ██  ██  ██  ██   ██ ██      ██ 
    ██   ██ ██   ████   ████   ██████  ██ ███████ 
    """)
    print(Fore.YELLOW + "AI vs AI: Password Security Showdown (Judge Mode)\n" + Style.RESET_ALL)

    # Judge inputs password
    while True:
        password = input(Fore.BLUE + "[Judge] Enter a 4-character password (letters/digits only): " + Style.RESET_ALL).strip()
        if len(password) == 4 and password.isalnum():
            break
        print(Fore.RED + "⚠️ Password must be exactly 4 characters and alphanumeric. Try again.")

    target_hash = hashlib.sha256(password.encode()).hexdigest()

    # Attacker setup
    attacker = AttackerAI()
    start_time = time.time()

    print(f"\n[Defender] 🔒 Hashed password: {Fore.BLUE}{target_hash}")
    print(f"[Attacker] {Fore.RED}🚀 Initiating brute-force attack...{Style.RESET_ALL}")

    # execute the attack
    cracked = attacker.brute_force_attack(target_hash)

    # Display results
    if cracked:
        print(f"\n💥 {Fore.RED}[Attacker] CRACKED! Password: {Fore.RED}{cracked}{Style.RESET_ALL}")
    else:
        print(f"\n🛡️ {Fore.GREEN}[Defender] VICTORY! Attack failed.{Style.RESET_ALL}")

    print(f"\n🔑 {Fore.CYAN}Original password: {Fore.GREEN}{password}{Style.RESET_ALL}")
    print(f"⏱️ {Fore.YELLOW}Time taken: {time.time() - start_time:.2f}s{Style.RESET_ALL}" "Type in Python simulator.py to play again!")

if __name__ == "__main__":
    simulate_battle()