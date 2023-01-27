# What this project does

Scraping images from a website and saves them into the local file system.

# Technology

- Docker
  - for development
  - built Docker image and container for the source code and the dev environment
  - bind mounts used for getting the saved images from the container to the local machine
- Python
  - web scraping libraries used

# Limitations

- The source code is specifically for scraping the URL of the "background-image" attribute under the HTML attribute "style" only. Not intended to be used universally

# Issues

- the HTML data got from the URL does not contain all the HTML li elements from the website. Only a portion of the photos is downloaded as a result.

  - current workaround: copy and paste HTML source code from the website to my local source.html
