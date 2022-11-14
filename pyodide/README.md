# pyodide sonic-utilities

## how to run

1. python3 server.py [port]

2. open url `localhost:[port]/test.html` on browser

3. check log in console

## contribution

1. revise `swsscommon/` for example 

2. rebuild whl file: `cd swsscommon; python3 setup.py bdist_wheel; mv dist/* ..`

3. re-open the url on browser