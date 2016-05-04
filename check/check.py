#!/usr/bin/python

import click
import requests
import sys
@click.command()
@click.option('--active/--no-active', default=True, help='If the node have to be active or not')
@click.option('--ip', default='',  help='IP address expected')

def check(ip, active):
    """Check if the digital ocean IP is assigned properly."""
    is_active = requests.get('http://169.254.169.254/metadata/v1/floating_ip/ipv4/active').text
    ip_assigned = requests.get('http://169.254.169.254/metadata/v1/floating_ip/ipv4/ip_address').text

    if (ip, active) == (ip_assigned, bool(is_active)):
        click.echo('Expected status for the float IP %s' % ip )
        sys.exit(0)
    else:
        click.echo('Unexpected status for the float IP %s' % ip )
        sys.exit(2)


if __name__ == '__main__':
    check()
