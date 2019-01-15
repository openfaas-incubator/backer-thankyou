# backer-thankyou

An automated thank-you for backers, patrons and sponsors via Twitter.

## Preview:

![screen shot](https://user-images.githubusercontent.com/6358735/33375960-b4815f6c-d503-11e7-8cf0-5525bd6d42e8.png)

## Installation

This is a Python OpenFaaS function that responds to webhooks from [Patreon](https://patreon.com/alexellis).

### Pre-reqs

You can deploy this code to any OpenFaaS cluster.

* OpenFaaS with public URL for gateway
* `faas-cli to deploy`

### Steps

* Clone the repo
* `cp secrets.example.yml secrets.yml`
* Setup a Twitter app to enable tweeting
* Setup a webhook on Patreon
* Edit `secrets.yml`
* Run `faas-cli deploy`

## Configuration

| env-var                | description                               | default |
|------------------------|-------------------------------------------|---------|
| `display_removed`      | Tweet when someone removes their pledge   | `false` |
| `consumer_key`         | consumer_key from Twitter API             | ``      |
| `consumer_secret`      | consumer_secret from Twitter API          | ``      |
| `access_token`         | access_token from Twitter API             | ``      |
| `access_token_secret`  | access_token_secret from Twitter API      | ``      |
| `webhook_secret`       | configured in Patreon to verify webhooks  | ``      |

## Contributions

Contributions are welcome, but must be tested end-to-end.

Commits should also be signed-off with `git commit -s`.

Roadmap:

* Move from env-vars to OpenFaaS secrets
* Allow Twitter handle and messages to be customized for other Patreon users
