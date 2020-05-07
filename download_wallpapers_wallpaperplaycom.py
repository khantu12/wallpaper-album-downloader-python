# wallpaperplay.com
from urllib.request import urlopen
from bs4 import BeautifulSoup
from os import mkdir

url = input(
    "Put in the URL from wallpaperplay.com with the collection of wallpapers that you want to download: \r\n"
)

# Get folder name from the URL and make the directory
folder_name = url.split("/")[-1:][0]
try:
    mkdir(f"D:\\Pictures\\Wallpapers\\{folder_name}")
except:
    pass

# Open the page and make a soup out of it
wallpaper_page = urlopen(url)
soup = BeautifulSoup(wallpaper_page, "html.parser")

# Get all divs
s = soup.find_all("div")

# Get number of images
total = 0
for link in s:
    if "data-download" in link.attrs:
        total += 1

# Go through every div
current = 0
for link in s:
    # If the div does not have attribute 'data-download', skip it
    if "data-download" not in link.attrs:
        continue
    # Increase the number of records downloaded
    current += 1

    picture_url = link.attrs["data-download"]  # Get the URL for the picture itself
    picture = urlopen(picture_url)  # Open the picture URL
    datatowrite = picture.read()  # Read the image from the URL

    # Get the filename for the picture from the last part of the URL
    filename = str(picture_url.split("/")[-1:][0])

    # Write to a specified file in a directory
    with open(f"D:\\Pictures\\Wallpapers\\{folder_name}\\{filename}.jpg", "wb",) as f:
        f.write(datatowrite)
    print(f"Downloaded: {filename}.jpg ({str(current)}/{str(total)})")

