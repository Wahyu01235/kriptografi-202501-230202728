import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp if timestamp else time.time()
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "nonce": self.nonce
        }

        block_string = json.dumps(block_content, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        start_time = time.time()

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()

        print(f"Block #{self.index} successfully mined")
        print(f"Hash       : {self.hash}")
        print(f"Nonce      : {self.nonce}")
        print(f"Time Taken : {end_time - start_time:.4f} seconds\n")

class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()

        new_block = Block(
            index=previous_block.index + 1,
            previous_hash=previous_block.hash,
            data=data
        )

        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Hash integrity check
            if current.hash != current.calculate_hash():
                print(f"Invalid hash at block {current.index}")
                return False

            # Chain linkage check
            if current.previous_hash != previous.hash:
                print(f"Invalid chain link at block {current.index}")
                return False

        return True

    def tamper_block(self, index, new_data):
        if index <= 0 or index >= len(self.chain):
            return

        print(f"\nTampering block #{index}...\n")
        self.chain[index].data = new_data
        self.chain[index].hash = self.chain[index].calculate_hash()

# ===============================
# TEST TINYCHAIN
# ===============================

my_chain = Blockchain(difficulty=4)

print("Mining block 1...")
my_chain.add_block("A → B : 10 Coin")

print("Mining block 2...")
my_chain.add_block("B → C : 5 Coin")

print("Mining block 3...")
my_chain.add_block("C → D : 2 Coin")

print("Blockchain valid?")
print(my_chain.is_chain_valid())

# ===============================
# ATTACK SCENARIO
# ===============================

my_chain.tamper_block(1, "A → B : 1000 Coin")

print("Blockchain valid after attack?")
print(my_chain.is_chain_valid())
# ===============================