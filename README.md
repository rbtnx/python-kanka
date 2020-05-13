# python-kanka
This is python client for https://kanka.io. It's still early development so use it at your own risk.

To get started you need an API token. Create the client with
```python
import kanka
token = {your_api_token_string}
client = kanka.api.KankaClient(token)
```

With this you can get a list of campaigns or import a campaign:
```python
client.get_campaigns()
my_campaign = client.campaign({campaign_id})
```
