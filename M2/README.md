# Milestone #1: Data Preparation

## Group T01G15

| Name               | GitHub                                                 |
| ------------------ | ------------------------------------------------------ |
| Bárbara Rodrigues  | [@babs3](https://github.com/babs3)                     |
| Rúben Monteiro     | [@FafnirNithhoggr](https://github.com/FafnirNithhoggr) |
| Sofia Merino Costa | [@sophie-mc-dev](https://github.com/sophie-mc-dev)     |
| Tiago Ribeiro      | [@TiagoMRib](https://github.com/TiagoMRib)             |

---

### Milestone Description

...

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