def read_and_write_file():
    try:
        # Ask user for the filename to read
        input_file = input("Enter the name of the file to read: ")

        # Attempt to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (you can customize this part)
        modified_content = content.upper()  # Example: convert to uppercase

        # Create a new filename to write modified content
        output_file = "modified_" + input_file

        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"✅ File processed successfully! Modified content saved to '{output_file}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist")
    except IOError:
        print("❌ Error: The file is not readable or writtable")
    except Exception as e:
        print(f"⚠️ Fatal! Error! Error! Abort: {e}")

read_and_write_file()