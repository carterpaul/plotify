# Plotify-2019
Repository for the Plotify Project

## How to run (javascript version)

1. Clone project with `git clone https://github.com/MCS-Drury/plotify-quokka.git`
2. cd into project directory
3. Run python http server: <br>
pn Mac/Linux: `python -m SimpleHTTPServer` <br>
on Windows: `python -m http.server` <br>
this will start a local http server on port 8888 by default. <br>
This is necessary to allow Spotify to redirect you back to Plotify after you log in.
4. Go to `localhost:8000/plotify.html`
5. Click on "Authorize" to pull up Spotify login
6. Click "Get Album Covers" to call the Spotify API using the newly acquired access token from the log in. This way should not require the access token to ever be manually updated. <br>
After ~30 seconds, the page will be populated with a png image collage.
