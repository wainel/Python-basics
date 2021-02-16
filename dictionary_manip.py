def make_team():
    """
    Write a function that takes a dictionary called people as input (see below) 
    and returns 3 lists named cook, gardener and clerk containing the name of 
    each individual with this job.
    """
    
    people = {
        'Pete': {
            'Age': 51,
            'Job': 'Cook'
        },
        'John': {
            'Age': 32,
            'Job': 'Gardener'
        },
        'Jim': {
            'Age': 45,
            'Job': 'Cook'
        },
        'Sheila': {
            'Age': 19,
            'Job': 'Clerk'
        },
        'Carol': {
            'Age': 67,
            'Job': 'Gardener'
        },
        'Richard': {
            'Age': 17,
            'Job': 'Clerk'
        }
    }
        
    cook = []
    gardener = []
    clerk = []
    # write your code here
    for key,value in people.items():
        for k,v in value.items():
            if k == 'Job':
                if v == 'Cook':
                    cook.append(key)
                if v == 'Gardener':
                    gardener.append(key)
                if v == 'Clerk':
                    clerk.append(key)
    
    
    return cook, gardener, clerk
