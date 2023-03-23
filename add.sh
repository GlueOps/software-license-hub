grep -v '^#' packages | while read -r line; do
    if [[ $line == *"github"* ]]; then
        ./newreleases project add github $line --auth-key ${API_KEY}
    elif [[ $line == *"artifacthub"* ]]; then
        ./newreleases project add artifacthub $line --auth-key ${API_KEY}
    elif [[ $line == *"hub.docker"* ]]; then
        ./newreleases project add dockerhub $line --auth-key ${API_KEY}
    fi
    sleep 10;
done

