# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/telegram-channel-growth-analytics").call(run_input={
    "channels": [
        "telegram",
        "durov",
        "bloomberg",
        "rian_ru",
        "tass_agency",
        "nexta_live",
        "botnews",
        "tginfo",
        "contest",
        "designers",
        "habr_com",
        "proxy_tg"
    ],
    "postsPerChannel": 40,
    "maxItems": 50
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
