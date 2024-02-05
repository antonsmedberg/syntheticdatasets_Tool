# import http.server
# import socketserver
import os

PORT = 8000  # You can choose any available port

# Replace this with the absolute path to your project's root directory
BASE_DIRECTORY = 'C:/Users/Anton/PycharmProjects/syntheticdatasets_Tool'

# Change the working directory to the root of your project
os.chdir(BASE_DIRECTORY)

# Define the directory to serve static files (CSS, JavaScript, and favicon)
STATIC_DIRECTORY = os.path.join(BASE_DIRECTORY, 'static')

# Define the directory to serve HTML files
HTML_DIRECTORY = os.path.join(BASE_DIRECTORY, 'public')

# Create a custom handler class that serves both static and HTML files
# class CustomHandler(http.server.SimpleHTTPRequestHandler):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, directory=STATIC_DIRECTORY, **kwargs)

# Use the custom handler as the second argument
# with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
#     print(f"Serving at port {PORT}")
#     httpd.serve_forever()


