import bs4
import requests

try:
    result = requests.get('https://www.videoschool.com/photography/')
    result.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

    soup = bs4.BeautifulSoup(result.text, 'html.parser')

    # Extracting images
    images = soup.select('img')

    for img in images:
        print(img)

except requests.RequestException as e:
    print(f"Error fetching URL: {e}")
except Exception as e:
    print(f"An error occurred: {e}")



# extracting paragraphs
#my_p = soup.select('p')[6].getText()

# extracting classes
#entral_block = soup.select(".fusion-text.fusion-text-1")









