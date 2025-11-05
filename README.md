Project Overview

The GradeBook Analyzer is a Python-based CLI tool that automates the process of analyzing and reporting student grades.
It allows users (teachers or administrators) to input student marks manually or upload them from a CSV file.
The program then computes statistical summaries, assigns grades, identifies pass/fail students, and displays a formatted results table.


Objectives

1)Automate grade processing using Python.

2)Apply modular programming and computational thinking concepts.

3)Practice loops, conditionals, and data structures.

4)Generate clear analytical summaries and visual-grade distribution.


Features

 Manual data entry or CSV import
 Calculates:

Average

Median

Highest & Lowest score

 Assigns grades (A–F)
 Shows grade distribution
 Filters pass/fail students
 Displays results in tabular format
 Simple text-based menu for repeated analysis

🧩 Tech Stack

Language: Python 

Libraries Used:

csv (for reading CSV files)

statistics (for mean/median calculations)

📊 Example Output
Welcome to the GradeBook Analyzer
1. Enter student data manually
2. Upload a CSV file
3. Exit
Choose an option (1-3): 1

Enter student name (or 'done' to finish): Parth
Enter marks for Parth: 95
Enter student name (or 'done' to finish): Prabhat
Enter marks for Prabhat: 80
Enter student name (or 'done' to finish): Aayan
Enter marks for Aayan:50
Enter student name (or 'done' to finish): Ishant
Enter marks for Ishant: 30
Enter student name (or 'done' to finish): Parmarth
Enter marks for Parmarth: 100
Enter student name (or 'done' to finish): Champ
Enter marks for Champ: 70

Name       Score      Grade
----------------------------
Parth      95         A
Prabhat    80         B
Aayan      50         D
Ishant     30         F
Parmarth   100        A
Champ      70         C

--- Analysis Summary ---
Average Marks: 70.8333333
Median Marks : 75.0
Highest Score: 100.0
Lowest Score : 30.0

--- Grade Distribution ---
A: 2 student(s)
B: 1 student(s)
C: 1 student(s)
D: 1 student(s)
F: 1 student(s)

 Passed Students: 5
Parth,Prabhat,Aayan,Parmarth,Champ
 Failed Students: 1
Ishant

Do you want to check again?(yes/no): no
Exiting the program.Goodbye!

🧠 Learning Outcome

Through this project, I practiced:

Modular design and function-based programming

Data handling and analysis

Basic CLI interaction

Application of computational thinking principles in a real-world scenario
