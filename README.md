# Minecraft Server Player List

Quick script that generates a list of recent players on your server, sorted
in order of who last logged in. Works by looking at the last modified time of
their `player.dat` files in `<server root>/world/playerdata`, and resolving
those UUIDs to a playername using Mojang's API.

## Usage

```
$ python3 playerlist.py -h
usage: playerlist.py [-h] [--out OUT] [--html] [-n N]
                     [--servername SERVERNAME]
                     worldpath

Generate a list of recent players on a minecraft server.

positional arguments:
  worldpath             Path to the world folder to scan (eg
                        <server_root>/world)

optional arguments:
  -h, --help            show this help message and exit
  --out OUT             Path to output file, defaults to stdout
  --html
  -n N                  Only return the last n usernames, default all
  --servername SERVERNAME
                        Server name for use in output
```

