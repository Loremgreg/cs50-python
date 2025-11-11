price = 50
valid_coins = [25, 10, 5]

def main():
    amount_due = price
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        insert_coin = int(input("Insert coin: "))
        if insert_coin in valid_coins:
             amount_due -= insert_coin
    if amount_due < 0:
        change_owed = 0 - amount_due
        print(f"Change Owed: {change_owed}")
    else:
        print("Change Owed: 0")
main() 
             
             


