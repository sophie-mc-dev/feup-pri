# Milestone #3: Search System

## Group T01G15

| Name               | GitHub                                                 |
| ------------------ | ------------------------------------------------------ |
| Bárbara Rodrigues  | [@babs3](https://github.com/babs3)                     |
| Ruben              | [@FafnirNithhoggr](https://github.com/FafnirNithhoggr) |
| Sofia Merino Costa | [@sophie-mc-dev](https://github.com/sophie-mc-dev)     |
| Tiago Ribeiro      | [@TiagoMRib](https://github.com/TiagoMRib)             |

---

### Milestone Description

The third milestone is achieved with the development of the final version of the search system. This version is an improvement over the previous milestone, making use of features and techniques with the goal of improving the quality of the search results.

For this milestone, each group is expected to explore innovative approaches and ideas, and will heavily depend on the context and data of each group. Additionally, an extended evaluation of the results and a comparison with the previous version of the search system is also expected.

## Commands

### For Windows

Open a wsl terminal:

```
wsl
```

If you don't have 'dos2unix' installed, run this command first:

```
sudo apt-get install dos2unix
```

Then convert the line endings in startup.sh from Windows-style (CRLF) to Unix-style (LF):

```
dos2unix startup.sh
```

Finally you are able to run the script:

```
./startup.sh
```

### For MacOS

If necessary, run the following command first:

```
chmod +x ./startup.sh
```

Then:

```
./startup.sh
```


### Update schema (Windows)

If you do some schema modifications, you can update the schema by deleting the core, create the core again, populate it and set the schema, just by running:

```
./updateSchema.sh
```

### Delete container

To remove the docker container, run the script `./abort.sh` and then run the `startup.sh` script again.


**Note:** How to access the container's shell:
``` 
docker exec -it plants_solr /bin/bash
```

### For semantic search

Run the script `./semantic-startup.sh` in the terminal. Make sure no other container is running in the same port. 