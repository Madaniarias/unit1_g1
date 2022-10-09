# Crypto Wallet

![cardano-meme-funny-cardano](https://user-images.githubusercontent.com/111761417/194739670-ee0ee505-57ce-4f73-b249-a0cce53ec717.gif)
<sub>Illustration by Cryptomkg</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

Design statement:
I will design and make a Crypto Wallet for a client who is local trader. The project will be about designing a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics and is constructed using the software Python 3.10.7. It will take about 3 weeks to make and will be evaluated according to the criteria below.

For this project, the cryptocurrency used will be Cardano.

Cardano is one of the biggest cryptocurrencies by market cap. It’s designed to be a flexible, sustainable, and scalable blockchain platform for running smart contracts — which will allow the development of a wide range of decentralized finance apps, new crypto tokens, games, and more. Cardano’s goal is to be the most environmentally sustainable blockchain platform. It uses a unique proof-of-stake consensus mechanism called Ouroboros, as opposed to the energy-intensive proof-of-work system currently used by Bitcoin and Ethereum. (Ethereum is also moving to a proof-of-stake system via the ETH2 upgrade). Cardano was launched in September 2017 by Ethereum co-founder Charles Hoskinson, and aims to be a third-generation blockchain (or blockchain 3.0) project — building on top of the technology pioneered by Bitcoin (first gen) and Ethereum (second gen). Cardano’s goal is to be a highly scalable and energy-efficient smart contract platform. In the second quarter of 2021, smart contract functionality is scheduled to arrive on the Cardano platform. Developers have also announced that the blockchain will become compatible with Ethereum-based smart contracts later in the year — potentially allowing it to run a wide range of existing apps and allowing developers to work on Cardano projects using the familiar Solidity programming language ([1])(https://www.coinbase.com/learn/crypto-basics/what-is-cardano)
The values of Cardano as of Sunday, October 2 is around 62.33 Japanese yen.

1. What is Cardano? Coinbase. September 23, 2022. https://www.coinbase.com/learn/crypto-basics/what-is-cardano

Justify the tools/structure of your solution

The following arguments make python a good tool for the solution of this project:
- It is a free software.
- Python is cross-platform and will work on Windows, macOS, and Linux so it will be accesible form almost any computer.
- Does not take much space and is easye to download (It can be download from their webpage in a matter of minutes).

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger displays records of transactions by month.
5. The electronic ledger diplays month to month to statistics: max income value, minumun balance, mean income.
6. The electronic ledger is protected by a password to gain access to the data.

# Criteria B: Design

## System Diagram

![image](https://user-images.githubusercontent.com/111761417/194739407-aeb7a1a7-aad3-451c-a7a5-07efc3689de7.png)


## Flow Diagrams

### FUNCTION VALIDATE_INT_INPUT

![image](https://user-images.githubusercontent.com/111761417/194739562-326b85ad-57e6-4a8c-a67b-834aaf3a60ec.png)

### FUNCTION VALIDATE_MONTH

![image](https://user-images.githubusercontent.com/111761417/194739540-9d33d699-437c-4f3f-9f73-c0e3462654bf.png)

### FUNCTION_SIMPLE_LOGIN

![image](https://user-images.githubusercontent.com/111761417/194739593-194266e3-b51f-4d49-a832-80487fe5e613.png)
![image](https://user-images.githubusercontent.com/111761417/194739615-a0a8327e-3976-43a0-8a1d-4cf479d42670.png)

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                                         | To have a clear idea of the hardware and software requirements for the proposed solution  | 10min         | Sep 22                 | B         |
| 2.      | Flow diagram login.  |   Created a flow diagram for the login system | 10 min | Sep 27 | B
| 3.      | Code and test login  | Code and tested login system | 50 min | Sep 27 | C
| 4.      | Test login　　　　　　| Login system runs             | 2 min  | Sep 27 | D


