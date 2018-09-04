import requests
from scrapy.selector import Selector


def make_request():
    """Makes request with given parameters for search and returns content"""
    key = "" #Enter any keywords for your cron/scheduled task
    loc = "" #Enter city and state abbreviation (city, ..) for the cron/scheduled task
    loc_dist = "" #Enter any distance parameters (in miles)
    if not loc_dist:
        loc_dist = "10"
    level = "" #Leave default
    if not level:
        level = "-1"
    brand = "" #Leave default
    if not brand:
        brand = "-1"

    search_url = "http://www.bestbuy-jobs.com/job-family/geek-squad/?"

    params = {'keywords': key,
              'location': loc,
              'locdist': loc_dist,
              'level': level,
              'brand': brand}

    req = requests.get(search_url, params=params)

    return req.content

def parse_content():
    content = make_request()
    not_avail = Selector(text=content).xpath("//div[@class='warning no-results']")
    if not_avail:
        print("Sorry, no jobs in this area")
    else:
        for posting in Selector(text=content).xpath("//tr[@class='odd'] |//tr[@class='even']"):
            title = posting.css("a::text").extract()
            job_url = posting.css("a::attr(href)").extract()
            job_cat = posting.css("td::text").extract()[1]
            job_level = posting.css("td::text").extract()[2]
            job_location = posting.css("td::text").extract()[3]
            print("Job title: {}\n"
                  "Job Category: {}\n"
                  "Job Level: {}\n"
                  "Job Location: {}\n"
                  "URL to job: {}\n".format(title, job_cat, job_level, job_location, job_url))


