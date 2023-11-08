from urls_from_sitemap import get_urls_from_sitemap

if __name__ == "__main__":
    #sitemap_url = "https://lumusimaging.com.au/our-locations-sitemap1.xml"
    sitemap_url = "https://www.prpimaging.com.au/wpsl_stores-sitemap.xml" # 403 forbidden

    print(get_urls_from_sitemap(sitemap_url))
