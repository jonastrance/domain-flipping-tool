# Domain Flipping Tool 🚀

Buy cheap domain names and resell at markup. Buy for $1-3, sell for $20-100+ per domain on Flippa/Brandpa.

## Overview

This toolkit helps you discover, manage, and sell domain names for profit. It includes:

1. **Namecheap Domain Scraper** - Find affordable expired/marketplace domains
2. **Pricing Spreadsheet Template** - Track purchases, sales, and calculate ROI
3. **Flippa Listing Generator** - Create professional domain listings

## Installation

```bash
# Clone the repository
git clone https://github.com/jonastrance/domain-flipping-tool.git
cd domain-flipping-tool

# Install dependencies
pip install -r requirements.txt
```

## Tools

### 1. Namecheap Domain Scraper

Search for domains on Namecheap marketplace within your budget.

**Usage:**
```bash
# Basic usage - find domains under $5
python namecheap_scraper.py --max-price 5 --output domains.csv

# Search multiple pages
python namecheap_scraper.py --max-price 10 --pages 5 --output cheap_domains.csv

# Export to JSON
python namecheap_scraper.py --max-price 3 --format json --output domains.json

# Search with keyword
python namecheap_scraper.py --keyword tech --max-price 5
```

**Options:**
- `--max-price` - Maximum price to consider (default: $5)
- `--pages` - Number of pages to scrape (default: 3)
- `--output` - Output filename (default: domains.csv)
- `--format` - Output format: csv or json (default: csv)
- `--keyword` - Search keyword/filter

**Note:** The scraper includes sample data for demonstration. For production use, integrate with Namecheap API or use authorized marketplace APIs while complying with Terms of Service.

### 2. Pricing Spreadsheet Template

Generate an Excel spreadsheet to track your domain portfolio.

**Usage:**
```bash
# Create template with default name
python create_pricing_template.py

# Custom filename
python create_pricing_template.py --output my_domains.xlsx
```

**Features:**
- **Domain Inventory Sheet**: Track purchased domains, costs, and target prices
- **Sold Domains Sheet**: Record sales with automatic profit/ROI calculation
- **Summary Sheet**: Portfolio overview with key metrics
- **Formulas included**: Automatic calculations for profit, ROI, and days held

**Template Structure:**

*Domain Inventory:*
- Domain name, purchase details, target prices
- Listing status and marketplace info
- Custom notes for each domain

*Sold Domains:*
- Automatic profit calculation: `Sale Price - Purchase Price - Fees`
- ROI calculation: `((Profit) / Purchase Price) × 100`
- Days held tracking

*Summary Dashboard:*
- Total investment and portfolio value
- Sales performance metrics
- Average ROI and time to sale

### 3. Flippa Listing Generator

Create professional domain listings for marketplaces like Flippa.

**Usage:**
```bash
# Generate single listing
python flippa_listing_generator.py --domain example.com --price 50

# Generate from scraped domains CSV
python flippa_listing_generator.py --from-csv domains.csv --output listings.txt

# Create template for manual entry
python flippa_listing_generator.py --create-template

# Custom description
python flippa_listing_generator.py --domain my-domain.io --price 100 \
  --description "Perfect for SaaS startups"
```

**Features:**
- Professional listing format with emojis
- Auto-generated features based on domain characteristics
- Use case suggestions
- Transfer process explanation
- Bulk generation from CSV files

## Workflow Example

Here's a complete domain flipping workflow:

```bash
# Step 1: Find cheap domains
python namecheap_scraper.py --max-price 3 --pages 5 --output found_domains.csv

# Step 2: Create portfolio tracker
python create_pricing_template.py --output my_portfolio.xlsx

# Step 3: Add purchased domains to the Excel file (manual step)

# Step 4: Generate Flippa listings
python flippa_listing_generator.py --from-csv found_domains.csv --output flippa_listings.txt

# Step 5: Post listings on Flippa/Brandpa

# Step 6: Track sales in the Excel "Sold Domains" sheet
```

## Profitability Tips

1. **Buy Low**: Target domains under $3 for maximum ROI
2. **Quality Matters**: Short, memorable, keyword-rich domains sell better
3. **Popular TLDs**: .com, .io, .net, .co have higher demand
4. **Markup Strategy**: Aim for 10-50x markup ($2 → $20-$100)
5. **List on Multiple Platforms**: Flippa, Brandpa, Sedo, Afternic
6. **Be Patient**: Good domains may take weeks/months to sell
7. **Portfolio Approach**: Buy 10-20 domains, expect 30-50% to sell

## Target Buyers

- Startups seeking brand names
- Small businesses going online
- App developers
- Marketing agencies
- Entrepreneurs

## Legal & Ethical Considerations

⚠️ **Important:**
- Respect trademark laws - don't squat on brand names
- Follow marketplace Terms of Service
- Be honest in listings - no false claims
- Don't engage in cybersquatting
- Use official APIs where available
- Comply with domain registration policies

## File Structure

```
domain-flipping-tool/
├── namecheap_scraper.py          # Domain scraper script
├── create_pricing_template.py     # Spreadsheet generator
├── flippa_listing_generator.py    # Listing generator
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## Requirements

- Python 3.7+
- requests
- beautifulsoup4
- pandas
- openpyxl

## Contributing

Contributions welcome! Feel free to:
- Add new marketplace scrapers
- Improve listing templates
- Add analytics features
- Enhance the spreadsheet template

## Disclaimer

This tool is for educational and business purposes. Users are responsible for:
- Complying with all applicable laws and regulations
- Following marketplace terms of service
- Respecting intellectual property rights
- Conducting legitimate business practices

## License

MIT License - See repository for details

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Happy Domain Flipping! 💰**
