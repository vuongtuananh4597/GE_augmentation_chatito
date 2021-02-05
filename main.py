from constant import *
from utils import *
from tqdm import tqdm
import random

def general_command_generate():
    clim1 = readFile(path_template_climate1)
    clim2 = readFile(path_template_climate2)
    quickcontrol = readFile(path_template_quickcontrol)
    radio = readFile(path_template_radio)
    generalcommand = readFile(path_template_general)
    all_template = clim1 + clim2 + quickcontrol + radio + generalcommand
    # <percent>, <level_all>, <temperature>, <temp_change>, <radio_name>\
    #  <frequency>, <channel>
    data = []
    for template in tqdm(all_template):
        if template.count("<") > 1 or template.count(">") > 1:
            print("template: ", template)
            break
        elif "<percent>" in template:
            data.append(template.replace("<percent>", random.choice(PERCENT)) )
            data.append(template.replace("<percent>", random.choice(PERCENT)) )
        elif "<level_all>" in template:
            data.append(template.replace("<level_all>", random.choice(LEVEL_ALL)) )
            data.append(template.replace("<level_all>", random.choice(LEVEL_ALL)) )
        elif "<temperature>" in template:
            data.append(template.replace("<temperature>", random.choice(TEMPERATURE)))
            data.append(template.replace("<temperature>", random.choice(TEMPERATURE)))
        elif "<temp_change>" in template:
            data.append(template.replace("<temp_change>", random.choice(TEMP_CHANGE)))
            data.append(template.replace("<temp_change>", random.choice(TEMP_CHANGE)))
        elif "<radio_name>" in template:
            data.append(template.replace("<radio_name>", random.choice(RADIO_NAME)))
            data.append(template.replace("<radio_name>", random.choice(RADIO_NAME)))
        elif "<frequency>" in template:
            data.append(template.replace("<frequency>", random.choice(FREQUENCY)))
            data.append(template.replace("<frequency>", random.choice(FREQUENCY)))
        elif "<channel>" in template:
            data.append(template.replace("<channel>", random.choice(CHANNEL)))
            data.append(template.replace("<channel>", random.choice(CHANNEL)))
        else:
            data.append(template)
    print(len(data))
    writeFile(data, "general_command/GE_general_command.txt")

def phone_command_generate():
    phone1 = readFile(path_template_phone1)
    phone2 = readFile(path_template_phone2)
    all_template = phone1 + phone2
    all_template = [" ".join(i.split()) for i in all_template]
    template_dict = dict()
    for i in all_template:
        template_dict[i] = getLabelFake(i)

    data = []
    data_label = []
    #  <phone_number>, <person>, <family>
    for template, template_label in tqdm(template_dict.items()):
        if template.count(">") > 1 or template.count("<") > 1:
            print("template: ", template)
            break
        elif "<phone_number>" in template:
            tmp_index = template.split().index("<phone_number>")
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PHONE_NUMBER.keys()) )
            template_label[tmp_index] = PHONE_NUMBER[temp]
            data.append(template.replace("<phone_number>", temp))
            data_label.append(flattenList(template_label))

        elif "<person>" in template:
            tmp_index = template.split().index("<person>")
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))
            temp = random.choice( list(PERSON.keys()) )
            template_label[tmp_index] = PERSON[temp]
            data.append(template.replace("<person>", temp))
            data_label.append(flattenList(template_label))

        elif "<family>" in template:
            tmp_index = template.split().index("<family>")
            temp = random.choice( list(FAMILY.keys()) )
            template_label[tmp_index] = FAMILY[temp]
            data.append(template.replace("<family>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(FAMILY.keys()) )
            tmp_index = template.split().index("<family>")
            template_label[tmp_index] = FAMILY[temp]
            data.append(template.replace("<family>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(FAMILY.keys()) )
            tmp_index = template.split().index("<family>")
            template_label[tmp_index] = FAMILY[temp]
            data.append(template.replace("<family>", temp))
            data_label.append(flattenList(template_label))

            temp = random.choice( list(FAMILY.keys()) )
            tmp_index = template.split().index("<family>")
            template_label[tmp_index] = FAMILY[temp]
            data.append(template.replace("<family>", temp))
            data_label.append(flattenList(template_label))
        
        else:
            data.append(template)
            data_label.append(template_label)
    data_label = [" ".join(i) for i in data_label]
    writeFile(data, "entity_command/phonebook/GE_phonebook.txt")
    writeFile(data_label, "entity_command/phonebook/GE_phonebook_label.txt")
    assert len(data) == len(data_label)
    print(len(data))

def navigation_command_generate():
    navi_template = readFile(path_template_navigation)
    data = []
    for template in tqdm(navi_template):
        if template.count(">") > 1 or template.count("<") > 1:
            print("template:", template)
            break
        elif "<address>" in template:
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(CITY)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))
            data.append(template.replace("<address>", random.choice(STREET_NAME)))

    writeFile(data, "entity_command/navigation/GE_navigation.txt")
    print(len(data))

def media_command_generate():
    media_template = readFile("entity_command/media/template/GE_media_template.txt")
    media_template_dict = dict()
    for t in media_template:
        media_template_dict[t] = getLabelFake(t)

    data = []
    data_label = []
    
    for template, template_label in media_template_dict.items():
        if "<artist>" in template and "<song>" in template:
            id_song = template.split().index("<song>")
            id_artist = template.split().index("<artist>")
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))

            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))
            triplet = random.choice(artist_album_song)
            data.append(template.replace("<artist>", triplet[0]).replace("<song>", triplet[2]) )
            template_label[id_artist] = ARTIST[triplet[0]]
            template_label[id_song] = SONG[triplet[2]]
            data_label.append(flattenList(template_label))


        elif "<song>" in template:
            id_song = template.split().index("<song>")
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))

            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))
            song = random.choice( list(SONG.keys()) )
            template_label[id_song] = SONG[song]
            data.append(template.replace("<song>", song))
            data_label.append(flattenList(template_label))



        elif "<artist>" in template:
            id_artist = template.split().index("<artist>")
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))

            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))
            artist = random.choice( list(ARTIST.keys()) )
            template_label[id_artist] = ARTIST[artist]
            data.append(template.replace("<artist>", artist))
            data_label.append(flattenList(template_label))

        elif "<album>" in template:
            id_album = template.split().index("<album>")
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))

            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
            album = random.choice( list(ALBUM.keys()) )
            template_label[id_album] = ALBUM[album]
            data.append(template.replace("<album>", album))
            data_label.append(flattenList(template_label))
        else:
            data.append(template)
            data_label.append(template_label)

    data_label = [" ".join(i) for i in data_label]
    writeFile(data, "entity_command/media/GE_media.txt")
    writeFile(data_label, "entity_command/media/GE_media_label.txt")
    assert len(data) == len(data_label)
    print(len(data_label))
if __name__ == "__main__":
    media_command_generate()