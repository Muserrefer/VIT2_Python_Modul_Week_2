############## Soru 1 ################

# 1.1
students = {
    "Muserref Erdogan": [85, 90, 78],
    "Ahmet Esref": [92, 88, 76],
    "Kamuran Aydogan": [78, 89, 95],
    "Ayse Yimaz": [65, 76, 89],
    "Ali Yilmaz": [45, 68, 70],
    "Rabia Erdogan": [70, 87, 80]
}

averages = []
for student, grades in students.items():
    average_grade = int(sum(grades) / len(grades))
    grades.append(average_grade)
    averages.append(average_grade)
print(students)

# 1.2
highest_grade = max(averages)
found_students = []
for key, values in students.items():
    if highest_grade in values:
        found_students.append(key)
print(found_students)

print(f"The student with the highest average grade is {highest_grade} scored by {found_students}")


# 1.3
names_surnames = [(name.split()[0], name.split()[1]) for name in students.keys()]
print(names_surnames)

# 1.4
sorted_names_surnames = sorted(names_surnames)
print("Sorted list of names alphabetically:")
for name, surname in sorted_names_surnames:
    print(f"{name} {surname}")

# 1.5
below_70_average_grade = {student for student, grades in students.items() if grades[3] < 70}
print("Students with an average grade below 70:", below_70_average_grade)

############## Soru 2 ################
import json
# 2.1
film_collection = {}

def add_film():
    film_name = input("Film name: ")
    director = input("Director: ")
    release_year = input("Release Year: ")
    genre = input("Genre: ")

    film_collection[film_name] = {"Director": director, "Release Year": release_year, "Genre": genre}
    print(f"{film_name} film has been added to the collection.")

# 2.2
def edit_film():
    film_name = input("Film name you want to edit: ")
    if film_name in film_collection:
        print("Which information do you want to edit?")
        print("1. Director")
        print("2. Release Year")
        print("3. Genre")
        choice = input("Your choice: ")
        if choice == "1":
            new_director = input("New director: ")
            film_collection[film_name]["Director"] = new_director
        elif choice == "2":
            new_release_year = input("New release year: ")
            film_collection[film_name]["Release Year"] = new_release_year
        elif choice == "3":
            new_genre = input("New genre: ")
            film_collection[film_name]["Genre"] = new_genre
        else:
            print("Invalid choice.")
    else:
        print("Film not found in the collection.")

def delete_film():
    film_name = input("Film name you want to delete: ")
    if film_name in film_collection:
        del film_collection[film_name]
        print(f"{film_name} film has been deleted from the collection.")
    else:
        print("Film not found in the collection.")

# 2.3
def view_collection():
    print("Film Collection:")
    for film_name, details in film_collection.items():
        print(film_name, ":", details)

# 2.4
def save_data():
    with open("film_collection.json", "w") as file:
        json.dump(film_collection, file)
    print("Film collection data has been saved.")

def load_data():
    global film_collection
    try:
        with open("film_collection.json", "r") as file:
            film_collection = json.load(file)
        print("Film collection data has been loaded.")
    except FileNotFoundError:
        print("No saved film collection data found.")

def main():
    load_data()

    while True:
        print("\nFilm Collection Management Panel")
        print("1. Add Film")
        print("2. Edit Film")
        print("3. Delete Film")
        print("4. View Collection")
        print("5. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            add_film()
        elif choice == "2":
            edit_film()
        elif choice == "3":
            delete_film()
        elif choice == "4":
            view_collection()
        elif choice == "5":
            save_data()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

############## Soru 3 ################

# 3.1 & 3.3
customers={}

def customer_registration():
    c_name=input("Please enter your name and surname:")
    c_email=input("Please enter your e-mail address:")
    c_phone_number=input("Please enter your phone number:")
    c_info={
        "Name Surname":c_name,
        "Email":c_email,
        "Phone Number":c_phone_number
    }
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    import random
    c_id= ''.join([random.choice(numbers) for i in range(4)])
    customers[c_id]=c_info
    print(customers)
    print("Customer is successfully registered")

# 3.4
    
def customer_info_update():
    id=input("Please enter the customer id: ")
    print(f"Existing information about customer with id number {id}:", customers.get(id))
    if id in customers:
        print("1. Name Surname")
        print("2. Email Address")
        print("3. Phone Number")
        print("Which customer information do you want to change?")
        which_info = input("Enter one of the numbers above: ")
        if which_info == "1":
            new_name = input("New Name Surname: ")
            customers[id]["Name Surname"] = new_name
        elif which_info == "2":
            new_mail = input("New Email: ")
            customers[id]["Email"] = new_mail
        elif which_info == "3":
            new_phone = input("New Phone Number: ")
            customers[id]["Phone Number"] = new_phone
        print(f"New information about customer with id number {id}:", customers.items(id))
        print(" Customer informations are successfully updated")

# 3.5   
def customer_del():
    c_del=input("Please enter the customer id to delete: ")
    if c_del in customers:
        customers.pop(c_del)
        print(" Customer is successfully deleted")

# 3.6
def customer_info_list():
    if not customers:
        print("No customer information available.")
       
    else:
        print("All customers' informations:")
        for keys,values in customers.items():
            print("Customer ID:", keys)
            print("Other informations:", values)    
# 3.2 & 3.7
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Register a new customer ")
        print("2. Update the information of a customer")
        print("3. Delete a customer")
        print("4. List the information of all customers")
        print("5. Exit")

        menu_choice = input("Enter one of the number above: ")

        if menu_choice == "1":
            customer_registration()
        elif menu_choice == "2":
            customer_info_update()
        elif menu_choice == "3":
            customer_del()
        elif menu_choice == "4":
            customer_info_list()
        elif menu_choice == "5":
            print("Exit program...")
            break        
main_menu()
