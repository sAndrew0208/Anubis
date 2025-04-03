import secrets
import string
import markovify

class DefenderAI:
    def __init__(self):
        self.markov_model = None

    def train_markov(self, dataset_path='data/rockyou_clean.txt'):
        try:
            with open(dataset_path, 'r', encoding='utf-8') as f:
                # Split passwords into individual characters
                passwords = [list(line.strip()) for line in f if line.strip()]
                # Train a character-level Markov chain
                self.markov_model = markovify.Chain(passwords, state_size=2)
        except Exception as e:
            print(f"Error training Markov model: {e}")
            self.markov_model = None

    def generate_password(self, length=12, use_markov=True):
        if use_markov and self.markov_model:
            try:
                # Generate password using Markov chain
                return ''.join(self.markov_model.walk())
            except:
                pass  # Fallback to random
        # Random password fallback
        chars = string.ascii_letters + string.digits
        return ''.join(secrets.choice(chars) for _ in range(length))