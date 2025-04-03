from attacker.attacker import AttackerAI
import hashlib

def test_attack():
    # Use a KNOWN password from rockyou.txt (e.g., "password" or "123456")
    test_password = "password"  # This is in the first 5k lines of rockyou.txt
    test_hash = hashlib.sha256(test_password.encode()).hexdigest()

    attacker = AttackerAI()
    print(f"Testing attack on password: {test_password}")
    cracked = attacker.hybrid_attack(test_hash)

    if cracked:
        print(f"\n[SUCCESS] Cracked: {cracked}")
    else:
        print("\n[FAILURE] Attack failed. Adjust parameters.")

if __name__ == "__main__":
    test_attack()