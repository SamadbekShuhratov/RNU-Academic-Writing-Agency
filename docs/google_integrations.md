# Google Sheets and Gmail Integration Instructions

## 1) Enable APIs
In Google Cloud, enable:
- Google Sheets API
- Gmail API

## 2) Service Account Setup
1. Create a service account.
2. Download JSON credentials.
3. Save file path and export:
   ```bash
   export GOOGLE_SERVICE_ACCOUNT_FILE="/absolute/path/to/service-account.json"
   ```

## 3) Google Sheets Ledger
1. Create a spreadsheet and sheet tab named `Ledger`.
2. Share spreadsheet with service-account email (Editor).
3. Export spreadsheet ID:
   ```bash
   export GOOGLE_SHEETS_ID="<spreadsheet-id>"
   ```

## 4) Gmail Daily Brief Delivery
For service-account domain-wide delegation, set delegated sender:
```bash
export GOOGLE_DELEGATED_USER="sender@yourdomain.com"
```
Set recipient:
```bash
export DAILY_BRIEF_TO="manager@yourdomain.com"
```

## 5) Run the Agency
```bash
python /home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/src/rnu_agency.py \
  --topic "Autonomous RNU Thesis Generation" \
  --output /home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/generated_thesis.md \
  --ledger /home/runner/work/RNU-Academic-Writing-Agency/RNU-Academic-Writing-Agency/ledger/agency_ledger.csv
```

If Google variables are not set, the script still runs locally and writes output + ledger CSV.
