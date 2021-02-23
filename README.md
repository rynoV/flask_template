# CPSC 329 Group 10: Vulnerability Explorer

## Setup

1. First make sure you have a recent version of Python, like 3.8.
2. Create a virtual environment in the project folder:
    ```script
    python -m venv .venv
    ```
3. Activate the virtual environment. This is different across systems, but the
   idea is to find an run the `activate` script within the `.venv` folder.

   On Windows the command is usually something like `.\.venv\Scripts\activate`.

   On Unix/Mac it's probably `./.venv/bin/activate`.
   
   You should see your prompt change to indicate that you have activated the
   environment successfully.
4. Run `pip install -r requirements.txt` to install project dependencies.
5. Run `flask run` to start up the development server. You should be able to go
   to http://127.0.0.1:5000/ in your browser to see the website. You can make
   changes to the source code and reload the webpage to see your changes.

## Notes

- XSS prevention is built-in to the templating system, see
  [here](https://jinja.palletsprojects.com/en/2.11.x/templates/#working-with-automatic-escaping)
  for disabling the automatic escaping.
- See
  [here](https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/#sqlite3)
  for an example of using SQLite with Flask.
- It may be necessary to hard-refresh the page to see changes in static content.