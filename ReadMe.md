PROPERTY MANAGEMENT SYSTEM  

Introduction To Blockchain

A blockchain is a network of computers or nodes that continuously records and replicates a digital and
distributed ledger of transactions. Before being permanently added as a new "block" at the end of the
"chain," each transaction must first undergo cryptographical validation via a consensus method carried
out by the nodes. Blockchain is also referred to as a peer-to-peer trustless system because no central
authority is required to approve the transaction.

Blockchain can be compared as a linked list with several transactions at each node. Each transaction
has a hash, which also depends on the hash of the prior transactions. We might therefore conclude that
the sequence of events is crucial. The hash of all subsequent transactions would be altered if we were
to change one transaction in any one place. This is among the factors that make blockchain a potent
method of storing transactions.

Problem Statement

The property management system has problems with security, high transaction costs, and a lack of
transparency.Conflicts between property owners, tenants, and property managers can result from a lack
of transparency into property management.

Due to intermediaries like brokers, attorneys, and service providers, the conventional property
management system has substantial transaction costs.The standard property management system is
centralized, which raises security problems because it depends on a central authority to handle and
secure data.

Solution

This project aims to develop a system for property management with the following characteristics
1. To register new users to the system by taking their username, password and aadhar number,
2. The user can buy or sell property.
3. Proof of Stake(PoS) consensus algorithm is incorporated to improve security of blockchain
4. Merkle tree implementation is used to get the root hash of each transaction in a block.
5. User can see assets owned by him and also the transaction history of a particular property

Zero Knowledge Proof

A zero-knowledge proof, also known as a zero-knowledge protocol, is a technique used in cryptography to
allow one person, known as the prover, to convince another, known as the verifier, that a particular
statement is true while withholding all other information. The fundamental idea behind zero-knowledge
proofs is that it is easy to demonstrate that one has knowledge of a certain piece of information
simply by exposing it; the trick is to demonstrate such knowledge without disclosing the information
itself or any extra information.

Zero Knowledge Proof Algorithm

Alice has sensitive data 𝑥 for which she chooses two numbers 𝑝 and 𝑔. 𝑝 can be a large prime
and 𝑔 is a generator for 𝑝. She calculates 𝑦 as 𝑦 = 𝑔^𝑥𝑚𝑜𝑑(𝑝). Now she performs
the following steps to create a zero knowledge proof for 𝑥.
1. Alice chooses a random number 0 ≤ 𝑟 < 𝑝 − 1 and sends it to Bob as ℎ = 𝑔^𝑟𝑚𝑜𝑑(𝑝)
2. Bob receives ℎ and sends back a random bit 𝑏 (could be 0/1).
3. Alice sends 𝑠 = (𝑟 + 𝑏𝑥)𝑚𝑜𝑑(𝑝 − 1) to Bob.
4. Bob computes 𝑔^𝑠𝑚𝑜𝑑(𝑝) which should equal ℎ𝑦^𝑏𝑚𝑜𝑑(𝑝)

Here Bob acts as a verifier and checks if Alice knows the value of without actually getting to know
what x is.

Block Structure:
1. Timestamp
2. Transactions
3. Hash of the previous block
4. Merkle root
5. Hash of the block

Transaction Structure:
1. Buyer ID/name
2. Seller ID/name
3. Property ID/name
4. Amount
5. Timestamp of transaction
6. pos

User Structure:
1. Username
2. password
3. aadhar(Verifed using Zero Knowledge proof )
4. wealth
5. assets

Merkle tree
MerkleTree which is used to create a Merkle tree data structure. A Merkle tree is a binary tree in
which each non-leaf node is the hash of its two children nodes. The leaves of the tree are the values 
that are being hashed. The getRootHash method returns the hash value of the root node of the Merkle
tree. This can be used as a fingerprint of the entire Merkle tree, and is useful for verifying the
integrity of the data.

Functions Implemented:

register():
This function allows a new user to register to the system by giving his username, password and aadhar
number. 

buy():
This function helpis in buying of properties. User logs in with his username and enters the propertyID
name he wishes to buy. If there is a owner to the property the function proceeds. A function find_pos
is called to find the user with the highest wealth in the system(Proof of Stake - highest stake in the
system) and then perform a zero-knowledge
proof to verify if a given user 'current_owner' is the rightful owner of a particular
'property_chosen'. Lastly a new trasaction is created and ownereship is transferref to curr_user.

transaction_history(): This function shows the transaction history of a property. It displays
information such as buyer,seller, timestamp and transactionID.

show_assets(): This function shows the assets of a particular user

register_property(): This function allows a user to register their property to the system. They need to
enter details like property name and price.

Steps to run the project:
1. Run the main.py file.
2. The output is displayed in the command prompt

Group member details:
2020A7PS1313H	Anish Agarwal
2020A7PS2197H 	Shubh Bhatnagar
2020A7PS1698H	Alankar Agarwal
2020A7PS0076H	Kulkarni Sreyas
2021A7PS2171H	Darsh Shani
