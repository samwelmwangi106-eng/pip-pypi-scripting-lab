from datetime import datetime


def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # STEP 2: Generate filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write log entries
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Return filename
    return filename


# Only run manual tests if executed directly
if __name__ == "__main__":
    sample_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    print(generate_log(sample_data))