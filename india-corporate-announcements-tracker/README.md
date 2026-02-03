# 📊 India Corporate Announcements Tracker

Automated system to track and analyze corporate announcements from BSE India, with key highlights extraction and investment implications assessment.

## 🌟 Features

- **Automated Daily Scraping**: GitHub Actions workflow runs every weekday after market hours
- **BSE Announcements**: Fetches latest corporate filings from BSE India
- **Smart Categorization**: Automatically categorizes announcements (Earnings, Dividends, M&A, etc.)
- **Key Highlights Extraction**: Extracts important metrics from announcement text
- **Investment Implications**: Color-coded assessment (Positive/Neutral/Cautious)
- **Excel Reports**: Professional formatted Excel with summary dashboard
- **PDF Links**: Direct links to original BSE filings

## 📁 Project Structure

```
india-corporate-announcements-tracker/
├── .github/
│   └── workflows/
│       └── scrape_announcements.yml    # GitHub Actions workflow
├── scripts/
│   └── scrape_announcements.py         # Main scraper script
├── output/                              # Generated Excel files
├── requirements.txt                     # Python dependencies
└── README.md                            # This file
```

## 🚀 Quick Start

### Option 1: Use GitHub Actions (Recommended)

1. **Fork this repository** to your GitHub account

2. **Enable GitHub Actions**:
   - Go to your forked repo → Settings → Actions → General
   - Select "Allow all actions and reusable workflows"
   - Click Save

3. **Run manually** (first time):
   - Go to Actions tab → "Scrape Indian Corporate Announcements"
   - Click "Run workflow" → "Run workflow"

4. **Automatic runs**: The workflow runs automatically every weekday at 6:30 PM IST

### Option 2: Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/india-corporate-announcements-tracker.git
   cd india-corporate-announcements-tracker
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the scraper**:
   ```bash
   python scripts/scrape_announcements.py
   ```

5. **Check output**: Excel file will be generated in the current directory

## 📊 Output Format

The generated Excel file contains:

### Sheet 1: Summary
- Total announcements count
- Category-wise breakdown
- Investment implications distribution
- Top companies by announcement count

### Sheet 2: Announcements
| Column | Description |
|--------|-------------|
| Company | Company name |
| Scrip Code | BSE scrip code |
| Category | Announcement type (Earnings, Dividend, etc.) |
| Subject | Announcement subject |
| Date | Announcement date |
| Time | Announcement time |
| Key Highlights | Extracted key metrics |
| Investment Implication | ★★★ Positive / ★★ Neutral / ★ Cautious |
| PDF Link | Direct link to BSE filing |

### Color Coding
- 🟢 **Green**: Strong Positive (★★★)
- 🟡 **Yellow**: Neutral/Watch (★★)
- 🔴 **Red**: Cautious (★)

## ⚙️ Configuration

### Customize Date Range

Edit the workflow file or set environment variable:
```bash
DAYS_BACK=7 python scripts/scrape_announcements.py
```

### Filter by Category

Modify `ANNOUNCEMENT_CATEGORIES` in the script to track specific types:
```python
ANNOUNCEMENT_CATEGORIES = [
    'Financial Results',
    'Dividend',
    'Acquisition',
    # Add or remove categories as needed
]
```

### Customize Investment Keywords

Edit `POSITIVE_KEYWORDS` and `NEGATIVE_KEYWORDS` in the script to adjust investment assessment.

## 🔄 GitHub Actions Schedule

The workflow is configured to run:
- **When**: Monday to Friday at 6:30 PM IST (1:00 PM UTC)
- **Why**: After Indian market hours to capture all day's announcements

To change the schedule, edit the cron expression in `.github/workflows/scrape_announcements.yml`:
```yaml
schedule:
  - cron: '0 13 * * 1-5'  # Current: 1:00 PM UTC daily
```

## 📧 Notifications

### On Failure
The workflow automatically creates a GitHub Issue if the scraper fails.

### Optional: Email Notifications
Add this step to the workflow for email alerts:
```yaml
- name: Send email notification
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: Corporate Announcements Update
    to: your-email@example.com
    from: GitHub Actions
    body: New announcements report is ready!
```

## 🔗 Integration with Google Sheets

To automatically update a Google Sheet:

1. Create a Google Cloud Service Account
2. Share your Google Sheet with the service account email
3. Add these secrets to your GitHub repo:
   - `GOOGLE_CREDENTIALS`: Service account JSON
   - `SPREADSHEET_ID`: Your Google Sheet ID

4. Add this script to upload to Google Sheets (coming soon)

## 🐛 Troubleshooting

### Common Issues

1. **No announcements found**
   - BSE website might be down
   - Check if date range is correct
   - API endpoint may have changed

2. **PDF extraction fails**
   - Some PDFs are image-based (not extractable)
   - Increase timeout for large files

3. **GitHub Actions timeout**
   - Large number of announcements
   - Reduce `DAYS_BACK` value

### Debug Mode

Run with verbose output:
```bash
python scripts/scrape_announcements.py --debug
```

## 📝 Changelog

### v1.0.0 (February 2026)
- Initial release
- BSE announcements scraping
- Excel report generation
- GitHub Actions automation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📜 License

MIT License - feel free to use and modify!

## ⚠️ Disclaimer

This tool is for informational purposes only. The investment implications are algorithmically generated and should not be considered as financial advice. Always do your own research before making investment decisions.

## 🙏 Acknowledgments

- BSE India for providing public announcements API
- GitHub Actions for free CI/CD

---

**Made with ❤️ for Indian investors**

📧 Questions? Create an issue or reach out!
