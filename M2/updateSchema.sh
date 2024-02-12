docker exec plants_solr bin/solr delete -c plants

docker exec plants_solr bin/solr create_core -c plants

# Populate synonyms.txt from container - to use in filters
docker cp synonyms.txt plants_solr:/var/solr/data/plants/conf

curl -X POST -H 'Content-type:application/json' \
    --data-binary "@./schemas/plants_schema.json" \
    http://localhost:8983/solr/plants/schema
    
docker exec plants_solr bin/post -c plants /data/data/plants.json