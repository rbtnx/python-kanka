# python-kanka ![](https://github.com/rbtnx/python-kanka/workflows/build/badge.svg)
This is a python interface to the API from https://kanka.io. It's still early development so use it at your own risk.
This module is compatible with Python >= 3.7.

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
char.age
last_session = my_campaign.journal({session_id})
last_session.name
```

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

You can also import all the entities of a campaign into a `StoredCampaign` object:
```python
my_campaign = client.import_campaig({campaign_id})
my_campaign.characters         # displays a list of all characters
my_campaign.characters[3].name # displays the name of the fourth character in the list
```

At the moment not all entities are implemented, see table below.

| Entity name | retrieve | create | update |
|:------------|:----------------------:|:----------------------:|:----------------------:|
|Profile      |:heavy_check_mark:      |||
|Campaign     |:heavy_check_mark:      |||
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
