#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import re

@click.command()
def extract_email():
    # with click.get_text_stream('stdin') as stdin_stream:

    prog = re.compile("[A-Za-z0-9][A-Za-z0-9\.]*[A-Za-z0-9]@[A-Za-z0-9]+\.[A-Za-z0-9]+")

    stdin_stream = click.get_text_stream('stdin')
    stdin_text = stdin_stream.readline()
    while stdin_text:
        # click.echo(stdin_text[0:-1])
        
        matched_texts = prog.findall(stdin_text)
        if matched_texts:
            for matched_text in matched_texts:
                click.echo(matched_text)
        
        stdin_text = stdin_stream.readline()

if __name__ == '__main__':
    extract_email()
