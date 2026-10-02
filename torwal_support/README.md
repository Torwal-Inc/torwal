# Torwal Support

Adds a **Torwal Support** app tile to the Odoo Apps drawer. Clicking it reads
a system parameter and redirects the user to the configured Torwal support
page — no code changes required to update the destination URL.

## How it works

1. A system parameter `torwal_support.url` is seeded with a default value
   (`https://hub.torwal.com/support`) via `data/torwal_support_data.xml`.
2. `views/torwal_support_menus.xml` defines:
   - A top-level `menuitem` (`menu_torwal_support_root`) that appears as an
     application tile in the Apps drawer.
   - An `ir.actions.server` (`action_open_torwal_support`) that runs when the
     tile is clicked. It reads `torwal_support.url` at click-time via
     `env['ir.config_parameter'].sudo().get_param(...)` and returns an
     `ir.actions.act_url` action that redirects the browser to that URL.

Because the URL is resolved at click-time from the system parameter (rather
than hard-coded in XML), it can be changed without upgrading the module.

## Changing the support URL

As an administrator:

1. Go to **Settings > Technical > Parameters > System Parameters**.
   (Enable developer mode first if the Technical menu isn't visible.)
2. Search for the key `torwal_support.url`.
3. Edit the **Value** field to the new URL and save.

The next click on the Torwal Support tile will redirect to the new URL
immediately — no restart or upgrade needed.

## Installation

1. Make sure the addons path for your Odoo instance includes the `torwal`
   folder (already the case for `configs/torwal.config`).
2. Restart the Odoo server.
3. Go to **Apps**, click **Update Apps List**, then search for and install
   **Torwal Support**.

## Module structure

```
torwal_support/
├── __init__.py
├── __manifest__.py
├── README.md
├── data/
│   └── torwal_support_data.xml   # default value for torwal_support.url
└── views/
    └── torwal_support_menus.xml  # app menu + redirect server action
```

## Notes

- No new models, views, or security rules are introduced by this module.
- The `static/description/icon.png` referenced by the app tile's `web_icon`
  has not been added yet; add a PNG at that path to replace the default
  placeholder icon shown in the Apps drawer.
- The server action's `model_id` is set to `ir.config_parameter` purely as a
  technical requirement of `ir.actions.server`; the code does not operate on
  any particular record of that model.

