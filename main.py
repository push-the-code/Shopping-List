item_list = {}
shop_list = []

def shopping_list ():
    cart = int(input("Enter how many items do you want to add to your cart:"))
    print("Enter %d items in your cart"%cart, end="\n")
    for i in range(0, cart):
        key = input("\nEnter item number %d:"%(i+1))
        val = input("Enter how much quantity:")
        item_list = {key:val}
        shop_list.append(item_list)
    print("\n________________________________________")
    print("\n\tYour Shopping List\n\n")
    print("No. \t Items \t \t Quantity\n")
    for i, item_list in enumerate(shop_list):
        for key, value in item_list.items():
            print("%d " %(i+1), "\t %s\t" %key, "\t %s   " %value)
        print()
    print("\n________________________________________")

    
def main():
    while True:
        shopping_list()
        ch = input("Do you want add more items?")
        if ch == "Yes" or ch == "yes":
            shopping_list()
            break
        else:
            exit(0)
            break
    
main()
