# Biophotonics Server Wiki
This is the backbone of the biophotonics server wiki at: [biophotonics-server-doc.readthedocs.io](biophotonics-server-doc.readthedocs.io)


## For Admins 
### Preview the website locally
1. Clone a copy of this repository locally with ``` git clone ```.

2. Make sure you are in the directory with ``` cd ```.

3. Run ``` sphinx-autobuild source build/html ``` and you should be be prompted to preview the website at ``` 127.0.0.1:8000 ```.

4. The first time you might need to install required packages ``` pip install -r /build/requirements.txt ```.


### Adding a new page
1. Add a ``` .md ``` file ``` /source/modules/NEWFILE.md ```.
2. Add the page to the ``` source/index.rst ``` as ``` modules/NEWFILE ``` in the desired section.
3. Save and preview the website.
