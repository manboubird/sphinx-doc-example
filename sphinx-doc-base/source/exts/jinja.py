# -*- coding: utf-8 -*-
"""
    jinja
    ~~~~~
    Modified version of https://github.com/tardyp/sphinx-jinja
    https://github.com/tardyp/sphinx-jinja/blob/3c779452aafd8fccd19acfb507380a3426aaaf80/sphinxcontrib/jinja.py
"""
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList
from jinja2 import Template, Environment, FileSystemLoader


class JinjaDirective(Directive):

    has_content = True
    required_arguments = 1
    option_spec = {
        "file": directives.path,
        "header_char": directives.unchanged,
    }
    app = None

    def run(self):
        node = nodes.Element()
        node.document = self.state.document
        jinja_context_name = self.arguments[0]
        template_filename = self.options.get("file")
        cxt = self.app.config.jinja_contexts[jinja_context_name]
        cxt["options"] = {
            "header_char": self.options.get("header_char")
        }

        if template_filename:
            loader = FileSystemLoader(searchpath="", encoding='utf8')
            env = Environment(loader = loader)
            tpl = env.get_template(template_filename)
        else:
            tpl = Template("\n".join(self.content))
        new_content = tpl.render(**cxt)
        # transform the text content into a string_list that the nested_parse
        # can use:
        new_content = StringList(new_content.split("\n"))
        self.state.nested_parse(new_content, self.content_offset,
                                node, match_titles=1)
        return node.children


def setup(app):
    JinjaDirective.app = app
    app.add_directive('jinja', JinjaDirective)
    app.add_config_value('jinja_contexts', {}, 'html')
