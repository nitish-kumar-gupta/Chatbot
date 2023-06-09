import random

def greet():
    greetings = ['Hello', 'Hi', 'Hey', 'Welcome']
    print(f'{random.choice(greetings)}! I am a chatbot that can help you find job openings on our website.')

def show_options():
    print('Here are the options you can choose from:')
    print('1. Show current job openings')
    print('2. Check eligibility for current job openings')
    print('3. Exit')

def show_openings(openings):
    print('Here are the current job openings on our website:')
    for opening, details in openings.items():
        print(f'{opening}:')
        print(f'  Qualifications: {", ".join(details["qualifications"])}')
        print(f'  Experience: {details["experience"]} years')
        print(f'  Skills: {", ".join(details["skills"])}')

def check_eligibility(openings):
    qualifications = input('Enter your qualifications (separated by commas): ').split(',')
    experience = int(input('Enter your years of work experience: '))
    skills = input('Enter your skills (separated by commas): ').split(',')

    eligible_openings = []
    for opening, details in openings.items():
        if any(skill in skills for skill in details['skills']):
            eligible_openings.append(opening)

    if eligible_openings:
        if len(eligible_openings) == 1:
            print(f'Based on your skills, you may be interested in the following job opening: {eligible_openings[0]}')
            choice = input('Would you like to see the details of this job opening? (yes/no): ')
            if choice.lower() == 'yes':
                opening = eligible_openings[0]
                details = openings[opening]
                print(f'{opening}:')
                print(f'  Qualifications: {", ".join(details["qualifications"])}')
                print(f'  Experience: {details["experience"]} years')
                print(f'  Skills: {", ".join(details["skills"])}')
                print(f'  Description: {details["description"]}')
                print(f'  How to apply: {details["how_to_apply"]}')
        else:
            print(f'Based on your skills, you may be interested in the following job openings: {", ".join(eligible_openings)}')
            choice = input('Would you like to see the details of a job opening? (yes/no): ')
            if choice.lower() == 'yes':
                opening = input('Enter the name of the job opening: ')
                if opening in openings:
                    details = openings[opening]
                    print(f'{opening}:')
                    print(f'  Qualifications: {", ".join(details["qualifications"])}')
                    print(f'  Experience: {details["experience"]} years')
                    print(f'  Skills: {", ".join(details["skills"])}')
                    print(f'  Description: {details["description"]}')
                    print(f'  How to apply: {details["how_to_apply"]}')
                else:
                    print('Sorry, we could not find that job opening.')
    else:
        print('Sorry, we could not find any job openings that match your skills.')

if __name__ == '__main__':
    openings = {
        'Software Engineer': {
            'qualifications': ['Bachelor\'s degree in Computer Science'],
            'experience': 3,
            'skills': ['Python', 'Java', 'C++'],
            'description': 'We are looking for a skilled software engineer to join our team.',
            'how_to_apply': 'To apply for this position, please send your resume and cover letter to hr@example.com.'
        },
        'Marketing Manager': {
            'qualifications': ['Bachelor\'s degree in Marketing'],
            'experience': 5,
            'skills': ['SEO', 'SEM', 'Social Media Marketing'],
            'description': 'We are looking for an experienced marketing manager to lead our marketing efforts.',
            'how_to_apply': 'To apply for this position, please fill out the online application form on our website.'
        },
        'Data Analyst': {
            'qualifications': ['Bachelor\'s degree in Mathematics or Statistics'],
            'experience': 2,
            'skills': ['SQL', 'R', 'Python'],
            'description': 'We are looking for a data analyst to help us make data-driven decisions.',
            'how_to_apply': 'To apply for this position, please send your resume and cover letter to hr@example.com.'
        }
    }
    greet()
    while True:
        show_options()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            show_openings(openings)
        elif choice == 2:
            check_eligibility(openings)
        elif choice == 3:
            break