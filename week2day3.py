shopping_cart=[]
def add_info(item):
    shopping_cart.append(item)
def del_info(item):
    shopping_cart.remove(item)
def show_info():
    print(shopping_cart)
def main():
    while True:
        choice=input('what would you like to do?show/add/delete or quit?')
        if choice.lower()=="show":
            show_info
        elif choice.lower()=="add":
            item = input("what would you like to add?")
            add_info(item)
        elif choice.lower()=="delete":
            item = input("what would you like to delete?")
        else:
            print("you chose to quit")
            break
        print(shopping_cart)
main()
              
import module
length = int(input("what is the length of your huse?"))        
width = int(input("what is the width of your house?")) 

print(f"your houses square footage is {module.square_foot(length,width)}")
radius = int(input("what is the radius of your circle?"))
print(f"The circumfrence of yourcircle is{module.circumfrence(radius)}")