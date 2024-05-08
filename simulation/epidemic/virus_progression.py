import random

# Initialize the database
database = {
    "infection_stages": ["asymptomatic", "symptomatic", "critical", "terminal"],
    "base_transmition_rate": 1.0,
    "mask_effectiveness": 0.4,
    "vaccination_effects": {
        "gets_better": 2,
        "gets_worse": 0.5,
        "nothing_happens": 1.0
    },
    "symptom_notoriety": {
        "normal_short_breath": 0.15,
        "normal_cough": 0.15,
        "normal_fever": 0.2,
        "back_ache": 0.1,
        "stomach_ache": 0.1,
        "lazyness": 0.05,
        "sleepiness": 0.1,
        "critical_short_breath": 0.2,
        "critical_cough": 0.2,
        "critical_fever": 0.25,
        "gastritis": 0.15,
        "candela": 0.2,
        "que_ostine": 0.15,
        "terminal_fever": 0.25
    },
    "possible_symptoms": {
        "symptomatic": ["normal_fever", "normal_cough", "normal_short_breath", "back_ache", "stomach_ache", "lazyness", "sleepiness"],
        "critical": ["critical_fever", "critical_cough", "critical_short_breath", "gastritis"],
        "terminal": ["terminal_fever", "candela", "que_ostine"],
        "recovered": []
    },
    "age_influence": {
        "young": {"gets_better": 0.005, "gets_worse": 0.003, "nothing_happens": 0.992},
        "adult": {"gets_better": 0.005, "gets_worse": 0.005, "nothing_happens": 0.990},
        "old": {"gets_better": 0.005, "gets_worse": 0.015, "nothing_happens": 0.980}
    },
    "symptom_progression": {
        "normal_fever": "critical_fever",
        "normal_cough": "critical_cough",
        "normal_short_breath": "critical_short_breath",
        "stomach_ache": "gastritis",
        "critical_fever": "terminal_fever"
    }
}

# Function to determine if the infection gets better
def infection_gets_better(symptoms, current_stage):
    next_symptoms = symptoms.copy()  # Make a copy of the symptoms
    next_stage = current_stage
    if symptoms:
        symptom = random.choice(symptoms)
        remove_symptom(symptom, symptoms, next_symptoms)
    if current_stage == 'asymptomatic':
        next_stage = 'recovered'
    elif current_stage == 'symptomatic' and count_symptomatic_symptoms(symptoms) == 0:
        next_stage = 'asymptomatic'
    elif current_stage == 'critical' and count_critical_symptoms(symptoms) == 0:
        next_stage = 'symptomatic'
    elif current_stage == 'terminal' and count_terminal_symptoms(symptoms) == 0:
        next_stage = 'critical'
    return next_stage, next_symptoms

# Function to determine if the infection gets worse
def infection_gets_worse(symptoms, current_stage, possible_symptoms):
    next_symptoms = symptoms.copy()  # Make a copy of the symptoms
    next_stage = current_stage

    if possible_symptoms:
        symptom = random.choice(possible_symptoms)
        add_symptom(symptom, symptoms, next_symptoms)

    if current_stage == 'asymptomatic':
        next_stage = 'symptomatic'
    elif current_stage == 'symptomatic' and count_symptomatic_symptoms(symptoms) >= 4:
        next_stage = 'critical'
    elif current_stage == 'critical' and count_critical_symptoms(symptoms) >= 2:
        next_stage = 'terminal'
    elif current_stage == 'terminal' and count_terminal_symptoms(symptoms) >= 1:
        next_stage = 'dead'

    return next_stage, next_symptoms

# Function to add a symptom
def add_symptom(symptom, symptoms, next_symptoms):
    if database["symptom_progression"].get(symptoms[-1]) == symptom:
        next_symptoms.append(symptom)
    else:
        next_symptoms.append(database["symptom_progression"].get(symptom))

def remove_symptom(symptom, symptoms, next_symptoms):
    if database["symptom_progression"].get(symptom):
        next_symptoms.remove(symptom)
        next_symptoms.append(database["symptom_progression"].get(symptom))
    else:
        next_symptoms.remove(symptom)

# Function to count symptomatic symptoms
def count_symptomatic_symptoms(symptoms):
    symptomatic_symptoms = database["possible_symptoms"]["symptomatic"]
    return sum(1 for symptom in symptoms if symptom in symptomatic_symptoms)

# Function to count critical symptoms
def count_critical_symptoms(symptoms):
    critical_symptoms = database["possible_symptoms"]["critical"]
    return sum(1 for symptom in symptoms if symptom in critical_symptoms)

# Function to count terminal symptoms
def count_terminal_symptoms(symptoms):
    terminal_symptoms = database["possible_symptoms"]["terminal"]
    return sum(1 for symptom in symptoms if symptom in terminal_symptoms)

# Class to manage the person database
class PersonDatabase:
    def __init__(self):
        self.persons = {}
        self.database = database
    
    # Add a new agent to the database
    def add_agent(self, person, vaccination_status, age_group):
        self.persons[person] = {
            'vaccination_status': vaccination_status,
            'age_group': age_group,
            'stage': 'asymptomatic',
            'symptoms': []
        }
    
    # Remove an agent from the database
    def remove_agent(self, person):
        if person in self.persons:
            del self.persons[person]
    
    # Update agent information
    def update_agent(self, person, new_stage, new_symptoms, new_vaccination_status, new_age_group):
        if person in self.persons:
            self.update_stage(person, new_stage)
            self.update_symptoms(person, new_symptoms)
            self.update_vaccination_status(person, new_vaccination_status)
            self.update_age_group(person, new_age_group)
    
    # Update the stage of an agent
    def update_stage(self, person, new_stage):
        if person in self.persons:
            self.persons[person]['stage'] = new_stage
    
    # Update the symptoms of an agent
    def update_symptoms(self, person, new_symptoms):
        if person in self.persons:
            self.persons[person]['symptoms'] = new_symptoms
    
    # Update the vaccination status of an agent
    def update_vaccination_status(self, person, new_vaccination_status):
        if person in self.persons:
            self.persons[person]['vaccination_status'] = new_vaccination_status
    
    # Update the age group of an agent
    def update_age_group(self, person, new_age_group):
        if person in self.persons:
            self.persons[person]['age_group'] = new_age_group
    
    # Perform a step for a given person
    def step(self, person):
        next_stage, new_symptoms, step_type = '', [], ''

        # Get the necessary information for the current agent
        vaccination_status = self.persons[person]['vaccination_status']
        current_stage = self.persons[person]['stage']
        age_group = self.persons[person]['age_group']
        current_symptoms = self.persons[person]['symptoms']

        # Determine if the infection will get worse, better, or remain the same
        self.step_type(age_group, vaccination_status, step_type)

        # Determine if there are any new symptoms to add
        possible_symptoms = self.available_symptoms(current_stage, current_symptoms)

        # Changing the stage of the person if possible
        if step_type == 'gets_better':
            self.infection_gets_better(current_symptoms, current_stage, next_stage, new_symptoms)
        elif step_type == 'gets_worse':
            self.infection_gets_worse(current_symptoms, current_stage, possible_symptoms, next_stage, new_symptoms)
        else:
            next_stage = current_stage
            new_symptoms = current_symptoms

        # Updating agent information
        if next_stage in ['recovered', 'dead']:
            self.remove_agent(person)
        else:
            self.update_stage(person, next_stage)
            self.update_symptoms(person, new_symptoms)
    
    # Determine the step type based on age group and vaccination status
    def step_type(self, age_group, vaccination_status, step_type):
        self.step_type_gen(age_group, vaccination_status, step_type)
    
    # Generate the step type based on age group and vaccination status
    def step_type_gen(self, age_group, vaccination_status, step_type):
        vaccination_effect_better = 2 if vaccination_status else 1.0
        vaccination_effect_worse = 0.5 if vaccination_status else 1.0

        age_influence_better = 0.005
        age_influence_worse = 0.015

        better = vaccination_effect_better * age_influence_better
        worse = vaccination_effect_worse * age_influence_worse

        random_value = random.uniform(0.0, 1.0)

        if random_value < better:
            step_type = 'gets_better'
        elif random_value < better + worse:
            step_type = 'gets_worse'
        else:
            step_type = 'nothing_happens'
    
    # Get available symptoms for a given stage and current symptoms
    def available_symptoms(self, stage, symptoms):
        possible_symptoms = []
        if stage in ['symptomatic', 'critical', 'terminal']:
            symp_symptoms = self.possible_symptoms_symptomatic()
            valid_symptoms1 = self.get_new_evol(symptoms, symp_symptoms)

            crit_symptoms = self.possible_symptoms_critical()
            valid_symptoms2 = self.get_new_evol(symptoms, crit_symptoms)

            ter_symptoms = self.possible_symptoms_terminal()
            valid_symptoms3 = self.get_new_evol(symptoms, ter_symptoms)

            possible_symptoms = valid_symptoms1 + valid_symptoms2 + valid_symptoms3

        return possible_symptoms
    
    # Get new evolving symptoms based on current symptoms
    def get_new_evol(self, symptoms, stage_symptoms):
        new_symptoms = []
        for symptom in stage_symptoms:
            if symptom not in symptoms and all(self.symptom_progression(old_symptom, symptom) for old_symptom in symptoms):
                new_symptoms.append(symptom)
        return new_symptoms
    
    # Progress the infection for a given person
    def infection_progression(self, person):
        current_person = self.persons[person]
        current_stage = current_person['stage']
        current_symptoms = current_person['symptoms']
        possible_symptoms = self.available_symptoms(current_stage, current_symptoms)

        if random.random() < 0.5:
            next_stage, next_symptoms = self.infection_gets_worse(current_symptoms, current_stage, possible_symptoms)
        else:
            next_stage, next_symptoms = self.infection_gets_better(current_symptoms, current_stage)
        if next_stage in ['recovered', 'dead']:
            self.remove_agent(person)
        else:
            self.update_stage(person, next_stage)
            self.update_symptoms(person, next_symptoms)