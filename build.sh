# /bin/sh
python3 setup.py bdist_wheel
pip3 uninstall dist/mkdocs_plugin_inline_svg_mod-0.1.0-py3-none-any.whl
pip3 install dist/mkdocs_plugin_inline_svg_mod-0.1.0-py3-none-any.whl
