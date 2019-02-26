Title: Static Sites part 1
Date: 2019-02-26
Category: How to
Tags: pelican, publishing, how-to, linux
Authors: aaron
Summary: how to set up a pelican static website


# **What is Pelican** 
[Pelican](https://blog.getpelican.com/) is a static site generator,
written in Python, that requires no database or server-side logic.

# **Setup and Install** 

# virtual environment setup 
`python -m venv venv`

`source ./venv/bin/activate`

# install pelican

`pip install pelican`

# init site

`pelican-quickstart`

this will generate the directory structure like

``` 
yourproject/
├── content
│   └── (pages)
├── output
├── tasks.py
├── Makefile
├── pelicanconf.py       # Main settings file
└── publishconf.py       # Settings to use when ready to publish
```

# **First Post**

Create a file named `hello-world.md` in your content directory
```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.
```

pelican comes with a generated `Makefile` file which makes it easier to 
get started. To run locally run `make devserver`!
