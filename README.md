# Atlas Document Search

## Background

This is a trivial code sample that will make documents searchable within MongoDB Atlas. 

_This is provided as-is strictly as sample or reference code and not to be used for production._

## Technology
* Python and Python Jupyter Notebooks for loading and demonstration
* [Apache Tika](https://tika.apache.org/) for document text and metadata extraction
* [MongoDB Atlas](https://www.mongodb.com/cloud) as a database 
* [MongoDB GridFS](https://docs.mongodb.com/manual/core/gridfs/) to store the files themselves in the database
* [MongoDB Atlas Search](https://www.mongodb.com/atlas/search) to provide full-text search analysis on the extracted data

## Prereqs
* Deploy a MongoDB Atlas cluster
* Create a database username/password
* Add your external IP address to the Network ACL for Atlas
* Have python and Jupyter installed
* Python packages required can be seen in the `Loader/requirements.txt`
* Have Java installed and in PATH via `sudo apt install openjdk-11-jdk` for example 

## Text Extraction Execution
* Paste your MongoDB connection string into `Loader/__init__.py` and `SearchExample.ipynb`
* Put some sample PDFs or other files into a folder and set that path to that folder in `Loader/__init__.py`
* Run the `__init__.py` to load the data from the documents folder into MongoDB

## Text Extraction Results
* In Atlas, you should see a `tika` database with several collections:
  * `tika.tika.files` and `tika.tika.chunks` the collections created to store the files themselves via GridFS
  * `tika.extracted` - the metadata extracted by Tika from the documents with one document per file and a `gsky` object within each document containing additional metadata like the name of the file and a pointer to the `_id` of the file in GridFS

## Search Execution
* Create a default Atlas Search index on `tika.extracted` using either the visual builder (all defaults) or via JSON and paste the JSON from `Indexes/default.json`
* You can then use the Atlas Search Tester to search for text that was within the documents
* You can also use the `SearchExample.ipynb` to see how to implement the search in code