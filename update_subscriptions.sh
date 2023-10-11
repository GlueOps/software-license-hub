#!/bin/bash

update-subscriptions () {
  owner=""
  gh_pat=""

    # Parse flags
    while [[ $# -gt 0 ]]; do
      key="$1"
      case $key in
        (-o|--owner)
          owner="$2"
          shift
          shift
          ;;
        (-t|--gh-pat)
          gh_pat="$2"
          shift
          shift
          ;;
        (--help)
          echo "Usage: update-subscriptions [options]"
          echo ""
          echo "Options:"
          echo "  -o, --owner VALUE   Select the owner who will be responsible for committing updates."
          echo "  -t, --gh-pat VALUE  Set the PAT from the SERVICE USER that will receive notifications"
          echo "  --help                    Show this help message and exit"
          return
          ;;
        (*)
          echo "Unknown option: $key"
          echo "Run 'update-subscriptions --help' for usage information."
          return
          ;;
      esac
    done

    # Check if arguments were provided
    if [[ -z $owner || -z $gh_pat ]]; then
        echo "Both arguments are required."
        echo "Run 'update-subscriptions --help' for usage information."
        return
    fi

    set -e
    docker build . -t notifs
    docker run -it -e GITHUB_PAT=$gh_pat -e REPO_OWNER=$owner notifs
}

