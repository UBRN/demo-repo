PS C:\> gci Cert:\ -Recurse | Where{$_.Subject -like "*Zero*"} | Remove-Item -Force -verbose