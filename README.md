# FullContact

![Microservice](https://img.shields.io/badge/microservice-ready-brightgreen.svg?style=for-the-badge)
[![Docker Build Status](https://img.shields.io/docker/build/microservices/fullcontact.svg?style=for-the-badge)](https://hub.docker.com/r/microservice/fullcontact/)

## Query a person

> https://docs.fullcontact.com/api/#person-enrichment

```sh
# Storyscript
data = fullcontact person email:"bart@fullcontact.com"
```

```js
data = {
  "email": "bart@fullcontact.com",
  "emailHash": "d77ff8a9f4d2d4fea4153c81ba5d39a2",
  "twitter": "@bartlorang",
  "phone": "+13035551234",
  "fullName": "Bart Lorang",
  ...
}
```

## Query a company

> https://docs.fullcontact.com/api/#company-enrichment

```sh
# Storyscript
data = fullcontact company domain:'fullcontact.com'
```

```js
data = {
  "name": "FullContact, Inc.",
  "location": "1755 Blake Street, Suite 450, Denver, Colorado, United States",
  "twitter": "@fullcontact",
  "linkedin": "https://www.linkedin.com/company/fullcontact-inc-",
  "facebook": "https://www.facebook.com/fullcontact",
  "bio": "FullContact is the ... contacts and be awesome with people.",
  ...
```
