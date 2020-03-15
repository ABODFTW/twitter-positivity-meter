# twitter-positivity-meter

This is a web app that identifies twitter accounts as being positive or
negative, so you know what you're getting your self into :)

## Main Features:

- Be able to search a page to be analyzed as positive or negative
- Showing a simple report of the account and the used words
- Identify the page as more positive or negative

## Additional features:

- Charts
- Show how is the page positivity in comparison to other pages
- Support Hashtags, Search Terms

## Technical Overview

- In the back-end we will need the following:
  - Natural Language Processing, Currently English only
  - Twitter Scraper/API
  - Basic Server Logic s- Database to store the twitter accounts and their
    scores
- In the front-end:
  - A simple UI
  - Charts

## TODO:

- [x] Create the server logic
- [x] Create Twitter Scraper/API
- [x] Connect it to the server logic
- [x] Implement the NLP
- [] Create the UI
- [] Optimize it by storing the data into DB
- [] Validate that there is an account with this name by using an external
  requests
- [] Adding external requests to twitter to fetch account image and name
- [] Add warning regarding the accuracy of the details, and that twitter has
  nothing to with this
- [] Deploy
