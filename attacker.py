import itertools
import hashlib
from tqdm import tqdm
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class AttackerAI:  
    def brute_force_attack(self, target_hash, max_length=4):
        charset = string.ascii_letters + string.digits  # A-Z, a-z, 0-9 Hashes for 256-SHA ENCRYPTION
        print(Fore.MAGENTA + "\n🔍 Brute-forcing all combinations up to 4 characters...")
        for length in range(1, max_length + 1):
            total_guesses = len(charset) ** length
            with tqdm(itertools.product(charset, repeat=length), 
                      desc=Fore.CYAN + "Cracking", 
                      total=total_guesses,
                      bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}") as pbar:
                for guess_tuple in pbar:
                    guess = ''.join(guess_tuple)
                    if hashlib.sha256(guess.encode()).hexdigest() == target_hash:
                        return guess
        return None