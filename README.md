# How to run a Flask project locally

This guide will show you how to run a Flask project on your computer using Python, Git, and virtualenv.

## Prerequisites

- You need to have [Python](https://www.markdownguide.org/) and [Git](https://www.geeksforgeeks.org/introduction-to-markdown/) installed on your computer. You can check their versions by running `python --version` and `git --version` in your terminal or command prompt. If you don't have them, you can download them from their official websites.
- You need to have `pip` and `virtualenv` installed. `pip` is a package manager for Python that lets you install modules from the Python Package Index (PyPI). `virtualenv` is a module that lets you create isolated Python environments for your projects. You can install them with `pip install pip virtualenv`.

## Steps

1. Create a virtual environment for your project. This will isolate your project's dependencies from other Python packages on your system. To create a virtual environment, go to the directory where you want to clone the project and run `virtualenv venv` to create a folder named `venv` that will store your virtual environment. To activate the virtual environment, run `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Linux or macOS.
2. Clone the Flask project from GitHub using the `git clone` command. You need to copy the repository URL from the GitHub page of the project you want to clone. For example, if you want to clone the [Flask examples project](https://www.markdownguide.org/getting-started/), you can run `git clone https://github.com/helloflask/flask-examples.git`. This will create a folder named `flask-examples` that contains the project files.
3. Install Flask and other dependencies for the project using the `pip install` command with the `requirements.txt` file that lists the required packages. Go to the project folder and run `pip install -r requirements.txt`. This will install Flask and other modules that the project needs.
4. Run the Flask project locally using the `flask run` command. You need to set the `FLASK_APP` environment variable to the name of the Python file that contains the Flask app instance or the app factory function. For example, if the file is named `app.py`, you can run `set FLASK_APP=app.py` on Windows or `export FLASK_APP=app.py` on Linux or macOS. Then, run `flask run` to start the development server. You should see a message like `* Running on http://127.0.0.1:5000/` that tells you the URL of your local server. You can visit this URL in your browser to see the Flask project running.
