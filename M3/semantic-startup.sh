#!/bin/bash

# This script expects a container started with the following command.
docker run -p 8983:8983 --name semantic_plants_solr -v "${PWD}:/data" -d solr:9.3 solr-precreate semantic_plants

echo "Waiting for Solr to start..."
sleep 20

# Populate synonyms.txt from container - to use in filters
docker cp synonyms.txt semantic_plants_solr:/var/solr/data/semantic_plants/conf

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary "@./schemas/semantic_schema.json" \
    http://localhost:8983/solr/semantic_plants/schema

# Index the JSON documents.
curl -X POST -H 'Content-type:application/json' \
    --data-binary "@./data/semantic_plants.json" \
    http://localhost:8983/solr/semantic_plants/update?commit=true


# Populate collection using mapped path inside container.
docker exec semantic_plants_solr bin/post -c plants /data/data/semantic_plants.json