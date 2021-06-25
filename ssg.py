import typer
from ssg.site import Site

def main(source='content', dest='dist'):
    config = {'source': source, 'dest': dest}
    Site.build(Site(**config))

typer.run(main)