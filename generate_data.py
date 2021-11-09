import json
from faker import Faker


YEARS = [2019, 2020, 2021]
NUM_INSTITUTIONS = 8
SUBJECTS = ['Biology', 'Chemistry', 'History', 'Maths']


def save_file(filename, object):
    with open(filename, 'w') as f:
            json.dump(object, f, indent=4)

def generate_institutions(fake):
    institutions = []
    for i in range(NUM_INSTITUTIONS):
        city = fake.city()
        institutions.append({
            'id': fake.uuid4(),
            'name': f'University of {city}' if fake.boolean() else f'{city} University',
            'city': city
        })
    save_file(f'institutions.json', institutions)
    return institutions
        
def generate_subjects(fake):
    subjects = []
    for subj in SUBJECTS:
        subjects.append({
            'name': subj,
            'academic_papers': fake.pyint(max_value=100),
            'students_total': fake.pyint(max_value=500),
            'student_rating': fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=1, max_value=5)
        })
    return subjects

def generate_submissions_for_year(fake, year, institutions):
    submissions = []
    for inst in institutions:
        submissions.append({
            'id': fake.uuid4(),
            'institution': inst['id'],
            'year': year,
            'staff_total': fake.pyint(max_value=100),
            'subjects': generate_subjects(fake)
        })
    return submissions

def generate_files(fake, institutions):
    for year in YEARS:
        submissions = generate_submissions_for_year(fake, year, institutions)
        save_file(f'submissions_{year}.json', submissions)


fake = Faker()
institutions = generate_institutions(fake)
generate_files(fake, institutions)
