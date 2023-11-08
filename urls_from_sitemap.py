import xml.etree.ElementTree as ET
import requests

def get_sitemap(sitemap_url):
    sitemap = requests.get(sitemap_url)
    if sitemap.status_code == 403:
        print("403 Forbidden access to sitemap, trying with headers")
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        return requests.get(sitemap_url, headers=headers).content
    return sitemap.content

def get_urls_from_sitemap(sitemap_url):
    root = ET.fromstring(get_sitemap(sitemap_url))
    urls = [url.text for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    return urls


if __name__ == "__main__":
    #sitemap_url = "https://lumusimaging.com.au/our-locations-sitemap1.xml"
    sitemap_url = "https://www.prpimaging.com.au/wpsl_stores-sitemap.xml" # 403 forbidden

    print(get_urls_from_sitemap(sitemap_url))
