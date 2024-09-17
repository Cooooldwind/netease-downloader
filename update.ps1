# 运行 Python 命令
& python cx_freeze_setup.py build

# 获取 build/Project/ 文件夹路径
$projectFolder = Join-Path -Path (Get-Location) -ChildPath "NeteaseDownloader/"

# 判断 md5_index.json 是否存在
if (Test-Path -Path (Join-Path -Path $projectFolder -ChildPath "md5_index.json")) {
    # 如果存在，进行 MD5 比对
    $existingHashes = Get-Content -Path (Join-Path -Path $projectFolder -ChildPath "md5_index.json") | ConvertFrom-Json
    $allFiles = Get-ChildItem -Path $projectFolder -File
    foreach ($file in $allFiles) {
        $currentHash = (Get-FileHash -Path $file.FullName).Hash
        if ($existingHashes.ContainsKey($file.Name)) {
            if ($existingHashes[$file.Name] -ne $currentHash) {
                Write-Host "MD5 mismatch for $($file.Name)"
            }
        } else {
            Write-Host "New file detected: $($file.Name)"
        }
    }
} else {
    # 如果不存在，生成并导入所有文件的 MD5
    $allFiles = Get-ChildItem -Path $projectFolder -File
    $newHashes = @{}
    foreach ($file in $allFiles) {
        $hash = (Get-FileHash -Path $file.FullName).Hash
        $newHashes[$file.Name] = $hash
    }
    $newHashes | ConvertTo-Json | Set-Content -Path (Join-Path -Path $projectFolder -ChildPath "md5_index.json")
}