import imgkit

url = "http://127.0.0.1:8000/"  # Replace with the actual URL or file path

options = {
    'quiet': '',
    'width': '600',  # Set the desired width of the image
    'height': '250',  # Set the desired height of the image
    'format': 'png'  # Specify the output format of the image
}

# Use the CSS selector to capture only the desired div element
css_selector = '.main'

imgkit.from_file(url, 'output.png', options=options, css=css_selector)
