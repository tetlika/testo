## Pre Requirements

Install next basic software:

* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant](http://www.vagrantup.com/)
* [Ansible](http://www.ansibleworks.com)

also install http://python-wordpress-xmlrpc.readthedocs.org/en/latest/overview.html using:

sudo pip install python-wordpress-xmlrpc

## Install

1. git clone git@github.com:tetlika/testo.git somefolder
2. cd somefolder
3. vagrant up

This will set the basic WP blog which will be accessible through: http://localhost:8080

## Use

To make posts, just fill file title.txt with post title and post.txt with post content and then run :

python post.py

Navigate to http://localhost:8080 and the post will be there.


# testo
