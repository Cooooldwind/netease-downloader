$targetFolder = "" # 将这里替换为实际的目标文件夹路径

Get-ChildItem -Path $targetFolder -Recurse -Directory | Where-Object { $_.Name -eq '__pycache__' } | ForEach-Object {
    Remove-Item -Path $_.FullName -Recurse -Force
}