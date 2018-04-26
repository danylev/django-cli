import click
import jinja2
import os

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENV = jinja2.Environment(
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENV.get_template(template_filename).render(context)


@click.command()
def main():
    click.echo('CLI tool for Django')
    fname = 'loan.py'
    name = 'loan'
    context = {
        'name': name.capitalize() 
    }
    with open(fname, 'w') as f:
        app = render_template('app_template.py', context)
        f.write(app)

if __name__=='__main__':
    main()