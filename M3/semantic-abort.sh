echo "Stopping semantic_plants_solr..."
docker stop semantic_plants_solr

sleep 5

echo "Removing semantic_plants_solr..."
docker rm semantic_plants_solr