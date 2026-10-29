$repo = "C:\Users\kevin\code\Structy-Hub"
$log  = Join-Path $env:LOCALAPPDATA "structy-sync.log"

function Log($m) { "$(Get-Date -Format s)  $m" | Add-Content $log }

try {
    Set-Location $repo
    if (git status --porcelain --untracked-files=no) {
        Log "Skipped: repo has uncommitted changes"
        exit 0
    }
    git pull --rebase | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "git pull failed" }

    $out = python "$repo\_tools\anki_progress.py" --readme "$repo\README.md" | Out-String
    if ($LASTEXITCODE -ne 0) { throw "anki script failed: $out" }

    if (git status --porcelain README.md) {
        git add README.md
        git commit -m "Update Anki progress" | Out-Null
        git push | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "git push failed" }
        Log "Pushed README update"
    } else {
        Log "No change"
    }
} catch {
    Log "ERROR: $_"
    exit 1
}
