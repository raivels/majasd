
def get_input():
    num1 = float(input("Ievadiet 1. skaitli: "))
    num2 = float(input("Ievadiet 2. skaitli: "))
    operator = input("Ievadiet operatoru (+, -, *, /, %): ")
    return num1, num2, operator

# Aprēķina summu


def add(num1, num2):
    return num1 + num2

# Aprēķina starpību


def subtract(num1, num2):
    return num1 - num2

# Aprēķina reizinājumu


def multiply(num1, num2):
    return num1 * num2

# Aprēķina dalījumu


def divide(num1, num2):
    if num2 == 0:
        return "Nepareizi , dalīt ar nulli nedrikst."
    else:
        return num1 / num2

# Aprēķina atlikumu


def modulus(num1, num2):
    if num2 == 0:
        return "Nepareizi , dalīt ar nulli nedrikst."
    else:
        return num1 % num2

# Apvieno iepriekšējās funkcijas, lai veiktu matemātisku darbību atkarībā no ievades


def calculator():
    num1, num2, operator = get_input()

    if operator == "+":
        print(num1, "+", num2, "=", add(num1, num2))
    elif operator == "-":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif operator == "*":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif operator == "/":
        print(num1, "/", num2, "=", divide(num1, num2))
    elif operator == "%":
        print(num1, "%", num2, "=", modulus(num1, num2))
    else:
        print("Nepareizi, lūdzu, ievadiet pareizo operatoru (+, -, *, /, %).")


# Izpilda kalkulatora funkciju, kamēr lietotājs to vēlas
while True:
    calculator()
    choice = input("Vai vēlaties turpināt? (jā/nē): ")
    if choice.lower() != "jā":
        break
    .
