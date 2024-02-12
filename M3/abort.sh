echo "Stopping plants_solr..."
docker stop plants_solr

sleep 5

echo "Removing plants_solr..."
docker rm plants_solr