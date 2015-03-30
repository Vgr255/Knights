from src import decorators
from src.decorators import *

import botconfig
import base64

from src import main

class RawHandler:
    def hook_handler(self, cli, prefix, hook_, *rest):
        if hook_ in decorators.Hooks:
            rest = list(rest)
            for i, arg in enumerate(rest):
                if isinstance(arg, bytes):
                    rest[i] = arg.decode("utf-8")
            for func in decorators.Hooks[hook_]:
                func(cli, prefix, *rest)

def connect_callback(cli):

    @hook("endofmotd", 130)
    def prepare_stuff(cli, *args):
        cli.join(botconfig.CHANNEL)

    def ns_regain(cli, *rest):
        if botconfig.PASS:
            cli.ns_regain()

    def ns_release(cli, *rest):
        if botconfig.PASS:
            cli.ns_release()
            cli.nick(botconfig.NICK)

    @hook("unavailresource", 180)
    @hook("nicknameinuse", 180)
    def use_temp_nick(cli, *rest):
        cli.nick(botconfig.NICK + "_")
        cli.user(botconfig.NICK, "")

        delete(180)

        hook("nicknameinuse")(ns_regain)
        hook("unavailresource")(ns_release)

    if botconfig.USE_SASL:

        @hook("authenticate")
        def auth_plus(cli, something, plus):
            if plus == "+":
                nick_b = bytes(botconfig.USERNAME if botconfig.USERNAME else botconfig.NICK, "utf-8")
                pass_b = bytes(botconfig.PASS, "utf-8")
                secret_msg = b'\0'.join((nick_b, nick_b, pass_b))
                cli.send("AUTHENTICATE " + base64.b64encode(secret_msg).decode("utf-8"))
    
        @hook("cap")
        def on_cap(cli, server, me, ack, cap):
            if ack.upper() == "ACK" and "sasl" in cap:
                cli.send("AUTHENTICATE PLAIN")
                
        @hook("903")
        def on_successful_auth(cli, *rest):
            cli.cap("END")
            
        @hook("904")
        @hook("905")
        @hook("906")
        @hook("907")
        def on_failure_auth(cli, *rest):
            cli.quit()
            print("SASL authentication failed.  Did you fill the account name " +
                  "in botconfig.USERNAME if it's different from the bot nick?")

@hook("ping")
def on_ping(cli, prefix, server):
    cli.send('PONG', server)
