def main():
    """ 
    Write some code that will read in the data from the provided text files and run it through
    read_motion(), read_emf(), read_temperature(), and also generate a report of this data.
    """
    location_name = "ravensnest"
    motion_data   = read_motion(location_name)
    emf_data      = read_emf(location_name)
    temp_data     = read_temperature(location_name)


    motion_expected = ["gameroom", "kitchen", "breakroom", "closet"]
    emf_expected    = ["kitchen", "breakroom"]
    temp_expected   = ["gameroom", "garage"]

    # Here is an example test for the motion data. If you wish, you can choose to create a function to
    # run tests on your other data, or you can copy and update this code to test your other functions.
    if motion_data == motion_expected:
        print("✅ Motion Data Test Passed")
    else:
        print("❌ Motion Data Test Failed")
        print(f"   Expected: {motion_expected}")
        print(f"   Actual Return Value: {motion_data}")
    if emf_data == emf_expected:
        print("✅ EMF Data Test Passed")
    else:
        print("❌ EMF Data Test Failed")
        print(f"   Expected: {emf_expected}")
        print(f"   Actual Return Value: {emf_data}")
    if temp_data == temp_expected:
        print("✅ Temp Data Test Passed")
    else:
        print("❌ Temp Data Test Failed")
        print(f"   Expected: {temp_expected}")
        print(f"   Actual Return Value: {temp_data}")


    # TODO: Test EMF Data and Temp Data

    # TODO: Generate a report based on the motion, emf, and temp data

def read_motion(location_name):
    """Return a list of room names, with no duplicates, where motion was detected in the file {location_name}.motion.txt. Motion files are formatted with a room on each line followed by a colon, space, and either the word "detected" or "undetected".
    
    Args:
        location_name (string): The name of the location. Files will be named {location_name}.motion.txt

    Returns:
        A list of room names that were "detected" in the text file.
    """
    rooms = []
    myfile = open("ravensnest.motion.txt" , "r")
    for line in myfile:
        line = line.strip()
        line = line.split(": ")
        if line[1] == "detected":
            rooms.append(line[0])
    myfile.close()
    return rooms

def read_emf(location_name):
    """Return a list of room names, with no duplicates, where average EMF > 3.0 was detected in the file {location_name}.emf.txt. EMF files are formatted with a name, a newline, and newlines containing an integer representing EMF values until reaching either the end-of-file or the next room name.

    Args:
        location_name (string): The name of the location. Files will be named {location_name}.emf.txt.

    Returns:
        A list of room names where the average EMF reading was > 3.0.
    """
    rooms = []
    myfile = open("ravensnest.emf.txt" , "r")
    for line in myfile:
        line = line.strip()
        if line.isdigit() == False:
            room = line
            total = 0
            count = 0
        elif line.isdigit() == True:
            total += int(line)
            count += 1
        if room not in rooms and count != 0:
            if (total/count) >= 3:
                rooms.append(room)
                continue
    myfile.close()
    return rooms

def read_temperature(location_name):
    """Return a list of room names, with no duplicates, where 5 or more consecutive negative temperatures were detected in the file {location_name}.temp.txt. Temp files are formatted with comma separated values: `room name,timestamp,float` on each line.

    Args:
        location_name (string): The name of the location. Files will be named {location_name}.temp.txt.

    Returns:
        A list of room names where five or more consecutive negative temperatures were detected in the file.
    """  
    rooms = []
    myfile = open("ravensnest.temp.txt", "r")
    oldroom = ""
    for line in myfile:
        line = line.strip()
        line = line.split(",")
        for value in range(len(line)):
            if line[value] != oldroom:
                total = 0
                count = 0
            if line[value].isdigit() == False:
                oldroom = line[value]
            elif line[value].isdigit() == True:
                if line[value] <= 170:
                    if line[value] <= 0:
                        total += 1
                        count += 1
                    else:
                        count = 0
        if total >= 5 and count == 5:
            rooms.append(oldroom)
    return rooms

# TODO: Write your generate_report and get_unique_rooms functions here, as well as the docstring (function comment documentation) for each based on the provided function examples.



# Using if __name__ == "__main__" is a weird Python check that determines
# whether we are running this file directly (in which case the hidden variable __name__ will be equal to "__main__")
# or if it was included as a module, giving us access to the functions without executing main.
# For now, just know that this is a common pattern in Python for running your main() function.
if __name__ == "__main__":
    main()
