from playwright.sync_api import sync_playwright

YC_JOBS_URL = "https://www.ycombinator.com/jobs"


def fetch_yc_jobs(limit=30):
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(YC_JOBS_URL, timeout=60000)

        page.wait_for_timeout(8000)

        # 🔑 THIS is the correct selector
        job_links = page.query_selector_all('a[href^="/companies/"]')

        print("Company job links found:", len(job_links))

        for link in job_links:
            href = link.get_attribute("href")
            text = link.inner_text().strip()

            if not href or not text:
                continue

            jobs.append({
                "job_title_raw": text,
                "job_url": "https://www.ycombinator.com" + href,
                "source": "YC Jobs"
            })

            if len(jobs) >= limit:
                break

        browser.close()

    return jobs
