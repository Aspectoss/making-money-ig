$inputJson = [Console]::In.ReadToEnd() | ConvertFrom-Json
$root = if ($inputJson.workspace_roots) { $inputJson.workspace_roots[0] } else { (Get-Location).Path }

$context = @"
MoneyTools automated site active.
Live: https://aspectoss.github.io/making-money-ig/
Maintain SEO tools and affiliate site. No Instagram.
Run: python generate_seo.py && python scripts/build-config.py
"@

@{ additional_context = $context } | ConvertTo-Json -Compress
exit 0
