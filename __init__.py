from rich.console import Console
from rich.panel import Panel
from rich.live_render import LiveRender
import sys
import os
import shutil

console = Console()

def hata (text):
   console.print(text, style="bold red")
def bilgi (text):
   console.print(text, style="blue")
def basarili (text):
   console.print(f"[bold green]{text}[/]")
def onemli (text):
   console.print(text, style="bold cyan")
def soru (soru):
   return console.input(f"[bold yellow]{soru}[/]")
def logo (dil = "Yoxdur"):
   surum = str(sys.version_info[0]) + "." + str(sys.version_info[1])
   console.print(Panel(f"[bold white]NEXUS USΞRBOT[/]\n\n[bold blue]Versiya: [/][i]2.1[/]\n[bold red]Python: [/][i]{surum}[/]\n[bold green]Dil: [/][i]{dil}[/]"), justify="center")                         
def tamamlandi (saniye):
   console.print(Panel(f"[bold green]Qurulum Tamamlandı!\n[i]Botu {round(saniye)} saniye içinde qurdunuz.[/]\n\n[bold green]Bir neçe deqiqe sonra her-hansı bir qrupa .alive yazaraq test edə bilersiniz.[/]"), justify="center")                         

def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)
