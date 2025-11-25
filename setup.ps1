Write-Host "============================================================"
Write-Host " TMDB DATA ANALYST — WINDOWS SETUP"
Write-Host "============================================================"

# ------------------------------------------------------------
# 1. Check Python installation
# ------------------------------------------------------------
Write-Host "`nChecking Python installation..."

$pythonVersion = python --version 2>$null

if (-not $pythonVersion) {
    Write-Host "[ERROR] Python is not installed or not added to PATH." -ForegroundColor Red
    exit 1
}

Write-Host "[OK] Python detected: $pythonVersion"


# ------------------------------------------------------------
# 2. Create virtual environment
# ------------------------------------------------------------
Write-Host "`nCreating virtual environment (.venv)..."

python -m venv .venv

if (-not (Test-Path ".venv")) {
    Write-Host "[ERROR] Failed to create virtual environment." -ForegroundColor Red
    exit 1
}

Write-Host "[OK] Virtual environment created."


# ------------------------------------------------------------
# 3. Activate virtual environment
# ------------------------------------------------------------
Write-Host "`nActivating virtual environment..."

# PowerShell activation
. ".\.venv\Scripts\Activate.ps1"

if (-not $env:VIRTUAL_ENV) {
    Write-Host "[ERROR] Failed to activate virtual environment." -ForegroundColor Red
    exit 1
}

Write-Host "[OK] Virtual environment activated."


# ------------------------------------------------------------
# 4. Install dependencies
# ------------------------------------------------------------
if (-not (Test-Path "requirements.txt")) {
    Write-Host "[ERROR] requirements.txt not found." -ForegroundColor Red
    exit 1
}

Write-Host "`nInstalling dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "[OK] Dependencies installed."


# ------------------------------------------------------------
# 5. Ensure folder structure
# ------------------------------------------------------------
Write-Host "`nEnsuring folder structure..."

$folders = @(
    "data",
    "data/raw",
    "data/processed",
    "data/clean",
    "credentials"
)

foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
    }
}

Write-Host "[OK] Folder structure ensured."


# ------------------------------------------------------------
# 6. Check .env file
# ------------------------------------------------------------
Write-Host "`nChecking .env file..."

if (-not (Test-Path ".env")) {
    Write-Host "[WARNING] .env not found. Copying .env.example → .env" -ForegroundColor Yellow
    if (Test-Path ".env.example") {
        Copy-Item ".env.example" ".env"
        Write-Host "[OK] .env created. Please edit it with your credentials."
    } else {
        Write-Host "[ERROR] .env.example not found. Cannot create .env automatically." -ForegroundColor Red
    }
} else {
    Write-Host "[OK] .env detected."
}


# ------------------------------------------------------------
# 7. Test TMDB API Key
# ------------------------------------------------------------
Write-Host "`nChecking TMDB_API_KEY from .env..."

$tmdbKey = Select-String -Path ".env" -Pattern "^TMDB_API_KEY=" | ForEach-Object { $_.ToString().Split("=")[1] }

if (-not $tmdbKey -or $tmdbKey -eq "") {
    Write-Host "[ERROR] TMDB_API_KEY not found in .env" -ForegroundColor Red
} else {
    Write-Host "[OK] TMDB_API_KEY detected."
}


# ------------------------------------------------------------
# 8. Final message
# ------------------------------------------------------------
Write-Host "`n============================================================"
Write-Host " SETUP COMPLETE"
Write-Host " To run the ETL, execute:"
Write-Host "   python src/etl/extract_tmdb.py"
Write-Host "   python src/etl/transform_tmdb.py"
Write-Host "   python src/etl/load_tmdb.py"
Write-Host "============================================================"
