Write-Host "=== Stratigus LM Studio Web Agent Setup ==="

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Python is not installed or not on PATH. Please install Python 3.10+ and try again." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment (.venv)..."
    python -m venv .venv
} else {
    Write-Host "Virtual environment (.venv) already exists. Skipping creation."
}

Write-Host "Activating virtual environment and installing dependencies..."
$venvActivate = ".\.venv\Scripts\Activate.ps1"
$cmd = "$venvActivate; pip install --upgrade pip; pip install lmstudio requests beautifulsoup4"
powershell -NoExit -Command $cmd
