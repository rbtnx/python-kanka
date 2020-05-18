# python-kanka ![](https://github.com/rbtnx/python-kanka/workflows/build/badge.svg)
This is a python interface to the API from https://kanka.io. It's still early development so use it at your own risk.
This module is compatible with Python >= 3.7.

To get started you need an API token, see <https://kanka.io/en-US/docs/1.0/setup>.

Create the client with
```python
import kanka
token = {your_api_token_string}
client = kanka.KankaClient(token)
```

With this you can get a list of campaigns or import a campaign and get entities from it:
```python
client.get_campaigns()
my_campaign = client.campaign({campaign_id})
my_campaign.get_characters()
char = my_campaign.character({character_id)
char.entry
```
