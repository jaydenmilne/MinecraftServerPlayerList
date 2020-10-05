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

## Example Output

### Plain Text
```console
$ python3 playerlist.py  /opt/mc/world
Players last seen on Server
=============================================
             Bob    Mon Oct 05 2020, 02:53 PM
             Dan    Mon Oct 05 2020, 02:12 PM
          George    Sun Oct 04 2020, 08:30 PM
```

### HTML

```html
<html>
  <head>
    <title>Server players</title>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  </head>
  <body>
    <h1>Players on Server</h1>
    <table><tbody>
      <tr><th>Player</th><th>Last Seen</th></tr>
      <tr><td>Bob</td><td>Mon Oct 05 2020, 02:53 PM</td></tr>
      <tr><td>Dan</td><td>Mon Oct 05 2020, 02:12 PM</td></tr>
      <tr><td>George</td><td>Sun Oct 04 2020, 08:30 PM</td></tr>
      </tbody></table>
  </body>
</html>
```
