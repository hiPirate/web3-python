## Tests

---

### **Table of Contents**
  - [Test Web3](#test-web3)
  - [Test Infura Node](#test-infura-node)
  - [Test Deploy](#test-deploy)

---

### Test Web3
Tests if your ``web3`` installation is capable of handling a transaction over the Ethereum testnet.

```bash
python testWeb3.py
```

---

### Infura Node Test
Tests if your Infura Ethereum Node is able to be connected.

First, set your [Infura](https://infura.io/) project API keys in your environment table:
```bash
export WEB3_INFURA_PROJECT_ID=YourProjectID
export WEB3_INFURA_API_SECRET=YourProjectSecret
```

Then run the Python script:
```bash
python testInfuraNode.py
```

If successful, it will print ``True`` in the console.

---

### Test Deploy
Tests if your ``web3`` installation is capable of deploying a contract to Ethereum.

Here is an example of a successful deploy of ``testContract.sol`` after running the test script with ``python testDeploy.py``:
```bash
[pirate@source src]$ python deploy.py
Deployed <stdin>:StoreVar to: 0xF2E246BB76DF876Cef8b38ae84130F4F55De395b

Gas estimate to transact with setVar: 45559
Sending transaction to setVar(255)

Transaction receipt mined:
{'blockHash': HexBytes('0xed6435c7b4882596330d06f1019dd121739fa89eacc749991f67de96a4521eba'),
 'blockNumber': 2,
 'contractAddress': None,
 'cumulativeGasUsed': 44966,
 'gasUsed': 44966,
 'logs': [AttributeDict({'type': 'mined', 'logIndex': 0, 'transactionIndex': 0, 'transactionHash': HexBytes('0x0f340e9f2e97b15fc6652e854bf1aa3f2acb4e75cc298aa132589b0e383f3a03'), 'blockHash': HexBytes('0xed6435c7b4882596330d06f1019dd121739fa89eacc749991f67de96a4521eba'), 'blockNumber': 2, 'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b', 'data': '0x', 'topics': [HexBytes('0x6c2b4666ba8da5a95717621d879a77de725f3d816709b9cbe9f059b8f875e284'), HexBytes('0x00000000000000000000000000000000000000000000000000000000000000ff')]})],
 'status': 1,
 'transactionHash': HexBytes('0x0f340e9f2e97b15fc6652e854bf1aa3f2acb4e75cc298aa132589b0e383f3a03'),
 'transactionIndex': 0}

Was transaction successful?
1
```

---
