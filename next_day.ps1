
& python next_day.py

$maxDay = Get-ChildItem -Directory | Where-Object { $_ -match "\d+" }  | ForEach-Object { [int]$_.Name } | Sort-Object -Descending | Select-Object -First 1

Set-Location ".\$maxDay\"

