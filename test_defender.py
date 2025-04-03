from defender.defender import DefenderAI

defender = DefenderAI()
defender.train_markov()

# Generate 5 passwords to test
for _ in range(5):
    password = defender.generate_password()
    print("Generated Password:", password)