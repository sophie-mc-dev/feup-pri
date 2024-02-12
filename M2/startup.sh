#!/bin/bash

# This script expects a container started with the following command.
docker run -p 8983:8983 --name plants_solr -v "${PWD}:/data" -d solr:9.3 solr-precreate plants

echo "Waiting for Solr to start..."
sleep 20

# Populate synonyms.txt from container - to use in filters
docker cp synonyms.txt plants_solr:/var/solr/data/plants/conf

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary "@./schemas/plants_schema.json" \
    http://localhost:8983/solr/plants/schema

# Populate collection using mapped path inside container.
docker exec plants_solr bin/post -c plants /data/data/plants.json
