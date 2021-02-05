import numpy as np
from utils import *

# path template general
path_template_general = "general_command/template/GE_common_general.txt"
path_template_radio = "general_command/template/GE_radio_template.txt"
path_template_quickcontrol = "general_command/template/GE_quickcontrol_template.txt"
path_template_climate1 = "general_command/template/GE_climate_template1.txt"
path_template_climate2 = "general_command/template/GE_climate_template2.txt"

PERCENT = [str(i) for i in np.arange(1,100)]
LEVEL_ALL = [str(i) for i in np.arange(1,7)]
TEMPERATURE = [str(i) for i in np.arange(15,36)]
TEMP_CHANGE = [str(i) for i in np.arange(2,11)]
RADIO_NAME = readFile("general_command/entity_file/RADIO.txt")
FREQUENCY, CHANNEL = readFileChannel("general_command/entity_file/CHANNEL.txt")

# path template phonebook
path_template_phone1 = "entity_command/phonebook/template/GE_phone_template1.txt"
path_template_phone2 = "entity_command/phonebook/template/GE_phone_template2.txt"

PERSON = readFileEntityWithLabelContact("entity_command/phonebook/entity_file/person.txt")
FAMILY = readFileEntityWithLabelContact("entity_command/phonebook/entity_file/family.txt")
PHONE_NUMBER = readFileEntityWithLabelFake("entity_command/phonebook/entity_file/phoneNumber.txt")

# path template navigation
path_template_navigation = "entity_command/navigation/template/GE_navigation_template.txt"
STREET_NAME = readFile("entity_command/navigation/entity_file/streetName.txt")
CITY = readFile("entity_command/navigation/entity_file/cities.txt")
CITY = ["nach " + i for i in CITY]

# path template media
path_template_media = "entity_command/media/template/GE_media_template.txt"
POP = readFile("entity_command/media/GermanSong/Pop.csv")
POP = POP[1:]
POP = [i.split(",") for i in POP]
POP = [(i[1].strip(), i[2].strip(), i[4].strip()) for i in POP]
RAP = readFile("entity_command/media/GermanSong/Rap.csv")
RAP = RAP[1:]
RAP = [i.split(",") for i in RAP]
RAP = [(i[1].strip(), i[2].strip(), i[4].strip()) for i in RAP]
ROCK = readFile("entity_command/media/GermanSong/Rock.csv")
ROCK = ROCK[1:]
ROCK = [i.split(",") for i in ROCK]
ROCK = [(i[1].strip(), i[2].strip(), i[4].strip()) for i in ROCK]
SCHLAGER = readFile("entity_command/media/GermanSong/Schlager.csv")
SCHLAGER = SCHLAGER[1:]
SCHLAGER = [i.split(",") for i in SCHLAGER]
SCHLAGER = [(i[1].strip(), i[2].strip(), i[4].strip()) for i in SCHLAGER]

artist_album_song = POP + RAP + ROCK + SCHLAGER
ARTIST, ALBUM, SONG = process_media_entities(artist_album_song)

