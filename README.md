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

#### Step 1 - prepare the repo / integrations

* Fork the repo into your own account. Your username will be the `USERNAME` variable we use later
* Setup a Twitter app to enable tweeting from the function. Save the access / consumer keys and secrets.
* Setup a webhook on Patreon to the URL where your function will run. Save the webhook and note down the secret

### Step 2 - Seal new secrets

```sh
# USERNAME corresponds to your username on OpenFaaS Cloud
export USERNAME="openfaas"

# You get this after adding your Patreon webhook
export PATREON_WEBHOOK_SECRET=""

export CONSUMER_KEY=""
export CONSUMER_SECRET=""

export ACCESS_TOKEN=""
export ACCESS_TOKEN_SECRET=""

faas-cli cloud seal --name "$USERNAME"-backer-thankyou-secrets \
    --literal patreon-webhook-secret="${PATREON_WEBHOOK_SECRET}" \
    --literal consumer-key="${CONSUMER_KEY}" \
    --literal consumer-secret="${CONSUMER_SECRET}" \
    --literal access-token="${ACCESS_TOKEN}" \
    --literal access-token-secret="${ACCESS_TOKEN_SECRET}"
```

### Step 3 - Deploy to OpenFaaS Cloud

Now install the OpenFaaS Cloud [Community Cluster] app to your repo and push your new changes.

### Step 4 - Test e2e with the Patreon webhook tester

If you run into any issues, please feel free to open a GitHub issue.

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
