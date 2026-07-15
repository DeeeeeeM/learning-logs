# Type Hint or an annotation allows declaring what type of data is the variable

# Basic types
def get_user_info(name: str, email: str, id_num: int) -> str:
    user_data = (
        "Username: " + name.title() +
        "\nEmail: " + email.lower() +
        "\nID: " + str(id_num)
    )
    return user_data

print (get_user_info("Heidel", "heidel@gmail.com", 23))

#Tuples, Lists, Sets
def process_metadata(info_meta: tuple[str, str, int], interest_meta: set[str]):
    print("== Metadata ==") 
    print("Name: " + info_meta[0])
    print("Gender: " + info_meta[1])
    print("Age: " + str(info_meta[2]))
    
    print("\n== Hobbies ==")
    for items in interest_meta:
        print(items)

meta = ("Heidel", "Male", 24)

interests = {
    "basketball",
    "chess",
    "reading"
}
process_metadata(meta, interests)

#Dicts with Union (Union can make the variable either int or str)
def display_inventory(fruits_data: dict[str, int | str]):
    for fruit_name, fruit_quantity in fruits_data.items():
        print(f"Fruit: {fruit_name} | Quantity: {fruit_quantity}")
        
fruits = {
    "Orange": 3,
    "Apple": 10,
    "Mango": "Out of stock"
}

display_inventory(fruits)


#Class

class Car:
    def __init__(self, name: str):
        self.name = name

def get_person_name(car_model: Car):
    return car_model.name

car_decl = Car("Tesla")
print(get_person_name(car_decl))

