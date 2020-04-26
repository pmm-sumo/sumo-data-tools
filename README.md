# sumo-data-tools
The repo contains a simple script which might be used for converting CSV into series of newline-separated
JSON records when uploading data to [Sumo Logic](https://sumologic.com)

## Parameters

There are several environment properties that control the execution of the script:

* `URL` - the actual URL where the POST is being sent (when empty, no data is being actually sent). The address 
of the HTTP type source can be found in Manage Data/Collection.
* `VERBOSE` - when set to True (or 1), the sent contents is being printed out on the console too
* `MAX_RECORDS_IN_POST` - number of records to include in a single request

## Running

Make sure dependencies are installed (`pip install -r requirements.txt`) 

### Making a dry run

`VERBOSE=1 ./upload-csv.py file.csv`

For example:

```
$ cat test.csv
first,last,age
Tom,Sawyer,12
Huckleberry,Finn,13

$ VERBOSE=1 ./upload-csv.py test.csv
{"first": "Tom", "last": "Sawyer", "age": "12"}
{"first": "Huckleberry", "last": "Finn", "age": "13"}
```

### Uploading results

Substitute the `MY_URL` with actual collector endpoint address and run it as:

`URL="https://MY_URL" ./upload-csv.py file.csv`



