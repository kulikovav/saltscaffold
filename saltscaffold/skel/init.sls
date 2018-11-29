# -*- coding: utf-8 -*-
# vim: ft=sls
# Init ${formula_name}
{%- from "${formula_name}/map.jinja" import ${formula_name} with context %}

include:
  - ${formula_name}.install
  - ${formula_name}.config
  - ${formula_name}.service
