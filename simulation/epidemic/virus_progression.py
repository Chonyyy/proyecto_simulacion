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
        "young": {"gets_better": 0.0005, "gets_worse": 0.0003, "nothing_happens": 0.9992},
        "adult": {"gets_better": 0.0005, "gets_worse": 0.0005, "nothing_happens": 0.9990},
        "old": {"gets_better": 0.0005, "gets_worse": 0.0015, "nothing_happens": 0.9980}
    },
    "symptom_progression": {
        "normal_fever": "critical_fever",
        "normal_cough": "critical_cough",
        "normal_short_breath": "critical_short_breath",
        "stomach_ache": "gastritis",
        "critical_fever": "terminal_fever"
    }
}

reverse_progression = dict(zip(database["symptom_progression"].values(), database["symptom_progression"].keys()))
database["reverse_progression"] = reverse_progression

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
        next_symptoms = add_symptom(symptom, symptoms, next_symptoms)

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
    if symptom in database["symptom_progression"].values():
        for key, value in database["symptom_progression"].items():
            if value == symptom:
                next_symptoms.remove(key)
                next_symptoms.append(symptom)
                return next_symptoms
    else:
        next_symptoms.append(symptom)
        return next_symptoms

def remove_symptom(symptom, symptoms, next_symptoms):#FIXME
    if symptom in database["reverse_progression"]:
        next_symptoms.remove(symptom)
        next_symptoms.append(database["reverse_progression"][symptom])
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

        # Get the necessary information for the current agent
        vaccination_status = self.persons[person]['vaccination_status']
        current_stage = self.persons[person]['stage']
        age_group = self.persons[person]['age_group']
        current_symptoms = self.persons[person]['symptoms']
        next_stage, new_symptoms = current_stage, current_symptoms

        # Determine if the infection will get worse, better, or remain the same
        step_type = self.step_type(age_group, vaccination_status)


        # Changing the stage of the person if possible
        if step_type == 'gets_better':
            next_stage, new_symptoms = infection_gets_better(current_symptoms, current_stage)#TODO: return next stage and next symptoms list
        elif step_type == 'gets_worse':
            # Determine if there are any new symptoms to add
            possible_symptoms = self.available_symptoms(current_stage, current_symptoms)
            next_stage, new_symptoms = infection_gets_worse(current_symptoms, current_stage, possible_symptoms)#TODO: return next stage and next symptoms list
        else:
            return next_stage

        # Updating agent information
        if next_stage in ['recovered', 'dead']:
            self.remove_agent(person)
        else:
            self.update_stage(person, next_stage)
            self.update_symptoms(person, new_symptoms)

        return next_stage
    
    # Determine the step type based on age group and vaccination status
    def step_type(self, age_group, vaccination_status):
        return self.step_type_gen(age_group, vaccination_status)
    
    # Generate the step type based on age group and vaccination status
    def step_type_gen(self, age_group, vaccination_status):
        vaccination_effect_better = database["vaccination_effects"]["gets_better"] if vaccination_status else 1.0
        vaccination_effect_worse = database["vaccination_effects"]["gets_worse"] if vaccination_status else 1.0

        age_influence_better = database["age_influence"][age_group]["gets_better"]
        age_influence_worse = database["age_influence"][age_group]["gets_worse"]

        better = vaccination_effect_better * age_influence_better
        worse = vaccination_effect_worse * age_influence_worse

        random_value = random.uniform(0.0, 1.0)

        if random_value < better:
            return 'gets_better'
        elif random_value < better + worse:
            return 'gets_worse'
        else:
            return 'nothing_happens'
    
    # Get available symptoms for a given stage and current symptoms
    def available_symptoms(self, stage, symptoms):
        if stage == 'symptomatic':
            symp_symptoms = database["possible_symptoms"]["symptomatic"]
            return self.get_new_evol(symptoms, symp_symptoms)

        if stage == "critical":
            crit_symptoms = database["possible_symptoms"]["critical"]
            return self.get_new_evol(symptoms, crit_symptoms)

        if stage == "terminal":
            ter_symptoms = database["possible_symptoms"]["terminal"]
            return self.get_new_evol(symptoms, ter_symptoms)

        return []
    
    # Get new evolving symptoms based on current symptoms
    def get_new_evol(self, symptoms, stage_symptoms):
        new_symptoms = []
        for symptom in stage_symptoms:
            if symptom in symptoms:
                continue
            if symptom not in database["symptom_progression"].values():
                new_symptoms.append(symptom)
            elif database["reverse_progression"][symptom] in symptoms:
                new_symptoms.append(symptom)
        return new_symptoms
    
    # Progress the infection for a given person
    # def infection_progression(self, person):
    #     current_person = self.persons[person]
    #     current_stage = current_person['stage']
    #     current_symptoms = current_person['symptoms']
    #     possible_symptoms = self.available_symptoms(current_stage, current_symptoms)

    #     if random.random() < 0.5:
    #         next_stage, next_symptoms = self.infection_gets_worse(current_symptoms, current_stage, possible_symptoms)
    #     else:
    #         next_stage, next_symptoms = infection_gets_better(current_symptoms, current_stage)
    #     if next_stage in ['recovered', 'dead']:
    #         self.remove_agent(person)
    #     else:
    #         self.update_stage(person, next_stage)
    #         self.update_symptoms(person, next_symptoms)