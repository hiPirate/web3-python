from web3 import Web3
from solcx import compile_source

# Solidity source
compiled_sol = compile_source(
    '''
    pragma solidity >0.5.0;

    contract TestContract {
        string public message;

        constructor() public {
            message = '0';
        }

        function setMessage(string memory _message) public {
            message = _message;
        }

        function getMessage() view public returns (string memory) {
            return message;
        }
    }
    '''
)

# Get the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# Get the bytecode/bin
bytecode = contract_interface['bin']

# Get the abi
abi = contract_interface['abi']

# Setup the web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

# Set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

# Build the contract
TestContract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Prints the contract to the console
print("Contract:")
print(TestContract)

# Submit the transaction that deploys the contract
tx_hash = TestContract.constructor().transact()

# Prints the transaction hash to the console
print("Hash:")
print(tx_hash)

# Wait for the transaction to be mined and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Prints the transaction receipt to the console
print("Receipt:")
print(tx_receipt)

# Gets contract
testContract = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# Prints the contract to the console
print("Contract:")
print(testContract)

# Prints '0' to the console
print(testContract.functions.getMessage().call())

# Set the message to '1'
tx_hash = testContract.functions.setMessage('1').transact()

# Prints the transaction hash to the console
print("Hash:")
print(tx_hash)

# Wait for the transaction to be mined and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Prints the transaction receipt to the console
print("Receipt:")
print(tx_receipt)

# Prints the message '1' to the console
print(testContract.functions.getMessage().call())