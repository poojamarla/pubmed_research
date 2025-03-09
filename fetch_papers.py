import requests
import csv
import argparse
import re
from typing import List, Dict, Optional

def fetch_papers(query: str) -> List[Dict]:
    """Fetches research papers from PubMed API based on the given query."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 10,  # Limit results for now
        "retmode": "json"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    return fetch_paper_details(paper_ids)

def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetches details for given PubMed paper IDs, including author affiliations."""
    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }
    response = requests.get(details_url, params=params)
    response.raise_for_status()
    
    # Parse the XML response to extract full author details including affiliations
    import xml.etree.ElementTree as ET
    root = ET.fromstring(response.text)
    
    papers = []
    for article in root.findall(".//PubmedArticle"):
        paper_id = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text
        pub_date = article.find(".//PubDate/Year")
        pub_date = pub_date.text if pub_date is not None else "N/A"
        
        authors = []
        for author in article.findall(".//Author"):
            last_name = author.find("LastName")
            fore_name = author.find("ForeName")
            affiliation = author.find(".//Affiliation")
            
            authors.append({
                "name": f"{fore_name.text if fore_name is not None else ''} {last_name.text if last_name is not None else ''}".strip(),
                "affiliation": affiliation.text if affiliation is not None else "Unknown"
            })
        
        papers.append({
            "PubmedID": paper_id,
            "Title": title,
            "Publication Date": pub_date,
            "Authors": authors
        })
    
    return papers


def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Filters papers to include only those with at least one non-academic author."""
    filtered_papers = []
    for paper in papers:
        non_academic_authors = []
        company_affiliations = []
        for author in paper.get("Authors", []):
            affiliation = author.get("affiliation", "")
            if affiliation and not re.search(r"university|college|institute", affiliation, re.IGNORECASE):
                non_academic_authors.append(author.get("name", "Unknown"))
                company_affiliations.append(affiliation)
        if non_academic_authors:
            filtered_papers.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": ", ".join(non_academic_authors),
                "Company Affiliation(s)": ", ".join(company_affiliations),
                "Corresponding Author Email": "N/A"  # Email retrieval needs further implementation
            })
    return filtered_papers

def save_to_csv(papers: List[Dict], filename: str):
    """Saves filtered papers to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"
        ])
        writer.writeheader()
        writer.writerows(papers)

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter PubMed papers.")
    parser.add_argument("query", help="Search query for PubMed.")
    parser.add_argument("-f", "--file", help="Output CSV file name.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    args = parser.parse_args()
    
    papers = fetch_papers(args.query)
    filtered_papers = filter_non_academic_authors(papers)
    
    if args.debug:
        print("Fetched Papers:", papers)
        print("Filtered Papers:", filtered_papers)
    
    if args.file:
        save_to_csv(filtered_papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in filtered_papers:
            print(paper)

if __name__ == "__main__":
    main()
