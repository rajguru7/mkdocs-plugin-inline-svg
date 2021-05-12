# mkdocs-plugin-inline-svg

> Reads SVG images referenced from Markdown and replaces them with the SVG
> file content

Since the SVG is included as part of the plain-text input to MkDocs, this means
the default MkDocs search supports searching SVG text, and hyperlinks are also
fully functional.

## Usage

Install the package with pip:

`pip install mkdocs-plugin-inline-svg`

Enable the plugin in your mkdocs.yml:

```
plugins:
    - search
    - inline-svg
```

> Note: If you have no plugins entry in your config file yet, you'll likely
> also want to add the search plugin. MkDocs enables it by default if there is
> no plugins entry set, but now you have to enable it explicitly.

More information about plugins in the MkDocs documentation

## Credits

I am not really a Python programmer, so I have borrowed plugin setup / utils /
inspiration from:

* https://github.com/stuebersystems/mkdocs-img2fig-plugin
* https://github.com/athackst/mkdocs-simple-plugin
