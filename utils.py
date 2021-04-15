import string, random


class UtilsPerson():
    def generate_uk_driving_licence_number(data):
        # in the given specification https://ukdriving.org.uk/licencenumber.html
        # there was nothing about Mac surnames, so I skipped this bit

        # I changed date to string for easier formatting, I could do it because I have validation
        str_date_of_birth = str(data["date_of_birth"])

        # Digit 1–5: The first five characters of the surname (extra 9's added for names shorter than 5 letters)
        part_1 = data["last_name"][0:5]
        if len(part_1) < 5:
            part_1 = part_1 + "9"

        # Digit 6: The decade digit from the year of birth (e.g. for 1977 it would be 7)
        part_2 = str_date_of_birth[2]

        # Digit 7–8: The month of birth (+5 for the first character if female)
        part_3 = str_date_of_birth[5:7]
        if data["gender"] == 'F':
            part_3 = int(part_3, 10) + 50

        # Digit 9–10: The day in the month of birth
        part_4 = str_date_of_birth[8:10]

        # Digit 11: The year digit from the year of birth (e.g. for 1977 it would be 7)
        part_5 = str_date_of_birth[3:4]

        # Digit 12–13: The first two initials of the first names, (9 if no middle name)
        part_6 = data["first_name"][0:1]

        part_7 = '9'
        if 'middle_name' in data:
            if data["middle_name"]:
                part_7 = data["middle_name"][0:1]

        # I could put more attention to this case
        # Digit 14: Arbitrary digit - often 9
        part_8 = "9"

        # Digit 15–16: Two computer digits
        letters = string.ascii_uppercase
        part_9 = ''.join(random.choice(letters) for i in range(2))

        return part_1.upper() + part_2 + str(part_3) + part_4 + part_5 + part_6.upper() + part_7 + part_8 + part_9
