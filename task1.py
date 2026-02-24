def main():
    #Collect Input for each
    #Variable: first Prompt: Child's First Name:
    first = input("Child's First Name: ")
    #Variable: last Prompt: Child's Last Name:
    last = input("Child's last Name: ")

    print(f"Camper's Name: {first} {last}")

    #Variable: birth Prompt: In what year was {first} {last} born:
    birth = input(f"In what year was {first} {last} born: ")

    print(f"Birth Year: {birth}")

    #Variable: days Prompt: How many days will {first} attend?
    days = input(f"How many days will {first} attend? ")

    print(f"Camp Duration: {days} days")

    #Variable: p_first Prompt: Parent's First Name:
    
    #Variable: p_last Prompt: Parent's Last Name:
    
    print(f"Parent's Name: {first} {last}")

    #Variable: phone Prompt: Parent's Phone #:
    
    print(f"Phone Number: (phone)")

    #Variable: street Prompt: Street Address:
street = input("Street Address:")

    #Variable: city Prompt: City:
city = input(f"City: ")

    #Variable: state Prompt: State Abbreviation:
state = input(f"State Abbreviation: ")

    #Variable: zip Prompt: Zip Code:
zip = input(f"Zip Code: ")

print(f"Address:{street}{city}, {state} {zip}")

if __name__ == "__main__":
    main()
