$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding
# 获取当前脚本文件所在的目录
$scriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

Get-ChildItem -Path $scriptDirectory -Filter *.ui | ForEach-Object {
    $uiFile = $_.FullName
    $pyFile = $uiFile -replace '\.ui$', '.py'
    & pyside6-uic $uiFile -o $pyFile
    Write-Host "Full path: $uiFile has been converted to $pyFile."
}