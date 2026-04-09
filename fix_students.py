#!/usr/bin/env python3
"""Fix and regenerate all student records with complete data."""

import json
import random
from datetime import datetime, timedelta

# Indian names
FIRST_NAMES = [
    'Aarav', 'Aditya', 'Arjun', 'Aryan', 'Ashok', 'Ananya', 'Anya', 'Anika', 'Anisha', 'Anita',
    'Anjali', 'Anjana', 'Anusha', 'Anushka', 'Anvita', 'Arya', 'Asha', 'Ashika', 'Ashita', 'Ashna',
    'Asmita', 'Ayana', 'Ayesha', 'Ayshita', 'Ayushi', 'Bhavesh', 'Bhavit', 'Bhavin', 'Brijesh', 'Bhavna',
    'Bhavya', 'Bhumika', 'Chirag', 'Chitraj', 'Chitra', 'Darshan', 'Darpan', 'Deepa', 'Deepali', 'Deepana',
    'Darshana', 'Darshani', 'Darshini', 'Deepak', 'Deba', 'Deven', 'Devendra', 'Devin', 'Disha', 'Dishita',
    'Divya', 'Divyaa', 'Esha', 'Eshita', 'Eshnaa', 'Eshna', 'Eshwari', 'Fatima', 'Fatimah', 'Faria',
    'Farida', 'Farina', 'Farzan', 'Garnik', 'Gajendra', 'Gamit', 'Ganesh', 'Ganesha', 'Gargi', 'Garima',
    'Geeta', 'Geetakshi', 'Geetali', 'Gita', 'Giyata', 'Gitika', 'Hamsa', 'Hamsini', 'Hasiya', 'Hasita',
    'Havita', 'Havya', 'Heena', 'Heetal', 'Heitra', 'Ishita', 'Ishana', 'Ishani', 'Ishanika', 'Ishara',
    'Jagadamba', 'Jagadambi', 'Jagana', 'Jaganak', 'Jyoti', 'Jyotika', 'Jyotikira', 'Jyotila', 'Jyotiri', 'Kaaveri',
    'Kaavya', 'Kabita', 'Kadambari', 'Kadambini', 'Kailasha', 'Kailashananda', 'Kajali', 'Kajalika', 'Kajalima', 'Kajalini',
    'Kalindi', 'Kalindi', 'Kanchan', 'Kanchanaa', 'Kamala', 'Kamali', 'Kana', 'Kanaka', 'Kanakavalli', 'Kanakalata',
    'Lakshmi', 'Lakshmi', 'Lakshmika', 'Lalita', 'Lalitakanya', 'Lalitaksha', 'Lalitasree', 'Madhavi', 'Madhavika', 'Madhula',
    'Madhulai', 'Madhulakshi', 'Mala', 'Malaa', 'Malabai', 'Malavati', 'Malavika', 'Mamata', 'Mamtaa', 'Mamtakshi',
    'Manada', 'Manchili', 'Mandakini', 'Mandala', 'Manjari', 'Manjarika', 'Manisha', 'Manishakanta', 'Manorama', 'Manoramala',
    'Marita', 'Maritalaya', 'Maya', 'Mayaa', 'Mayabati', 'Meena', 'Meenakara', 'Meenakari', 'Meenaksha', 'Megha',
    'Meghaa', 'Meghadhi', 'Meghadota', 'Mera', 'Merabai', 'Meradevi', 'Mira', 'Miraa', 'Mirabai', 'Mirajyoti',
    'Misha', 'Mishaa', 'Mishakara', 'Naina', 'Nainaa', 'Nainakanya', 'Nalini', 'Nalinakara', 'Namita', 'Namitaa',
    'Natalia', 'Natalya', 'Natasha', 'Naveen', 'Naveena', 'Naveenakara', 'Navi', 'Navya', 'Navyakara', 'Neelaksha',
    'Neelakshi', 'Neelakshya', 'Neelamani', 'Neelanjali', 'Neelima', 'Nikita', 'Nikitaa', 'Nisha', 'Nishaa', 'Nishtha',
]

LAST_NAMES = [
    'Sharma', 'Singh', 'Gupta', 'Kumar', 'Patel', 'Desai', 'Verma', 'Reddy', 'Khan', 'Malhotra',
    'Iyer', 'Menon', 'Nair', 'Pillai', 'Rao', 'Bhat', 'Saha', 'Jain', 'Chopra', 'Batra',
    'Saxena', 'Pandey', 'Yadav', 'Mishra', 'Arora', 'Kapoor', 'Khanna', 'Bhatt', 'Shah',
    'Modi', 'Trivedi', 'Dwivedi', 'Tiwari', 'Upadhyay', 'Dubey', 'Tyagi', 'Kashyap', 'Banerjee', 'Roy',
    'Bose', 'Dutta', 'Sengupta', 'Lahiri', 'Mukherjee', 'Chatterjee', 'Mallik', 'Sinha', 'Das',
    'Nath', 'Mitra', 'Ghosh', 'Mazumdar', 'Dasgupta', 'Mukerji', 'Sil', 'Chakraborty'
]

GRADES = ['9', '10', '11', '12']
SECTIONS = ['A', 'B', 'C', 'D']
SUBJECTS = ['Science', 'Mathematics', 'English', 'History', 'Geography', 'Literature', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Arts', 'Music', 'Physical Education']
CITIES = ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Pune', 'Kolkata', 'Chennai', 'Chandigarh', 'Ahmedabad', 'Surat', 'Jaipur', 'Lucknow']
NOTES = [
    'Excellent academic performance.', 'Good participation in class activities.', 'Needs improvement in studies.',
    'Talented in sports.', 'Active in cultural programs.', 'Shy but intelligent student.', 'Very disciplined.',
    'Requires extra attention.', 'Science enthusiast.', 'Math wizard.', 'Art lover.', 'Debate champion.',
    'Deserving of scholarship.', 'Leadership qualities.', 'Needs motivation.', 'Very creative.',
]

ORIGINAL_STUDENTS = [
    {'email': 'aarav.s@school.edu', 'name': 'Aarav Sharma'},
    {'email': 'ananya.g@school.edu', 'name': 'Ananya Gupta'},
    {'email': 'arjun.k@school.edu', 'name': 'Arjun Kumar'},
    {'email': 'anaya.p@school.edu', 'name': 'Anaya Patel'},
    {'email': 'nikhil.s@school.edu', 'name': 'Nikhil Singh'},
    {'email': 'priya.d@school.edu', 'name': 'Priya Desai'},
    {'email': 'jagrit.v@school.edu', 'name': 'Jagrit Verma'},
    {'email': 'aisha.r@school.edu', 'name': 'Aisha Reddy'},
    {'email': 'farhan.k@school.edu', 'name': 'Farhan Khan'},
    {'email': 'zara.m@school.edu', 'name': 'Zara Malhotra'},
]

def generate_complete_student(id, email, name):
    """Generate complete student record."""
    grade = random.choice(GRADES)
    section = random.choice(SECTIONS)
    age = random.randint(14, 18)
    phone = f"+91-{random.randint(98000, 99999)}-{random.randint(10000, 99999)}"
    gpa = round(random.uniform(2.0, 4.0), 2)
    status = random.choices(['Active', 'Inactive'], weights=[95, 5])[0]
    
    years_back = random.randint(0, 3)
    joined_date = (datetime.now() - timedelta(days=365*years_back + random.randint(0, 365))).strftime('%Y-09-01')
    
    subject = random.choice(SUBJECTS)
    first_name = name.split()[0]
    last_name = name.split()[-1] if len(name.split()) > 1 else name
    avatar = (first_name[0] + last_name[0]).upper()
    attendance = random.randint(65, 99)
    city = random.choice(CITIES)
    address = f"Sector {random.randint(1, 50)}, {city}"
    
    parent_first = random.choice(FIRST_NAMES)
    parent_last = last_name
    parent_name = f"{parent_first} {parent_last}"
    parent_phone = f"+91-{random.randint(98000, 99999)}-{random.randint(10000, 99999)}"
    notes = random.choice(NOTES)
    
    return {
        "id": id,
        "name": name,
        "grade": f"{grade}-{section}",
        "age": age,
        "email": email,
        "phone": phone,
        "gpa": gpa,
        "status": status,
        "joined": joined_date,
        "subject": subject,
        "avatar": avatar,
        "attendance": attendance,
        "address": address,
        "parent": parent_name,
        "parentPhone": parent_phone,
        "notes": notes,
        "password": "student123"
    }

if __name__ == '__main__':
    # Load existing admin and teacher data
    with open('/home/atul/Documents/method/accounts.json', 'r') as f:
        data = json.load(f)
    
    # Generate complete student records for original 10 students
    students = []
    for i, orig in enumerate(ORIGINAL_STUDENTS, 1):
        student = generate_complete_student(i, orig['email'], orig['name'])
        students.append(student)
    
    # Generate 800 new students
    used_emails = set([s['email'] for s in students])
    for i in range(len(students) + 1, len(students) + 801):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        
        base_email = f"{first_name.lower()}.{last_name.lower()}@school.edu"
        email = base_email
        counter = 1
        while email in used_emails:
            email = f"{first_name.lower()}.{last_name.lower()}{counter}@school.edu"
            counter += 1
        used_emails.add(email)
        
        student = generate_complete_student(i, email, f"{first_name} {last_name}")
        students.append(student)
    
    # Update data
    data['students'] = students
    
    # Save
    with open('/home/atul/Documents/method/accounts.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Fixed all student records")
    print(f"✓ Total students: {len(students)}")
    print(f"✓ Each student now has complete data fields")
    print(f"✓ File saved: accounts.json")
