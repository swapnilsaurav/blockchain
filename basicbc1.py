import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + self.timestamp + self.data + self.previous_hash
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []

    def create_genesis_block(self):
        genesis_block = Block(0, time.ctime(), "Genesis Block", "0")
        self.chain.append(genesis_block)
        print("Genesis Block Created.")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.ctime(), data, latest_block.hash)
        self.chain.append(new_block)
        print("New Block Added.")

    def print_chain(self):
        for block in self.chain:
            print("\nIndex:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

def menu():
    bc = Blockchain()
    while True:
        print("\n--- Blockchain Menu ---")
        print("1. Create Genesis Block")
        print("2. Add New Block")
        print("3. Print Blockchain")
        print("4. Validate Blockchain")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            if not bc.chain:
                bc.create_genesis_block()
            else:
                print("Genesis block already exists.")
        elif choice == '2':
            if not bc.chain:
                print("Create the genesis block first.")
            else:
                data = input("Enter data for the block: ")
                bc.add_block(data)
        elif choice == '3':
            if not bc.chain:
                print("Blockchain is empty.")
            else:
                bc.print_chain()
        elif choice == '4':
            if bc.is_chain_valid():
                print("Blockchain is valid.")
            else:
                print("Blockchain is not valid!")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()
