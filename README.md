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
$ python3 playerlist.py  /opt/mc/all_biomes
Players last seen on Big Daddy
=============================================
        CforJohn    Mon Oct 05 2020, 02:53 PM
       roguenerd    Mon Oct 05 2020, 02:12 PM
    AmberAlert03    Sun Oct 04 2020, 08:30 PM
           _Ro1_    Thu Sep 24 2020, 08:38 PM
        alpal923    Sun Sep 20 2020, 07:58 PM
  TangoTangoMike    Wed Aug 05 2020, 09:42 PM
       LiamLopey    Wed Aug 05 2020, 09:33 PM
     iiridescent    Fri Jul 24 2020, 09:47 PM
           vvvin    Fri Jul 24 2020, 09:47 PM
communistdictatr    Sun Jun 14 2020, 11:12 PM
        Entrippy    Tue Jun 09 2020, 08:47 PM
     Twinkislaya    Sat Jun 06 2020, 10:34 PM
        KolbyWan    Tue Jun 02 2020, 11:53 PM
        Terrefeu    Tue Jun 02 2020, 02:22 PM
          kesnow    Sat May 23 2020, 12:15 AM
           mule0    Mon May 18 2020, 11:04 PM
          zbrogz    Mon May 18 2020, 10:06 PM
   laxmanisbeast    Fri May 15 2020, 06:41 PM
      Lupineeyes    Sat Apr 11 2020, 04:14 PM
```

### HTML
https://bigdaddy.cf/map/players/
