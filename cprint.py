try:
    from colorama import init, Fore, Back, Style
except:
    import os
    print("!-> Install the required module <-!")
    os.system("pip install colorama")
    print("!-> Done <-!")
from colorama import init, Fore, Back, Style 

def font(par):
    tmp02 = {"black":Fore.BLACK, "red":Fore.RED, "green":Fore.GREEN, "yellow":Fore.YELLOW, "blue":Fore.BLUE, "magneta":Fore.MAGENTA, "cyan":Fore.CYAN, "white":Fore.WHITE, "n":Fore.RESET}
    return tmp02[par]

def bag(par):
    tmp02 = {"black":Back.BLACK, "red":Back.RED, "green":Back.GREEN, "yellow":Back.YELLOW, "blue":Back.BLUE, "magneta":Back.MAGENTA, "cyan":Back.CYAN, "white":Back.WHITE, "n":Back.RESET}
    return tmp02[par]

def mode(par):
    tmp02 = {"l":Style.DIM, "n":Style.NORMAL, "b":Style.BRIGHT, "reset":Style.RESET_ALL}
    return tmp02[par]

def create_one(text):
    tmp01 = text.split("}~")
    params = tmp01[0]
    del tmp01[0]
    only_text = "}~".join(tmp01)
    if params == "reset":
        return mode("reset") + only_text
    text_ready = ""
    pars_params = params.split(":")
    if pars_params[0] != "":
        text_ready = font(pars_params[0]) + text_ready
    if pars_params[1] != "":
        text_ready = bag(pars_params[1]) + text_ready
    if pars_params[2] != "":
        text_ready = mode(pars_params[2]) + text_ready
    return text_ready + only_text

def cprint(text):
    if "~{" not in text:
        print(text)
        return 0
    pars_text = text.split("~{")
    ready_text = ""
    for one_pars in pars_text:
        if one_pars == "":
            continue
        ready_text += create_one(one_pars)
    init(autoreset=True)
    print (ready_text + mode("reset"))

__all__ = ['cprint']