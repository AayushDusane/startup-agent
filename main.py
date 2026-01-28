import pandas as pd
from src.fetch_yc import fetch_yc_jobs
from src.parser import parse_title
from src.enrich import find_company_website
from src.founder import find_founder_from_website
from src.send_email import send_email_with_attachment
from src.linkedin_finder import find_founder_linkedin




def main():
    jobs = fetch_yc_jobs(limit=30)
    rows = []

    for job in jobs:
        company, role = parse_title(job["job_title_raw"])


        website = find_company_website(company) if company else ""
        founder = find_founder_from_website(website)
        founder_linkedin = find_founder_linkedin(founder, company)

        


        rows.append({
    "company": company,
    "role": role,
    "job_url": job["job_url"],
    "source": job["source"],
    "website": website,
    "founder": founder,
    "founder_linkedin": founder_linkedin,
    "email": ""

    
})


    df = pd.DataFrame(rows)
    df.to_csv("output/startups.csv", index=False)

    print(f"Saved {len(df)} enriched rows to output/startups.csv 🚀")


if __name__ == "__main__":
    main()

send_email_with_attachment(
        sender_email="aayushdusane8030@gmail.com",
        app_password="jvftrkyryjsltvmu",
        receiver_email="aayushdusane8030@gmail.com",
        attachment_path="output/startups.csv"
    )

print("Email sent successfully 📧")

