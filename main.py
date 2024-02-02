item_list = {}
shop_list = []

def shopping_list ():
    cart = int(input("Enter how many items do you want to add to your shopping cart:"))
    print("Enter %d items in your cart"%cart, end="\n")
    for i in range(0, cart):
        key = input("\nEnter item number %d:"%(i+1))
        val = input("Enter how much quantity:")
        item_list = {key:val}
        shop_list.append(item_list)

    print("_"*50)
    print("\n\tYour Shopping List\n\n")
    print("No. \t Items \t\t    Quantity\n")
    for i, item_list in enumerate(shop_list):
        for key, value in item_list.items():
            print("%d " %(i+1), "\t %s " %key, "\t\t%s" %value)
        print()
    print("_"*50)

    
def main():
    while True:
        shopping_list()
        ch = input("\nDo you want add more items?")
        if ch == "Yes" or ch == "yes":
            shopping_list()
            break
        else:
            break
    
main()
