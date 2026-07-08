import urllib.request, json 
from pprint import pprint
import re

emf_link_julia = "https://www.emfcamp.org/favourites.json?token=2761-5gJV4HRMtHwVArn2HMbP"

def get_events(link):
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
    events = {}
    for d in data:
        entry_dictionary = dict(d)
        id_key = (entry_dictionary.get('id'))
        keys = ["cost", "drop_in", "equipment", "title","type"]
        subset_dictionary = {key:entry_dictionary[key] for key in keys if key in entry_dictionary}
        events.update({id_key:subset_dictionary})
    return events


def duo_overlap_dictionary(events_a, events_b):
    keys_a = list(events_a.keys())
    keys_b = list(events_b.keys())
    overlap_interest = list(set(keys_a) & set(keys_b))
    overlap_interest.sort()
    return {key:events_a[key] for key in overlap_interest if key in events_a}

def overlap_dictionary(dictionary_list):
    if len(dictionary_list) == 1:
        return dictionary_list[0]
    if len(dictionary_list) == 2:
        return duo_overlap_dictionary(dictionary_list[0], dictionary_list[1])
    if len(dictionary_list) > 2: 
        a = dictionary_list.pop()
        b = dictionary_list.pop()
        c = duo_overlap_dictionary(a, b)
        dictionary_list.append(c)
        return overlap_dictionary(dictionary_list)

def organize(event_dictionary):
    talks_dict = {key:value for key,value in event_dictionary.items() if value.get('type') == 'talk'}
    workshop_dict = {key:value for key,value in event_dictionary.items() if value.get('type') == 'workshop'}
    film_dict = {key:value for key,value in event_dictionary.items() if value.get('type') == 'film'}
    music_dict = {key:value for key,value in event_dictionary.items() if value.get('type') == 'music'}
    performance_dict = {key:value for key,value in event_dictionary.items() if value.get('type') == 'performance'}
    familyworkshop_dict = {key:value for key,value in event_dictionary.items() if value.get('type') == 'familyworkshop'}
    return {'talks': talks_dict, 'workshops': workshop_dict, 'films': film_dict, 
            'music': music_dict, 'performances': performance_dict, 
            'familyworkshop': familyworkshop_dict}

def cost_dictionary(event_dictionary):
    cost_dict = {}
    ## could be a one liner but I find it easier to seperate conditions into singular variable lines.
    for key,value in event_dictionary.items():
        has_cost =  'cost' in value.keys()
        cost_value_not_empty = value.get('cost') != ''
        cost_value_not_free = value.get('cost') != 'free'
        if has_cost and cost_value_not_empty and cost_value_not_free:
            cost_dict.update({key:value})
    return cost_dict

def equipment_dictionary(event_dictionary):
    equipment_dict = {}
    ## could be a one liner but I find it easier to seperate conditions into singular variable lines.
    for key, value in event_dictionary.items():
        has_equipment = 'equipment' in value.keys() 
        equipment_value_not_empty = value.get('equipment') != ''
        if has_equipment and equipment_value_not_empty:
            equipment_dict.update({key:value})
    return equipment_dict

def summation(cost_dictionary):
    # get all the costs for every event in the dictionary 
    # (you have already made sure they have a cost associated with them)
    costs = [value.get('cost') for _,value in cost_dictionary.items()]
    ## strip them of any notes in parentheses, and drop the pound sign that prepends all of them
    pounds = [re.sub("\(.*\)|\s-\s.*", "", string[1:]).strip() for string in costs if "£" in string]
    ## return the sum of all of them and if there are any ranges, grab the higher of the range
    return sum([int(re.sub("^.*-", "", numbers)) for numbers in pounds])

def cost_andor_equipment(event_dictionary, cost = False, equipment = False, cost_sum= False):
    ## if cost_sum is set to true, print out the sum of the costs given
    if cost_sum:
        cost_dict = cost_dictionary(event_dictionary)
        pounds_sum = summation(cost_dict)
        print(f"The sum of costs for the given events is £{pounds_sum}")
     ## if both true return a comprehensive dictionary of the two
    if equipment and cost: return cost_dictionary(event_dictionary) | equipment_dictionary(event_dictionary)
    ## else just return one or the other
    elif cost: return cost_dictionary(event_dictionary)
    elif equipment: return equipment_dictionary(event_dictionary)
    ## if neither are true, return an empty dictionary
    else: return {}


def dict_to_txt(dict,txt_path):
    with open(txt_path, "w") as file:
        json.dump(dict, file, indent=3)


events_julia = get_events(emf_link_julia)
cost_andor_equipment(events_julia, cost_sum= True)

