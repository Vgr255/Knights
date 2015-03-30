# third-party libs
from lib.oyoyo.client import IRCClient
from lib import logger

from src import irc_handler
import botconfig

def main():
    handler = irc_handler.RawHandler()

    log = logger.NamedLevelsLogger(
          levels={"warning": 15, "debug": 10, "normal": 15},
          bypassers=[("level", set(), {(botconfig, "DEBUG_MODE"),
                     (botconfig, "VERBOSE_MODE")}, None, 15)],
          ts_format="[%Y-%m-%d] (%H:%M:%S)", write=False, level=15,
          print_ts=True)

    cli = IRCClient(
                     {"": handler.hook_handler},
                     host=botconfig.HOST,
                     port=botconfig.PORT,
                     authname=botconfig.USERNAME,
                     password=botconfig.PASS,
                     nickname=botconfig.NICK,
                     ident=botconfig.IDENT,
                     real_name=botconfig.REALNAME,
                     sasl_auth=botconfig.USE_SASL,
                     use_ssl=botconfig.USE_SSL,
                     connect_cb=irc_handler.connect_callback,
                     stream_handler=log.logger,
    )
    cli.mainLoop()

if __name__ == "__main__":
    main()
