# PyGame game template
 My personal template for starting up pygame projects.

## Description
This project represents my usual workflow when creating pygame projects. It contains the very basics you need to start up your own idea with an organized approach.

## How to use
First and foremost I strongly suggest to create a virtual environment in your prefered way. The easiest way might be:
`python -m venv /path/to/new/virtual/environment` (If you have already navigated to the project directory use: `python -m venv .`)

Then you have to activate the environment. Execute:
`.\Scripts\activate` (Assuming that you are currenly in the project directory. Otherwise replace '.' with the path to it.)

Finally you should install all required modules. If you are starting fresh you can simply run `pip install -r .\requirements.txt`. That should install just pygame. (Keep in mind that its a good practice to keep the requirements file up to date with all the modules you are currently using!)

And you are done! You can start the project from the main.py file.

#### Attempted to include most of the commonly used features, but if you have your own view on how to improve this 'template' feel free to drop your suggestion or open a PR. :)
