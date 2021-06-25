import click
import re
import sys

@click.command()
@click.argument('mail_addr')
def hello(mail_addr):
    pattern = re.compile('[\w\-\._]+@[\w\-\._]+\.[A-Za-z]+')
    result = pattern.fullmatch(mail_addr)
    if result is None:
        click.echo('bad address.')
        sys.exit(1)  
    click.echo(mail_addr)

if __name__ == '__main__':
    hello()
