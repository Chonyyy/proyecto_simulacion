from pyswip import Prolog
from typing import Tuple
import random
from simulation.enviroment.sim_nodes import *
class Knowledge:
    """
    Class representing the knowledge base of an agent.

    Attributes:
        prolog (Prolog): The Prolog engine for querying the knowledge base.
    """
    def __init__(self):
        """
        Initialize the knowledge base.
        """
        self.prolog = Prolog()
        self.prolog.consult('./simulation/agents/hierarchical_agent_KB.pl')
        self.facts = {}

    def add_node_k(self, node: SimNode):
        
        node_info = {
            'addr': node.addr,
            'capacity_status': node.capacity_status,
            'node_type': node.node_type,
            # 'oppening_hours': node.oppening_hours,
            # 'closing_hours': node.closing_hours,
            'mask_required': node.mask_required
        }#TODO: add if the place is open
        try:
            node_info['oppening_hours'] = node.oppening_hours,
            node_info['closing_hours'] = node.closing_hours
            
        except:
            pass
            
        if "map" in self.facts:
            self.facts['map'][node.id] = node_info
        else: 
            self.facts['map'] = {
                node.id: node_info
            } 
               
    def add_date_k(self, date):
        """
        Add a date to the knowledge base.

        Args:
            date (tuple): The date to add.
        """
        self.facts[date] = {
            'week_day': date[0],
            'day': date[1],
            'hour': date[2],
            'min': date[3] 
        }
        
    def add_symptom_k(self, symptom):
        """
        Add a symptom to the knowledge base.

        Args:
            symptom (str): The symptom to add.
        """
        list(self.prolog.query(f'add_symptom({symptom})'))
        
        if 'symptoms' in self.facts:
            self.facts['symptoms'].add(symptom)
        else:
            self.facts['symptoms'] = set()
    
    def add_hospital_k(self, hospital_id: int, hospital_addr: Tuple[int,int]):
        """
        Add a hospital to the knowledge base.

        Args:
            hospital_id (int): The identifier of the hospital.
            hospital_addr (str): The address of the hospital.
        """
        # list(self.prolog.query(f'add_hospital({hospital_id}, {hospital_addr})'))
        raise not NotImplementedError()
        
    def add_home(self, home_id: int):
        """
        Add a home to the knowledge base.

        Args:
            home_id (int): The identifier of the home.
        """
        self.facts['home'] = home_id
            
    def add_work_place(self, node):
        """
        Add a workplace to the knowledge base.

        Args:
            wp_id (int): The identifier of the workplace.
        """
        self.facts['work_place'] = {
            'id': node.id,
            'addr':node.addr,
            'opening_hours': node.opening_hours,
            'closing_hours': node.closing_hours
        }
    
    def add_open_place(self, id: int, open: bool):
        """
        Add an open place to the knowledge base.

        Args:
            id (int): The identifier of the place.
            open (bool): Whether the place is open.
        """
        # list(self.prolog.query(f'add_open_place({id}, {str(open).lower()})'))
        raise NotImplementedError()
    
    def add_open_hours(self, id: int, opening_hours: int, closing_hours: int):
        """
        Add open hours to the knowledge base.

        Args:
            id (int): The identifier of the place.
            opening_hours (int): The opening hours of the place.
            closing_hours (int): The closing hours of the place.
        """
        # list(self.prolog.query(f'add_open_hours_place({id}, {opening_hours}, {closing_hours})'))
        raise NotImplementedError()
    
    def add_dissease_symptoms(self, symptom_list: list):
        """
        Add disease symptoms to the knowledge base.

        Args:
            symptom_list (list): The list of symptoms.
        """
        # list(self.prolog.query(f'add_dissease_symptoms({symptom_list})'))
        raise NotImplementedError()
        
    def add_current_location(self, location_id: int):
        """
        Add current location id

        Args:
            location_id (int): The id of the node the agent is currently in
        """
        # list(self.prolog.query(f'add_location({location_id})'))
        self.facts['location'] = location_id
    
    def add_is_medical_personnel(self, medical_personnel: bool):
        """
        Add medical personnel information to the knowledge base.

        Args:
            medical_personnel (bool): Whether the agent is medical personnel.
        """
        # list(self.prolog.query(f'add_if_is_medical_personal({str(medical_personnel).lower()})'))
        self.facts['is_medic'] = medical_personnel
    
    def add_mask_necessity(self, mask_necessity: bool):
        """
        Add mask necessity information to the knowledge base.

        Args:
            mask_necessity (bool): Whether a mask is necessary.
        """
        # list(self.prolog.query(f'add_mask_necessity({mask_necessity})'))
        self.facts['mask_necesity'] = mask_necessity
    
    def add_mask_requirement(self, place_id: int, requirement: bool):
        """
        Add mask requirement information to the knowledge base.

        Args:
            place_id (int): The identifier of the place.
            requirement (bool): Whether a mask is required.
        """
        # list(self.prolog.query(f'add_place_to_use_mask({place_id}, {requirement})'))
        if 'map' in self.facts and place_id in self.facts['map']:
            self.facts['maps'][place_id]['mask_required'] = requirement
    
    def add_social_distancing(self, requirement: bool):
        # list(self.prolog.query(f'add_social_distancing({requirement})'))
        self.facts['social_distancing'] = requirement
    
    def add_tests_and_diagnosis(self, requirement: bool):
        # list(self.prolog.query(f'add_tests_and_diagnosis({requirement})'))
        raise NotImplementedError()
    
    def add_isolation(self, requirement: bool):
        # list(self.prolog.query(f'add_isolation({requirement})'))
        raise NotImplementedError()
    
    def add_friends(self, friend_list: list):
        # if friend_list:
        #     list(self.prolog.query(f'add_friends({friend_list})'))
        if 'friends' in self.facts:
            self.facts['friends'].extend(friend_list)
        else:
            self.facts['friends'] = set()
    
    def add_wearing_mask(self, wearing_mask: bool):
        self.facts['wearing_mask'] = wearing_mask
        
    def add_location(self, location: int):
        self.facts['location'] = location
    
    def feedback(self, location, wearing_mask):
        if location:
            self.add_location(location)
        if wearing_mask:
            self.add_wearing_mask(wearing_mask)
    
    def query(self, queryString):
        """
        Query the knowledge base.

        Args:
            queryString (str): The query string.

        Returns:
            list: The results of the query.
        """
        return list(self.prolog.query(queryString))

    def retract_goal(self, goal_type, target_node=None):
        if goal_type in self.goals:
            del self.goals[goal_type]

    def assert_goal(self, goal_type, target_node=None):
        self.goals[goal_type] = target_node


class KnowledgeCanelo:
    """
    Class representing the knowledge base of canelo.

    Attributes:
        prolog (Prolog): The Prolog engine for querying the knowledge base.
    """
    def __init__(self):
        """
        Initialize the knowledge base.
        """
        self.knowledge = Prolog()
        self.knowledge.consult('./simulation/agents/canelo.pl')
        
    def query(self, queryString):
        """
        Query the knowledge base.

        Args:
            queryString (str): The query string.

        Returns:
            list: The results of the query.
        """
        action = list(self.knowledge.query(queryString))[0]
        return action['Recommendation'], action['RecomendationPlaces']

class BehaviorLayer:
    """
    Class representing the behavior layer of an agent.

    Attributes:
        world_model (Graph): The world model of the agent.
        knowledge (Knowledge): The knowledge base of the agent.
    """
    def __init__(self, world_model, knowledge: Knowledge):
        """
        Initialize the behavior layer.

        Args:
            world_model (Graph): The world model of the agent.
            knowledge (Knowledge): The knowledge base of the agent.
        """
        self.world_model = world_model
        self.knowledge = knowledge
        try:
            self.add_map_to_k()
        except:
            pass

    def add_map_to_k(self):
        """
        Add the world model to the knowledge base.
        """
        k = self.knowledge
        for node in self.world_model.nodes.values():
            if node.node_type == 'hospital':
                k.add_node_k(node)
            elif node.node_type == 'block':
                k.add_node_k(node)
            elif node.node_type == 'public_space':
                k.add_node_k(node)
            elif node.node_type == 'work_space':
                k.add_node_k(node)
            elif node.node_type == 'bus_stop':
                k.add_node_k(node)
            elif node.node_type == 'hospital':
                k.add_node_k(node)
            else:
                pass

    def react(self, queryString):
        """
        React to a query string.

        Args:
            queryString (str): The query string.

        Returns:
            tuple: The action and arguments to perform.
        """
        query = f"{queryString}"
        action1 = []
        
        for x in self.knowledge.query(query):
            action1.append(x['Action'])
            action1.append(x['Arguments'])
            
        try:
            action = list(self.knowledge.query(query))[0]
            return action['Action'], action['Arguments']
        except:
            return None, None
        
    def search_friend(self, agent, plan):
        message, place = self._split_string(plan) if plan else None, None
        self.world_model.comunicate(agent, message, place)
        
    def _split_string(self, s):
        parts = s.split('(', 1)
        outside_parentheses = parts[0]
        inside_parentheses = parts[1].split(')', 1)[0] if len(parts) > 1 else ''
        return outside_parentheses, inside_parentheses
    
class LocalPlanningLayer:
    """
    Class representing the local planning layer of an agent.

    Attributes:
        behavior_layer_based (BehaviorLayer): The behavior layer based on which the local planning is performed.
        prolog (Knowledge): The knowledge base of the agent.
    """
    def __init__(self, behavior_layer_based: BehaviorLayer, knowledge: Knowledge):
        """
        Initialize the local planning layer.

        Args:
            behavior_layer_based (BehaviorLayer): The behavior layer based on which the local planning is performed.
            knowledge (Knowledge): The knowledge base of the agent.
        """
        self.behavior_layer_based = behavior_layer_based
        self.knowledge = knowledge
        self.plans = {} 

    def plan(self, queryString):
        """
        Plan based on a query string.

        Args:
            queryString (str): The query string.
        """
        query = f"{queryString}"
        plan = list(self.knowledge.query(query))
        return plan[0]['X'] if plan != [] else []
    
    def plan_coperative(self, agent, plan):
        self.behavior_layer_based.search_friend(agent, plan)

class CooperativeLayer:
    """
    Class representing the cooperative layer of an agent.

    Attributes:
        local_planning_layer (LocalPlanningLayer): The local planning layer of the agent.
        prolog (Knowledge): The knowledge base of the agent.
    """
    def __init__(self, local_planning_layer, knowledge: Knowledge):
        """
        Initialize the cooperative layer.

        Args:
            local_planning_layer (LocalPlanningLayer): The local planning layer of the agent.
            knowledge (Knowledge): The knowledge base of the agent.
        """
        self.local_planning_layer: LocalPlanningLayer = local_planning_layer
        self.knowledge = knowledge

    def cooperate(self,agent, queryString):
        """
        Cooperate based on a query string.

        Args:
            queryString (str): The query string.
        """
        self.local_planning_layer.plan_coperative(agent, self.generate_plan())
    
    def generate_plan(self):
        plan = self.local_planning_layer.plan('planification_step(X)')
        return plan
    
    def evaluate_plan():
        pass
        
    
