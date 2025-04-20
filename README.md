# Password List Generator

A powerful and customizable password list generator written in Python. This tool allows you to generate either random passwords or all possible combinations of passwords based on selected character sets. Ideal for penetration testers, developers, or anyone needing a robust password generation utility.

## Features

- Generate **random passwords** of custom length and quantity.
- Generate **all possible combinations** based on chosen character sets.
- Supports **uppercase**, **lowercase**, **numbers**, **symbols**, and **custom character sets** from a file.
- Displays **progress updates** during generation.
- Uses `colorama` for colorful CLI output.
- Supports banners via an external `banner_module`.

## Requirements

- Python 3.x
- `colorama` module

Install dependencies:

```bash
pip install colorama
```

## Usage

Run the script using:

```bash
python password_generator.py
```

### Steps:

1. Enter the desired password length (minimum 2).
2. Select a character set from the provided options.
3. Choose between:
   - Generating random passwords
   - Generating all possible combinations

For **random passwords**, you can set the quantity (default is 300).  
For **combinations**, the tool will calculate all possible combinations and save them.

## Character Set Options

1. All Alphabets (Uppercase)  
2. All Alphabets (Lowercase)  
3. Both Uppercase & Lowercase  
4. All Numbers  
5. All Symbols  
6. Alphabets (Lowercase) & Numbers  
7. Alphabets (Lowercase) & Symbols  
8. Alphabets (Uppercase) & Numbers  
9. Alphabets (Uppercase) & Symbols  
10. Numbers & Symbols  
11. Custom (from file `custom_pass_file.txt`)  
12. All (Uppercase, Lowercase, Numbers, Symbols)

## Output

Generated passwords are saved in the current directory:

- **Random passwords:** `option_name_random_pass.txt`
- **Combinations:** `option_name_combinations.txt`

## Custom Character Set

To use your own characters:

1. Create a file named `custom_pass_file.txt`
2. Add all desired characters on a single line
3. Select option 11 during execution

## Banner Support

Ensure you have a `banner_module.py` file with a `display_banner_and_social()` function to show the ASCII banner and social links/info.

## Example

```bash
Enter password length (min 2): 4
Enter your choice (1-12): 6
Choose an option:
1. Generate random passwords
2. Generate all possible combinations
Enter your choice (1/2): 1
Enter the number of random passwords to generate (min 2, default 300): 100
```

This will generate 100 random passwords using lowercase letters and numbers.

## License

This project is open-source and available under the MIT License.
