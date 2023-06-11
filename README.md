# software-license-hub
A place to track all the software glueops uses for it's platform offering.

Note: This does not take into account our dependencies dependencies.


## Requirements:

- docker
- A clean github account that doesn't have any repos starred or notifications configured.
- Using the clean/new github account create a [Personal Access Token](https://github.com/settings/tokens/new?scopes=repo,notifications&description=GLUEOPS%20-%20Codespaces%20GITHUB_TOKEN_FOR_NOTIFS)
  - You can set the expiration to 1 day or even 1 hour. This script runs very quickly.

## Usage


```bash
export GITHUB_PAT="<<<the-PAT-you-just-created-above>>"
docker build . -t notifs
docker run -it -e GITHUB_PAT=$GITHUB_PAT notifs
```
