# Create an admission program to calculate the aggregate score and tell the student the faculty and department he or she is likely to be admitted to.

Faculties = [
    "Education",
    "Engineering",
    "Human Medicine",
    "Law",
    "Agriculture",
    "Social Sciences",
]

Departments = [
    ["Physical Education", "CRS Education", "Social Studies Education"],
    ["Mechanical Engineering", "Civil Engineering", "Electrical Engineering"],
    ["Medicine and Surgery", "Anatomy", "Dentistry"],
    ["Civil Law", "Islamic Law"],
    ["Soil Science", "Botany", "Agronomy", "Soil Science"],
    ["Economics", "Banking", "Marketing"],
]

Sciences = ["Maths", "English", "Biology", "Chemistry", "Physics"]
Social_science = ["Maths", "English", "Geography", "Economics", "Commerce"]
Arts = ["Maths", "English", "Religion", "Government", "Literature"]

subjects_input = input(
    "Welcome. Choose your subjects by typing in one of either: \n Arts, Commerce or Sciences \n"
)
subjects = subjects_input.lower()

if subjects != "arts" and subjects != "commerce" and subjects != "sciences":
    print("Please type in exactly one subject area from the three listed above")


Total_Score = 0
if subjects == "sciences":
    for i in Sciences:
        subject_score = int(input("Please input your scores in " + i + ":"))
        Total_Score = Total_Score + subject_score

    percentage_score = str(Total_Score / 5)
    if Total_Score / 5 > 50:
        print("\n Congratulations! Your aggregate score is " + str(Total_Score))
        print("and your percentage score is " + percentage_score + "%")
        if Total_Score / 5 >= 80:
            print(
                "You qualify for the following courses in the Faculty of "
                + Faculties[2]
                + "\n"
            )
            for i in Departments[2]:
                print(i)
        elif Total_Score / 5 < 80 >= 70:
            print(
                "You qualify for the following courses in the Faculty of "
                + Faculties[1]
                + "\n"
            )
            for i in Departments[1]:
                print(i)
        elif Total_Score / 5 < 70 >= 50:
            print(
                "You qualify for the following courses in the Faculty of "
                + Faculties[4]
                + "\n"
            )
            for i in Departments[4]:
                print(i)
    else:
        print(
            "\n Unfortunately, your score of "
            + percentage_score
            + "% does not qualify for any of our courses at this time."
        )

if subjects == "arts":
    for i in Arts:
        subject_score = int(input("Please input your scores in " + i + ":"))
        Total_Score = Total_Score + subject_score

    percentage_score = str(Total_Score / 5)
    if Total_Score / 5 > 50:
        print("\n Congratulations! Your aggregate score is " + str(Total_Score))
        print("and your percentage score is " + percentage_score + "%")
        print(
            "You qualify for the following courses in the Faculty of "
            + Faculties[3]
            + "\n"
        )
        if Total_Score / 5 >= 75:
            for i in Departments[3]:
                print(i)
        elif Total_Score / 5 < 75 >= 50:
            print(
                "You qualify for the following courses in the Faculty of "
                + Faculties[0]
                + "\n"
            )
            for i in Departments[0][1:]:
                print(i)
    else:
        print(
            "\n Unfortunately, your score of "
            + percentage_score
            + "% does not qualify for any of our courses at this time."
        )

if subjects == "commerce":
    for i in Social_science:
        subject_score = int(input("Please input your scores in " + i + ":"))
        Total_Score = Total_Score + subject_score

    percentage_score = str(Total_Score / 5)
    if Total_Score / 5 > 50:
        print("\n Congratulations! Your aggregate score is " + str(Total_Score))
        print("and your percentage score is " + percentage_score + "%")
        print(
            "You qualify for the following courses in the Faculty of "
            + Faculties[5]
            + "\n"
        )
        if Total_Score / 5 >= 70:
            print(Departments[5][0])
        elif Total_Score / 5 < 70 >= 50:
            print(
                "You qualify for the following courses in the Faculty of "
                + Faculties[5]
                + "\n"
            )
            for i in Departments[5][1:]:
                print(i)
    else:
        print(
            "\n Unfortunately, your score of "
            + percentage_score
            + "% does not qualify for any of our courses at this time."
        )
