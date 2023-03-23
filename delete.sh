# Run this script multiple times until it says No projects found.

./newreleases project list --auth-key ${API_KEY} | tail -n +2 | awk '{print $1}' | while read -r value; do
    ./newreleases project remove $value --auth-key ${API_KEY}
done

./newreleases project list --auth-key ${API_KEY}