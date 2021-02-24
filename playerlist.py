import http.client
from http import HTTPStatus
import argparse
import json
import glob
import os
import sys
import datetime
import cgi


class Player:
    def __init__(self, uuid, last_modified):
        self.uuid = uuid
        self.last_modified = last_modified
        self.username = None

    def get_last_modified_date(self):
        return datetime.datetime.fromtimestamp(self.last_modified).strftime(
            "%a %b %d %Y, %I:%M %p"
        )

    def get_username(self):
        if self.username is not None:
            return self.username

        if self.uuid.startswith("00000000-0000-0000-000"):
            self.username = "Bedrock Player"
            return self.username

        # perform request
        conn = http.client.HTTPSConnection("api.mojang.com")

        uuid = self.uuid.replace("-", "")

        conn.request("GET", f"/user/profiles/{uuid}/names")
        r = conn.getresponse()
        if r.status == HTTPStatus.NOT_FOUND or r.status == HTTPStatus.NO_CONTENT:
            print(f"Player `{self.uuid}` not found!")
            return self.uuid

        assert (
            r.status == HTTPStatus.OK
        ), f"Unexpected API error! {r.status}: {r.reason}"

        body = json.loads(r.read().decode("utf-8"))
        self.username = body[-1]["name"]
        return self.username


def get_max_player_name_length(players):
    longest = 0
    for p in players:
        longest = max(len(p.get_username()), longest)
    return longest


def get_players(worldpath):
    """
    Returns a list of players, sorted from most recent to last
    """
    datfiles = glob.glob(f"{worldpath}/playerdata/*.dat")

    players = []

    for datfile in datfiles:
        uuid = os.path.basename(datfile).replace(".dat", "")
        mtime = os.path.getmtime(datfile)
        players.append(Player(uuid, mtime))

    players.sort(key=lambda x: x.last_modified, reverse=True)
    return players


def write_text_output(out, players, servername):
    """
    Writes a textual representation of the output to stdout
    """
    header = f"Players last seen on {servername}"
    print(header, file=out)

    longest = get_max_player_name_length(players)

    max_row_len = 4 + longest + 4 + len("Mon Oct 05 2020, 02:33 PM")
    print("=" * max(len(header), max_row_len), file=out)

    count = 1
    for p in players:
        print(
            f"{{:<3}} {{:>{longest}}}    {{}}".format(
                count, p.get_username(), p.get_last_modified_date()
            ),
            file=out,
        )
        count += 1


def write_html_output(out, players, servername):
    """
    Writes a basic HTML representation of the output to stdout
    """
    header = f"<html><head><!-- generated with github.com/jaydenmilne/minecraft-server-player-list -->"
    header += f"<title>{servername} players</title><meta name='viewport' content='width=device-width, initial-scale=1.0'></head><body><h1>Players on {servername}</h1>"
    print(header, file=out)
    print("<table><tr><th>Place</th><th>Player</th><th>Last Seen</th></tr>", file=out)

    count = 1
    for p in players:
        print(
            f"<tr><td>{count}<td>{cgi.escape(p.get_username())}</td><td>{p.get_last_modified_date()}</td></tr>",
            file=out,
        )
        count += 1

    print("</table></body></html>", file=out)


def main(worldpath, out, html, n, servername):
    players = get_players(worldpath)

    if n != -1:
        players = players[: int(n)]

    if out is None:
        f = sys.stdout
    else:
        f = open(out, "w")

    if html:
        write_html_output(f, players, servername)
    else:
        write_text_output(f, players, servername)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a list of recent players on a minecraft server."
    )

    parser.add_argument(
        "worldpath",
        type=str,
        help="Path to the world folder to scan (eg <server_root>/world)",
    )
    parser.add_argument(
        "--out",
        type=str,
        help="Path to output file, defaults to stdout",
        required=False,
        default=None,
    )
    parser.add_argument(
        "--html",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "-n",
        required=False,
        help="Only return the last n usernames, default all",
        default=-1,
    )
    parser.add_argument(
        "--servername",
        required=False,
        help="Server name for use in output",
        default="server",
    )

    args = parser.parse_args()
    main(args.worldpath, args.out, args.html, args.n, args.servername)
