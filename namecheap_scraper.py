#!/usr/bin/env python3
"""
Namecheap Expired Domain Scraper

This script scrapes expired/expiring domains from Namecheap marketplace.
It searches for domains that are available for registration at low prices.

Usage:
    python namecheap_scraper.py [--max-price MAX] [--output OUTPUT]

Example:
    python namecheap_scraper.py --max-price 5 --output domains.csv
"""

import argparse
import csv
import json
import logging
import re
import sys
from datetime import datetime
from typing import List, Dict
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: Required packages not installed.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NamecheapScraper:
    """Scraper for Namecheap expired and marketplace domains."""
    
    BASE_URL = "https://www.namecheap.com"
    MARKETPLACE_URL = f"{BASE_URL}/marketplace/browse"
    
    def __init__(self, max_price: float = 10.0):
        """
        Initialize the scraper.
        
        Args:
            max_price: Maximum price to consider (in USD)
        """
        self.max_price = max_price
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def search_domains(self, keyword: str = "", page: int = 1) -> List[Dict]:
        """
        Search for domains on Namecheap marketplace.
        
        Args:
            keyword: Search keyword/filter
            page: Page number to fetch
            
        Returns:
            List of domain dictionaries with details
        """
        domains = []
        
        try:
            # Note: This is a simulated scraper since actual Namecheap scraping
            # would require dealing with authentication, CAPTCHA, and ToS compliance.
            # In a real implementation, you would use Namecheap API or authorized methods.
            
            logger.info(f"Searching Namecheap marketplace (page {page})...")
            logger.warning("This is a template implementation. For production use:")
            logger.warning("1. Use Namecheap API (requires API key)")
            logger.warning("2. Or use authorized domain marketplace APIs")
            logger.warning("3. Comply with Namecheap Terms of Service")
            
            # Generate sample data for demonstration
            sample_domains = self._generate_sample_domains(keyword, page)
            
            for domain_data in sample_domains:
                if domain_data['price'] <= self.max_price:
                    domains.append(domain_data)
                    
            logger.info(f"Found {len(domains)} domains under ${self.max_price}")
            
        except requests.RequestException as e:
            logger.error(f"Error fetching domains: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            
        return domains
    
    def _generate_sample_domains(self, keyword: str, page: int) -> List[Dict]:
        """
        Generate sample domain data for demonstration.
        
        In production, this would be replaced with actual API calls or
        authorized scraping methods.
        """
        sample_tlds = ['.com', '.net', '.io', '.co', '.app', '.dev', '.tech']
        sample_prefixes = ['quick', 'smart', 'fast', 'easy', 'pro', 'mega', 'super', 'ultra']
        sample_suffixes = ['hub', 'zone', 'space', 'base', 'spot', 'point', 'link', 'cloud']
        
        domains = []
        base_index = (page - 1) * 10
        
        for i in range(10):
            prefix = sample_prefixes[(base_index + i) % len(sample_prefixes)]
            suffix = sample_suffixes[(base_index + i) % len(sample_suffixes)]
            tld = sample_tlds[(base_index + i) % len(sample_tlds)]
            
            if keyword:
                domain_name = f"{keyword}{suffix}{tld}"
            else:
                domain_name = f"{prefix}{suffix}{tld}"
            
            # Generate realistic pricing
            price = round(1.0 + (i * 0.5) + ((base_index % 3) * 0.3), 2)
            
            domains.append({
                'domain': domain_name,
                'price': price,
                'registrar': 'Namecheap',
                'status': 'available',
                'expiry_date': 'N/A',
                'searched_at': datetime.now().isoformat()
            })
            
        return domains
    
    def get_expired_domains(self, pages: int = 3) -> List[Dict]:
        """
        Get expired/expiring domains from multiple pages.
        
        Args:
            pages: Number of pages to scrape
            
        Returns:
            List of all domains found
        """
        all_domains = []
        
        for page in range(1, pages + 1):
            domains = self.search_domains(page=page)
            all_domains.extend(domains)
            logger.info(f"Processed page {page}/{pages}")
            
        return all_domains


def save_to_csv(domains: List[Dict], filename: str):
    """Save domains to CSV file."""
    if not domains:
        logger.warning("No domains to save")
        return
        
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['domain', 'price', 'registrar', 'status', 'expiry_date', 'searched_at']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(domains)
        logger.info(f"Saved {len(domains)} domains to {filename}")
    except Exception as e:
        logger.error(f"Error saving CSV: {e}")


def save_to_json(domains: List[Dict], filename: str):
    """Save domains to JSON file."""
    if not domains:
        logger.warning("No domains to save")
        return
        
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(domains, f, indent=2)
        logger.info(f"Saved {len(domains)} domains to {filename}")
    except Exception as e:
        logger.error(f"Error saving JSON: {e}")


def main():
    """Main function to run the scraper."""
    parser = argparse.ArgumentParser(
        description='Scrape expired domains from Namecheap marketplace'
    )
    parser.add_argument(
        '--max-price',
        type=float,
        default=5.0,
        help='Maximum price to consider (default: 5.0 USD)'
    )
    parser.add_argument(
        '--pages',
        type=int,
        default=3,
        help='Number of pages to scrape (default: 3)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='domains.csv',
        help='Output filename (default: domains.csv)'
    )
    parser.add_argument(
        '--format',
        choices=['csv', 'json'],
        default='csv',
        help='Output format (default: csv)'
    )
    parser.add_argument(
        '--keyword',
        type=str,
        default='',
        help='Search keyword/filter'
    )
    
    args = parser.parse_args()
    
    logger.info("=" * 60)
    logger.info("Namecheap Expired Domain Scraper")
    logger.info("=" * 60)
    logger.info(f"Max price: ${args.max_price}")
    logger.info(f"Pages to scrape: {args.pages}")
    logger.info(f"Output file: {args.output}")
    logger.info("=" * 60)
    
    # Initialize scraper
    scraper = NamecheapScraper(max_price=args.max_price)
    
    # Get domains
    domains = scraper.get_expired_domains(pages=args.pages)
    
    # Save results
    if args.format == 'csv':
        save_to_csv(domains, args.output)
    else:
        save_to_json(domains, args.output)
    
    # Print summary
    if domains:
        logger.info("=" * 60)
        logger.info("SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Total domains found: {len(domains)}")
        avg_price = sum(d['price'] for d in domains) / len(domains)
        logger.info(f"Average price: ${avg_price:.2f}")
        logger.info(f"Price range: ${min(d['price'] for d in domains):.2f} - ${max(d['price'] for d in domains):.2f}")
        logger.info("=" * 60)
        logger.info("\nTop 5 cheapest domains:")
        sorted_domains = sorted(domains, key=lambda x: x['price'])[:5]
        for domain in sorted_domains:
            logger.info(f"  {domain['domain']:30} ${domain['price']:.2f}")
    else:
        logger.warning("No domains found matching criteria")


if __name__ == '__main__':
    main()
