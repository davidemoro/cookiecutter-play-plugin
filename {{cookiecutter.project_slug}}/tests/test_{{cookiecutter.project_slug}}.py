#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""


def test_provider():
    from {{ cookiecutter.project_slug }} import providers
    print_provider = providers.NewProvider(None)
    assert print_provider.engine is None
    print_provider.command_print(
        {'provider': '{{cookiecutter.project_slug}}',
         'type': 'print',
         'message': 'Hello, World!'})
