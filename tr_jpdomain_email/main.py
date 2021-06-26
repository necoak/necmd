import click
import re
import sys

domain_pattern = re.compile('[\w\-\._]+\.[A-Za-z]+')
mail_pattern = re.compile('([\w\-\._]+)@([\w\-\._]+\.[A-Za-z]+)')


@click.command()
@click.argument('from_domain')
@click.argument('to_domain')
def cmd(from_domain, to_domain):
    # SetUp
    # Validate: from_domain, to_domain  
    from_domain_result = domain_pattern.fullmatch(from_domain)
    to_domain_result = domain_pattern.fullmatch(to_domain)
    
    if from_domain_result is None:
        raise click.BadParameter('Bad FromDomain')
    if to_domain is None:
        raise click.BadParameter('Bad ToDomain')

    click.echo('Mail Address domain trans: ' + from_domain + ' -> ' + to_domain)
    click.echo('Input MailAddress')

    # 
    read_flg = True
    in_mail_addrs = []
    while (read_flg):
        in_text = input()
        if in_text == '':
            read_flg = False
        else:
            in_mail_addrs.append(in_text)

    click.echo('----- trans domain output -----')
    
    success_num = 0
    for in_mail_addr in in_mail_addrs:
        tred_mail_addr, err_msg = tr_mail_addr(from_domain, to_domain, in_mail_addr)
        if err_msg is None:
            success_num += 1
            click.echo(tred_mail_addr)
        else:
            click.echo(err_msg)

    click.echo('')
    click.echo('trans success result: {} / {}'.format(success_num, len(in_mail_addrs)))


def tr_mail_addr(from_domain, to_domain, in_mail_addr):
    # Validate: mail_addr   
    mail_addr_result = mail_pattern.fullmatch(in_mail_addr)

    if mail_addr_result is None:
        return None, 'Bad MailAddress: ' + in_mail_addr

    local_mail_addr, domain_mail_addr = mail_addr_result.groups()

    if domain_mail_addr != from_domain:
        return None, 'Bad Domain: ' + in_mail_addr

    new_mail_addr = ''.join([local_mail_addr, '@', to_domain])
    return new_mail_addr, None



if __name__ == '__main__':
    cmd()
