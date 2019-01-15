# backer-thankyou

An automated thank-you for backers, patrons and sponsors via Twitter.

Python OpenFaaS function that responds to webhooks from [Patreon](https://patreon.com/alexellis)

Preview:

![screen shot](https://user-images.githubusercontent.com/6358735/33375960-b4815f6c-d503-11e7-8cf0-5525bd6d42e8.png)



| env-var                | description                               | default |
|------------------------|-------------------------------------------|---------|
| `display_removed`      | Tweet when someone removes their pledge   | `false` |
| `consumer_key`         | consumer_key from Twitter API             | ``      |
| `consumer_secret`      | consumer_secret from Twitter API          | ``      |
| `access_token`         | access_token from Twitter API             | ``      |
| `access_token_secret`  | access_token_secret from Twitter API      | ``      |
| `webhook_secret`       | configured in Patreon to verify webhooks  | ``      |
