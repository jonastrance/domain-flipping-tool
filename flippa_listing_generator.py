#!/usr/bin/env python3
"""
Flippa Listing Generator

Generates formatted domain listings for Flippa marketplace.
Creates professional descriptions and pricing information.

Usage:
    python flippa_listing_generator.py --domain example.com --price 50
    python flippa_listing_generator.py --from-csv domains.csv
"""

import argparse
import csv
import sys
from datetime import datetime
from typing import Dict, List


def generate_listing(domain: str, price: float, description: str = "") -> str:
    """
    Generate a formatted Flippa listing for a domain.
    
    Args:
        domain: Domain name
        price: Asking price
        description: Optional custom description
        
    Returns:
        Formatted listing text
    """
    # Extract domain components
    parts = domain.rsplit('.', 1)
    if len(parts) == 2:
        name, tld = parts
    else:
        name, tld = domain, "com"
    
    # Generate features based on domain characteristics
    features = []
    
    if len(name) <= 8:
        features.append("✓ Short and memorable domain name")
    
    if '-' not in name:
        features.append("✓ No hyphens - easy to remember and type")
    
    if any(keyword in name.lower() for keyword in ['quick', 'fast', 'smart', 'easy', 'pro', 'tech', 'digital', 'cloud', 'app']):
        features.append("✓ Contains premium keywords")
    
    if tld in ['com', 'io', 'net', 'co']:
        features.append(f"✓ Popular .{tld} extension")
    
    features.append("✓ Instant transfer available")
    features.append("✓ Clear ownership, ready to use")
    
    # Create the listing
    listing = f"""
{'=' * 70}
DOMAIN LISTING: {domain.upper()}
{'=' * 70}

💰 ASKING PRICE: ${price:.2f}

📝 DESCRIPTION:
{description if description else f'''
Premium domain name available for immediate purchase!

{domain} is a brandable domain name perfect for:
• Technology startups
• Digital services
• SaaS applications
• Online marketplaces
• Mobile apps
• Business ventures

This domain has strong commercial potential and can help establish
a professional online presence for your business.
'''}

✨ KEY FEATURES:
{chr(10).join(features)}

📊 DOMAIN DETAILS:
• Domain Name: {domain}
• Extension: .{tld}
• Age: Recently registered / Available
• Registrar: Transferrable from major registrars
• Transfer: Fast and secure transfer process

💡 IDEAL FOR:
• Startups looking for a memorable brand name
• Entrepreneurs building their online presence
• Companies seeking a domain upgrade
• Developers launching new projects
• Marketing agencies needing client domains

🔒 TRANSFER PROCESS:
1. Purchase completed securely through Flippa
2. Domain unlocked and auth code provided
3. Transfer initiated to your registrar
4. Ownership transferred within 5-7 days

💵 PRICING:
• Listed Price: ${price:.2f}
• Open to reasonable offers
• Fast sale preferred

📞 CONTACT:
• Ready to answer questions
• Flexible on transfer timeline
• Professional and responsive seller

⚡ ACT FAST - Premium domains like this don't last long!

{'=' * 70}
"""
    
    return listing


def generate_bulk_listings(domains: List[Dict], output_file: str = "flippa_listings.txt"):
    """
    Generate multiple listings from a list of domains.
    
    Args:
        domains: List of domain dictionaries
        output_file: Output filename
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"FLIPPA DOMAIN LISTINGS\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Domains: {len(domains)}\n")
        f.write("=" * 70 + "\n\n")
        
        for domain_data in domains:
            domain = domain_data.get('domain', '')
            # Calculate suggested markup (10-50x)
            purchase_price = float(domain_data.get('price', 2.0))
            suggested_price = round(purchase_price * 20, 2)  # 20x markup
            
            listing = generate_listing(
                domain=domain,
                price=suggested_price,
                description=domain_data.get('description', '')
            )
            f.write(listing)
            f.write("\n" * 3)
    
    print(f"✓ Generated {len(domains)} listings in {output_file}")


def load_domains_from_csv(filename: str) -> List[Dict]:
    """Load domains from CSV file."""
    domains = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                domains.append(row)
        print(f"✓ Loaded {len(domains)} domains from {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)
    
    return domains


def create_template_csv(filename: str = "domains_template.csv"):
    """Create a template CSV file for bulk listing generation."""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['domain', 'price', 'description'])
        writer.writerow(['example-domain.com', '2.99', 'Great for tech startups'])
        writer.writerow(['quick-app.io', '8.99', 'Perfect for mobile applications'])
        writer.writerow(['smart-hub.net', '1.99', ''])
    
    print(f"✓ Created template CSV: {filename}")
    print(f"  Fill in your domains and run:")
    print(f"  python flippa_listing_generator.py --from-csv {filename}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Generate Flippa domain listings',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate single listing
  python flippa_listing_generator.py --domain example.com --price 50

  # Generate listings from CSV
  python flippa_listing_generator.py --from-csv domains.csv

  # Create template CSV
  python flippa_listing_generator.py --create-template
        """
    )
    
    parser.add_argument(
        '--domain',
        type=str,
        help='Domain name for single listing'
    )
    parser.add_argument(
        '--price',
        type=float,
        help='Asking price for single listing'
    )
    parser.add_argument(
        '--description',
        type=str,
        default='',
        help='Custom description for single listing'
    )
    parser.add_argument(
        '--from-csv',
        type=str,
        metavar='FILE',
        help='Generate listings from CSV file'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='flippa_listings.txt',
        help='Output filename (default: flippa_listings.txt)'
    )
    parser.add_argument(
        '--create-template',
        action='store_true',
        help='Create a template CSV file'
    )
    
    args = parser.parse_args()
    
    if args.create_template:
        create_template_csv()
    elif args.from_csv:
        domains = load_domains_from_csv(args.from_csv)
        generate_bulk_listings(domains, args.output)
    elif args.domain and args.price:
        listing = generate_listing(args.domain, args.price, args.description)
        print(listing)
        
        # Also save to file
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(listing)
        print(f"\n✓ Listing saved to {args.output}")
    else:
        parser.print_help()
        print("\nError: Please provide either --domain and --price, --from-csv, or --create-template")
        sys.exit(1)


if __name__ == '__main__':
    main()
