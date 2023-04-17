# mkdocs-plugin-inline-svg-mod

> Reads SVG images referenced from Markdown and replaces them with the SVG
> file content

Since the SVG is included as part of the plain-text input to MkDocs, this means
the default MkDocs search supports searching SVG text, and hyperlinks are also
fully functional.

## Usage

Install the package with pip:

`pip install mkdocs-plugin-inline-svg-mod`

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

### Options

You can filter with the extension to select files to be inline. Useful to mix regular and inlined svgs.:

```
plugins:
    - search
    - inline-svg:
        extension: ".inline.svg"
        delete: "<regex-string>"
```

The delete parameter will remove the matching string from the SVG file content.
Example:

**Sample SVG content**
```xml
<svg>
<defs>
</defs>
<svg>
```

**YAML config**
`delete: "(?s)<defs>.*</defs>|\n"`

**SVG content loaded into HTML will become:**
```xml
<svg></svg>
```

## Credits

I am not really a Python programmer, so I have borrowed plugin setup / utils /
inspiration from:

* https://github.com/stuebersystems/mkdocs-img2fig-plugin
* https://github.com/athackst/mkdocs-simple-plugin

**rajguru7**
I have cloned this from <https://gitlab.com/nicolas.dupont/mkdocs-plugin-inline-svg/-/tree/master> which is a fork of <https://gitlab.com/craig0990/mkdocs-plugin-inline-svg>

Credits to @craig0990 and @nicolar.dupont (GitLab) for the base plugin.
