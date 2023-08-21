## IMPORTANT

This process will remove/unsubscribe from any repos that are not in the packages.json. So make sure you pass in the token for the github account you want to have this process run against.


# software-license-hub
A place to track all the software glueops uses for it's platform offering.

Note: This does not take into account our dependencies dependencies.

## Requirements

- docker
- A clean github account that doesn't have any repos starred or notifications configured.
- Using the clean/new github account create a [Personal Access Token](https://github.com/settings/tokens/new?scopes=repo,notifications&description=GLUEOPS%20-%20Codespaces%20GITHUB_TOKEN_FOR_NOTIFS)
  - You can set the expiration to 1 day or even 1 hour. This script runs very quickly.

## Usage

```bash
export GITHUB_PAT="<<<the-PAT-you-just-created-above>>"
export REPO_OWNER="usually your githubid however, it likely isn't the githubID you are using for these notifications."
docker build . -t notifs
docker run -it -e GITHUB_PAT=$GITHUB_PAT -e REPO_OWNER=$REPO_OWNER notifs
```

## IMPORTANT

This process will remove/unsubscribe from any repos that are not assigned to you in the packages.json. So make sure you pass in the token for the github account you want to have this process run against.
