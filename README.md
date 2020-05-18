# python-kanka ![](https://github.com/rbtnx/python-kanka/workflows/build/badge.svg)
This is a python interface to the API from https://kanka.io. It's still early development so use it at your own risk.

## Installation
This module is compatible with Python >= 3.7. When inside the repository root, install the module with
```
pip setup.py install
```
A virtual environment is recommended.

## Usage
To get started you need an API token, see <https://kanka.io/en-US/docs/1.0/setup> (oAuth is not supported by this module):

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
char.entry
last_session = my_campaign.journal({session_id})
last_session.name
```

At the moment not all entities are implemented, see table below.

| Entity name | retrieve | create | update |
|:------------|:----------------------:|:----------------------:|:----------------------:|
|Profile      |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Campaign     |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Character    |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Location     |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Family       |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Organisation |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Item         |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Note         |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Event        |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Calendar     |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Race         |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Quest        |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Journal      |:heavy_check_mark:      |:heavy_multiplication_x:|:heavy_multiplication_x:|
|Ability      |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Tag          |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Conversation |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
|Dice Roll    |:heavy_multiplication_x:|:heavy_multiplication_x:|:heavy_multiplication_x:|
