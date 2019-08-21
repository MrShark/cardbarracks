import click
import os

import cardbarracks.input
import cardbarracks.cards
import cardbarracks.output


@click.command()
@click.option('-c', '--cardformat', default="use_me",
              help='Cardformat')
@click.argument('barrackfile')
def script(cardformat, barrackfile):
    cardclass = cardbarracks.cards.get_class(cardformat)
    pdf = cardbarracks.output.pdffile("out.pdf", cardclass)
    barrackfile = os.path.abspath(barrackfile)
    os.chdir(os.path.dirname(barrackfile))
    barrackfile = os.path.basename(barrackfile)
    for grunt in cardbarracks.input.readfile(barrackfile):
        card = cardclass(grunt)
        pdf.add_card(card)
    pdf.close()
