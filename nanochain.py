import hashlib
import time

def calculate_hash(index, timestamp, data, previous_hash, nonce):
    """Calculates the SHA-256 hash of a block's contents."""
    block_string = f"{index}{timestamp}{data}{previous_hash}{nonce}".encode()
    return hashlib.sha256(block_string).hexdigest()

def proof_of_work(block, difficulty=3):
    """
    Finds a nonce that produces a hash matching the difficulty target.
    Target: Hash must start with '0' * difficulty
    """
    target = '0' * difficulty
    nonce = 0
    while True:
        # Calculate a potential hash with the current nonce
        hash_attempt = calculate_hash(
            block['index'],
            block['timestamp'],
            block['data'],
            block['previous_hash'],
            nonce
        )

        # Check if the hash meets the difficulty requirement
        if hash_attempt.startswith(target):
            # Nonce found, return it
            return nonce, hash_attempt
        else:
            # Increment the nonce and try again
            nonce += 1

# Example Usage:
new_block_data = {
    'index': 2,
    'timestamp': time.time(),
    'data': 'A simple transaction',
    'previous_hash': 'abcdef12345'
}

print("Starting minimal mining...")
nonce_found, valid_hash = proof_of_work(new_block_data)

print(f"\nMining successful!")
print(f"Nonce: {nonce_found}")
print(f"Block Hash: {valid_hash}")
