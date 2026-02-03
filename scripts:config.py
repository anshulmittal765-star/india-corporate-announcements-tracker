"""
Configuration file for India Corporate Announcements Tracker
Customize settings here without modifying the main script
"""

import os
from datetime import datetime

# =============================================================================
# DATE RANGE SETTINGS
# =============================================================================

# Number of days to look back for announcements
DAYS_BACK = int(os.environ.get('DAYS_BACK', 4))

# =============================================================================
# API ENDPOINTS
# =============================================================================

BSE_ANNOUNCEMENTS_URL = "https://api.bseindia.com/BseIndiaAPI/api/AnnGetData/w"
BSE_PDF_BASE_URL = "https://www.bseindia.com/xml-data/corpfiling/AttachLive"
NSE_ANNOUNCEMENTS_URL = "https://www.nseindia.com/api/corporate-announcements"

# =============================================================================
# REQUEST SETTINGS
# =============================================================================

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.bseindia.com/',
    'Origin': 'https://www.bseindia.com'
}

# Request timeout in seconds
REQUEST_TIMEOUT = 30

# Delay between requests (seconds) to avoid rate limiting
REQUEST_DELAY = 1

# =============================================================================
# ANNOUNCEMENT CATEGORIES
# =============================================================================

# Categories to track (modify as needed)
ANNOUNCEMENT_CATEGORIES = [
    'Board Meeting',
    'Financial Results',
    'Dividend',
    'AGM/EGM',
    'Acquisition',
    'Investment',
    'Fund Raising',
    'Merger/Demerger',
    'Change in Directors',
    'Corporate Action',
    'Investor Presentation',
    'Concall Transcript',
    'Order Win',
    'New Contract',
    'Expansion',
    'Capex',
    'Rating',
    'Others'
]

# Priority categories (highlighted in report)
PRIORITY_CATEGORIES = [
    'Financial Results',
    'Dividend',
    'Acquisition',
    'Investment',
    'Fund Raising',
    'Order Win'
]

# =============================================================================
# INVESTMENT ASSESSMENT KEYWORDS
# =============================================================================

# Keywords indicating positive developments
POSITIVE_KEYWORDS = [
    'profit increase', 'profit up', 'revenue growth', 'dividend', 'bonus',
    'acquisition', 'expansion', 'new order', 'contract win', 'upgrade',
    'record', 'highest ever', 'beat estimates', 'outperform', 'growth',
    'investment', 'capex', 'expansion plan', 'new plant', 'capacity addition',
    'margin improvement', 'cost reduction', 'efficiency', 'positive outlook',
    'strong demand', 'market share gain', 'debt reduction', 'rating upgrade',
    'new product launch', 'partnership', 'strategic alliance', 'buyback'
]

# Keywords indicating negative developments
NEGATIVE_KEYWORDS = [
    'profit decline', 'profit down', 'revenue decline', 'loss', 'downgrade',
    'resign', 'exit', 'closure', 'default', 'penalty', 'fraud',
    'miss estimates', 'underperform', 'weak', 'challenging', 'headwinds',
    'margin pressure', 'cost increase', 'debt increase', 'impairment',
    'write-off', 'provision', 'negative outlook', 'demand weakness',
    'market share loss', 'rating downgrade', 'legal issues', 'regulatory action'
]

# =============================================================================
# OUTPUT SETTINGS
# =============================================================================

# Output directory
OUTPUT_DIR = os.environ.get('OUTPUT_DIR', './output')

# Output filename format (supports datetime formatting)
OUTPUT_FILENAME_FORMAT = "India_Corporate_Announcements_{date}.xlsx"

# Maximum announcements to process (0 = no limit)
MAX_ANNOUNCEMENTS = 0

# =============================================================================
# PDF EXTRACTION SETTINGS
# =============================================================================

# Whether to extract text from PDFs (slower but more detailed)
EXTRACT_PDF_TEXT = False

# Maximum pages to extract from each PDF
MAX_PDF_PAGES = 3

# =============================================================================
# COMPANY FILTERS (Optional)
# =============================================================================

# List of scrip codes to track (empty = track all)
# Example: ['500325', '532540', '500180']
TRACK_SCRIP_CODES = []

# List of company names to track (partial match, empty = track all)
# Example: ['RELIANCE', 'TCS', 'HDFC']
TRACK_COMPANIES = []

# Companies to exclude (partial match)
EXCLUDE_COMPANIES = []

# =============================================================================
# NIFTY 50 COMPANIES (for filtering)
# =============================================================================

NIFTY_50_COMPANIES = [
    'RELIANCE', 'TCS', 'HDFCBANK', 'ICICIBANK', 'INFY', 'HINDUNILVR',
    'ITC', 'SBIN', 'BHARTIARTL', 'KOTAKBANK', 'LT', 'AXISBANK',
    'HCLTECH', 'ASIANPAINT', 'MARUTI', 'SUNPHARMA', 'TITAN',
    'BAJFINANCE', 'WIPRO', 'ULTRACEMCO', 'NESTLEIND', 'ONGC',
    'NTPC', 'POWERGRID', 'M&M', 'JSWSTEEL', 'TATAMOTORS', 'TATASTEEL',
    'ADANIENT', 'ADANIPORTS', 'BAJAJFINSV', 'TECHM', 'HDFCLIFE',
    'SBILIFE', 'GRASIM', 'DIVISLAB', 'DRREDDY', 'CIPLA', 'BRITANNIA',
    'EICHERMOT', 'INDUSINDBK', 'COALINDIA', 'BPCL', 'TATACONSUM',
    'APOLLOHOSP', 'HEROMOTOCO', 'UPL', 'SHREECEM', 'HINDALCO'
]

# =============================================================================
# LOGGING
# =============================================================================

# Log level: DEBUG, INFO, WARNING, ERROR
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

# Log file path (None = console only)
LOG_FILE = None

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_output_filename():
    """Generate output filename with current date"""
    return OUTPUT_FILENAME_FORMAT.format(
        date=datetime.now().strftime('%Y%m%d')
    )

def should_track_company(company_name, scrip_code=''):
    """Check if company should be tracked based on filters"""
    # Check exclusion list
    if any(exc.lower() in company_name.lower() for exc in EXCLUDE_COMPANIES):
        return False
    
    # If no filters, track all
    if not TRACK_SCRIP_CODES and not TRACK_COMPANIES:
        return True
    
    # Check scrip code filter
    if TRACK_SCRIP_CODES and scrip_code in TRACK_SCRIP_CODES:
        return True
    
    # Check company name filter
    if TRACK_COMPANIES:
        return any(comp.lower() in company_name.lower() for comp in TRACK_COMPANIES)
    
    return False
