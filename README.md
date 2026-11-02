# drive-to-hermes-connector

Public informational pages for a personal Google Drive / Docs / Sheets connection to a local Hermes installation. This repository is **not** the connector runtime and contains no OAuth credentials, tokens, user files, or chat history.

## Pages

- `docs/index.html` — application description
- `docs/privacy.html` — privacy and data-use policy
- `docs/terms.html` — terms of use

GitHub Pages source: `main` branch, `/docs` folder. No packages, build step, third-party JavaScript, remote fonts, or analytics are required.

## Checks

```sh
python tests/test_site.py
```

The policy describes local token storage, possible local history retention, configured AI-provider processing, and Google Limited Use restrictions. It does not claim that every AI-provider configuration is compliant or that Google has verified the app.

## Safety

Never commit Google client JSON, access/refresh tokens, `.env` files, documents, or conversation exports. Public support is via repository Issues; do not post sensitive material there.
