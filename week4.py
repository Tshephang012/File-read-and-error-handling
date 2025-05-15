def modify_content(content):
    # Modify the content — here we convert it to uppercase
    return content.upper()

def main():
    try:
        # Ask user for input file name
        input_filename = input("Enter the name of the file to read: ")

        # Try to open the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Define output file name
        output_filename = "modified_" + input_filename

        # Write to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
