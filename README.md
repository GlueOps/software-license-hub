# software-license-hub
A place to track all the software glueops uses for it's platform offering.

Note: This does not take into account our dependencies dependencies.

## Requirements:

- newreleases cli: https://github.com/newreleasesio/cli-go
- create an API key

## Usage

Export your API key for newreleases

```bash
export API_KEY=""
```

Delete existing projects first

```bash
./delete.sh
```
Note: You may have to run the delete multiple times to remove everything.


Add new projects based on packages file

```bash
./add.sh
```

Google drive link to track updates: https://docs.google.com/spreadsheets/d/1h3qxbiI3QNF2MI_oVzP88tcAdeFtQ7X0bg76Dqdm7wQ/edit?usp=sharing

