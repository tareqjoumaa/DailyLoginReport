## Daily Login Report

## Features

- **Automated CSV Generation:** Generates a CSV file containing user login statistics (first name, last name, number of login attempts).
- **Scheduled Email Reports:** Emails the CSV report daily to a configurable recipient.
- **Configurable Settings:** Uses a Single DocType ("Daily Login Report Settings") for managing the recipient email.


## Installation

1. **Get the daily_login_report App:** 
    `bench get-app <your-site-name> https://github.com/tareqjoumaa/DailyLoginReport.git`

2. **Install on your site:**
    `bench --site <yoursite> install-app daily_login_report`

3. **Migrate and Restart:**
    `bench migrate`
    `bench restart`    


## Prerequisites

- **Default Outgoing Email Account:** An outgoing email account must be configured under **Settings > Email Account** for the report emails to be sent.

#### License

mit