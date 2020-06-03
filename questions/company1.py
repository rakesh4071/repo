Write a program/script that accepts a path to a log file and prints the following information:

- How many requests were made throughout the entire log?
- How many failed requests appear in the log?
- How many unique pages were requested? What were they and how many times was each requested?
- How many unique clients made requests? How many requests did each client make? Display the top 10 to keep output manageable.
- How many requests per second (on average) are made during each day in the log?

Log Format
----------
The logs are an ASCII file with one line per request, with the following columns:

1. host making the request. A hostname when possible, otherwise the Internet address if the name could not be looked up. missing data will be represented by a single "-"
2. timestamp in the format "DAY MON DD HH:MM:SS YYYY", where DAY is the day of the week, MON is the name of the month, DD is the day of the month,
   HH:MM:SS is the time of day using a 24-hour clock, and YYYY is the year. The timezone is -0400
3. request given in quotes
4. HTTP reply code
5. bytes in the reply
