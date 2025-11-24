# Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Find Cheap Domains

```bash
# Find domains under $3
python namecheap_scraper.py --max-price 3 --pages 5 --output cheap_domains.csv
```

This creates a CSV file with potential domain purchases.

### 3. Create Your Portfolio Tracker

```bash
python create_pricing_template.py --output my_portfolio.xlsx
```

Open `my_portfolio.xlsx` in Excel/LibreOffice and:
- Add purchased domains to "Domain Inventory" sheet
- Enter purchase price and target sale price
- Track listings on Flippa/Brandpa

### 4. Generate Flippa Listings

```bash
# From your scraped domains
python flippa_listing_generator.py --from-csv cheap_domains.csv --output my_listings.txt

# Or single domain
python flippa_listing_generator.py --domain my-domain.com --price 50
```

### 5. Post and Sell

1. Copy listings from `my_listings.txt`
2. Post on [Flippa](https://flippa.com), [Brandpa](https://brandpa.com), or [Sedo](https://sedo.com)
3. When sold, record in Excel "Sold Domains" sheet
4. Profit! 💰

## 💡 Pro Tips

- **Aim for 10-50x markup**: Buy at $1-3, sell at $20-100
- **Focus on quality**: Short, memorable domains sell faster
- **Be patient**: Good sales can take 2-8 weeks
- **Diversify**: Buy 10-20 domains to improve odds

## 📊 Expected Returns

Based on typical domain flipping:

| Purchase Price | Target Sale | Realistic Profit | ROI |
|---------------|-------------|------------------|-----|
| $1.99         | $20-40      | $15-35          | 750-1700% |
| $2.99         | $30-60      | $25-55          | 835-1840% |
| $8.99         | $80-150     | $70-140         | 778-1557% |

**Success Rate**: 20-40% of domains typically sell within 6 months.

## ⚠️ Legal Notes

- Don't register trademarked names
- Follow marketplace terms
- Be honest in listings
- Respect intellectual property

## 📚 Next Steps

1. Read full [README.md](README.md) for detailed documentation
2. Start small with 5-10 domains
3. Track your results in the Excel template
4. Scale up as you learn what sells

**Happy flipping!** 🎉
