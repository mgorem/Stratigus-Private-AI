Write-Host "=== Running Stratigus LM Studio Web Agent ==="

if (-not (Test-Path ".venv")) {
    Write-Host "Virtual environment not found. Please run setup_agent.ps1 first." -ForegroundColor Red
    exit 1
}

$venvActivate = ".\.venv\Scripts\Activate.ps1"
$cmd = "$venvActivate; python agent.py"
powershell -NoExit -Command $cmd
