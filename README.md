# test-deploy-bot
Sandbox for deploying a dummy Telegram bot to Digitalocean

This bot knows when it was built and deployed. Nothing else.

## Example

```
> /start
Hi! I was built at 2020-04-24 00:15 and deployed at Fri Apr 24 00:17:01 UTC 2020
```

## Explore

Most of the interesting stuff lies in `.github/workflows/dockerpublish.yml`.
The rest is in `Dockerfile`.

Enjoy!
