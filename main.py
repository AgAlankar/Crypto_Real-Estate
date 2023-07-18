from block import BlockChain
from models import Property, User
from models import Transaction
from pos import find_pos
import setup

# initializing the blockchain
blockchain = BlockChain()

g=5
p=2000000579


def register():

    print('------------------------------------------------------------------ \n')
    print('Enter a username and password:')
    username = str(input("Username: "))
    password = str(input("Password: "))
    aadhar = input("Aadhar(8 digit number): ")
    wealth = int(input("Wealth(default 15): "))

    if (username != '' and password != ''):
        User(username, password, aadhar, wealth)
        print(f'\n {username} registered successfully!')
        return
    else:
        print("\n Username and/or password can't be empty, try again \n")
        register()


def buy():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("\n User does not exist, create a user")
        return

    print('\n Enter the ID of the property you want to buy: ')
    propertyId = int(input())
    property_chosen = Property.properties[propertyId]

    if property_chosen.owner != None:
        current_owner = property_chosen.owner
        print("\nOwner: "+current_owner.username)
        print("User: "+curr_user.username)
        if curr_user.username == current_owner.username:
            print("\nProperty already belongs to the user")
            return  
    else:
        current_owner = None

    res = find_pos(curr_user, current_owner, property_chosen)
    if res == -1:
        print('Insufficient balance \n')
        return
    else:
        current_owner.remove_property(property_chosen)
        transaction = Transaction(
            current_owner, curr_user, property_chosen, res)
        curr_user.add_property(property_chosen)
        curr_user.transactions.append(transaction)

        property_chosen.transaction_history.append(transaction)
        res.wealth += property_chosen.amount // 2
        prev_block = blockchain.last_block()
        blockchain.new_block(prev_block['hash'], transaction)

        print(
            f"\n {curr_user.username} bought {property_chosen.name} successfully! \n {blockchain.last_block()['merkle_root']}")


def transaction_history():

    print('------------------------------------------------------------------ \n')
    print("Enter the ID of the property whose transaction history you want to see: ")
    propertyId = int(input())

    if propertyId >= len(Property.properties):
        print('Invalid selection, choose again \n')
        transaction_history()

    property_chosen = Property.properties[propertyId]

    for transaction in property_chosen.transaction_history:
        print(f'''
            Buyer: {transaction.buyer.username},
            Seller: {transaction.seller.username}
            Timestamp: {transaction.timestamp},
            TxnID: {transaction.transactionId}
        \n''')
        
def user_history():
    
    print('------------------------------------------------------------------ \n')
    print("Enter the username whose transaction history you want to see: ")
    userId = str(input())

    user_found = False
    for user in User.users:
        if user.username == userId:
            user_found = True
            curr_user = user
    
    if not user_found:
        print("\n User does not exist, create a user")
        return


    for transaction in curr_user.transactions:
        print(f'''
            Buyer: {transaction.buyer.username},
            Seller: {transaction.seller.username}
            Timestamp: {transaction.timestamp},
            TxnID: {transaction.transactionId}
        \n''')
               

def show_assets():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    else:
        print(f'\n -> Properties owned by {username} are:')
        curr_user.get_assets()


def register_property():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    else:
        print('Enter the name of the property:')
        name = input('')
        print('Enter the price of the property:')
        price = int(input(''))
        new_property = Property(name, price)
        curr_user.reg_property(new_property)
        print(
            f'\n {new_property.name} registered in the system by {curr_user.username}')


# main loop
while True:

    print(""" \n ------------------------------------------------------------------ \n
    Choose an action:
        1. Register User
        2. Buy Property
        3. View transaction history for a property
        4. View assets owned by a user
        5. Register property
        6. User history
    """)

    choice = int(input())

    if (choice == 1):
        register()
    elif (choice == 2):
        buy()
    elif (choice == 3):
        transaction_history()
    elif (choice == 4):
        show_assets()
    elif (choice == 5):
        register_property()
    elif (choice == 6):
        user_history()
    else:
        print("Invalid choice, choose again")
