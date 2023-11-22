# ICO-Domains
This project provides an in-depth analysis of backlinks for 19 Initial Coin Offering (ICO) domains. The aim is to understand the web presence and authority of these domains by analysing various metrics such as backlink counts, referring domains, and domain authority scores.
Dataset Overview
The analysis is based on a dataset containing information about the ICO domains, their backlinks, referring domains, and associated metadata. The data has been collected, processed, and then visualized in a comprehensive dashboard.

# Methodology
The data was processed using a Python script (ico_drops.py) that:

Converts country codes to country names using the pycountry library.
Cleans and prepares the data by stripping unnecessary whitespace from column names and ensuring the correct case is used.
Saves the cleaned data to a new CSV file for further analysis.
The project structure follows best practices, with separate directories for raw data (/data/raw), processed data (/data/processed), documentation (/documents), and scripts (/script).

# Dashboard Highlights
The dashboard made on Tableau presents:

Activity by Country: Showcasing the geographic distribution of backlinks and referring domains.
Total Backlinks and Referring Domains: Summarizing the overall backlink profile of analyzed ICO domains.
Average Authority Score: Indicating the trustworthiness and quality of the backlinks.
Activity by Target Domain (ICOs): Detailing the backlink and domain authority score evolution over time.
Top 10 Most Used Referring Domains: Identifying the domains that contribute the most backlinks to the ICO domains.
Stakes

The dashboard serves as a tool for stakeholders to:
Gauge the online influence and reach of ICO domains.
Identify key referral sources and potential areas for partnership or marketing.
Assess the quality of the backlink profile which is critical for search engine ranking and web reputation.
Conclusion
This dashboard offers valuable insights for marketers, SEO specialists, and domain owners to strategize their online presence and understand the competitive landscape of ICOs.

# Usage
To replicate the analysis, follow the setup instructions detailed in the script folder and run the ico_drops.py Python script. Ensure you have the required dependencies installed as listed in the requirements.txt file.
