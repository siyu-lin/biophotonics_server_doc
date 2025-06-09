# Biophotonics Server Wiki
This is the backbone of the biophotonics server wiki at: [biophotonics-server-doc.readthedocs.io](biophotonics-server-doc.readthedocs.io)


## For Admins 
### Preview the website locally
1. Clone a copy of this repository locally with ``` git clone ```.

2. Make sure you are in the directory with ``` cd ```.

3. Run ``` sphinx-autobuild source build/html ``` and you should be be prompted to preview the website at ``` 127.0.0.1:8000 ```.

4. The first time you might need to install required packages ``` pip install -r /source/requirements.txt ```.


### Adding a new page
1. Add a ``` .md ``` file ``` /source/modules/NEWFILE.md ```.
2. Add the page to the ``` source/index.rst ``` as ``` modules/NEWFILE ``` in the desired section.
3. Save and preview the website.


### Deploying the website
1. Preview and confirm no errors locally.
2. Push to the GitHub repository.
3. Website will be compiled and deployed automatically at [https://app.readthedocs.org/projects/biophotonics-server-doc/](app.readthedocs.org/projects/biophotonics-server-doc/).
4. Confirm no errors on deployment.
