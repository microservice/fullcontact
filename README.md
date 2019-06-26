# _FullContact_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)
<!-- [![Docker Build Status](https://img.shields.io/docker/build/microservices/fullcontact.svg?style=for-the-badge)](https://hub.docker.com/r/microservice/fullcontact/) -->

FullContact is a contact management software designed for individuals and teams. It has the capability to collect contact data and information of companies, enterprises, and professionals; and organizes them into a centralized location.

## Direct usage in [Storyscript](https://storyscript.io/):

##### Query a person
```coffee
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

##### Query a company
```coffee
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

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Query a person
```shell
$ omg run person -a email=<EMAIL_ADDRESS> -a twitter=<TWITTER> -a phone=<PHONE_NUMBER> -e API_KEY=<API_KEY> -e USER_AGENT=<USER_AGENT>
```
##### Query a company
```shell
$ omg run company -a domain=<DOMAIN> -e API_KEY=<API_KEY> -e USER_AGENT=<USER_AGENT>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/fullcontact/blob/master/LICENSE).
