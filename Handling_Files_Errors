def modify_file_content(content):
    """
    Modify the file content.
    Example modification: convert text to uppercase.
    You can change this to anything you like.
    """
    return content.upper()


filename = input("Enter the filename to read: ")

try:
    # Try opening and reading the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_file_content(content)

    # Create a new filename
    new_filename = "modified_" + filename

    # Write modified content to new file
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"✅ File successfully modified and saved as '{new_filename}'")

except FileNotFoundError:
    print("❌ Error: The file does not exist.")

except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")

except Exception as e:
    print(f"❌ Unexpected error occurred: {e}")