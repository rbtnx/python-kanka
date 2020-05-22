# python-kanka ![](https://github.com/rbtnx/python-kanka/workflows/build/badge.svg)
This is a python interface to the API from https://kanka.io. It's still early development so use it at your own risk.

## Installation
This module is compatible with Python >= 3.7. When inside the repository root, install the module with
```
pip install -r requirements.txt
python setup.py install
```
A virtual environment is recommended.


## Usage
To get started you need an API token, see <https://kanka.io/en-US/docs/1.0/setup> (oAuth is not supported by this module).

Create the client with
```python
import kanka
token = {your_api_token_string}
client = kanka.KankaClient(token)
```

With this you can get a list of campaigns and import a campaign by its ID:
```python
client.get_campaigns()
my_campaign = client.campaign({campaign_id})
```

With the campaign object you have access to its entities. Get a list of entities wih `Campaign.get_list_of({entities})` or import an entity with the matching method. 
```python
my_campaign.get_list_of("characters")
my_campaign.get_list_of("journals")

char = my_campaign.character({character_id)
char.age
last_session = my_campaign.journal({session_id})
last_session.name
```

### **Searching for entities**
You can search for entities using the [/search](https://kanka.io/en/docs/1.0/search) endpoint of the kanka API:
```python
match = my_campaign.search("Legolas")
```
This returns a list of entity objects with names matching the search term. If for example the term `"Legolas"` matches twos characters and one location, the variable `match` will contain two `StoredCharacter` objects and one `StoredLocation` object as a `list`. You can access the entity's attributes as shown above with
```python
match[0].name    # match[0] is the first list entry,
                 # a StoredCharacter object
match[2].map_url # match[2] is the third list entry,
                 # a StoredLocation object
```

### **Create new entity**
You can create a new (empty) entity with for example
```python
gimli = my_campaign.new_entity("character")
vulcan = my_campaign.new_entity("race")
```
All attributes will be set to `None` except the entity name, which is set to `"New {entity}"`. You can fill out as many attributes as you like and then upload the entity with
```pyhon
gimli.upload()
```
You'll receive a json dictionary with the data of the newly created entity if successfull.

### **Delete an entity**
Delete an entity of a campaign using the campaigns `delete` method by specifying the entity type and the entity id, for example:
```python
my_campaign.delete("character", 666666)
```
If successfull, the method returns `True`.

### **Download campaign data**

You can also import all the entities of a campaign into a `StoredCampaign` object:
```python
my_campaign = client.import_campaign({campaign_id})
my_campaign.characters         # displays a list of all characters
my_campaign.characters[3].name # displays the name of the fourth character in the list
```

At the moment not all entities are implemented, see table below.

| Entity name | retrieve | create | update | delete |
|:------------|:----------------------:|:----------------------:|:----------------------:|:----------------------:|
|Profile      |:heavy_check_mark:      ||||
|Campaign     |:heavy_check_mark:      ||||
|Character    |:heavy_check_mark:      |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|heavy_check_mark:|
|Location     |:heavy_check_mark:      |:heavy_check_mark:|:heavy_check_mark:|heavy_check_mark:|
|Family       |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Organisation |:heavy_check_mark:      |:heavy_check_mark:|:heavy_check_mark:|heavy_check_mark:|
|Item         |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Note         |:heavy_check_mark:      |:heavy_check_mark:|:heavy_check_mark:|heavy_check_mark:|
|Event        |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Calendar     |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Race         |:heavy_check_mark:      |:heavy_check_mark:|:heavy_check_mark:|heavy_check_mark:|
|Quest        |:heavy_check_mark:      |:heavy_check_mark:|:heavy_check_mark:|heavy_check_mark:|
|Journal      |:heavy_check_mark:      |:heavy_check_mark:|:heavy_check_mark:|heavy_check_mark:|
|Ability      |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Tag          |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Conversation |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Dice Roll    |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
