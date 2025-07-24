📘 Python Data Types
Python is a dynamically typed language, meaning you don't have to explicitly declare variable types — Python automatically detects them based on the value assigned.

Below are the 4 most common basic data types:

1. 🔢 int (Integer)
Definition: Used to represent whole numbers without a decimal point.

Examples:
age = 25

count = -10

year = 2025

Common uses: Age, years, counters, indexes, loop iterations, etc.

2. 🔣 float (Floating Point Number)

Definition: Used to represent numbers with decimals (real numbers).

Examples:

height = 5.9

salary = 45000.75

temperature = -12.3

Common uses: Precise measurements, financial calculations, scientific data.

3. 🔤 str (String)

Definition: Represents text. Strings are sequences of characters enclosed in quotes.

Examples:

name = "Anand"

message = 'Hello, world!'

country = "India"

Multiline String Example:

paragraph = """This is a

multiline string."""

Common uses: Names, messages, addresses, user input, file paths.

4. ✅ bool (Boolean)

Definition: Represents True or False values.

Only two possible values:

is_student = True

is_employed = False

Common uses: Conditions, flags, logic-based checks, decision making.

**🧪 Type Checking**

Use the type() function to check the data type of any variable:

x = 3.5

print(type(x))  # Output: <class 'float'>

🔄 Type Conversion (Casting)

Python allows you to convert from one type to another using built-in functions:


int("10")       # Converts string to int → 10

float("3.14")   # Converts string to float → 3.14

str(123)        # Converts int to string → "123"

bool("")        # False (empty string)

bool("hello")   # True (non-empty string)

📝 Summary Table

Type	Description	Example

int	Whole numbers	25, -8

float	Decimal numbers	3.14, 0.0

str	Text values	"Anand"

bool	True or False	True, False
