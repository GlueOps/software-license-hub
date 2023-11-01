# software-license-hub

A place to track all the software glueops uses for it's platform offering.

Note: This does not take into account our dependencies dependencies.

## Requirements

- docker
- A clean github account that doesn't have any repos starred or notifications configured.
- Using the clean/new github account create a [Personal Access Token](https://github.com/settings/tokens/new?scopes=repo,notifications&description=GLUEOPS%20-%20Codespaces%20GITHUB_TOKEN_FOR_NOTIFS)
  - You can set the expiration to 1 day or even 1 hour. This script runs very quickly.

## Usage

Load the `update_subscriptions` function to your environment.

```bash
source update_subscriptions.sh
```

Run the command to update your subscriptions, passing in the following arguments:

`-o` : The GitHub id that will be committing update changes in dependent repositories.
</br>
`-t` : The PAT just created above.

For example

```bash
update-subsctiptions -o "my-gh-user-committing-updates" -t "ghp_XXXXXXXXXXXXXXXX"
```

## IMPORTANT

This process will remove/unsubscribe from any repos that are not assigned to you in the packages.json. So make sure you pass in the token for the github account you want to have this process run against.
